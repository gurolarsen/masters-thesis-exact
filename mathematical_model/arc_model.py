import os
import sys
sys.path.append( os.path.join(os.path.split(__file__)[0],'..'))  # Include subfolders

import gurobipy as gp
from gurobipy import GRB
from mathematical_model.variable_generator import *
#from data_generation.GlobalVariables import instanceFolder
#instanceFolder.setGlobalVaribale("base120a5e")
from mathematical_model.constraint_generator import *
from data_generation.parameter_generator import *

# Weights for objectives
weight_C = 0.0              # Max continuity of care #TODO: Hvorfor har vi denne??
weight_DW = 0.3             # Balance daily workload
weight_WW = 0.3             # Balance weekly workload
weight_S = 0.2              # Min skill difference
weight_SG = 0.2             # Balance specialist/generalist

def run_model():
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
        h_avg_over_g = initalize_highest_avg_heaviness_variables(m)
        h_avg_under_g = initalize_lowest_avg_heaviness_variables(m)
        z_i = initialize_preferred_speciality_variables(m)

        # OBJECTIVE
        m.setObjectiveN(
            gp.quicksum(S_p[p] * delta_i[i]
                        for p in PATIENTS
                        for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p]),
            index=0, priority=4, weight=-1)
        
        #Kommentar om j og i 
        m.setObjectiveN(
            gp.quicksum(C_ie[j][e] * x_ijed[i, j, e, d]
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for j in ACTIVITIES_HEALTH_CARE
                        for i in setOFI_iActDepo_jAct[d][e][j]),
            index=1, priority=3, weight=-1)
        
        m.setObjectiveN(
            weight_WW*gp.quicksum(h_avg_over_g[g] - h_avg_under_g[g]
                        for g in PROFESSION_GROUPS)

            + weight_DW*gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g]
                        for d in DAYS
                        for g in EMPLOYEES_ON_DAY_IN_GROUP[d])

            + weight_S*gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j])
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for j in ACTIVITIES_WITHOUT_DUMMY
                        for i in setOFI_iActDepo_jAct[d][e][j])

            + weight_SG*gp.quicksum(z_i[i]
                        for i in ACTIVITIES_WITH_PREFERRED_SPECIALITY),

            index=2, priority=2)
        
        m.setObjectiveN(
            gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d]
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for i in ACTIVITIES_DEPOT
                        for j in setOFJ_iActDepo_jActDepo[d][e][i]),
            index=3, priority=1)
            
        # CONSTRAINTS
        add_vrp0_constraint(m, h_p)
        add_vrp1_constraint(m, x_ijed, h_p)
        add_vrp2_constraint(m, x_ijed)
        add_vrp3_constraint(m, x_ijed)
        add_vrp4_constraint(m, x_ijed)
        add_tw1_constraint(m, s_i, D_i, T_ij, bigM_ij_tw1, x_ijed)
        add_tw2_constraint(m, S_start_de, T_ij, bigM_j_tw2, x_ijed, s_i)
        add_tw3_constraint(m, s_i, D_i, T_ij, bigM_i_tw3, x_ijed, S_end_de)
        add_tw4_constraint(m, x_ijed, delta_i)
        add_tw5_constraint(m, T_earliest_i, delta_i, s_i)
        add_tw6_constraint(m, delta_i, s_i, T_latest_i)
        add_period1_constraint(m, y_bc, h_p)
        add_period2_constraint(m, x_ijed, A_bvcd, y_bc)
        add_sync_constraint(m, s_i)
        add_precedence1_constraint(m, s_i, D_i, delta_i)
        add_precedence2_constraint(m, s_i, D_i, G_ij)
        add_precedence3_constraint(m, x_ijed)
        add_heaviness1_constraint(m, H_i, x_ijed, h_over_dg)
        add_heaviness2_constraint(m, H_i, x_ijed, h_under_dg)
        add_heaviness3_constraint(m, H_i, x_ijed,h_avg_over_g)
        add_heaviness4_constraint(m, H_i, x_ijed, h_avg_under_g)
        add_preferred_speciality1_constraint(m, L_e, F_i, x_ijed, z_i)
        add_preferred_speciality2_constraint(m, L_e, F_i, x_ijed, z_i)

        

        add_subtour_contraint(m,POS_SUBTOURS, x_ijed)    
        #add_symmterty_breaking_logPersonell(m, x_ijed)
        add_symmterty_breaking_syncAct(m, x_ijed)
        #m.addConstr(h_p[22]==1,  name='lock_patient')
        add_dummy1_constraint(m, x_ijed)
        add_dummy2_constraint(m, x_ijed)

        
        # Åpne filen for å skrive
        with open("results.txt", "w") as log_file:
            # Omdiriger sys.stdout til filen
            original_stdout = sys.stdout
            sys.stdout = log_file
            
            #Update the model
            m.update()
            # Optimize
            m.Params.IntFeasTol = 1e-7
            # Optimize model
            m.optimize()

            for v in m.getVars():
                if v.X != 0.0:
                    print(f'{v.VarName:10s} {v.X}')

            # Tilbakestill sys.stdout til original
            sys.stdout = original_stdout
        
        # Writing to terminal
        for v in m.getVars():
            if v.X != 0.0:
                print(f'{v.VarName:10s} {v.X}')

        # For network plotting
        tolerance = 1e-5  # Setter en toleransegrense på 0.00001
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

#Objektiv fra prosjektoppgaven
'''
m.setObjectiveN(
    gp.quicksum(S_p[p] * delta_i[i]
                for p in PATIENTS
                for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p]),
    index=0, priority=5, weight=-1)

m.setObjectiveN(
    gp.quicksum(h_avg_over_g[g] - h_avg_under_g[g]
                for g in PROFESSION_GROUPS),
    index=1, priority=4)

m.setObjectiveN(
    gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g]
                for d in DAYS
                for g in EMPLOYEES_ON_DAY_IN_GROUP[d]),
    index=2, priority=3)

m.setObjectiveN(
    gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j])
                for d in DAYS
                for e in EMPLOYEES_ON_DAY[d]
                for j in ACTIVITIES
                for i in setOFI_iActDepo_jAct[d][e][j]),
    index=3, priority=2)

m.setObjectiveN(
    gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d]
                for d in DAYS
                for e in EMPLOYEES_ON_DAY[d]
                for i in ACTIVITIES_DEPOT
                for j in setOFJ_iActDepo_jActDepo[d][e][i]),
    index=4, priority=1)
'''

#Under er et helt vanlig objektiv som funker
"""
  m.setObjective(
            (gp.quicksum(S_p[p] * delta_i[i]
                         for p in PATIENTS
                         for i in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[p])

            - gp.quicksum(h_avg_over_g[g] - h_avg_under_g[g]
                        for g in PROFESSION_GROUPS)

            - gp.quicksum(h_over_dg[d, g] - h_under_dg[d, g]
                        for d in DAYS
                        for g in EMPLOYEES_ON_DAY_IN_GROUP[d])

            - gp.quicksum(x_ijed[i, j, e, d] * (Q_e[e] - Q_i[j])
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for j in ACTIVITIES
                        for i in setOFI_iActDepo_jAct[d][e][j])

            - gp.quicksum(T_ij[i][j] * x_ijed[i, j, e, d]
                        for d in DAYS
                        for e in EMPLOYEES_ON_DAY[d]
                        for i in ACTIVITIES_DEPOT
                        for j in setOFJ_iActDepo_jActDepo[d][e][i])),
            GRB.MAXIMIZE)

"""