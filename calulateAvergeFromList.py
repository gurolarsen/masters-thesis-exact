def calculate_averages(list_of_lists):
    # Transpose the list of lists to group elements by index
    transposed = list(zip(*list_of_lists))
    
    # Calculate the average for each group
    averages = [round(sum(group) / len(group),2) for group in transposed]
    
    return averages

# Example usage:
list_of_lists = [
    [29.0, 5, 184, 0],
    [29.0, 5, 301, 0],
    [35.25, 5, 307, 0]
]

averages = calculate_averages(list_of_lists)
print(averages)