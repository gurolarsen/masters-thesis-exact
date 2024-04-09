from .set_generator import  *
from .parameter_generator import *

patient_history = {key: [] for key in PATIENTS}
continuity_groups = []

for node in nested_dict_nodes:
    if len(nested_dict_nodes[node]['employeeHistory']) >= len(patient_history[nested_dict_nodes[node]['patient']]):
        patient_history[nested_dict_nodes[node]['patient']] = nested_dict_nodes[node]['employeeHistory']
    if nested_dict_nodes[node]['continuityGroup'] not in continuity_groups:
        continuity_groups.append(nested_dict_nodes[node]['continuityGroup'])

contintyGroup_Bar = {key: float for key in continuity_groups}
#DETTE UNDER  MA  SPESSIFISERES I FORHOLD TIL DATASETTET DET KJORES PÅ
contintyGroup_Bar[1] = 0.4
contintyGroup_Bar[2] = 0.3
contintyGroup_Bar[3] = 0.1

def checkContinity(i, e, d):
    if i not in ACTIVITIES_HEALTH_CARE:
        return True
    patient = nested_dict_nodes[i].get('patient')
    y = 10
    y = min(y, len(patient_history[patient]))
    count_e = 0
    count_other = 0
    for index in range(y):
        if patient_history[patient][index] in EMPLOYEES_ON_DAY[d] and patient_history[patient][index] != e:
            count_other += 1
        if patient_history[patient][index] == e:
            count_e += 1
    if count_other + count_e == 0:
        return True
    return count_e/(count_other+count_e) >= contintyGroup_Bar[nested_dict_nodes[i].get('continuityGroup')]

def checkTimeWindow(i,j):
    return T_earliest_i[i] + D_i[i] + T_ij[i][j] <= T_latest_i[j]

def checkPattern(i, d):
    for pattern in A_bvcd[nested_dict_nodes[i].get('treatment')][nested_dict_nodes[i].get('visit')]:
        if A_bvcd[nested_dict_nodes[i].get('treatment')][nested_dict_nodes[i].get('visit')][pattern][d - 1] == 1:
            return True
    return False

def checkPresedens(i, j):
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

def checkSkillRequirement(i,e):
    if nested_dict_employees[e].get('SkillLevel') - nested_dict_nodes[i].get('skillRequirement') >= 0:
        return True
    return False

def getSetOfjNY(d, SETOFe, SETOFi, SETOFj):
    dict_j = {e: {i: [] for i in SETOFi} for e in SETOFe}
    for i in SETOFi:
        for j in SETOFj:
            for e in SETOFe:
                if not checkNotSameNode(i, j):
                    continue
                if i == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPresedens(i,j))
                #if i == 22 and j ==  39 and d == 1 and e == 3:
                    #print("checkPattern(j,d)",checkPattern(j,d))
                    #print("checkSkillRequirement(j,e)",checkSkillRequirement(j,e))
                    #print("checkEmployeeRestriction(j,e)",checkEmployeeRestriction(j,e))
                    #print("checkPattern(i,d)",checkPattern(i,d))
                    #print("checkSkillRequirement(i,e)",checkSkillRequirement(i,e))
                    #print("checkEmployeeRestriction(i,e)",checkEmployeeRestriction(i,e))
                    #print("checkTimeWindow(i,j)",checkTimeWindow(i,j))
                    #print("checkPresedens(i,j))",checkPresedens(i,j))
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
                    nodeOK = checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPresedens(i,j))
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
                    nodeOK = checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    nodeOK = checkContinity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    nodeOK = (checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPresedens(i,j))
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
                    if not checkContinity(j,e,d):
                        #print(i, j, e, d, "fjernet continuity")
                        count_continuity += 1
                    if not checkPattern(j,d):
                        #print(i, j, e, d, "fjernet pattern")
                        count_pattern += 1

                    if not checkEmployeeRestriction(j,e):
                        #print(i, j, e, d, "fjernet employeeRes")
                        count_employees += 1
                    nodeOK = checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                elif j == 0 and checkNotSameNode(i,j):
                    if not checkSkillRequirement(i,e):
                        #print(i, j, e, d, "fjernet skill")
                        count_skill += 1
                    if not checkContinity(i,e,d):
                        #print(i, j, e, d, "fjernet continuity")
                        count_continuity += 1
                    if not checkPattern(i,d):
                        #print(i, j, e, d, "fjernet pattern")
                        count_pattern += 1
                    if not checkEmployeeRestriction(i,e):
                        #print(i, j, e, d, "fjernet employeeRes")
                        count_employees += 1
                    nodeOK = checkContinity(i, e, d) and checkPattern(i, d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                else:
                    if not checkSkillRequirement(i,e) or not checkSkillRequirement(j,e):
                        #print(i, j, e, d, "fjernet skill")
                        count_skill += 1
                    if not checkContinity(i,e,d) or not checkContinity(j,e,d):
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
                    if not checkPresedens(i,j):
                        #print(i, j, e, d, "fjernet Precesens")
                        count_precedence += 1
                    nodeOK = (checkContinity(j,e,d) and checkPattern(j,d) and checkSkillRequirement(j,e) and checkEmployeeRestriction(j,e)
                              and checkContinity(i,e,d) and checkPattern(i,d) and checkSkillRequirement(i,e) and checkEmployeeRestriction(i,e)
                              and checkTimeWindow(i,j) and checkPresedens(i,j))
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

