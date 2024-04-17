from data_generation.set_functions import *
from mathematical_model.variable_generator import *

bigM = 2000  # må finne ut hva vi skal gjøre med bigM



def add_vrp1_constraint(model, x_ijed, h_p):
    print("Entered VRP1")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                                  for d in DAYS
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for i in setOFI_iActDepo_jAct[d][e][j])
                      - h_p[p] == 0
                      for p in PATIENTS
                      for v in VISITS_FOR_PATIENT[p]
                      for j in ACTIVITIES_IN_VISIT[v] if j not in ACTIVITIES_DUMMY), name='vrp1')


def add_vrp2_constraint(model, x_ijed):
    print("Entered VRP2")
    model.addConstrs((gp.quicksum(x_ijed[0, j, e, d]
                                  for j in setOFJ_iActDepo_jAct[d][e][0]) == 1
                                  #getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)[e][0])
                      for d in DAYS
                      for e in EMPLOYEES_ON_DAY[d]), name='vrp2')


def add_vrp3_constraint(model, x_ijed):
    print("Entered VRP3")
    model.addConstrs((gp.quicksum(x_ijed[i, 0, e, d]
                                  for i in setOFI_iAct_jActDepo[d][e][0]) == 1
                      #getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[e][0])
                      for d in DAYS
                      for e in EMPLOYEES_ON_DAY[d]), name='vrp3')

#Litt usikker pa hva som genereres her med ddenn
def add_vrp4_constraint(model, x_ijed):
    print("Entered VRP4")
    model.addConstrs((gp.quicksum(x_ijed[j, i, e, d]
                                  for i in setOFJ_iAct_jActDepo[d][e][j])
                                  #getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[e][j])
                      - gp.quicksum(x_ijed[i, j, e, d]
                                    for i in setOFI_iActDepo_jAct[d][e][j])
                      == 0
                                    #getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)[e][j])

                      for j in ACTIVITIES
                      for d in DAYS
                      for e in EMPLOYEES_ON_DAY[d]), name='vrp4')
    
'''
Det er ingen tidsvinduere på disse nodene. 
Kan det bli noe feil når vi henter ut 
Må teste endringene opp mot data som er 

Det er bare lov å kjøre til og fra dummynode fra depoet. - Gjort 

Hva er problemet med å bare kjøre 

TODO: Usikker på disse med hp, tror den kan settes til å bare gjelde de andre 

Har ikke lagt inn på heaviness constraintsene. Sjekker først hvodan det blir 
'''

def add_tw1_constraint(model, s_i, D_i, T_ij, bigM_ij_tw1, x_ijed):
    print("Entered TW1")
    model.addConstrs((s_i[i] + D_i[i] + T_ij[i][j] - bigM_ij_tw1[i][j] * (1 -
                            gp.quicksum(x_ijed[i, j, e, d]
                                        for d in DAYS
                                        for e in setOFE_iAct_jAct[d][i][j]))
                                        #getSetOfeNY(d,EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES)[i][j]))
                            - s_i[j] <= 0
                      for i in ACTIVITIES_WITHOUT_DUMMY
                      for j in ACTIVITIES_WITHOUT_DUMMY if i != j), name='tw1')


def add_tw2_constraint(model, S_start_de, T_ij, bigM_j_tw2, x_ijed, s_i):
    print("Entered TW2")
    model.addConstrs(((gp.quicksum(S_start_de[d][e] * x_ijed[0, j, e, d]
                                        for d in DAYS
                                        for e in setOFE_iActDepo_jAct[d][0][j]))
                     + T_ij[0][j]
                      - bigM_j_tw2[j] * (1 - gp.quicksum(x_ijed[0, j, e, d]
                                        for d in DAYS
                                        for e in setOFE_iActDepo_jAct[d][0][j]))
                                 <= s_i[j]
                      for j in ACTIVITIES_WITHOUT_DUMMY), name='tw2')

#Ikke aggregert tw2 contraint
"""
def add_tw2_constraintG(model, S_start_de, T_ij, bigM, x_ijed, s_i):
    print("Entered TW2")
    model.addConstrs((S_start_de[d][e] + T_ij[0][j] - bigM * (1 - x_ijed[0, j, e, d]) <= s_i[j]
                      for d in DAYS
                      for e in EMPLOYEES_ON_DAY[d]
                      for j in getSetOfjNY(d, EMPLOYEES, ACTIVITIES_DEPOT, ACTIVITIES)[e][0]), name='tw2')
"""

#DEN FUNGERER SLIK DEN ER NÅ, MEN SYNES DET ER LITT RART AT DEN KLARER Å INDEKSERE PÅ DENNE VEIEN
def add_tw3_constraint(model, s_i, D_i, T_ij, bigM_i_tw3, x_ijed, S_end_de):
    print("Entered TW3")
    model.addConstrs((s_i[i] + D_i[i] + T_ij[i][0] - bigM_i_tw3[i] * (1 - gp.quicksum(x_ijed[i, 0, e, d]
                                        for d in DAYS
                                        for e in setOFE_iAct_jActDepo[d][i][0]))
                      <= gp.quicksum(S_end_de[d][e] * x_ijed[i, 0, e, d]
                                        for d in DAYS
                                        for e in setOFE_iAct_jActDepo[d][i][0])
                      for i in ACTIVITIES_WITHOUT_DUMMY), name='tw3')

"""
def add_tw3_constraint_NOT_IN_USE(model, s_i, D_i, T_ij, bigM, x_ijed, S_end_de):
    print("Entered TW3")
    model.addConstrs((s_i[i] + D_i[i] + T_ij[i][0] - bigM * (1 -
                         gp.quicksum(x_ijed[i, 0, e, d]
                                    for d in DAYS
                                    for e in getSetOfeNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[i][0]))
                      <= gp.quicksum(S_end_de[d][e] * x_ijed[i][0][e][d]
                                    for d in DAYS
                                    for e in getSetOfeNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[i][0])
                      for i in ACTIVITIES), name='tw3')def add_tw3_constraint_NOT_IN_USE(model, s_i, D_i, T_ij, bigM, x_ijed, S_end_de):
    print("Entered TW3")
    model.addConstrs((s_i[i] + D_i[i] + T_ij[i][0] - bigM * (1 -
                         gp.quicksum(x_ijed[i, 0, e, d]
                                    for d in DAYS
                                    for e in getSetOfeNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[i][0]))
                      <= gp.quicksum(S_end_de[d][e] * x_ijed[i][0][e][d]
                                    for d in DAYS
                                    for e in getSetOfeNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)[i][0])
                      for i in ACTIVITIES), name='tw3')
"""

def add_tw4_constraint(model, x_ijed, delta_i):
    print("Entered TW4")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                              for d in DAYS
                              for e in EMPLOYEES_ON_DAY[d]
                              for i in setOFI_iActDepo_jAct[d][e][j]) == delta_i[j]
                                  #getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)[e][j])
                      for j in ACTIVITIES_WITHOUT_DUMMY), name='tw4')

def add_tw5_constraint(model, T_earliest_i, delta_i, s_i):
    print("Entered TW5")
    model.addConstrs((T_earliest_i[i] * delta_i[i] <= s_i[i]
                      for i in ACTIVITIES_WITHOUT_DUMMY), name='tw5')

def add_tw6_constraint(model, delta_i, s_i, T_latest_i):
    print("Entered TW6")
    model.addConstrs((T_latest_i[i] * delta_i[i] >= s_i[i]
                      for i in ACTIVITIES_WITHOUT_DUMMY), name='tw6')

def add_period1_constraint(model, y_bc, h_p):
    print("Entered Period1")
    model.addConstrs(((gp.quicksum(y_bc[b, c]
                                   for c in PATTERNS_FOR_TREATMENT[b]) - h_p[p]) == 0
                      for p in PATIENTS
                      for b in TREATMENTS_FOR_PATIENT[p]), name='period1')


def add_period2_constraint(model, x_ijed, A_bvcd, y_bc):
    print("Entered Period2")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for i in setOFI_iActDepo_jAct[d][e][j])
                      - gp.quicksum(A_bvcd[b][v][c][d-1] * y_bc[b, c]
                                  for c in PATTERNS_FOR_TREATMENT[b]) <= 0
                     for b in TREATMENTS
                     for v in VISITS_IN_TREATMENT[b]
                     for j in ACTIVITIES_IN_VISIT[v] if j not in ACTIVITIES_DUMMY
                     for d in DAYS), name='period2')


def add_sync_constraint(model, s_i):
    print("Entered Sync")
    model.addConstrs((s_i[i] == s_i[j]
                      for i, j in SYNCHRONISED_NODE_PAIRS), name='sync')


def add_precedence1_constraint(model, s_i, D_i, delta_i):
    print("Entered Prec1")
    model.addConstrs((s_i[i] + D_i[i] * delta_i[i] <= s_i[j]
                      for i, j in PRECEDENCE_NODE_PAIRS), name='prec1')


def add_precedence2_constraint(model, s_i, D_i, G_ij):
    print("Entered Prec2")
    model.addConstrs((s_i[i] + D_i[i] + G_ij[i, j] >= s_i[j]
                     for i,j in PRECEDENCE_NODE_PAIRS), name='prec2')


def add_precedence3_constraint(model, x_ijed):
    print("Entered Prec3")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                                  for i in setOFI_iActDepo_jAct[d][e][j])
                      - gp.quicksum(x_ijed[i, k, e, d] for i in setOFI_iActDepo_jAct[d][e][k]) == 0
                      for d in DAYS
                      for e in EMPLOYEES_ON_DAY[d]
                      for j, k in SAME_EMPLOYEE_NODE_PAIRS
                      ), name='prec3')

def add_heaviness1_constraint(model, H_i, x_ijed, h_over_dg):
    print("Heaviness1")
    model.addConstrs((gp.quicksum(H_i[j] * x_ijed[i, j, e, d]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e][i])
                      <= h_over_dg[d, g]
                     for d in DAYS
                     for g in PROFESSION_GROUPS
                     for e in EMPLOYEES_ON_DAY_IN_GROUP[d][g]), name='heaviness1')


def add_heaviness2_constraint(model, H_i, x_ijed, h_under_dg):
    print("Heaviness2")
    model.addConstrs((gp.quicksum(H_i[j] * x_ijed[i, j, e, d]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e][i]) >= h_under_dg[d, g]
                     for d in DAYS
                     for g in PROFESSION_GROUPS
                     for e in EMPLOYEES_ON_DAY_IN_GROUP[d][g]), name='heaviness2')


def add_heaviness3_constraint(model, H_i, x_ijed, h_avg_over_g):
    print("Heaviness3")
    model.addConstrs((gp.quicksum(H_i[j] * x_ijed[i, j, e, d]/ len(EMPLOYEES_ON_DAY_IN_GROUP[d][g])
                                  for e in EMPLOYEES_ON_DAY_IN_GROUP[d][g]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e][i])
                      <= h_avg_over_g[g]
                     for d in DAYS
                     for g in PROFESSION_GROUPS), name='heaviness3')


def add_heaviness4_constraint(model, H_i, x_ijed, h_avg_under_g):
    print("Heaviness4")
    model.addConstrs((gp.quicksum(H_i[j] * x_ijed[i, j, e, d]/ len(EMPLOYEES_ON_DAY_IN_GROUP[d][g])
                                  for e in EMPLOYEES_ON_DAY_IN_GROUP[d][g]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e][i])
                      >= h_avg_under_g[g]
                     for d in DAYS
                     for g in PROFESSION_GROUPS), name='heaviness4')

def add_subtour_contraint(model, SUB_SETS, x_ijed):
    print("SubtourGenerator")
    model.addConstrs((gp.quicksum( x_ijed[i, j, e, d]
                                  for i in POS_SUBTOURS[d][e][S_index]
                                  for j in POS_SUBTOURS[d][e][S_index] if checkxEksist(i,j,e,d)) <= len(POS_SUBTOURS[d][e][S_index]) -1

                     for d in DAYS
                     for e in EMPLOYEES_ON_DAY[d]
                     for S_index in range (len(POS_SUBTOURS[d][e]))), name='subtour')


#Denne funskjonene forutsetter at de logstikkansatte på jobb har påfølgende ansatt ID. 
def add_symmterty_breaking_logPersonell(model, x_ijed):
    print("SymmetryLogisticPersonel")
    model.addConstrs((gp.quicksum( x_ijed[i, j, e, d]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e][i])
                      -  (gp.quicksum(x_ijed[i, j, e+1, d]
                                  for i in ACTIVITIES_DEPOT
                                  for j in setOFJ_iActDepo_jAct[d][e+1][i]))
                                 <= 0
                    for d in DAYS
                    for e in EMPLOYEES_ON_DAY_IN_GROUP[d][3] if e != getEmplLargestNum(EMPLOYEES_ON_DAY_IN_GROUP[d][3])), name='tw2')

def add_symmterty_breaking_syncAct(model, x_ijed):
    print("SymmetrySyncAct")
    model.addConstrs((gp.quicksum( e * x_ijed[l, i, e, d]
                                  for d in DAYS
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for l in setOFI_iActDepo_jAct[d][e][i])
                      -  (gp.quicksum(e* x_ijed[l, j, e, d]
                                  for d in DAYS
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for l in setOFI_iActDepo_jAct[d][e][j]))
                                 <= 0
                    for i, j in SYNCHRONISED_NODE_PAIRS), name='tw2')


def add_dummy1_constraint(model, x_ijed):
    print("Entered dummy1")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                                  for d in DAYS
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for i in setOFI_iAct_jAct[d][e][j])
                      == 0
                      for j in ACTIVITIES_DUMMY), name='dummy1')
    
def add_dummy2_constraint(model, x_ijed):
    print("Entered dummy2")
    model.addConstrs((gp.quicksum(x_ijed[i, j, e, d]
                                  for d in DAYS
                                  for e in EMPLOYEES_ON_DAY[d]
                                  for j in setOFJ_iAct_jAct[d][e][i])
                      == 0
                      for i in ACTIVITIES_DUMMY), name='dummy2')