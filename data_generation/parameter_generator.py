from .data import *
from .set_generator import *
import math

from .distance_matrix import travel_matrix


D_i = {key: int for key in ACTIVITIES}
T_earliest_i =  {key: int for key in ACTIVITIES} #idexed by day and employee
T_latest_i = {key: int for key in ACTIVITIES}
H_i = {key: int for key in ACTIVITIES}
Q_i = {key: int for key in ACTIVITIES}


for node in nested_dict_nodes:
    D_i[node] = nested_dict_nodes[node]['duration']
    T_earliest_i[node] = nested_dict_nodes[node]['earliestStartTime']
    T_latest_i[node] = nested_dict_nodes[node]['latestStartTime']
    H_i[node] = nested_dict_nodes[node]['heaviness']
    Q_i[node] = nested_dict_nodes[node]['skillRequirement']

#Maximum time intervall between acitivy i and actitity j
G_ij = {key: [] for key in PRECEDENCE_NODE_PAIRS}

#Den skal gjelde for alle parr i precedence. Settes til tusen for de som ikke har avhengighet
for pres_pair in PRECEDENCE_NODE_PAIRS:
    for second_node in nested_dict_nodes[pres_pair[0]]['nextPrece']:
        if not isinstance(second_node, int) and pres_pair[1] == int(second_node.split(":")[0]):
            G_ij[pres_pair] = int(second_node.split(":")[1])
        else:
            G_ij[pres_pair] = 10000


#Start time for employee

S_start_de = {day: {employee: [] for employee in EMPLOYEES_ON_DAY[day]} for day in DAYS}     #start time for employee
S_end_de = {day: {employee: [] for employee in EMPLOYEES_ON_DAY[day]} for day in DAYS}      #end time for employee e shift on day d
Q_e = {employee: [] for employee in EMPLOYEES}        #qualification level of employee e


for employee in EMPLOYEES:
    Q_e[employee] = nested_dict_employees[employee]["professionalLevel"]
    for shift in list(nested_dict_employees[employee]["schedule"]):
        S_start_de[nested_dict_shifts[shift]["Day"]][employee] = nested_dict_shifts[shift]["Start"]
        S_end_de[nested_dict_shifts[shift]["Day"]][employee] = nested_dict_shifts[shift]["End"]


A_bvcd = {treatment: {visit: {pattern: [] for pattern in PATTERNS_FOR_TREATMENT[treatment]}
                     for visit in VISITS_IN_TREATMENT[treatment]}
         for treatment in TREATMENTS}           #1 if visit v is assigned to day d in pattern c, 0 otherwiseP

for treatment in TREATMENTS:
    counter = 0
    visit_counter = 0
    for visit in VISITS_IN_TREATMENT[treatment]:
        visit_counter += 1
        for pattern in nested_dict_patterns[PATTERNTYPE_FOR_TREATMENT[treatment]]:
            # Nå ser vi på alle patterns for denne behandlingen visitet inngår i
            plan = nested_dict_patterns[PATTERNTYPE_FOR_TREATMENT[treatment]][pattern]
            visit_plan = [0] * len(DAYS)
            pattern_counter = 1
            for i in range(len(plan)):
                if plan[i] == 1 and visit_counter == pattern_counter:
                    visit_plan[i] = 1
                if plan[i] == 1:
                    pattern_counter += 1
            A_bvcd[treatment][visit][pattern] = visit_plan

S_p = {patient: [] for patient in PATIENTS}            #suitability score for home treatment for patient p
for node in nested_dict_nodes:
    if not S_p[nested_dict_nodes[node]['patientId']]:
        S_p[nested_dict_nodes[node]['patientId']] = nested_dict_nodes[node]["utility"]

# driving time between activity i and j
T_ij = {i: {j: float for j in ACTIVITIES_DEPOT for i in ACTIVITIES_DEPOT}}

'''
df_distance = pd.read_csv(os.getcwd()+'/Input/'+reading_instance_file+'/Distances.csv')
dict_distances = df_distance.to_dict(orient='records')
'''
#NY MÅTE FRA MASTER
depot_row = pd.DataFrame({'activityId': [0], 'location': [(59.9365, 10.7396)]})
depot_row = depot_row.set_index(['activityId'])
# Legger til depot_row i begynnelsen av df_activities
df_activities_depot = pd.concat([depot_row, df_nodes], axis=0)

T_ij = travel_matrix(df_activities_depot)
'''
T_ij = {i: {j: float for j in ACTIVITIES_DEPOT} for i in ACTIVITIES_DEPOT}

for arc in dict_distances:
    nodes = arc['Unnamed: 0'].replace("'","").replace("(","").replace(")","")
    nodes_list = list(nodes.split(", "))
    T_ij[int(nodes_list[0])][int(nodes_list[1])] = float(arc['0'])
'''
S_end_de_as_list = []
S_start_de_as_list = []
for day in DAYS:
    for employee in EMPLOYEES_ON_DAY[day]:
        S_start_de_as_list.append(S_start_de[day][employee])
        S_end_de_as_list.append(S_end_de[day][employee])

# big M_ij for constraints tw1
bigM_ij_tw1 = {activity_i: {activity_j: int for activity_j in ACTIVITIES} for activity_i in ACTIVITIES}
for i in ACTIVITIES:
    for j in ACTIVITIES:
        bigM_ij_tw1[i][j] = T_latest_i[i] + D_i[i] + math.ceil(T_ij[i][j])

# big M_j for constraints tw2
bigM_j_tw2 = {activity_j: int for activity_j in  ACTIVITIES}
for j in ACTIVITIES:
    bigM_j_tw2[j] = math.ceil(T_ij[0][j]) 


# big M_i for constraints tw3
bigM_i_tw3 = {activity_j: int for activity_j in  ACTIVITIES}
for i in ACTIVITIES:
    bigM_i_tw3[i] = D_i[i] + math.ceil(T_ij[i][0]) + T_latest_i[i]
