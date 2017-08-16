# script to separate the books of the bible in clean text files

codes = {
    "01O" : "Genesis",
    "02O" : "Exodus",
    "03O" : "Leviticus",
    "04O" : "Numbers",
    "05O" : "Deuteronomy",
    "06O" : "Joshua",
    "07O" : "Judges",
    "08O" : "Ruth",
    "09O" : "1 Samuel",
    "10O" : "2 Samuel",
    "11O" : "1 Kings",
    "12O" : "2 Kings",
    "13O" : "1 Chronicles",
    "14O" : "2 Chronicles",
    "15O" : "Ezra",
    "16O" : "Nehemiah",
    "17O" : "Esther",
    "18O" : "Job",
    "19O" : "Psalms",
    "20O" : "Proverbs",
    "21O" : "Ecclesiastes",
    "22O" : "Song of Solomon",
    "23O" : "Isaiah",
    "24O" : "Jeremiah",
    "25O" : "Lamentations",
    "26O" : "Ezekiel",
    "27O" : "Daniel",
    "28O" : "Hosea",
    "29O" : "Joel",
    "30O" : "Amos",
    "31O" : "Obadiah",
    "32O" : "Jonah",
    "33O" : "Micah",
    "34O" : "Nahum",
    "35O" : "Habakkuk",
    "36O" : "Zephaniah",
    "37O" : "Haggai",
    "38O" : "Zechariah",
    "39O" : "Malachi",
    "40N" : "Matthew",
    "41N" : "Mark",
    "42N" : "Luke",
    "43N" : "John",
    "44N" : "Acts of the Apostles",
    "45N" : "Romans",
    "46N" : "1 Corinthians",
    "47N" : "2 Corinthians",
    "48N" : "Galatians",
    "49N" : "Ephesians",
    "50N" : "Philippians",
    "51N" : "Colossians",
    "52N" : "1 Thessalonians",
    "53N" : "2 Thessalonians",
    "54N" : "1 Timothy",
    "55N" : "2 Timothy",
    "56N" : "Titus",
    "57N" : "Philemon",
    "58N" : "Hebrews",
    "59N" : "James",
    "60N" : "1 Peter",
    "61N" : "2 Peter",
    "62N" : "1 John",
    "63N" : "2 John",
    "64N" : "3 John",
    "65N" : "Jude",
    "66N" : "Revelation",
    "67A" : "Tobit",
    "68A" : "Judith",
    "69A" : "Esther, Greek",
    "70A" : "Wisdom of Solomon",
    "71A" : "Ecclesiasticus (Sira",
    "72A" : "Baruch",
    "73A" : "Epistle of Jeremiah",
    "74A" : "Prayer of Azariah",
    "75A" : "Susanna",
    "76A" : "Bel and the Dragon",
    "77A" : "1 Maccabees",
    "78A" : "2 Maccabees",
    "79A" : "3 Maccabees",
    "80A" : "4 Maccabees",
    "81A" : "1 Esdras",
    "82A" : "2 Esdras",
    "83A" : "Prayer of Manasseh",
    "84A" : "Psalm 151",
    "85A" : "Psalm of Solomon",
    "86A" : "Odes",
}

tdir = '../corpus/'
f = "kjv_apocrypha_utf8_FINAL.txt"
r = open(tdir+f,"r")
t = r.readlines()
tt = {}
for b in codes:
    tt[b] = []

for line in t:
    if line.startswith("<br>"):
        l = line[4:].replace("\n", "")
        tt[akey].append(l)
    else:
        akey = line[3:6]

for b in tt:
    if not tt[b]:
        print(b)
    else:
        text = " ".join(tt[b])
        aname = codes[b].replace(" ","").lower()
        f = open(tdir+aname, "w")
        f.write(text)
        f.close()



