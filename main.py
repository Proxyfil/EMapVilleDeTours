import json


def getStops():
    f = open('./20220829-filbleu-gtfs/stops.txt', 'r')
    output = {}

    for line in f:
        formatted = line.replace("\"","").split(',')
        print(formatted[5])
        if(formatted[5] == ''):
            print("Handeling",formatted[0])
            output[formatted[0]] = {"name":formatted[2],"lat":formatted[6],"lon":formatted[7]}
        else:
            output[formatted[0]] = {"name":formatted[2],"lat":formatted[5],"lon":formatted[6]}

    out = open('./output/stops.json', 'w')
    out.write(json.dumps(output, indent=4))

def getStopsHours():
    f = open('./20220829-filbleu-gtfs/stop_times.txt', 'r', encoding='utf-8')
    stops = json.loads(open('./output/stops.json', 'r').read())
    output = {}
    count = 0

    lines = f.readlines()
    print("Lines : ",len(lines))

    for line in lines:
        count += 1
        if(count%10000 == 0):
            print("Looking for line",count)

        formatted = line.replace("\"","").split(',')
        if(formatted[3] in list(output.keys())):
            output[formatted[3]]["amount"] += 1
        else:
            output[formatted[3]] = {"amount":1,"name":formatted[5]}

    for idStop in list(output.keys()):
        if(idStop in list(stops.keys())):
            output[idStop]["name"] = stops[idStop]["name"]
            output[idStop]["lat"] = stops[idStop]["lat"]
            output[idStop]["lon"] = stops[idStop]["lon"]
        else:
            print("Error for",idStop)

    out = open('./output/stopsHours.json', 'w', encoding="utf-8")
    out.write(json.dumps(output, indent=4, ensure_ascii=False))

def frequency():
    f = open('./frequentations-par-ligne-du-reseau-fil-bleu.json', 'r', encoding='utf-8')

    data = json.loads(f.read())

    output = {}

    for line in data:
        if(line["fields"]["date"][0:4] == "2019"):
            if(line["fields"]["lignes"] in list(output.keys())):
                output[line["fields"]["lignes"]]["amount"] += line["fields"]["frequentation"]
            else:
                output[line["fields"]["lignes"]] = {"amount":line["fields"]["frequentation"]}

    print(output)

frequency()