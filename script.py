import os

def process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        result = ""
        for i in range(2, len(lines), 4):
            result += lines[i].strip() + " "
    output_filename = f"{os.path.splitext(filename)[0]}.txt"
    with open(output_filename, 'w') as f:
        f.write(result)
    print(f"Wrote output to {output_filename}")

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.srt'):
            full_path = os.path.join(root, filename)
            process_file(full_path)