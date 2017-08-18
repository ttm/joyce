import pickle, numpy as n

def pRead(tfilename):
    with open(tfilename,"rb") as f:
        tobject=pickle.load(f)
    return tobject

m = pRead("measures.pickle")

# PCA of all of them
# compare synset depths and fraction of known words
nbooks = sum([len(i) for i in m])
nmetrics = len(m[0][0])

matrix = n.zeros((nbooks, nmetrics))

i = 0
for books in m:
    for book in books:
        matrix[i] = n.array(book)
        i+=1

# take zscore of each column
M = n.copy(matrix)
for i in range(M.shape[1]):
    if M[:, i].std():
        M[:, i]=(M[:, i]-M[:, i].mean())/M[:, i].std()
    else:
        M[:, i]=0.

#### make PCA
final_dimensions = 3
# convariance matrix:
C=n.cov(M.T,bias=1)

eig_values, eig_vectors = n.linalg.eig(C)
# Ordering eigenvalues and eigenvectors
args=n.argsort(eig_values)[::-1]
eig_values=eig_values[args]
eig_vectors=eig_vectors[:,args]
# retaining only some eigenvectors
feature_vec=eig_vectors[:,:final_dimensions]
final_data=n.dot(M,feature_vec)
x=final_data[:,0]
y=final_data[:,1]
z=final_data[:,2]

# if we wanted to study how the measurements combine into the principal components
eig_values_=100*eig_values/n.sum(n.abs(eig_values))
eig_vectors_=n.array([100*eig_vectors[:,i]/n.abs(eig_vectors[:,i]).sum() for i in range(eig_vectors.shape[1])]).T
feature_vec_=n.array([100*feature_vec[:,i]/n.abs(feature_vec[:,i]).sum() for i in range(feature_vec.shape[1])]).T

def placeTitles(x,y,texts):
    for xx, yy, ttext in zip(x,y,texts):
        p.text(xx,yy,ttext)
names = ['finnegans',
          'portrait',
           'stephen',
           'ulysses',
         'dubliners',
]
# plot PCA
import pylab as p
p.clf()
p.plot(x[:len(m[0])], y[:len(m[0])], "ro", ms=3, label="Joyce")
p.plot(x[len(m[0]):len(m[0])+len(m[1])], y[len(m[0]):len(m[0])+len(m[1])], "g^", ms=3, label="Shakespeare")
p.plot(x[len(m[0])+len(m[1]):], y[len(m[0])+len(m[1]):], "b+", ms=3, label="Bible")
p.xlabel( 'first component')
p.ylabel('second component')
placeTitles(x[:len(m[0])], y[:len(m[0])], names)
p.legend(loc="lower right")
p.savefig("../latex/figs/pca.png")

p.clf()
p.plot(x[:len(m[0])], z[:len(m[0])], "ro", ms=3)
p.plot(x[len(m[0]):len(m[0])+len(m[1])],
        z[len(m[0]):len(m[0])+len(m[1])], "g^", ms=3)
p.plot(x[len(m[0])+len(m[1]):], z[len(m[0])+len(m[1]):], "b+", ms=3)
p.xlabel( 'first component')
p.ylabel('third component')
placeTitles(x[:len(m[0])], z[:len(m[0])], names)
p.savefig("../latex/figs/pca2.png")

p.clf()
p.plot(y[:len(m[0])], z[:len(m[0])], "ro", ms=3)
p.plot(y[len(m[0]):len(m[0])+len(m[1])],
        z[len(m[0]):len(m[0])+len(m[1])], "g^", ms=3)
p.plot(y[len(m[0])+len(m[1]):], z[len(m[0])+len(m[1]):], "b+", ms=3)
p.xlabel( 'second component')
p.ylabel('third component')
placeTitles(y[:len(m[0])], z[:len(m[0])], names)
p.savefig("../latex/figs/pca3.png")

# plot ABSTRACT
p.clf()
x = matrix[:,-4]
y = matrix[:,-2]
p.plot(x[:len(m[0])], y[:len(m[0])], "ro", ms=3)
p.plot(x[len(m[0]):len(m[0])+len(m[1])],
        y[len(m[0]):len(m[0])+len(m[1])], "g^", ms=3)
p.plot(x[len(m[0])+len(m[1]):], y[len(m[0])+len(m[1]):], "b+", ms=3)
p.xlabel( r'$\mu(min\;depth\;of\;synset)$')
p.ylabel( r'$\mu(max\;depth\;of\;synset)$')
placeTitles(x[:len(m[0])], y[:len(m[0])], names)
p.savefig("../latex/figs/abst1.png")

p.clf()
x = matrix[:,3]
y = matrix[:,5]
p.plot(x[:len(m[0])], y[:len(m[0])], "ro", ms=3)
p.plot(x[len(m[0]):len(m[0])+len(m[1])],
        y[len(m[0]):len(m[0])+len(m[1])], "g^", ms=3)
p.plot(x[len(m[0])+len(m[1]):], y[len(m[0])+len(m[1]):], "b+", ms=3)
p.xlabel( '(number of known words) / (number of tokens)')
p.ylabel('(number of known word) / (number of most meaningful words)')
placeTitles(x[:len(m[0])], y[:len(m[0])], names)
p.savefig("../latex/figs/abst2.png")
