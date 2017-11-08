import re
full = []
try:
    with open("poenggrenser_2011.csv", "r") as f:
        for line in f:
            full.append(line.split(","))

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
                new.append(new_line[0])
            new_full.append(new)
        full = new_full
except:
    print("File not found!")


def alle_kom_inn():
    global full
    all = 0
    for major in full:
        if(major[1] == "Alle"):
            all += 1
    return "Antall studier hvor alle kom inn:", all

alle_kom_inn()


def snitt_ntnu():
    global full
    sum = 0
    points = 0
    for major in full:
        if(major[0][0:4] == "NTNU" and major[1] != "Alle"):
            points += float(major[1])
            sum += 1
    return "Gjennomsnittlig opptaksgrense for NTNU var:", round(points/sum, 3)

snitt_ntnu()


def lavest():
    global full
    lowest = 60.6
    low_major = ""
    for major in full:
        if(major[1] != "Alle" and float(major[1]) < lowest):
            low_major = major[0]
            lowest = float(major[1])
    return "Studiet som hadde den laveste opptaksgrensen var:", low_major

lavest()
