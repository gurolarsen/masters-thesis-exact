from data_generation.data import weight_DW, weight_WW, weight_S, weight_SG 

def process_results(file_path):
    # Initialize storage for parsed data
    assignments = []
    start_times = {}
    objective = []
    objective2 = []

    # Read and parse the file
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('x_'):
                parts = line.split()
                variable, value = parts[0], float(parts[1])
                if value == 1.0:
                    _, activity_from, activity_to, employee, day = variable.split('_')
                    assignments.append((int(activity_to), int(employee), int(day)))
            elif line.startswith('s_'):
                parts = line.split()
                variable, start_time = parts[0], float(parts[1])
                activity = int(variable.split('_')[1])
                start_times[activity] = start_time
            if line.startswith('Solution count '):
                parts = line.split()
                objective.append(parts[3])
            if line.startswith("Solution:"): 
                parts = line.split()
                objective2 = parts[3:7]
                del parts[3:7]
                print(parts, "parts")
                del parts[0]
                print("parts", parts)
                if len(objective) != 4: 
                    objective = objective + [0 for i in range(4-len(objective))]
                if objective[0] == 0:  
                    objective[0] = parts[0]
                if objective[2] == 0:  
                    objective[2] = parts[1]
                if objective[3] == 0:  
                    objective[3] = parts[2]
               
    print("objective2", objective2)
    print("objective", objective)
    objective2 = [float(obj) for obj in objective2]
    objective[1] = objective2[0]/weight_DW + objective2[1]/weight_WW + objective2[2]/weight_S + objective2[3]/weight_SG
    



    # Organize data by day and employee
    organized_info = {}
    for activity, employee, day in assignments:
        if day not in organized_info:
            organized_info[day] = {}
        if employee not in organized_info[day]:
            organized_info[day][employee] = []
        if activity in start_times:  # Ensure there's a start time
            organized_info[day][employee].append((activity, start_times[activity]))

    # Sort the data
    for day in organized_info:
        for employee in organized_info[day]:
            organized_info[day][employee].sort(key=lambda x: x[1])

    # Write the organized information to a new file
    output_file_path = file_path.replace('.txt', '_organized.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"objective {objective}\n")
        output_file.write(f"objective2 {objective2}\n")
        output_file.write(f"    \n")
        for day in sorted(organized_info):
            for employee in sorted(organized_info[day]):
                output_file.write(f"DAG {day} ANSATT {employee}\n")
                for activity, start_time in organized_info[day][employee]:
                    output_file.write(f"activity {activity} start {start_time}\n")
                output_file.write("---------------------\n")

    return output_file_path

# Path to the uploaded results.txt file
username = 'agnesost'
file_path = 'c:\\Users\\'+username+'\\masters-thesis-exact\\results1.txt'
output_path = process_results(file_path)
