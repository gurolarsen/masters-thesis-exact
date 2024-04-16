from .set_generator import  *
from .parameter_generator import *
from .data import *

def checkSkillRequirement(i,e):
    if nested_dict_employees[e].get('professionalLevel') - nested_dict_nodes[i].get('skillRequirement') >= 0:
        return True
    return False

patient_history = {key: [] for key in PATIENTS}
continuity_groups = []

#print("nested_dict_nodes[17]['employeeHistory']", nested_dict_nodes[17]['employeeHistory'])
#print("type(nested_dict_nodes[17]['employeeHistory']", type(nested_dict_nodes[17]['employeeHistory']))

#Gammelt, trengs ikke lenger 
'''
#['1,2,3,4,5,6']
def getHistoryList(list_tuple_in_list):
    employee_history_list = []
    if len(list_tuple_in_list) == 0:
        return []
    else: 
    #if not isinstance(list_tuple_in_list, int):
       # print(list_tuple_in_list[0])
       # print(type(list_tuple_in_list[0]))
        if isinstance(list_tuple_in_list[0], int): 
            employee_history_list = list_tuple_in_list
        else: 
            for employee in list_tuple_in_list[0].replace("'", "").split(","):
                employee_history_list.append(int(employee))
    return employee_history_list
'''
for node in nested_dict_nodes:
    '''
    if len(getHistoryList(nested_dict_nodes[node]['employeeHistory'])) >= len(patient_history[nested_dict_nodes[node]['patientId']]):
        patient_history[nested_dict_nodes[node]['patientId']] = getHistoryList(nested_dict_nodes[node]['employeeHistory'])
    '''
#Lager settet av kontinuitetsgruppr
    if nested_dict_nodes[node]['continuityGroup'] not in continuity_groups:
        continuity_groups.append(nested_dict_nodes[node]['continuityGroup'])


contintyGroup_Bar = {group: {'bar': float, 'numEmp': int} for group in continuity_groups}
#DETTE UNDER  MA  SPESSIFISERES I FORHOLD TIL DATASETTET DET KJORES PÅ. ER PARAMETERE.
contintyGroup_Bar[1]['bar'] = 0
contintyGroup_Bar[2]['bar'] = 0
contintyGroup_Bar[3]['bar'] = 0
contintyGroup_Bar[1]['numEmp'] = 100
contintyGroup_Bar[2]['numEmp'] = 100
contintyGroup_Bar[3]['numEmp'] = 100


#DEN UNDER ER GAMMEL FOR Å SJEKKE KONTINUITET, KAN NOK SLETTES ETTERHVERT
'''
def checkContinuity(i, e, d):
    if i not in ACTIVITIES_HEALTH_CARE:
        return True
    patient = nested_dict_nodes[i].get('patient')
    count_e = 0
    count_other = 0
    for index in range(len(patient_history[patient])):
        if patient_history[patient][index] in EMPLOYEES_ON_DAY[d] and patient_history[patient][index] != e:
            count_other += 1
        if patient_history[patient][index] == e:
            count_e += 1
    if count_other + count_e == 0:
        return True
    return count_e/(count_other+count_e) >= contintyGroup_Bar[nested_dict_nodes[i].get('continuityGroup')]['bar']
'''

#ANTAR AT VI LESER HELE PASIENTHISTORIKKEN,
# FORDI DET IKKE VIL VÆRE GUNSTIG Å SETTE INN MER PASIENTHUSTORIKK ENN VI SKAL LESE
def checkContinuity(i, e, d):
    patient = nested_dict_nodes[i].get('patientId')
    if i not in ACTIVITIES_HEALTH_CARE or len(patient_history[patient]) == 0:
        return True
    #MA FØRST TELLE EGET ANTALL.
    employee_act_count = 0
    for employee in patient_history[patient]:
        if employee == e:
            employee_act_count += 1

    #SKAL SJEKKE EMPLOYEES ANTALL OPP MOT ANDRE

    sum_other_employees_activity_count = 0
    number_of_better_employees = 0
    for other_employee in EMPLOYEES_ON_DAY[d]:
        other_employee_act_count = 0
        if not checkSkillRequirement(i, other_employee):
            continue
        for employee in patient_history[patient]:
            if employee == other_employee:
                other_employee_act_count += 1
        if other_employee_act_count > employee_act_count:
            number_of_better_employees += 1
        sum_other_employees_activity_count += other_employee_act_count

    #kan være at ingen av de som står på employee history er på jobb denn dagen 

    if (sum_other_employees_activity_count+employee_act_count) == 0: 
        okOverContinuityBar = True
    else: 
        okOverContinuityBar = employee_act_count/(sum_other_employees_activity_count+employee_act_count) >= contintyGroup_Bar[nested_dict_nodes[i].get('continuityGroup')]['bar']
    okInPriorityList = number_of_better_employees < contintyGroup_Bar[nested_dict_nodes[i].get('continuityGroup')]['numEmp']
    return okInPriorityList or okOverContinuityBar



def checkTimeWindow(i,j):
    return T_earliest_i[i] + D_i[i] + T_ij[i][j] <= T_latest_i[j]

def checkPattern(i, d):
    for pattern in A_bvcd[nested_dict_nodes[i].get('treatmentId')][nested_dict_nodes[i].get('visitId')]:
        if A_bvcd[nested_dict_nodes[i].get('treatmentId')][nested_dict_nodes[i].get('visitId')][pattern][d - 1] == 1:
            return True
    return False

def checkPrecedence(i, j):
    if (j, i) in PRECEDENCE_NODE_PAIRS:
        return False
    return True

def checkNotSameNode(i, j):
    if i == j:
        return False
    return True

def checkEmployeeRestriction(i,e):
    if e in nested_dict_nodes[i].get('employeeRestriction'):
        return False
    return True



def getSetOfjNY(d, SETOFe, SETOFi, SETOFj):
    dict_j = {e: {i: [] for i in SETOFi} for e in SETOFe}
    for i in SETOFi:
        for j in SETOFj:
            for e in SETOFe:
                if not checkNotSameNode(i, j):
                    continue
                if i == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinuity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPrecedence(i,j))
                #if i == 22 and j ==  39 and d == 1 and e == 3:
                    #print("checkPattern(j,d)",checkPattern(j,d))
                    #print("checkSkillRequirement(j,e)",checkSkillRequirement(j,e))
                    #print("checkEmployeeRestriction(j,e)",checkEmployeeRestriction(j,e))
                    #print("checkPattern(i,d)",checkPattern(i,d))
                    #print("checkSkillRequirement(i,e)",checkSkillRequirement(i,e))
                    #print("checkEmployeeRestriction(i,e)",checkEmployeeRestriction(i,e))
                    #print("checkTimeWindow(i,j)",checkTimeWindow(i,j))
                    #print("checkPrecedence(i,j))",checkPrecedence(i,j))
                if nodeOK:
                    dict_j[e][i].append(j)
    return dict_j


def getSetOfiNY(d, SETOFe,  SETOFi, SETOFj):
    #Ser på kombinasjonen av i til j. For kombinasjoner av j, hva er lov av i da
    dict_i = {e: {j: [] for j in SETOFj} for e in SETOFe}
    for i in SETOFi:
        for j in SETOFj:
            for e in SETOFe:
                if not checkNotSameNode(i, j):
                    continue
                if i == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinuity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPrecedence(i,j))
                if nodeOK:
                    dict_i[e][j].append(i)
    return dict_i

def getSetOfeNY(d, SETOFe, SETOFi, SETOFj):
    # Ser på kombinasjon av e til (i,j). For ulike (i,j), hva er lovlig?
    dict_e =  {i: {j: [] for j in SETOFj} for i in SETOFi}
    for i in SETOFi:
        for j in SETOFj:
            for e in SETOFe:
                if not checkNotSameNode(i, j):
                    continue
                if i == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinuity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinuity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPrecedence(i,j))
                if nodeOK:
                    dict_e[i][j].append(e)
    return dict_e


#DENNE KAN BRUKES TIL Å TELLE HVOR MANGE SOM FJERNES PGA DE ULIKE DELENE AV PREPROSSESING
def getSetOfjWITHCOUNT(d, SETOFe, SETOFi, SETOFj):
    dict_j = {e: {i: [] for i in SETOFi} for e in SETOFe}
    count_continuity = 0
    count_pattern = 0
    count_skill = 0
    count_employees = 0
    count_timewindow = 0
    count_precedence = 0
    for i in SETOFi:
        for j in SETOFj:
            for e in SETOFe:
                if not checkNotSameNode(i, j):
                    continue
                if i == 0 and checkNotSameNode(i,j):
                    if not checkSkillRequirement(j,e):
                        #print(i, j, e, d, "fjernet skill")
                        count_skill += 1
                    if not checkContinuity(j,e,d):
                        #print(i, j, e, d, "fjernet continuity")
                        count_continuity += 1
                    if not checkPattern(j,d):
                        #print(i, j, e, d, "fjernet pattern")
                        count_pattern += 1

                    if not checkEmployeeRestriction(j,e):
                        #print(i, j, e, d, "fjernet employeeRes")
                        count_employees += 1
                    nodeOK = checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    if not checkSkillRequirement(i,e):
                        #print(i, j, e, d, "fjernet skill")
                        count_skill += 1
                    if not checkContinuity(i,e,d):
                        #print(i, j, e, d, "fjernet continuity")
                        count_continuity += 1
                    if not checkPattern(i,d):
                        #print(i, j, e, d, "fjernet pattern")
                        count_pattern += 1
                    if not checkEmployeeRestriction(i,e):
                        #print(i, j, e, d, "fjernet employeeRes")
                        count_employees += 1
                    nodeOK = checkContinuity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    if not checkSkillRequirement(i,e) or not checkSkillRequirement(j,e):
                        #print(i, j, e, d, "fjernet skill")
                        count_skill += 1
                    if not checkContinuity(i,e,d) or not checkContinuity(j,e,d):
                        #print(i, j, e, d, "fjernet continuity")
                        count_continuity += 1
                    if not checkPattern(i,d) or not checkPattern(j,d):
                        #print(i, j, e, d, "fjernet pattern")
                        count_pattern += 1
                    if not checkEmployeeRestriction(i,e) or not checkEmployeeRestriction(j,e):
                        #print(i, j, e, d, "fjernet employeeRes")
                        count_employees += 1
                    if not checkTimeWindow(i,j):
                        #print(i, j, e, d, "fjernet timeWindow")
                        count_timewindow += 1
                    if not checkPrecedence(i,j):
                        #print(i, j, e, d, "fjernet Precesens")
                        count_precedence += 1
                    nodeOK = (checkContinuity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinuity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPrecedence(i,j))
                if nodeOK:
                    dict_j[e][i].append(j)
    print("count_continuity",count_continuity)
    print("count_pattern", count_pattern)
    print("count_skill", count_skill)
    print("count_employeeres", count_employees)
    print("count_timewindow", count_timewindow)
    print("count_precedens", count_precedence)
    return dict_j

setOFJ_iActDepo_jActDepo = {d: {} for d in DAYS}
setOFJ_iAct_jActDepo = {d: {} for d in DAYS}
setOFJ_iActDepo_jAct = {d: {} for d in DAYS}
setOFJ_iAct_jAct = {d: {} for d in DAYS}

setOFI_iActDepo_jActDepo = {d: {} for d in DAYS}
setOFI_iAct_jActDepo = {d: {} for d in DAYS}
setOFI_iActDepo_jAct = {d: {} for d in DAYS}

setOFE_iAct_jAct = {d: {} for d in DAYS}
setOFE_iActDepo_jAct = {d: {} for d in DAYS}
setOFE_iAct_jActDepo= {d: {} for d in DAYS}

for d in DAYS:
    #Brukes til variable generator
    setOFJ_iActDepo_jActDepo[d] = getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES_DEPOT)
    #Brukes til VRP1
    setOFI_iActDepo_jAct[d] = getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)
    #Brukes til VRP2
    setOFJ_iActDepo_jAct[d] = getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)
    #Brukes til VRP3
    setOFI_iAct_jActDepo[d] = getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)
    #Brukes til VRP4
    setOFJ_iAct_jActDepo[d] = getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)
    setOFI_iActDepo_jAct[d] = getSetOfiNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)

    #Til TW-constraints
    setOFE_iAct_jAct[d] = getSetOfeNY(d,EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES)
    setOFE_iActDepo_jAct[d] = getSetOfeNY(d,EMPLOYEES_ON_DAY[d], ACTIVITIES_DEPOT, ACTIVITIES)
    #TW3
    setOFE_iAct_jActDepo[d] = getSetOfeNY(d,EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES_DEPOT)

    #Subtourcosntrint
    setOFJ_iAct_jAct[d] = getSetOfjNY(d, EMPLOYEES_ON_DAY[d], ACTIVITIES, ACTIVITIES)



def checkIfSgeneratesanyX(e, d, S):
    for i in S:
        if len(getSetOfjNY(d, EMPLOYEES_ON_DAY[d], S, S)[e][i]) > 0:
            return True
    return False





def checkSubset(subset):
    num = 0
    for element in subset:
        if element - num <= 0:
            return False
        num = element
    return True



# LAGER SUBSETS PÅ STØRRELSE 2 OG 3 UNDER.
#DEN BRUKES IKKE, MEN KAN KJØRES HVIS MAN VIL SE HVOR MANGE SUBTORUS SOM GENERERS I UTGANGSPUNKTET
'''
SUB_SETS = []
for i in ACTIVITIES:
    for j in ACTIVITIES:
        if not checkSubset([i, j]):
            continue
        SUB_SETS.append([i, j])
        for k in ACTIVITIES:
            if checkSubset([i, j, k]):
                SUB_SETS.append([i, j, k])
'''

def checkSameLocation(list_of_nodes):
    loc = nested_dict_nodes[list_of_nodes[0]]['location']
    for index in range(1, len(list_of_nodes)):
        if nested_dict_nodes[list_of_nodes[index]]['location'] != loc:
            return False
    return True

def checkCloseLocation(list_of_nodes, max_distance):
    for node1 in list_of_nodes:
        for node2 in list_of_nodes:
            if T_ij[node1][node2] > max_distance:
                return False
    return True

POS_SUBTOURS = {day: {employee: [] for employee in EMPLOYEES_ON_DAY[day]} for day in DAYS}
for d in DAYS:
    for e in EMPLOYEES_ON_DAY[d]:
        SUB_SETS = []
        #Skal legge til alle subtours som er mulige på denne dagen
        for i in ACTIVITIES:
            #Sjekke om den kan gjøres på denne dagen
            nodeOK = checkContinuity(i, e,d) and checkSkillRequirement(i,e) and checkPattern(i, d) and checkEmployeeRestriction(i,e)
            if not nodeOK:
                continue
            for j in ACTIVITIES:
                if not (checkSameLocation([i,j]) and checkSubset([i, j])):
                    continue
                nodeOK = checkContinuity(j, e, d) and checkSkillRequirement(j, e) and checkPattern(j,d) and checkEmployeeRestriction(j, e)
                arcOK =  checkPrecedence(i, j) and checkPrecedence(j,i) and checkTimeWindow(i,j ) and checkTimeWindow(j, i)
                if arcOK and nodeOK:
                    SUB_SETS.append([i,j])
                for k in ACTIVITIES:
                    if not (checkSubset([i, j, k]) and checkSameLocation([i,j,k])):
                        continue
                    nodeOK = checkContinuity(k, e, d) and checkSkillRequirement(k, e) and checkPattern(k, d) and checkEmployeeRestriction( k, e)
                    arcsOK = checkPrecedence(i, j) and checkPrecedence(j,k) and checkPrecedence(k,i) and checkTimeWindow(i, j) and checkTimeWindow(j,k) and checkTimeWindow(k,i)
                    arcs_inverseOK = checkPrecedence(j,i) and checkPrecedence(k,j) and checkPrecedence(i,k) and checkTimeWindow(j,i) and checkTimeWindow(k,j) and checkTimeWindow(i,k)
                    if nodeOK and (arcsOK or arcs_inverseOK):
                        SUB_SETS.append([i, j, k])

                    #Alternativ 1 er (i,j) (j,k) (k,i)
                    #Alternativ 2 er (j,i) (k,j) (i,k)

        POS_SUBTOURS[d][e] = SUB_SETS

#TELLER HVOR MANGE SUBTORUS SOM GENERERES
count = 0
for d in DAYS:
    for e in EMPLOYEES_ON_DAY[d]:
        for element in POS_SUBTOURS[d][e]:
            count += 1

def checkxEksist(i,j,e,d):
    return j in setOFJ_iActDepo_jActDepo[d][e][i]

'''
Utgangspunkt: Vi generer alle mulige kombinsjoner av subset på størrelse 2 og 3.
Dette gir 170640 subsett. 


    1) Tatt bort alle subset hvor de tikke finnes feasible arcs som utgjør en subtour i settet. 
    Det gir 58849 
    
    2) Samme geografiske lokasjon:   1610
    
    3) Distanse mellom nodene tilsvarende lav. Jeg vet ikke hvor mye dette har å si. 
    Er vel like sannsynlig at den velger ruter hvor lokasjonen    
    Tester for 15 min mellomrom i kjøretid:  19933
    Tester for 10 minutter i kjøretid: 7293
    
'''

def getEmplLargestNum(list):
    largest = None
    for element in list: 
        if largest == None or element > largest: 
            largest = element
    return largest