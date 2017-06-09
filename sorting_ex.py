lines = []
with open("laikai_test.txt", "r") as f:
    for line in f:
        if (line.strip() is not ""):
            lines.append(line.strip())

def sortLines(s):
    return ":".join(s.split("\t")[1].split(":")[0].zfill(2))

for line in lines:
    print(line)

print("\n")

lines = sorted(lines, key=sortLines)

for line in lines:
    print(line)