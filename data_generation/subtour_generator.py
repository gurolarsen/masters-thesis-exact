from set_generator import  *

#LAGE SET OF SUBTOURS
SUB_SETS = []
#Vil ha en funskjon som sjekker om det er den samme som vi allerdde har laget.
#De kan heller ikke være de samme


        #Legge til hvis ulike og ikke i sub_sets
        #for k in activities:

def checkSubset(subset):
    num = 0
    for element in subset:
        if element - num <= 0:
            return False
        num = element
    return True

for i in ACTIVITIES:
    print(i)
    for j in ACTIVITIES:
        new_set = [i,j]
        if not checkSubset(new_set):
            continue
        if new_set not in SUB_SETS:
            SUB_SETS.append(new_set)
        for k in ACTIVITIES:
            new_set = [i,j, k]
            if checkSubset(new_set) and new_set not in SUB_SETS:
                SUB_SETS.append(new_set)


print(SUB_SETS)