# open Joyce works in ../corpus
# use Genesis (Bible) and Shakespeare (at least Hamlet) to compare against
# these last works are in NLTK

# metrics: size of words, sentences and paragraphs.
# fraction of stopwords and known english words
# relations with wordnet synsets to measure abstraction

files = ['finnegans.txt',
    'portrait.txt',
    'stephen.txt',
    'ulysses.txt',
]
tdir = '../corpus/'
ts = [] # Joyce's texts
for f in files:
    r = open(tdir+f,"r")
    t = r.readlines()
    tt = []
    for line in t:
        if line == "\n" or line.startswith("[}"):
            pass
        else:
            tt.append(line[:-1])
    ts.append(" ".join(tt))

import nltk as k

tss = [] # Shakespeare's texts
for f in k.corpus.shakespeare.fileids():
    tss.append(" ".join(k.corpus.shakespeare.words(f)))

tsb = [] # Bible's texts
raw = k.corpus.gutenberg.raw("bible-kjv.txt")
for f in k.corpus.shakespeare.fileids():
    tss.append(" ".join(k.corpus.shakespeare.words(f)))
