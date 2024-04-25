from .data import *  #Her må det være punktum før data om arc_model skal kjøre og bare data om distance function skal kjøre. 


DAYS = [1,2,3,4,5]                       #D
skill_requirement_for_healthcare_activity = 2

ACTIVITIES = list(nested_dict_nodes.keys())                        #N
PATIENTS = []                           #P
TREATMENTS = []                         #B
VISITS = []                             #V
ACTIVITIES_DEPOT = []                   #N^0 #Ikke lost enda, usikker på hvordan skal se ut
ACTIVITIES_HEALTH_CARE = []

ACTIVITIES_WITHOUT_DUMMY = []



for node in dict_nodes:
#Folger rekkefølgen pa sets fra matematisk modell
    if node['patientId'] not in PATIENTS:
        PATIENTS.append(node['patientId'])
    if node['treatmentId'] not in TREATMENTS:
        TREATMENTS.append(node['treatmentId'])
    if node['visitId'] not in VISITS:
        VISITS.append(node['visitId'])
    if node['skillRequirement'] >= skill_requirement_for_healthcare_activity:
        ACTIVITIES_HEALTH_CARE.append((node['activityId']))
    if node['activityType'] != "D": 
        ACTIVITIES_WITHOUT_DUMMY.append((node['activityId']))



ACTIVITIES_DEPOT = ACTIVITIES.copy()
ACTIVITIES_DEPOT.insert(0, 0)

#visit in treatments
VISITS_IN_TREATMENT = {key: [] for key in TREATMENTS} #V_b
#visits for patient
VISITS_FOR_PATIENT = {key: [] for key in PATIENTS}   #V_p
#actitivties in visits
ACTIVITIES_IN_VISIT= {key: [] for key in VISITS}  #N_v

ACTIVITIES_HEALTH_CARE_FOR_PATIENT = {key: [] for key in PATIENTS}


for node in dict_nodes:
    if node['visitId'] not in VISITS_IN_TREATMENT[node['treatmentId']]:
        VISITS_IN_TREATMENT[node['treatmentId']].append(node['visitId'])
    if node['visitId'] not in VISITS_FOR_PATIENT[node['patientId']]:
        VISITS_FOR_PATIENT[node['patientId']].append(node['visitId'])
    if node['activityId'] not in ACTIVITIES_IN_VISIT[node['visitId']]:
        ACTIVITIES_IN_VISIT[node['visitId']].append(node['activityId'])
    if node['activityId'] not in ACTIVITIES_HEALTH_CARE_FOR_PATIENT[node['patientId']] and node['skillRequirement'] >= skill_requirement_for_healthcare_activity:
        ACTIVITIES_HEALTH_CARE_FOR_PATIENT[node['patientId']].append(node['activityId'])

#Set of employee groups
PROFESSION_GROUPS = []
EMPLOYEES = list(nested_dict_employees.keys())
#E#G
for employee in dict_employees:
    if employee["professionalLevel"] not in PROFESSION_GROUPS:
        PROFESSION_GROUPS.append(employee["professionalLevel"])

#Set of employees working day in group g
#Set of feasible patterns for treatment b
EMPLOYEES_ON_DAY = {key: [] for key in DAYS}    #E_d
EMPLOYEES_ON_DAY_IN_GROUP = {key: {key: [] for key in PROFESSION_GROUPS } for key in DAYS }           #E_dg

for employee in nested_dict_employees:
    shifts = list(nested_dict_employees[employee]["schedule"])
    for shift in shifts:
        day = int(shift) // 3
        if (int(shift) % 3 != 0):
            day += 1
        EMPLOYEES_ON_DAY[day].append(employee)
        EMPLOYEES_ON_DAY_IN_GROUP[day][nested_dict_employees[employee]["professionalLevel"]].append(employee)

#Dobbel dictionary som kan instansieres på
PATTERNS_FOR_TREATMENTgammel = {key: [] for key in TREATMENTS}    #C_b
PATTERNS_FOR_TREATMENT = {key: [] for key in TREATMENTS}
PATTERNTYPE_FOR_TREATMENT = {key: [] for key in TREATMENTS}

for node in nested_dict_nodes:
    PATTERNTYPE_FOR_TREATMENT[nested_dict_nodes[node]['treatmentId']] = nested_dict_nodes[node]['patternType']
    PATTERNS_FOR_TREATMENT[nested_dict_nodes[node]['treatmentId']] = (
        list(nested_dict_patterns[nested_dict_nodes[node]["patternType"]].keys()))

    #hvis listen er tom så skal vi fylle på

TREATMENTS_FOR_PATIENT = {key: [] for key in PATIENTS}
for node in nested_dict_nodes:
    if nested_dict_nodes[node]["treatmentId"] not in TREATMENTS_FOR_PATIENT[nested_dict_nodes[node]["patientId"]]:
        TREATMENTS_FOR_PATIENT[nested_dict_nodes[node]["patientId"]].append(nested_dict_nodes[node]["treatmentId"])

#Set of acitivities that should be syncroniced
#Set of activities with precedence
#Set of acitivites done by same employee
SYNCHRONISED_NODE_PAIRS = []            #I^S
PRECEDENCE_NODE_PAIRS = []              #I^P
SAME_EMPLOYEE_NODE_PAIRS = []           #I^E

def getPresNode(pres_node):
    if not isinstance(pres_node, int):
        return int(pres_node.split(":")[0])
    return pres_node

PATIENTS_ALLOCATED = []
for node in nested_dict_nodes:
    if nested_dict_nodes[node]["synchronisation"] != 0 and node < nested_dict_nodes[node]["synchronisation"] :
        SYNCHRONISED_NODE_PAIRS.append((node, nested_dict_nodes[node]["synchronisation"]))
    for pres_node in nested_dict_nodes[node]["nextPrece"]:
        PRECEDENCE_NODE_PAIRS.append((node, getPresNode(pres_node)))
    if nested_dict_nodes[node]["sameEmployeeActivityId"] != 0 and node < nested_dict_nodes[node]["sameEmployeeActivityId"] :
        SAME_EMPLOYEE_NODE_PAIRS.append((node, nested_dict_nodes[node]["sameEmployeeActivityId"]))
    if nested_dict_nodes[node]['allocation'] == 1 and nested_dict_nodes[node]['patientId'] not in PATIENTS_ALLOCATED: 
        PATIENTS_ALLOCATED.append(nested_dict_nodes[node]['patientId'] )
    



#Her ser vi på alle mulige hvor det er.
'''
Alternativer: 
1) Enten så kan vi sjekke her om det er mulig. Det er vanskelig fordi da må vi vite hvilken dag og ansatt det er, så ikke mulig
2) Kalle på de funksjonene for å sjekke om det er mulig 



'''

print("PATIENTS_ALLOCATED", PATIENTS_ALLOCATED)



ACTIVITIES_DUMMY = []
for act in ACTIVITIES: 
    if act not in ACTIVITIES_WITHOUT_DUMMY: 
        ACTIVITIES_DUMMY.append(act)