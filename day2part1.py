def is_safe_report(report):
    levels = list(map(int, report.split()))
    
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return increasing or decreasing


def count_safe_reports(file_path):
    with open(file_path, 'r') as file:
        reports = file.readlines()
    
    safe_count = sum(1 for report in reports if is_safe_report(report.strip()))
    return safe_count

input_file = "/Users/macbookair/Desktop/input.txt"
safe_reports = count_safe_reports(input_file)
print(f"Number of safe reports: {safe_reports}")