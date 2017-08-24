# open Joyce works in ../corpus
# use Genesis (Bible) and Shakespeare (at least Hamlet) to compare against
# these last works are in NLTK

# metrics: size of words and sentences
# fraction of stopwords and known english words
# relations with wordnet synsets to measure abstraction

files = ['finnegans.txt',
    'portrait.txt',
    'stephen.txt',
    'ulysses.txt',
    'dubliners.txt',
]
tdir = '../corpus/'
tsj = [] # Joyce's texts
for f in files:
    r = open(tdir+f,"r")
    t = r.readlines()
    tt = []
    for line in t:
        if line == "\n":
            pass
        else:
            tt.append(line[:-1])
    tsj.append(" ".join(tt))


tss = [] # Shakespeare's texts
sbooks = ['thefirstpartofkinghenrythefourth.txt', 'thetragedyofothello,moorofvenice.txt', "alover'scomplaint.txt", 'thefirstpartofhenrythesixth.txt', 'thelifeoftimonofathens.txt', 'allswellthatendswell.txt', 'kingrichardthesecond.txt', "love'slabour'slost.txt", 'thetragedyofjuliuscaesar.txt', 'thetempest.txt', 'muchadoaboutnothing.txt', 'thetragedyofromeoandjuliet.txt', 'themerchantofvenice.txt', 'thehistoryoftroilusandcressida.txt', 'thecomedyoferrors.txt', 'cymbeline.txt', "thewinter'stale.txt", 'thesecondpartofkinghenrythesixth.txt', 'thetamingoftheshrew.txt', 'thetragedyofantonyandcleopatra.txt', 'twelfthnight;or,whatyouwill.txt', 'thetragedyofcoriolanus.txt', 'kingjohn.txt', 'thetragedyofmacbeth.txt', 'thetragedyofhamlet,princeofdenmark.txt', 'thesonnets.txt', 'measureformeasure.txt', 'thetragedyoftitusandronicus.txt', 'thetragedyofkinglear.txt', 'kingrichardiii.txt', 'asyoulikeit.txt', 'thethirdpartofkinghenrythesixth.txt', 'secondpartofkinghenryiv.txt', 'thetwogentlemenofverona.txt', "amidsummernight'sdream.txt", 'kinghenrytheeighth.txt', 'thelifeofkinghenrythefifth.txt', 'themerrywivesofwindsor.txt']
for b in sbooks:
    r = open(tdir+b,"r")
    tss.append(r.read())

tsb = [] # Bible books
bbooks = ['titus.txt', '1corinthians.txt', 'nahum.txt', 'jude.txt', '1chronicles.txt', 'zechariah.txt', 'job.txt', 'mark.txt', 'galatians.txt', 'jonah.txt', 'psalms.txt', 'daniel.txt', 'obadiah.txt', '1esdras.txt', 'haggai.txt', 'philemon.txt', 'proverbs.txt', 'deuteronomy.txt', 'amos.txt', '1timothy.txt', 'genesis.txt', 'judges.txt', '2john.txt', '2chronicles.txt', 'revelation.txt', 'leviticus.txt', '2peter.txt', 'actsoftheapostles.txt', '2kings.txt', '2timothy.txt', 'exodus.txt', 'esther.txt', 'belandthedragon.txt', 'esther,greek.txt', 'songofsolomon.txt', 'hosea.txt', 'habakkuk.txt', 'susanna.txt', 'isaiah.txt', '2corinthians.txt', 'ecclesiastes.txt', 'ruth.txt', '1samuel.txt', 'nehemiah.txt', 'ecclesiasticus(sira.txt', 'john.txt', 'baruch.txt', 'ezekiel.txt', 'wisdomofsolomon.txt', 'colossians.txt', 'numbers.txt', 'lamentations.txt', '1john.txt', 'judith.txt', 'james.txt', 'joshua.txt', 'philippians.txt', '2samuel.txt', '1maccabees.txt', 'hebrews.txt', 'epistleofjeremiah.txt', 'romans.txt', 'ezra.txt', '1peter.txt', '2esdras.txt', 'ephesians.txt', 'prayerofmanasseh.txt', 'malachi.txt', '1kings.txt', '3john.txt', 'micah.txt', '2maccabees.txt', '1thessalonians.txt', 'jeremiah.txt', 'joel.txt', 'matthew.txt', '2thessalonians.txt', 'tobit.txt', 'luke.txt', 'prayerofazariah.txt', 'zephaniah.txt']
for b in bbooks:
    r = open(tdir+b,"r")
    tsb.append(r.read())


###########################
## measuring and analyzing
import nltk as k, os, string, numpy as n
from nltk.corpus import wordnet as wn
w=open(os.path.join(tdir,"words.txt"),"r")
w=w.read()
WL=w.split()
known_words=set(WL)

stopwords = set(k.corpus.stopwords.words("english"))
punctuations = set(string.punctuation)
def takeMeasures(book):
    # achievement of meaninful sets
    book = book.lower()
    sentences = k.tokenize.sent_tokenize(book)
    tokens = k.tokenize.wordpunct_tokenize(book)
    tokens_ = set(tokens)
    sw = [i for i in tokens if i in stopwords]
    kw = [i for i in tokens if i in known_words and i not in stopwords and i not in punctuations]
    pt = [i for i in tokens if i in punctuations]
    w_sp = [i for i in tokens if i not in stopwords and i not in punctuations]
    ss = [wn.synsets(i) for i in kw]
    ss = [i[0] for i in ss if i] # for depth

    # quantization
    st_sz = [len(i) for i in sentences]
    tk_sz = [len(i) for i in tokens]
    kw_sz = [len(i) for i in kw]
    w_sp_sz = [len(i) for i in w_sp]
    d1 = [i.max_depth() for i in ss]
    d2 = [i.min_depth() for i in ss]

    # measurements
    tk_st  = len(tokens)/len(sentences)
    tk_div = len(tokens_)/len(tokens)
    sw_tk  = len(sw)/len(tokens)
    kw_tk  = len(kw)/len(tokens)
    pt_tk  = len(pt)/len(tokens)
    kw_w_sp = len(kw)/len(w_sp)

    stM    = n.mean(st_sz)
    stD    = n.std( st_sz)
    tkM    = n.mean(tk_sz)
    tkD    = n.std( tk_sz)
    kwM    = n.mean(kw_sz)
    kwD    = n.std( kw_sz)
    w_spM  = n.mean(w_sp_sz)
    w_spD  = n.std( w_sp_sz)
    stM    = n.mean(st_sz)
    stD    = n.std( st_sz)
    d1M    = n.mean(d1)
    d1D    = n.std( d1)
    d2M    = n.mean(d2)
    d2D    = n.std( d2)

    return tk_st, tk_div, sw_tk, kw_tk, pt_tk, kw_w_sp, stM, stD, tkM, tkD, kwM, kwD, w_spM, w_spD, stM, stD, d1M, d1D, d2M, d2D

print("starting analizes")
anj = []
for i, t in enumerate(tsj):
    anj.append(takeMeasures(t))
    print("j", i)
ans = []
for i, t in enumerate(tss):
    ans.append(takeMeasures(t))
    print("s", i)
anb = []
for i, t in enumerate(tsb):
    anb.append(takeMeasures(t))
    print("b", i)

import pickle
def pDump(tobject,tfilename):
    with open(tfilename,"wb") as f:
        pickle.dump(tobject,f,-1)
pDump([anj, ans, anb], "measures.pickle")
