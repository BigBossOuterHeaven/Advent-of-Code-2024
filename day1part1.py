def calculate_total_distance(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

file_path = '/Users/macbookair/Desktop/columns.txt'
total_distance = calculate_total_distance(file_path)
print(f"The total distance between the lists is: {total_distance}")