from typing import List

from data import *
from set_generator import *
import json
import requests
import pandas as pd


def get_coordinates_string_from_list(list):
    coordinates_string = ";".join(str(item) for item in list)
    return coordinates_string.replace("(", "").replace(")", "").replace(" ", "").replace("[","").replace("]","")

def get_distance_matrix(coordinates_string):
    # Documntation for this API: http://project-osrm.org/docs/v5.10.0/api/#general-options
    url = 'http://router.project-osrm.org/table/v1/driving/'+coordinates_string+''
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'durations' in data:  # Make sure 'durations' key exists
            # Process and return the durations data as needed
            return data['durations']
        else:
            # 'durations' key does not exist, return a default value or handle the error as appropriate
            print("Durations data not provided in the API response.")
            return None  # You could return an empty list or dict instead, depending on your use case
    else:
        # The API did not return a successful response
        print(f"Error fetching data: {response.status_code}")
        return None


#HAR LAGET EN DICTIONARY MED ALLE AKTIVITETER OG DEPOET
nested_dict_nodes_depot = {0:{'location':[59.9365, 10.7396]}}
nested_dict_nodes_depot.update(nested_dict_nodes)


#LAGER LISTE MED ALLE PASIENTENE PLUSS DEPOET OG SORTERER DEN I STIGENDE REKKEFØLGE
patients_with_depo = [0]
patients_with_depo.extend(PATIENTS)


#LAGER EN LISTE MED ALLE LOKASJONER MED INDEX TILHØRENDE PASIENT
#patients_coordinate_list = [None]* (len(patients_with_depo)) #Ser bort fra dednne nå, for alt skal i dict

#LAGE DICTIONARY HVOR INDEXEN KOMMER FREM, DA TRENGER VI EGENTLIG IKKE HA DEN PASIENT LISTEN
patients_coordinate_dict = {patient: {'index': int, 'location': tuple } for patient in patients_with_depo}

#Legger inn indexen de skal ha i string_listen inn i dictionarien
index_count = 0
for patient in patients_coordinate_dict:
    patients_coordinate_dict[patient]['index'] = index_count
    index_count += 1

#Vil nå legge inn locasjonen ded skal ha i dictionarien
for node in nested_dict_nodes:
    if ((nested_dict_nodes[node]['location'][0] - nested_dict_nodes_depot[0]['location'][0] != 0)
            and (nested_dict_nodes[node]['location'][1] - nested_dict_nodes_depot[0]['location'][0] != 0)):
        patients_coordinate_dict[nested_dict_nodes[node]['patient']]['location'] = (nested_dict_nodes_depot[node]['location'][1], nested_dict_nodes_depot[node]['location'][0])


#Legger til depot lokasjonen
depot_location = (10.7396, 59.9365)
patients_coordinate_dict[0]['location'] = depot_location


#Lage listen som skal sendes inn i funskjonen
patients_coordinate_list = []
for patient in patients_coordinate_dict:
    patients_coordinate_list.append(patients_coordinate_dict[patient]['location'])

#Kjører funskjonen som henter ut lsiten med koordinater som string
coordinate_string_patient = get_coordinates_string_from_list(patients_coordinate_list)
duration_matrix_patients = get_distance_matrix(coordinate_string_patient)

T_ij_todf = {i: {j: float for j in ACTIVITIES_DEPOT} for i in ACTIVITIES_DEPOT}
for i in ACTIVITIES_DEPOT:
    #hvis lokasjon til i er sykehus så må hente
    if nested_dict_nodes_depot[i]['location'] == [depot_location[1], depot_location[0]]:
        index_loc_i= 0
    else:
        index_loc_i = patients_coordinate_dict[nested_dict_nodes_depot[i]['patient']]['index']
    for j in ACTIVITIES_DEPOT:
        if nested_dict_nodes_depot[j]['location'] == [depot_location[1], depot_location[0]]:
            index_loc_j = 0
        else:
            index_loc_j = patients_coordinate_dict[nested_dict_nodes_depot[j]['patient']]['index']
        T_ij_todf[i][j] = round(duration_matrix_patients[index_loc_i][index_loc_j] / 60, 4)

T_ij_dataframe = pd.DataFrame.from_dict({(i,j): T_ij_todf[i][j]
                           for i in T_ij_todf.keys()
                           for j in T_ij_todf[i].keys()},
                       orient='index')


path = (os.getcwd()+'/Input/'+reading_instance_file+'/Distances.csv')
pd.DataFrame.to_csv(self=T_ij_dataframe, path_or_buf=path)

#Hente tilbake fra CSV fila til en dictionary.




