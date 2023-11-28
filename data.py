import json
import datetime

date = datetime.datetime.now()

def read():
    f = open('data/ideias.json', "r")
    data = json.load(f)
    f.close()
    return data

def write(object):
    data = read()
    data.append(object)

    with open("data/ideias.json", "w") as arquivo:     
        json.dump(data, arquivo, indent=4)

def getLastId():
    data = read()
    return data[len(data) - 1]["id"]

def append(title, desc):

    if title and desc:
        ideia = {}
        ideia["id"] = getLastId() + 1
        ideia["title"] = title
        ideia["desc"] = desc
        ideia["date"] = date.strftime("%d/%m/%Y")

        write(ideia)

        return True
    
    return False

append("Tema", "Fazer um tema especifico")
for i in read():
    print(i)