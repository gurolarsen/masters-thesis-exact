import sys
sys.path.append('C:\\Users\\gurl\\project-thesis')

import gurobipy as gp
from gurobipy import GRB
from mathematical_model.variable_generator import *
#from data_generation.GlobalVariables import instanceFolder
#instanceFolder.setGlobalVaribale("base120a5e")
from mathematical_model.constraint_generator import *
from data_generation.parameter_generator import *



#Hvorfor vil ikke den første sette de første før går videre
#Denne henter fra variablegenerator, og fr.
#Alt henter fra data, også vil du ikke k
#Ide lage et dataobjekt. Slik at du kan ha ulike data_objekter å kjøre på.
#For nå kjører vi bare på datafilen og den må hente fra uliek



def run_model():
    #Dette fungerer ikke fordi vi setter filen til a å være

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

        # OBJECTIVE
        """
          m.setObjective(gp.quicksum(S_p[p] * delta_i[i]
                        for p in PATIENTS
                        for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p]), GRB.MAXIMIZE)
        """

        m.setObjectiveN(
            gp.quicksum(S_p[p] * delta_i[i]
                        for p in PATIENTS
                        for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p]),
            index=0, priority=4, weight=-1)

        m.setObjectiveN(
            gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g]
                        for d in DAYS
                        for g in EMPLOYEES_ON_DAY_IN_GROUP[d]),
            index=1, priority=3)

        m.setObjectiveN(
            gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j])
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for j in ACTIVITIES
                        for i in setOFI_iActDepo_jAct[d][e][j]),
                        #getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)[e][j]),
            index=2, priority=2)

        m.setObjectiveN(
            gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d]
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for i in ACTIVITIES_DEPOT
                        for j in setOFJ_iActDepo_jActDepo[d][e][i]),
                        #getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES_DEPOT)[e][i]),
            index=3, priority=1)


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

        # Optimize
        m.Params.IntFeasTol = 1e-7
        m.optimize()


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

print(run_model())
#Under er et helt vanlig objektiv som funker
"""
m.setObjective(
            (gp.quicksum(S_p[p] * delta_i[i]
                         for p in PATIENTS
                         for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p])
             - gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d]
                           for d in DAYS
                           for e in EMPLOYEES_ON_DAY[d]
                           for i in ACTIVITIES_DEPOT
                           for j in getSetOfj(EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES_DEPOT)[e][i])
             - gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g]
                           for d in DAYS
                           for g in EMPLOYEES_ON_DAY_IN_GROUP[d])
             - gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j])
                           for d in DAYS
                           for e in EMPLOYEES_ON_DAY[d]
                           for j in ACTIVITIES
                           for i in getSetOfi(EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)[e][j])),
            GRB.MAXIMIZE)
"""