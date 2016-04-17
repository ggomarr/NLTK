'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# Chapter 2

# 1 Create a variable phrase containing a list of words. Review the operations described in the previous chapter, including addition, multiplication, indexing, slicing, and sorting.

# NA

# 2 Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?

len(nltk.corpus.gutenberg.words('austen-persuasion.txt'))
len(set(nltk.corpus.gutenberg.words('austen-persuasion.txt')))

# 3 Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.

# NA

# 4 Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and people in each document. What has happened to the usage of these words over time?

su=nltk.corpus.state_union
cfd=nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in su.fileids()
    for w in su.words(fileid)
    for target in ['men', 'women','people']
    if w.lower().startswith(target))
cfd.plot()

# 5 Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().

[ concept.member_holonyms() for concept in nltk.corpus.wordnet.synsets('person') ]
[ concept.member_meronyms() for concept in nltk.corpus.wordnet.synsets('school') ]
[ concept.part_holonyms() for concept in nltk.corpus.wordnet.synsets('button') ]
[ concept.part_meronyms() for concept in nltk.corpus.wordnet.synsets('person') ]
[ concept.substance_holonyms() for concept in nltk.corpus.wordnet.synsets('iron') ]
[ concept.substance_meronyms() for concept in nltk.corpus.wordnet.synsets('person') ]

# 6 In the discussion of comparative wordlists, we created an object called translate which you could look up using words in both German and Spanish in order to get corresponding words in English. What problem might arise with this approach? Can you suggest a way to avoid this problem?

# NA

# 7 According to Strunk and White's Elements of Style, the word however, used at the start of a sentence, means "in whatever way" or "to whatever extent", and not "nevertheless". They give this example of correct usage: However you advise him, he will probably do as he thinks best. (http://www.bartleby.com/141/strunk3.html) Use the concordance tool to study actual usage of this word in the various texts we have been considering. See also the LanguageLog posting "Fossilized prejudices about 'however'" at http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html

for textid in nltk.corpus.gutenberg.fileids():
    print(textid)
    nltk.Text(nltk.corpus.gutenberg.words(textid)).concordance("however")
[ nltk.Text(nltk.corpus.gutenberg.words(textid)).concordance("However") for textid in nltk.corpus.gutenberg.fileids() ]
[ txt.concordance("However") for txt in [ nltk.Text(nltk.corpus.gutenberg.words(textid)) for textid in nltk.corpus.gutenberg.fileids() ] ]

# 8 Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).

names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

# 9 Pick a pair of texts and study the differences between them, in terms of vocabulary, vocabulary richness, genre, etc. Can you find pairs of words which have quite different meanings across the two texts, such as monstrous in Moby Dick and in Sense and Sensibility?

# NA

# 10 Read the BBC News article: UK's Vicky Pollards 'left behind' http://news.bbc.co.uk/1/hi/education/6173441.stm. The article gives the following statistic about teen language: "the top 20 words used, including yeah, no, but and like, account for around a third of all words." How many word types account for a third of all word tokens, for a variety of text sources? What do you conclude about this statistic? Read more about this on LanguageLog, at http://itre.cis.upenn.edu/~myl/languagelog/archives/003993.html.

wds=[wd for wd in nltk.corpus.gutenberg.words() if wd.isalpha()==True]
fd=nltk.FreqDist(wds)
sum( [ fd.freq(wd[0]) for wd in fd.most_common(20) ] )
# 0.304
wds=[wd for wd in nltk.corpus.brown.words() if wd.isalpha()==True]
fd=nltk.FreqDist(wds)
sum( [ fd.freq(wd[0]) for wd in fd.most_common(20) ] )
# 0.301
wds=[wd for wd in nltk.corpus.reuters.words() if wd.isalpha()==True]
fd=nltk.FreqDist(wds)
sum( [ fd.freq(wd[0]) for wd in fd.most_common(20) ] )
# 0.274
wds=[wd for wd in nltk.corpus.webtext.words() if wd.isalpha()==True]
fd=nltk.FreqDist(wds)
sum( [ fd.freq(wd[0]) for wd in fd.most_common(20) ] )
# 0.235
wds=[wd for wd in nltk.corpus.nps_chat.words() if wd.isalpha()==True]
fd=nltk.FreqDist(wds)
sum( [ fd.freq(wd[0]) for wd in fd.most_common(20) ] )
# 0.296

# 11 Investigate the table of modal distributions and look for other patterns. Try to explain them in terms of your own impressionistic understanding of the different genres. Can you find other closed classes of words that exhibit significant differences across different genres?

# NA

# 12 The CMU Pronouncing Dictionary contains multiple pronunciations for certain words. How many distinct words does it contain? What fraction of words in this dictionary have more than one possible pronunciation?

cmu=nltk.corpus.cmudict.dict()
len(cmu)
cmu=nltk.corpus.cmudict.words()
len(set(cmu))
1-1.0*len(set(cmu))/len(cmu)

# 13 What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n').

wn=nltk.corpus.wordnet.all_synsets('n')
totwn=0
nohyp=0
for w in wn:
    totwn=totwn+1
    if w.hyponyms()==[]:
        nohyp=nohyp+1
print(1.0*nohyp/totwn)

# 14 Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.

def supergloss(syn):
    auxdef=[ syn.definition() ]
    for subsyn in syn.hyponyms():
        auxdef = auxdef + [ subsyn.definition() ]
    for supersyn in syn.hypernyms():
        auxdef = auxdef + [ supersyn.definition() ]
    return auxdef

# 15 Write a program to find all words that occur at least three times in the Brown Corpus.

bn=nltk.corpus.brown.words()
fd=nltk.FreqDist(bn)
outlist=[]
for wd in fd.most_common():
    if wd[1]>=3:
        outlist=outlist + [ wd ]
    else:
        break
print(outlist)

# 16 Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in 1.1. Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()). Which genre has the lowest diversity (greatest number of tokens per type)? Is this what you would have expected?

bn=nltk.corpus.brown
for genre in bn.categories():
    genretok=[ wd.lower() for wd in bn.words(categories=genre) if wd.isalpha()==True ]
    lexdiv=1.0*len(set(genretok))/len(genretok)
    print('%s %0.3f' % (genre.rjust(15), lexdiv))

# 17 Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

def freq_non_stop(text, maxnum, isal=True):
    fd=nltk.FreqDist(text)
    auxout=[]
    num=0
    stp=nltk.corpus.stopwords.words()
    for wd in fd.most_common():
        if wd[0].lower() not in stp:
            if isal==False or wd[0].isalpha()==True:
                auxout = auxout + [ wd[0].lower() ]
                num=num+1
        if num==maxnum:
            break
    return auxout

# 18 Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text,
# omitting bigrams that contain stopwords.

def big_non_stop(text=['more', 'is', 'said', 'than', 'done', 'allergies', 'rockandrolla'], maxnum=5, isal=True):
    bigs=list(nltk.bigrams(text))
    fd=nltk.FreqDist(bigs)
    auxout=[]
    num=0
    s_stp=set(nltk.corpus.stopwords.words())
    for fd_big in fd.most_common():
        big=[ wd.lower() for wd in fd_big[0] ]
        if set(big) & s_stp==set([]):
            if isal==False or sum([ wd.isalpha() for wd in big ])==len(big):
                auxout = auxout + [ fd_big[0] ]
                num=num+1
        if num==maxnum:
            break
    return auxout

# 19 Write a program to create a table of word frequencies by genre, like the one given in 1 for modals.
# Choose your own words and try to find words whose presence (or absence) is typical of a genre.
# Discuss your findings.

def word_by_genre(word_list=['passion','power','impact','likely'], genre_list=['romance','adventure','science_fiction','news']):
    if genre_list=='':
        genre_list=nltk.corpus.brown.categories()
    genre_word = [ (genre, word)
                   for genre in genre_list
                   for word in nltk.corpus.brown.words(categories=genre)
                   if word in word_list ]
    cfd=nltk.ConditionalFreqDist(genre_word)
    cfd.tabulate()
    return True

# 20 Write a function word_freq() that takes a word and the name of a section of the Brown Corpus
# as arguments, and computes the frequency of the word in that section of the corpus.

def word_freq(word='door',sec='news',freq_counts=True):
    if freq_counts:
        return nltk.corpus.brown.words(categories=sec).count(word)
    else:
        return 1.0*nltk.corpus.brown.words(categories=sec).count(word)/len(nltk.corpus.brown.words())

# 21 Write a program to guess the number of syllables contained in a text,
# making use of the CMU Pronouncing Dictionary.

def num_sylls(text=['more', 'is', 'said', 'than', 'done', 'allergies', 'take', 'a', 'lot', 'of', 'effort']):
    pronuntiation = nltk.corpus.cmudict.dict()
    syllables = sum([ 1 for pho2 in [ pho1 for wd in text for pho1 in pronuntiation[wd][0] ] if pho2[-1].isnumeric() ])
    return syllables

# 22 Define a function hedge(text) which processes a text and produces a new version
# with the word 'like' between every third word.

def hedge(text=['more', 'is', 'said', 'than', 'done', 'allergies', 'take', 'a', 'lot', 'of', 'effort'],stopper='like',every=3):
    hedged = [ text[pos:pos+every]+[stopper]*(pos<len(text)-every) for pos in range(0,len(text),every) ]
    hedged = [ inner for outer in hedged for inner in outer ]
    return hedged

# 23 Zipf's Law: Let f(w) be the frequency of a word w in free text.
# Suppose that all the words of a text are ranked according to their frequency,
# with the most frequent word first. Zipf's law states that the frequency of a word type
# is inversely proportional to its rank (i.e. f × r = k, for some constant k).
# For example, the 50th most common word type should occur three times as frequently
# as the 150th most common word type.
#  - Write a function to process a large text and plot word frequency against word rank
#    using pylab.plot. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale).
#    What is going on at the extreme ends of the plotted line?
#  - Generate random text, e.g., using random.choice("abcdefg "),
#    taking care to include the space character. You will need to import random first.
#    Use the string concatenation operator to accumulate characters into a (very) long string.
#    Then tokenize this string, and generate the Zipf plot as before, and compare the two plots.
#    What do you make of Zipf's Law in the light of this?

def zipfs_law(text='',textlength=1000000,seedchars='abcdefg '):
    import pylab, numpy, random
    if text=='':
        for _ in range(textlength):
            text=text+random.choice(seedchars)
        text=text.split()
    text=[ wd.lower() for wd in text if wd.isalpha()==True ]
    fd=nltk.FreqDist(text)
    counts=fd.values()
    counts.sort(reverse=True)
    xes=range(1,len(counts)+1)
    pylab.plot(numpy.log(xes),numpy.log(counts))
    return True

# 24 Modify the text generation program in 2.2 further, to do the following tasks:
#  - Store the n most likely words in a list words then randomly choose a word from the list using random.choice(). (You will need to import random first.)
#  - Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts. Train the model on this corpus and get it to generate random text. You may have to experiment with different start words. How intelligible is the text? Discuss the strengths and weaknesses of this method of generating random text.
#  - Now train your system using two distinct genres and experiment with generating text in the hybrid genre. Discuss your observations.

def random_text(train_set='', dict_length=50, target_length=25):
    import random
    if train_set=='':
        train_set=nltk.corpus.brown.words()
    train_set=[wd.lower() for wd in train_set if wd.isalpha()]
    fd=nltk.FreqDist(train_set)
    wds=[ wd[0] for wd in fd.most_common(dict_length) ]
    r_text=[]
    for _ in range(target_length):
        r_text=r_text+ [ random.choice(wds) ]
    r_text=' '.join(r_text)
    return r_text

# 25 Define a function find_language() that takes a string as its argument,
# and returns a list of languages that have that string as a word.
# Use the udhr corpus and limit your searches to files in the Latin-1 encoding.

def find_language(wd='universal'):
    lang_list = [lang_id[0:lang_id.index('-')]
                 for lang_id in nltk.corpus.udhr.fileids()
                 if lang_id[-7:]=='-Latin1' and
                 wd in nltk.corpus.udhr.words(lang_id)]
    return lang_list

# 26 What is the branching factor of the noun hypernym hierarchy?
# I.e. for every noun synset that has hyponyms — or children in the hypernym hierarchy —
# how many do they have on average? You can get all noun synsets using wn.all_synsets('n').

def branching_factor(hierarchy='n'):
    branch_list = [len(syn.hyponyms())
                   for syn in nltk.corpus.wordnet.all_synsets(hierarchy)
                   if syn.hyponyms()!=[]]
    return 1.0*sum(branch_list)/len(branch_list)

# 27 The polysemy of a word is the number of senses it has. Using WordNet,
# we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')).
# Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.

def polysemy_factor(hierarchy='n'):
    polysemy_list = [len(nltk.corpus.wordnet.synsets(lm, hierarchy))
                     for lm in nltk.corpus.wordnet.all_lemma_names(hierarchy)]
    return 1.0*sum(polysemy_list)/len(polysemy_list)

# 28 Use one of the predefined similarity measures to score the similarity
# of each of the following pairs of words. Rank the pairs in order of decreasing similarity.
# How close is your ranking to the order given here, an order that was established experimentally
# by (Miller & Charles, 1998): car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore,
# asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock, bird-crane,
# tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle,
# cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave,
# coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string

def wd_distance(wd_list=''):
    if wd_list=='':
        wd_list=[['car', 'automobile'],
                 ['gem', 'jewel'],
                 ['journey', 'voyage'],
                 ['boy', 'lad'],
                 ['coast', 'shore'],
                 ['asylum', 'madhouse'],
                 ['magician', 'wizard'],
                 ['midday', 'noon'],
                 ['furnace', 'stove'],
                 ['food', 'fruit'],
                 ['bird', 'cock'],
                 ['bird', 'crane'],
                 ['tool', 'implement'],
                 ['brother', 'monk'],
                 ['lad', 'brother'],
                 ['crane', 'implement'],
                 ['journey', 'car'],
                 ['monk', 'oracle'],
                 ['cemetery', 'woodland'],
                 ['food', 'rooster'],
                 ['coast', 'hill'],
                 ['forest', 'graveyard'],
                 ['shore', 'woodland'],
                 ['monk', 'slave'],
                 ['coast', 'forest'],
                 ['lad', 'wizard'],
                 ['chord', 'smile'],
                 ['glass', 'magician'],
                 ['rooster', 'voyage'],
                 ['noon', 'string']]
    aux_list=[]
    for wds in wd_list:
        syn1=nltk.corpus.wordnet.synsets(wds[0])[0]
        syn2=nltk.corpus.wordnet.synsets(wds[1])[0]
        aux_list=aux_list + [ (syn1.path_similarity(syn2),wds) ]
    aux_list.sort(reverse=True)
    return aux_list