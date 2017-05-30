lines = []
with open("laikai_test.txt", "r") as f:
    for line in f:
        if (line.strip() is not ""):
            lines.append(line.strip())

def sortLines(s):
    return s.split("\t")[1]

for line in lines:
    print(line)

print("\n")

lines = sorted(lines, key=sortLines)

for line in lines:
    print(line)