import pandas as pd
import copy
import os

# Reading instance
reading_instance_file = "newDataStructure"
print("RUNNING MODEL FOR TEST INSTANCE: ", reading_instance_file)
#Her kan jeg lage funksjon som adder ekstra aktiviteter som er dumme:))
df_nodes = pd.read_csv(os.getcwd()+'/Input/'+reading_instance_file+'/activitiesNewTimeWindows.csv')
df_employees = pd.read_csv(os.getcwd()+'/Input/'+reading_instance_file+'/employees.csv')
df_shifts = pd.read_csv(os.getcwd()+'/Input/Shifts.csv')
df_patterns = pd.read_csv(os.getcwd()+'/Input/Patterns.csv')

#Funksjon for å legge til dummy nodes nederst
def add_dummy_nodes(df_nodes, df_employees, file_path):
    # Remove previously added dummy nodes
    print(f"Original number of activities: {len(df_nodes)}")
    df_nodes_new = df_nodes[df_nodes['activityType'] != 'D']
    print(f"Number of activities after removing 'D': {len(df_nodes_new)}")
    df_nodes_new.to_csv(file_path, index=False)

    max_activity_id = df_nodes_new['activityId'].max()
    max_visit_id = df_nodes_new['visitId'].max()
    max_treatment_id = df_nodes_new['treatmentId'].max()
    max_patient_id = df_nodes_new['patientId'].max()
    days = [1,2,3,4,5]
    employees = []
    for employee_id in df_employees['employeeId']:
        if employee_id not in employees:
            employees.append(employee_id)
    
    dummy_activities = []
    restricted_employees = employees
    emp_count = 0

   
    for empl in employees:
        restricted_employees = copy.copy(employees)
        restricted_employees.remove(empl)
        for day in days:
            max_activity_id += 1
            max_visit_id += 1
            max_treatment_id += 1
            max_patient_id += 1
            dummy_activity = {
                'activityId': max_activity_id,
                'patientId': max_patient_id,  
                'activityType': 'D',
                'numActivitiesInVisit': 1,
                'earliestStartTime': 480,
                'latestStartTime': 960,
                'duration': 0,
                'skillRequirement': 1,
                'visitId': max_visit_id, 
                'treatmentId': max_treatment_id,
                'location': '(59.9365, 10.7396)',
                #'employeeRestriction': [restricted_employees],
                'heaviness': 0,
                'utility': 0,
                'allocation': 0, 
                'patternType': 6,
                'continuityGroup': 1,
                'a_complexity': 0,
                'v_complexity': 0,
                'nActInTreat': 1,
                't_complexity': 0,
                'nActInPatient': 1,
            }
            dummy_activities.append(dummy_activity)

    df_dummy_activities = pd.DataFrame(dummy_activities)
    df_nodes_new = pd.concat([df_nodes_new, df_dummy_activities], ignore_index=True)
    df_nodes_new.to_csv(file_path, index=False)

# Usage
activities_file_path = os.getcwd()+'/Input/'+reading_instance_file+'/activitiesNewTimeWindows.csv'
add_dummy_nodes(df_nodes, df_employees, activities_file_path)

# Funksjon for å konvertere formatet på nextPrece-kolonnen
def convert_precedence_format(s):
    if isinstance(s, str):
        parts = s.split(", ")
        if ":" in s:
            keys = [part.split(":")[0] for part in parts if ":" in part]
            value = parts[0].split(":")[1].strip() if ":" in parts[0] else ""
            return f"({', '.join(keys)}: {value})" if keys else "()"
        else:
            return f"({s})"
    elif pd.isna(s):
        return "()"
    else:
        return f"({s})"
df_nodes['nextPrece'] = df_nodes['nextPrece'].apply(convert_precedence_format)

# Funksjon for å konvertere formatet på employee history fra "[1, 2, 3]" til "(1, 2, 3)"
def convert_employee_history_format(s):
    if not s or s == "[]":
        return "()"
    elif pd.isna(s):
        return "()"
    else:
        return s.replace('[', '(').replace(']', ')')
df_nodes['employeeHistory'] = df_nodes['employeeHistory'].apply(convert_employee_history_format)

# Funksjon for å konvertere formatet på employee restriction"
def convert_employee_restriction_format(s):
    if pd.isna(s):
        return "()"
    else:
        return s.replace('[', '(').replace(']', ')')
df_nodes['employeeRestriction'] = df_nodes['employeeRestriction'].apply(convert_employee_restriction_format)

dict_nodes = df_nodes.to_dict(orient='records')
dict_employees = df_employees.to_dict(orient='records')
dict_patterns = df_patterns.to_dict(orient='records')
dict_shifts = df_shifts.to_dict(orient='records')

def convert_numbers_to_int_or_float(d):
    if isinstance(d, list):
        for i, item in enumerate(d):
            if isinstance(item, str):
                if item.isdigit():
                    d[i] = int(item)
                elif is_float(item):
                    d[i] = float(item)
    elif isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, str):
                if value.isdigit():
                    d[key] = int(value)
                elif is_float(value):
                    d[key] = float(value)
            elif isinstance(value, (list, dict)):
                convert_numbers_to_int_or_float(value)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def clean_nodes_data(dict):
    nested_dict_nodes = {}
    for record in dict_nodes:
        # Cleaning
        for key, value in record.items():
            # Convert values with parantheses to lists
            if isinstance(value, str) and '(' in value and ')' in value:
                value_list = value.strip('()').split(', ')
                record[key] = value_list
        # Nested dictionary where the key is the Activity id
        employee_id = record['activityId']
        nested_dict_nodes[employee_id] = record
        # Convert numbers from str to int
        convert_numbers_to_int_or_float(nested_dict_nodes)
        # Convert [''] to empty lists []
        for record in nested_dict_nodes.values():
            for key, value in record.items():
                if isinstance(value, list) and value == ['']:
                    record[key] = []
    return nested_dict_nodes

def clean_employee_data(dict):
    nested_dict_employees = {}
    for record in dict_employees:
        #Cleaning
        for key, value in record.items():
            #Convert values with parantheses to lists
            if isinstance(value, str) and '[' in value and ']' in value:
                value_list = value.strip('[]').split(', ')
                record[key] = value_list
        #Nested dictionary where the key is the EmployeeID
        employee_id = record['employeeId']
        nested_dict_employees[employee_id] = record
        # Convert numbers from str to int
        convert_numbers_to_int_or_float(nested_dict_employees)
        # Convert [''] to empty lists []
        for record in nested_dict_employees.values():
            for key, value in record.items():
                if isinstance(value, list) and value == ['']:
                    record[key] = []
    return nested_dict_employees

def clean_pattern_data(dict_pattern):
    #Lager de listene forst, også konstruere dictionarien etterpå
    frekvenser = []
    for monster in dict_patterns:
        if monster['Frekvens'] not in frekvenser:
            frekvenser.append(monster['Frekvens'])
    nested_dict_patterns = {key: {} for key in frekvenser}

    for monster in dict_patterns:
        pattern = []
        for element in monster.values():
            pattern.append(element)
        pattern.pop(0)
        pattern.pop(0)
        nested_dict_patterns[monster['Frekvens']][monster['Mønster']] = pattern
    return nested_dict_patterns

def clean_shift_data(shift_dict):
    nested_dict_shifts = {}
    for record in shift_dict:
        shift_id = record['Shift']
        nested_dict_shifts[shift_id] = record
    return nested_dict_shifts

nested_dict_nodes = clean_nodes_data(dict_nodes)
nested_dict_employees = clean_employee_data(dict_employees)
nested_dict_patterns = clean_pattern_data(dict_patterns)
nested_dict_shifts = clean_shift_data(dict_shifts)

