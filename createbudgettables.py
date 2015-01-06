#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, codecs, re

master = {'projects':[],'expenses':{},'income':{}}
projectCount = 0

REMAP=1
BALANCE=1

if REMAP:
	MAPPERSCOMPILED=0
	from mappers import emappers

def remap(name):
	global emappers,MAPPERSCOMPILED
	if not MAPPERSCOMPILED:
		ee = {}
		for cat,regs in emappers.iteritems():
			rr = []
			for r in regs:
				rr.append(re.compile(r,re.I))	
			ee[cat]=rr
		emappers=ee	
		MAPPERSCOMPILED=1

	for cat,regs in emappers.iteritems():
		for r in regs:
			if r.search(name):
				return cat
	return name+u'?'

def fillTables(src,dst,count,direction):
    for i in src:
        name = i["name"]
        budget = i["budget"]["amount"]
        balance = i["balance"]["amount"]
	if BALANCE:
		value=balance
	else:
		value=budget
	if REMAP:
		name=remap(name)
        if name not in dst.keys():
            dst[name]=[]
        while(len(dst[name])<=count):
            dst[name].append(0)
        dst[name][-1]+=float(value)*direction

def loadProjectData(data):
    global master, projectCount
    project = data["pool"]["name"]
    master["projects"].append(project)
    mexp = master['expenses']
    minc = master['income']
    exp = data["expense_categories"]
    inc = data["income_categories"]
    fillTables(exp,mexp,projectCount,-1)
    fillTables(inc,minc,projectCount,+1)
    projectCount+=1

def fillOutTable(dst):
    for name in dst.keys():
        while(len(dst[name])<projectCount):
            dst[name].append('0')

def csvOutput():
    f = codecs.open("budget.csv",'w','utf-8')
    f.write(u',"'+u'","'.join(master["projects"])+u'"\n')
    for cat in master["income"].keys():
        f.write(u'"'+cat+u'"')
	for v in master["income"][cat]:
		f.write(u','+str(v))
	f.write(u'\n')
    for cat in master["expenses"].keys():
        f.write(u'"'+cat+u'"')
	for v in master["expenses"][cat]:
		f.write(u','+str(v))
	f.write(u'\n')
    f.close()

if __name__ == "__main__":
    f = open("holvilist.txt")
    for holvi in f:
        h = open(holvi.strip().split("#")[0]+'.json')
        data = json.load(h)
        loadProjectData(data)
        h.close()
    f.close()
    fillOutTable(master["income"])
    fillOutTable(master["expenses"])
    #import pdb;pdb.set_trace()
    #print master
    csvOutput()
