(cover)


#title:
A Simple Text Analytics Model To Assist Literary Criticism:
comparative approach and example on james joyce against shakespeare and the bible

#authors:
Renato Fabbri and Luis Henrique Garcia
(ICMC/USP)

#ENMC2017
(XX Encontro Nacional de Modelagem Computacional)
18/Out/2017


















=========================
(slide 1)

*Introduction*

* Literaty criticism

* Text analytics





















==========================
(slide 2)

*Materials*

* Complete works by Shakespeare
  - 36 plays (tragedies, comedies, historical)
  - 2 poetry books

* The 80 books of the Bible (KJV)
  - 39 books of the Old Testament
  - 14 apocrypha books
  - 27 books of the New Testament

* Selection of novels by James Joyce
  - Stephen Hero (1905)
  - Dubliners (1914)
  - A Portrait of the Artist as a Young Man (1916)
  - Ulysses (1922)
  - Finnegans Wake (1939)






















==========================
(slide 3)

*Pre-processing*

* Separation of the Bible and Shakespeare books

* Paragraphs were discarded





















==========================
(slide 4)

*Analysis*

* Elements: sentences, tokens, stopwords,
known words (which are not stopwords), punctuations,
tokens which are not stopwords or punctuation,
Wordnet synsets

* Quantization:
  - Number of characters
  - Fraction of incidence
  - Synset characteristics

* PCA after z-scores

* Scatter plots

* Discussions





















==========================
(slide 5)

*Results*

* Better presented through the scatter plots
  - ../latex/figs/pca.png
  - ../latex/figs/pca2.png
  - ../latex/figs/pca3.png
  - ../latex/figs/abst1.png
  - ../latex/figs/abst2.png















==========================
(slide 6)

*Conclusions*

* Simple, adaptable, robust analysis

* Facilitates the communication of the interested parties

* Useful results for literary criticism
  - The example application revealed insights
  on the works by James Joyce

* Further work:
  - Deepen the analysis of the reference literature
  - Expand the use of Wordnet
  - Report this endeavor to the Literary Criticism community
  - Measures of abstraction
  - Vary the methods
  - Investigate Figure 4
  - Investigate the unexpected fraction of unknown words in Dubliners

Thanks: FAPESP, ICMC/USP, ENMC2017
