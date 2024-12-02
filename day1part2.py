from collections import Counter

def calculate_similarity_score(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    right_count = Counter(right_list)
    
    similarity_score = sum(left * right_count[left] for left in left_list)
    
    return similarity_score

file_path = '/Users/macbookair/Desktop/columns.txt'
similarity_score = calculate_similarity_score(file_path)
print(f"The similarity score between the lists is: {similarity_score}")