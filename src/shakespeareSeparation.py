# script to separate the books of the bible in clean text files

import string, re


tdir = '../corpus/'
f = "pg100.txt"
r = open(tdir+f,"r")
t = r.readlines()

tt = {}

tag = "by William Shakespeare"
tag2 = "THE END"
tag3 = "dramatis personae"
jump_tags = ["SCENE", "SCENE:", "SCENE.",  "SCENE.-","ACT", "PROLOGUE", "EPILOGUE", "EPILOGUE."]
enters = ["Enter", "Re-enter"]

titles = []
i=0
keep = False
end = False
for line in t:
    if line.startswith(tag):
        title = t[i-2][:-1]
        titles.append(title)
        tt[title] = []
        keep = True
        end = False
    elif line.startswith(tag2):
        keep = False
        end = True
    elif line.lower().startswith(tag3):
        keep = False
    elif line.startswith("<<"):
        keep = False
    elif line[:-1].endswith(">>") and not end:
        keep = True
    elif sum([i in line.split() for i in jump_tags]):
        keep = True
        pass
    elif sum([line.strip().startswith(i) for i in enters]):
        pass
    elif keep == False:
        pass
    elif not line:
        pass
    elif sum([i in string.digits for i in line.strip()]) == len(line.strip()):
        pass
    else:
        l = line.strip().replace('\n', '')
        l_ = re.sub("^[ ]*[a-zA-Z]{3,4}\. ","", l)
        l__ = re.sub("[A-Z ]+\. ", "", l_)
        l___ = re.sub(" +", " ", l__)
        # l__ = re.sub("^[a-zA-Z]{3}\. ","", l_)
        tt[title].append(l___)
    i += 1

names = []
for b in tt:
    if not tt[b]:
        print(b)
    else:
        print("NOT", b)
        text = " ".join(tt[b])
        aname = b.replace(" ","").lower() + ".txt"
        f = open(tdir+aname, "w")
        f.write(text)
        f.close()
        names.append(aname)
