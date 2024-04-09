import sys
sys.path.append('C:\\Users\\gurl\\project-thesis')

import gurobipy as gp
from gurobipy import GRB
from mathematical_model.variable_generator import *
from mathematical_model.constraint_generator import *
from data_generation.set_generator import *
from data_generation.parameter_generator import *


def get_objective_expression(m, index, delta_i, h_over_dg, h_under_dg, x_ijed):
    if index == 0:
        return gp.quicksum(S_p[p] * delta_i[i] for p in PATIENTS for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p])
    elif index == 1:
        return gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g] for d in DAYS for g in EMPLOYEES_ON_DAY_IN_GROUP[d])
    elif index == 2:
        return gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j]) for d in DAYS for e in EMPLOYEES_ON_DAY[d] for j in ACTIVITIES for i in setOFI_iActDepo_jAct[d][e][j])
    elif index == 3:
        return gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d] for d in DAYS for e in EMPLOYEES_ON_DAY[d] for i in ACTIVITIES_DEPOT for j in setOFJ_iActDepo_jActDepo[d][e][i])
    else:
        raise ValueError("Invalid objective index")


def run_model_with_deviation():
    try:
        m = gp.Model("distributedCare")

        # VARIABLES
        x_ijed = initialize_arc_flow_variables(m)
        y_bc = initialize_pattern_variables(m)
        h_p = initialize_patient_home_variables(m)
        delta_i = initalize_activity_home_variables(m)
        s_i = initialize_start_time_variables(m)
        h_over_dg = initalize_highest_heaviness_variables(m)
        h_under_dg = initalize_lowest_heaviness_variables(m)

        # CONSTRAINTS
        add_vrp1_constraint(m, x_ijed, h_p)
        add_vrp2_constraint(m, x_ijed)
        add_vrp3_constraint(m, x_ijed)
        add_vrp4_constraint(m, x_ijed)
        add_period1_constraint(m, y_bc, h_p)
        add_period2_constraint(m, x_ijed, A_bvcd, y_bc)
        add_sync_constraint(m, s_i)
        add_precedence1_constraint(m, s_i, D_i, delta_i)
        add_precedence2_constraint(m, s_i, D_i, G_ij)
        add_precedence3_constraint(m, x_ijed)
        add_heaviness1_constraint(m, H_i, x_ijed, h_over_dg)
        add_heaviness2_constraint(m, H_i, x_ijed, h_under_dg)
        add_tw1_constraint(m, s_i, D_i, T_ij, bigM_ij_tw1, x_ijed)
        add_tw2_constraint(m, S_start_de, T_ij, bigM, x_ijed, s_i)
        add_tw4_constraint(m, x_ijed, delta_i)
        add_tw5_constraint(m, T_earliest_i, delta_i, s_i)
        add_tw6_constraint(m, delta_i, s_i, T_latest_i)
        add_tw3_constraint(m, s_i, D_i, T_ij, bigM, x_ijed, S_end_de)

        #Update the model
        m.update()

        # Tolerance for variables in the model
        m.Params.IntFeasTol = 1e-7

        #OPTIMAL VALUE VARIABLES
        optimal_values = []

        # SOLVING FOR OBJECTIVES ITERATIVELY

        #Dette er ikke sett noe på og bare notater
        for obj_index in range(4):  # Four objectives
            if obj_index == 0:
                obj_expr0 = m.setObjectiveN(get_objective_expression(m, obj_index, delta_i, h_over_dg, h_under_dg, x_ijed), index=obj_index, priority=(4 - obj_index))
                optimal_values.append(obj_expr0)
            if obj_index == 1:
                m.addConstr(obj_expr0 >= 0.95 * optimal_val)
                m.addConstr(obj_expr0 <= 1.05 * optimal_val)
                m.setObjectiveN(get_objective_expression(m, obj_index, delta_i, h_over_dg, h_under_dg, x_ijed), index=obj_index, priority=(4 - obj_index))
            if obj_index == 2:
                m.addConstr(obj_expr1 >= 0.95 * optimal_val)
                m.addConstr(obj_expr1 <= 1.05 * optimal_val)
                m.setObjectiveN(get_objective_expression(m, obj_index, delta_i, h_over_dg, h_under_dg, x_ijed), index=obj_index, priority=(4 - obj_index))
            if obj_index == 3:
                m.addConstr(obj_expr2 >= 0.95 * optimal_val)
                m.addConstr(obj_expr2 <= 1.05 * optimal_val)
                m.setObjectiveN(get_objective_expression(m, obj_index, delta_i, h_over_dg, h_under_dg, x_ijed), index=obj_index, priority=(4 - obj_index))
            
            if obj_index > 0:
                # Legg til avviksrestriksjoner for de tidligere målene
                for prev_index in range(obj_index):
                    obj_expr = get_objective_expression(m, prev_index, delta_i, h_over_dg, h_under_dg, x_ijed)
                    optimal_val = optimal_values[prev_index]
                    m.addConstr(obj_expr >= 0.95 * optimal_val)
                    m.addConstr(obj_expr <= 1.05 * optimal_val)

            m.optimize()

            # Lagre optimal verdi
            optimal_values[obj_index] = m.ObjVal

        """
        for obj_index in range(4):  # Four objectives
            m.setObjectiveN(get_objective_expression(m, obj_index, delta_i, h_over_dg, h_under_dg, x_ijed), index=obj_index, priority=(4 - obj_index))

            if obj_index > 0:
                # Legg til avviksrestriksjoner for de tidligere målene
                for prev_index in range(obj_index):
                    obj_expr = get_objective_expression(m, prev_index, delta_i, h_over_dg, h_under_dg, x_ijed)
                    optimal_val = optimal_values[prev_index]
                    m.addConstr(obj_expr >= 0.95 * optimal_val)
                    m.addConstr(obj_expr <= 1.05 * optimal_val)

            m.optimize()

            # Lagre optimal verdi
            optimal_values[obj_index] = m.ObjVal
        """
        for v in m.getVars():
            if v.X != 0.0:
                print(f'{v.VarName:10s} {v.X}')

        tolerance = 1e-5  # Setter en toleransegrense på 0.00001

        # For network plotting
        result_arcs = []
        for v in m.getVars():
            if abs(v.X - 1.0) <= tolerance and v.VarName[0] == 'x':  # Sjekker om verdien er nær nok til
                result_arcs.append(v.VarName)

        #m.printStats()
        #m.display()

        #Dispose the model when done
        #m.dispose()

        return result_arcs #For network plotting

    except gp.GurobiError as e:
        print(f'Error code {e.errno}: {e}')

    except AttributeError as e:
        print(f'Encountered an attribute error: {e}')

print(run_model_with_deviation())
