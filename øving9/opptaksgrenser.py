import re
full = []
try:
    with open("poenggrenser_2011.csv", "r") as f:
        for line in f:
            full.append(line.split(","))
except:
    print("File not found!")


def fix(full):
    new_full = []
    for line in full:
        new = []
        for i in line:
            new_line = re.split('[,"\n]', i)
            for j, value in enumerate(new_line):
                if(new_line[j] == "" or new_line[j] == "\n"):
                    new_line.pop(j)
            if(new_line[0] == "Alle"):
                new_line.pop(1)
            new.append(new_line)
        new_full.append(new)
    return new_full

full = fix(full)
