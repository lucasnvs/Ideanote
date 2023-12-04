import json
import datetime

date = datetime.datetime.now()

def read():
    f = open('data/ideias.json', "r")
    data = json.load(f)
    f.close()
    
    return data

def write(data):
    with open("data/ideias.json", "w") as arquivo:     
        json.dump(data, arquivo, indent=4)

def writeObject(object):
    data = read()
    data.append(object)

    with open("data/ideias.json", "w") as arquivo:     
        json.dump(data, arquivo, indent=4)

def append(title, desc):

    if title and desc:
        ideia = {}
        ideia["id"] = getLastId() + 1
        ideia["title"] = title
        ideia["desc"] = desc
        ideia["date"] = date.strftime("%d/%m/%Y")

        writeObject(ideia)

        return True
    
    return False

def update(id, ideia):
    data = read()

    for idea in data:
        if(idea["id"] == id):
            data[data.index(idea)] = ideia
            break
    
    write(data)

def getLastId():
    data = read()
    return data[len(data) - 1]["id"]

def findById(id):
    data = read()

    for idea in data:
        if(idea.get("id") == id): 
            return idea