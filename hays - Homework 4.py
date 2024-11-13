#Logan Hays
#Lab Section 13
#11/12/24
#Sources, help given to/received from google (How to open and close files)

from pathlib import Path

path = Path('prompt.txt')

contents = path.read_text()

lines = contents.splitlines()

second_file = Path("out.txt")

out_file = open(second_file, 'w')

for line in lines:
    line = line.strip()

    if not line:
        continue

    pairs = line.split()

    output_line = ""

    for pair in pairs:
        if ":" in pair:
            key, value = pair.split(":")
            count = int(value)

            if key == 'w':
                output_line += ' ' * count
            elif key == '*':
                output_line += '*' * count

    out_file.write(output_line + "\n")

out_file.close()

print("Coding is done. Check out.file to see the output.")