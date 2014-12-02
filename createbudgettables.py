import json, codecs

master = {'projects':[],'expenses':{},'income':{}}
projectCount = 0

def fillTables(src,dst,count):
    for i in src:
        name = i["name"]
        budget = i["budget"]["amount"]
        balance = i["balance"]["amount"]
        if name not in dst.keys():
            dst[name]=[]
            for x in range(0,count):
                dst[name].append('0')
        while(len(dst[name])<count):
            dst[name].append('0')
        dst[name].append(balance)

def loadProjectData(data):
    global master, projectCount
    project = data["pool"]["name"]
    master["projects"].append(project)
    mexp = master['expenses']
    minc = master['income']
    exp = data["expense_categories"]
    inc = data["income_categories"]
    fillTables(exp,mexp,projectCount)
    fillTables(inc,minc,projectCount)
    projectCount+=1

def fillOutTable(dst):
    for name in dst.keys():
        while(len(dst[name])<projectCount):
            dst[name].append('0')

def csvOutput():
    f = codecs.open("budget.csv",'w','utf-8')
    f.write(u',"'+u'","'.join(master["projects"])+'"\n')
    for cat in master["income"].keys():
        f.write(u'"'+cat+u'",'+u','.join(master["income"][cat])+'\n')
    for cat in master["expenses"].keys():
        f.write(u'"'+cat+u'",-'+u',-'.join(master["expenses"][cat])+'\n')
    f.close()

if __name__ == "__main__":
    f = open("holvilist.txt")
    for holvi in f:
        h = open(holvi.strip()+'.json')
        data = json.load(h)
        loadProjectData(data)
        h.close()
    f.close()
    fillOutTable(master["income"])
    fillOutTable(master["expenses"])
    #print master
    csvOutput()