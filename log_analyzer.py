import json
from collections import Counter

def analyze_logs(file_path):
    with open(file_path, 'r') as f:
        logs = [json.loads(line) for line in f]

    error_levels = Counter(log['level'] for log in logs)
    modules = Counter(log['module'] for log in logs if log['level'] == 'ERROR')

    print("📊 Log Summary:")
    print("---------------")
    for level, count in error_levels.items():
        print(f"{level}: {count}")
    print("\nModules with most ERRORs:")
    for mod, count in modules.most_common(5):
        print(f"{mod}: {count}")

if __name__ == "__main__":
    path = input("Enter JSON log file path: ")
    analyze_logs(path)
