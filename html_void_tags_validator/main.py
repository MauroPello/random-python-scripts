import sys

tags = open("special_tags.txt", "r").read().split("\n")
lastDetections = [0 for tag in tags]
html = open(sys.argv[1], "r").read().lower()
toPrint = []
hasDetected = True
while hasDetected:
    hasDetected = False
    for i in range(0, len(tags)):
        if html.count(tags[i], lastDetections[i]) != 0:
            hasDetected = True
            start = html.index(tags[i], lastDetections[i])
            closing = html.index(">", start)
            lastDetections[i] = closing
            if html[closing - 1] != "/" or html[closing - 2] != " ":
                toPrint.append(str(html.count("\n", 0, closing) + 1) + ":" + str(start) + " - " + tags[i][1:])
        else:
            hasDetected = hasDetected or False

if len(toPrint) > 0:
    toPrint.sort(key=lambda s: int(str(s).split(":")[0]) * 10**10 + int(str(s)[str(s).index(":") + 1:str(s).index(" -")]))
    for line in toPrint:
        print(line)
else:
    print("No problems found.")