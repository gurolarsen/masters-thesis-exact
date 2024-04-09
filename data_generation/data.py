import pandas as pd
import os

# Reading instance
reading_instance_file = "base150a6e"
print("RUNNING MODEL FOR TEST INSTANCE: ", reading_instance_file)
df_nodes = pd.read_csv(os.getcwd()+'/Input/'+reading_instance_file+'/Nodes.csv')
df_employees = pd.read_csv(os.getcwd()+'/Input/'+reading_instance_file+'/Employees.csv')
df_shifts = pd.read_csv(os.getcwd()+'/Input/Shifts.csv')
df_patterns = pd.read_csv(os.getcwd()+'/Input/Patterns.csv')

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
        employee_id = record['id']
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
            if isinstance(value, str) and '(' in value and ')' in value:
                value_list = value.strip('()').split(', ')
                record[key] = value_list
        #Nested dictionary where the key is the EmployeeID
        employee_id = record['EmployeeID']
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

