'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# Chapter 4

# 1 Find out more about sequence objects using Python's help facility. In the interpreter, type help(str), help(list), and help(tuple). This will give you a full list of the functions supported by each type. Some functions have special names flanked with underscore; as the help documentation shows, each such function corresponds to something more familiar. For example x.__getitem__(y) is just a long-winded way of saying x[y].

# NA

# 2 Identify three operations that can be performed on both tuples and lists. Identify three list operations that cannot be performed on tuples. Name a context where using a list instead of a tuple generates a Python error.

# NA    

# 3 Find out how to create a tuple consisting of a single item. There are at least two ways to do this.

tup1 = (1,)
tup2 = tuple([1])

# 4 Create a list words = ['is', 'NLP', 'fun', '?']. Use a series of assignment statements (e.g. words[1] = words[2]) and a temporary variable tmp to transform this list into the list ['NLP', 'is', 'fun', '!']. Now do the same transformation using tuple assignment.

words = ['is', 'NLP', 'fun', '?']
words[3] = words[0]
words[0] = words[1]
words[1] = words[3]
words[3] = '!'

words = ['is', 'NLP', 'fun', '?']
words[0], words[1], words[3] = words[1], words[0], '!'

# 5 Read about the built-in comparison function cmp, by typing help(cmp). How does it differ in behavior from the comparison operators?

print cmp(1,2)<0     # True
print cmp(1,1)==0    # True
print cmp('B','A')>0 # True

# 6 Does the method for creating a sliding window of n-grams behave correctly for the two limiting cases: n = 1, and n = len(sent)?

# NA

# 7 We pointed out that when empty strings and empty lists occur in the condition part of an if clause, they evaluate to False. In this case, they are said to be occurring in a Boolean context. Experiment with different kind of non-Boolean expressions in Boolean contexts, and see whether they evaluate as True or False.

# NA

# 8 Use the inequality operators to compare strings, e.g. 'Monty' < 'Python'. What happens when you do 'Z' < 'a'? Try pairs of strings which have a common prefix, e.g. 'Monty' < 'Montague'. Read up on "lexicographical sort" in order to understand what is going on here. Try comparing structured objects, e.g. ('Monty', 1) < ('Monty', 2). Does this behave as expected?

# NA

# 9 Write code that removes whitespace at the beginning and end of a string, and normalizes whitespace between words to be a single space character.
# do this task using split() and join()
# do this task using regular expression substitutions

' '.join(' test1    test2 '.split())

import re
re.sub('\s+',' ',re.sub('^\s*|\s*$','',' test1    test2 '))

# 10 Write a program to sort words by length. Define a helper function cmp_len which uses the cmp comparison function on word lengths.

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
sorted(sent, lambda x, y: cmp(len(x), len(y)))

# 11 Create a list of words and store it in a variable sent1. Now assign sent2 = sent1. Modify one of the items in sent1 and verify that sent2 has changed.
# Now try the same exercise but instead assign sent2 = sent1[:]. Modify sent1 again and see what happens to sent2. Explain.
# Now define text1 to be a list of lists of strings (e.g. to represent a text consisting of multiple sentences. Now assign text2 = text1[:], assign a new value to one of the words, e.g. text1[1][1] = 'Monty'. Check what this did to text2. Explain.
# Load Python's deepcopy() function (i.e. from copy import deepcopy), consult its documentation, and test that it makes a fresh copy of any object.

sent1 ='Create a list of words and store it in a variable sent1'.split()
sent2 = sent1
sent1[1] = 'Monty'
print sent2

sent1 ='Create a list of words and store it in a variable sent1'.split()
sent2 = sent1[:]
sent1[1] = 'Monty'
print sent2

text1 =[ 'Create a list of words and store it in a variable sent1'.split(),
         'Now try the same exercise but instead assign sent2 = sent1[:]'.split(),
         'Now define text1 to be a list of lists of strings'.split() ]
text2 = text1[:]
text1[1][1] = 'Monty'
print text2[1]

import copy
text1 =[ 'Create a list of words and store it in a variable sent1'.split(),
         'Now try the same exercise but instead assign sent2 = sent1[:]'.split(),
         'Now define text1 to be a list of lists of strings'.split() ]
text2 = copy.deepcopy(text1)
text1[1][1] = 'Monty'
print text2[1]

# 12 Initialize an n-by-m list of lists of empty strings using list multiplication, e.g. word_table = [[''] * n] * m. What happens when you set one of its values, e.g. word_table[1][2] = "hello"? Explain why this happens. Now write an expression using range() to construct a list of lists, and show that it does not have this problem.

lst=[[''] * 3] * 4
lst[1][2]='Monty'
print lst

lst=[]
for i in range(4):
    lst.append([''] * 3)
lst[1][2]='Monty'
print lst

# 13 Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.

def count_vowels(txt='Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.'.split()):
    lst = [ (len(wd), len(re.findall('[aeiou]',wd))) for wd in txt ]
    max_wd_len = max(lst)[0]
    max_wd_vow = max([n[1] for n in lst])
    auxout=[]
    for i in range(max_wd_len):
        auxout.append([ 0 ] * max_wd_vow)
    for n in lst:
        auxout[n[0]-1][n[1]-1]=auxout[n[0]-1][n[1]-1]+1
    return auxout

# 14 Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.

def novel_n(txt='Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.', n=0.1):
    txt=txt.split()
    cut = int((1-n) * len(txt))
    wds1, wds2 = set(txt[:cut]), set(txt[cut:])
    return wds2 - wds1

# 15 Write a program that takes a sentence expressed as a single string, splits it and counts up the words. Get it to print out each word and the word's frequency, one per line, in alphabetical order.

def fdist_txt(txt='Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.'):
    txt=txt.split()
    wds=set(txt)
    fwds=[ (1.0*txt.count(wd)/len(txt), wd) for wd in wds ]
    fwds=sorted(fwds,reverse=True)
    for wd in fwds:
        print(wd[1], wd[0])
    return fwds

# 16 Read up on Gematria, a method for assigning numbers to words, and for mapping between words having the same number to discover the hidden meaning of texts (http://en.wikipedia.org/wiki/Gematria, http://essenes.net/gemcal.htm).
# Write a function gematria() that sums the numerical values of the letters of a word, according to the letter values in letter_vals:
# >>> letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
# ... 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
# ... 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
# Process a corpus (e.g. nltk.corpus.state_union) and for each document, count how many of its words have the number 666.
# Write a function decode() to process a text, randomly replacing words with their Gematria equivalents, in order to discover the "hidden meaning" of the text.

def gematria(wd='example',
             letter_vals={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
                          'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
                          'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}):
    return sum(letter_vals[ch.lower()] for ch in wd if ch in letter_vals.keys())

def find_gematria_vals(txt=nltk.corpus.state_union.words(),gematria_val=666):
    txt=[ wd.lower() for wd in txt ]
    txt=set(txt)
    wds=[]
    for wd in txt:
        if gematria(wd)==gematria_val:
            wds=wds+[wd]
    return sorted(wds)

# 17 Write a function shorten(text, n) to process a text, omitting the n most frequently occurring words of the text. How readable is it?

def shorten_text(txt=nltk.corpus.state_union.words(),num_remove=3):
    txt=[ wd.lower() for wd in txt if wd.isalpha()]
    fdist=nltk.FreqDist(txt)
    rem_lst=[ wd[0] for wd in fdist.most_common(num_remove) ]
    return [ rem_lst, [ wd for wd in txt if wd.lower() not in rem_lst ] ]

# 18 Write code to print out an index for a lexicon, allowing someone to look up words according to their meanings (or pronunciations; whatever properties are contained in lexical entries).

def prepare_index(txt='Write code to print out an index for a lexicon'.split()):
    cmu=nltk.corpus.cmudict.dict()
    txt=[ wd.lower() for wd in txt ]
    lst_pron = [ ('_'.join(cmu_i), wd) for wd in txt for cmu_i in cmu[wd] if cmu.has_key(wd) ]
    lst_mean = [ (syn.definition(), wd) for wd in txt for syn in nltk.corpus.wordnet.synsets(wd) ]
    return nltk.Index(lst_pron + lst_mean)

ind=prepare_index()
ind['IH1_N_D_EH0_K_S']
# ['index']
ind['a fabric with a dyed pattern pressed onto it (usually by engraved rollers)']
# ['print']

# 19 Write a list comprehension that sorts a list of WordNet synsets for proximity to a given synset. For example, given the synsets minke_whale.n.01, orca.n.01, novel.n.01, and tortoise.n.01, sort them according to their shortest_path_distance() from right_whale.n.01.

lst=['minke_whale.n.01', 'orca.n.01', 'novel.n.01', 'tortoise.n.01']
tgt='right_whale.n.01'
[ sort_syn[1] for sort_syn in sorted([(nltk.corpus.wordnet.synset(tgt).shortest_path_distance(nltk.corpus.wordnet.synset(syn)), syn) for syn in lst]) ]
# ['minke_whale.n.01', 'orca.n.01', 'tortoise.n.01', 'novel.n.01']

# 20 Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by decreasing frequency. E.g. if the input list contained 10 instances of the word table and 9 instances of the word chair, then table would appear before chair in the output list.

def fdist_lst(wds=nltk.word_tokenize('Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by decreasing frequency. E.g. if the input list contained 10 instances of the word table and 9 instances of the word chair, then table would appear before chair in the output list.')):
    wds=[ wd.lower() for wd in wds if wd.isalpha() ]
    fdist=nltk.FreqDist(wds)
    return [ wd[0] for wd in fdist.most_common() ]

# 21 Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings. Can you do this in a single line, using set.difference()?

def vocab_diff(txt='Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings. Can you do this in a single line, using set.difference()?', vocab='can you do this in a single line using set difference'.split()):
    txt_set = set( [ wd.lower() for wd in nltk.word_tokenize(txt) if wd.isalpha() ] )
    vocab_set = set(vocab)
    return txt_set-vocab_set
    
# 22 Import the itemgetter() function from the operator module in Python's standard library (i.e. from operator import itemgetter). Create a list words containing several words. Now try calling: sorted(words, key=itemgetter(1)), and sorted(words, key=itemgetter(-1)). Explain what itemgetter() is doing.

import operator
lst='Import the itemgetter() function from the operator module in Python\'s standard library (i.e. from operator import itemgetter). Create a list words containing several words. Now try calling: sorted(words, key=itemgetter(1)), and sorted(words, key=itemgetter(-1)). Explain what itemgetter() is doing.'.split()
lst=[wd for wd in lst if len(wd)>1]
sorted(lst, key=operator.itemgetter(1))  # sorts by char in pos 1
sorted(lst, key=operator.itemgetter(-1)) # sorts by char in pos -1

# 23 Write a recursive function lookup(trie, key) that looks up a key in a trie, and returns the value it finds. Extend the function to return a word when it is uniquely determined by its prefix (e.g. vanguard is the only word that starts with vang-, so lookup(trie, 'vang') should return the same thing as lookup(trie, 'vanguard')).

def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value
trie = {}
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
insert(trie, 'chic', 'stylish')
insert(trie, 'avant-garde', 'vanguard')

def lookup_trie(trie, wd):
    if trie.has_key('value'):
        return trie['value']
    if wd=='' and len(trie.keys())==1:
        return lookup_trie(trie[trie.keys()[0]], '')
    if wd!='':
        if trie.has_key(wd[0]):
            return lookup_trie(trie[wd[0]], wd[1:])
    return False

lookup_trie(trie,'surprise')
# False
lookup_trie(trie,'chat')
# 'cat'
lookup_trie(trie,'ch')
# False
lookup_trie(trie,'avant')
# 'vanguard'

# 24 Read up on "keyword linkage" (chapter 5 of (Scott & Tribble, 2006)). Extract keywords from NLTK's Shakespeare Corpus and using the NetworkX package, plot keyword linkage networks.

# Reference material not found

# 25 Read about string edit distance and the Levenshtein Algorithm. Try the implementation provided in nltk.edit_distance(). In what way is this using dynamic programming? Does it use the bottom-up or top-down approach? [See also http://norvig.com/spell-correct.html]

# Edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other
# The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other. It is named after Vladimir Levenshtein, who considered this distance in 1965.

# PSEUDOCODE

# Iterative with full matrix[edit]
# Main article: Wagner–Fischer algorithm
# Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.
# This algorithm, an example of

# *** bottom-up dynamic programming, ***

# is discussed, with variants, in the 1974 article The String-to-string correction problem by Robert A. Wagner and Michael J. Fischer.[3]
# This is a straightforward pseudocode implementation for a function LevenshteinDistance that takes two strings, s of length m, and t of length n, and returns the Levenshtein distance between them:
# 
# function LevenshteinDistance(char s[1..m], char t[1..n]):
#   // for all i and j, d[i,j] will hold the Levenshtein distance between
#   // the first i characters of s and the first j characters of t;
#   // note that d has (m+1)*(n+1) values
#   declare int d[0..m, 0..n]
#  
#   set each element in d to zero
#  
#   // source prefixes can be transformed into empty string by
#   // dropping all characters
#   for i from 1 to m:
#       d[i, 0] := i
#  
#   // target prefixes can be reached from empty source prefix
#   // by inserting every character
#   for j from 1 to n:
#       d[0, j] := j
#  
#   for j from 1 to n:
#       for i from 1 to m:
#           if s[i] = t[j]:
#             d[i, j] := d[i-1, j-1]              // no operation required
#           else:
#             d[i, j] := minimum(d[i-1, j] + 1,   // a deletion
#                                d[i, j-1] + 1,   // an insertion
#                                d[i-1, j-1] + 1) // a substitution
#  
#   return d[m, n]

# ACTUAL CODE

# def _edit_dist_init(len1, len2):
#     lev = []
#     for i in range(len1):
#         lev.append([0] * len2)  # initialize 2D array to zero
#     for i in range(len1):
#         lev[i][0] = i           # column 0: 0,1,2,3,4,...
#     for j in range(len2):
#         lev[0][j] = j           # row 0: 0,1,2,3,4,...
#     return lev
# 
# 
# def _edit_dist_step(lev, i, j, s1, s2, transpositions=False):
#     c1 = s1[i - 1]
#     c2 = s2[j - 1]
# 
#     # skipping a character in s1
#     a = lev[i - 1][j] + 1
#     # skipping a character in s2
#     b = lev[i][j - 1] + 1
#     # substitution
#     c = lev[i - 1][j - 1] + (c1 != c2)
# 
#     # transposition
#     d = c + 1  # never picked by default
#     if transpositions and i > 1 and j > 1:
#         if s1[i - 2] == c2 and s2[j - 2] == c1:
#             d = lev[i - 2][j - 2] + 1
# 
#     # pick the cheapest
#     lev[i][j] = min(a, b, c, d)
# 
# 
# [docs]def edit_distance(s1, s2, transpositions=False):
#     """
#     Calculate the Levenshtein edit-distance between two strings.
#     The edit distance is the number of characters that need to be
#     substituted, inserted, or deleted, to transform s1 into s2.  For
#     example, transforming "rain" to "shine" requires three steps,
#     consisting of two substitutions and one insertion:
#     "rain" -> "sain" -> "shin" -> "shine".  These operations could have
#     been done in other orders, but at least three steps are needed.
# 
#     This also optionally allows transposition edits (e.g., "ab" -> "ba"),
#     though this is disabled by default.
# 
#     :param s1, s2: The strings to be analysed
#     :param transpositions: Whether to allow transposition edits
#     :type s1: str
#     :type s2: str
#     :type transpositions: bool
#     :rtype int
#     """
#     # set up a 2-D array
#     len1 = len(s1)
#     len2 = len(s2)
#     lev = _edit_dist_init(len1 + 1, len2 + 1)
# 
#     # iterate over the array
#     for i in range(len1):
#         for j in range(len2):
#             _edit_dist_step(lev, i + 1, j + 1, s1, s2, transpositions=transpositions)
#     return lev[len1][len2]

# 26 The Catalan numbers arise in many applications of combinatorial mathematics, including the counting of parse trees (6). The series can be defined as follows: C0 = 1, and Cn+1 = Σ0..n (CiCn-i).
# Write a recursive function to compute nth Catalan number Cn.
# Now write another function that does this computation using dynamic programming.
# Use the timeit module to compare the performance of these functions as n increases.

def naive_catalan(n=0):
    if n==0:
        return 1
    return sum([ naive_catalan(i) * naive_catalan(n-1-i) for i in range(n) ])

def dynamic_catalan(n=0):
    cat_lst=[ 1 ]
    for i in range(n):
        cat_lst = cat_lst + [ sum([ cat_lst[j] * cat_lst[i-j] for j in range(i+1) ]) ]
    return cat_lst[n]

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

import timeit
num=11
nc=wrapper(naive_catalan,num)
nd=wrapper(dynamic_catalan,num)
naive_t=timeit.Timer(nc)
dynamic_t=timeit.Timer(nd)
naive_t.repeat(3,100)   
dynamic_t.repeat(3,100)

# num=10
# naive:   [1.6463429927825928, 1.644212007522583, 1.6704611778259277]
# dynamic: [0.0019729137420654297, 0.0012919902801513672, 0.0012080669403076172]
# num=11
# naive:   [5.00885009765625, 4.844187021255493, 5.000247001647949]
# dynamic: [0.0013511180877685547, 0.0013480186462402344, 0.0013689994812011719]

# 27 Reproduce some of the results of (Zhao & Zobel, 2007) concerning authorship identification.

# Reference material not found

# 28 Study gender-specific lexical choice, and see if you can reproduce some of the results of http://www.clintoneast.com/articles/words.php

# Reference material not found

import newspaper

def extract_articles(news_source='http://cnn.com',num=10):
    news_source = newspaper.build(news_source, memoize_articles=False)
    output=[]
    for art in news_source.articles[:min(num,len(news_source.articles))]:
        art.download()
        art.parse()
        raw=art.text
        output=output+nltk.word_tokenize(raw)
    return output
        
def find_common(txt=nltk.corpus.brown.words(),num=10,remove_stopwords=True):
    txt = [ wd.lower() for wd in txt if wd.isalpha()]
    if remove_stopwords:
        stopwords=nltk.corpus.stopwords.words('english')
        txt = [ wd for wd in txt if wd not in stopwords ]
    fdist = nltk.FreqDist(txt)
    return [ wd[0] for wd in fdist.most_common(num) ]

def find_signature(txt=nltk.corpus.brown.words(),sign_length=100,remove_stopwords=False):
    txt = [ wd.lower() for wd in txt if wd.isalpha()]
    if remove_stopwords:
        stopwords=nltk.corpus.stopwords.words('english')
        txt = [ wd for wd in txt if wd not in stopwords ]
    fdist = nltk.FreqDist(txt)
    return [(wd[0], i) for (i, wd) in enumerate(fdist.most_common(sign_length))]

female_magazines=['http://www.elle.com','http://www.cosmopolitan.com']
fem=[]
for src in female_magazines:
    fem=fem+extract_articles(src,num=100)
fem_mc = find_common(fem,25)
fem_t = nltk.Text(fem)
male_magazines=['http://www.maxim.com']
mal=[]
for src in male_magazines:
    mal=mal+extract_articles(src,num=100)
mal_mc = find_common(mal,25)
mal_t = nltk.Text(mal)
com_mc = sorted(list(set(mal_mc) & set(fem_mc)))
# [u'also', u'back', u'even', u'first', u'get', u'got', u'like', u'new', u'one', u'said', u'time', u'women', u'would']

fem_sig_ws=find_signature(fem,sign_length=1000,remove_stopwords=False)
fem_sig_ns=find_signature(fem,sign_length=1000,remove_stopwords=True)
mal_sig_ws=find_signature(mal,sign_length=1000,remove_stopwords=False)
mal_sig_ns=find_signature(mal,sign_length=1000,remove_stopwords=True)

# test_src=['http://www.elle.com','http://www.cosmopolitan.com', 'http://www.maxim.com', 'http://www.huffingtonpost.com', 'http://www.glamour.com', '' 'http://cnn.com', 'http://www.time.com', 'http://www.ted.com']
test_src=['http://www.elle.com','http://www.cosmopolitan.com', 'http://www.maxim.com']
lst=[]
for src in test_src:
    txt=extract_articles(src,num=10)
    txt_sig_ws=find_signature(txt,sign_length=1000,remove_stopwords=False)
    txt_sig_ns=find_signature(txt,sign_length=1000,remove_stopwords=True)
    lst=lst+ [ [ src,
                 nltk.spearman_correlation(txt_sig_ws, fem_sig_ws),
                 nltk.spearman_correlation(txt_sig_ns, fem_sig_ns),
                 nltk.spearman_correlation(txt_sig_ws, mal_sig_ws),
                 nltk.spearman_correlation(txt_sig_ns, mal_sig_ns) ] ]
# ['http://www.elle.com', -3.7880321254308464, -7.913619616139419, -4.392126028805952, -11.42968626823723]
# ['http://www.cosmopolitan.com', -0.7200827425758876, -2.0631836483509884, -2.343372184363161, -5.471496896822967]
# ['http://www.maxim.com', -6.033499667091246, -19.795347645052622, -4.359960113887133, -10.742962959669567]

# 29 Write a recursive function that pretty prints a trie in alphabetically sorted order, e.g.:
# chair: 'flesh'
# ---t: 'cat'
# --ic: 'stylish'
# ---en: 'dog'

# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         trie['value'] = value
# trie = {}
# insert(trie, 'chat', 'cat')
# insert(trie, 'chien', 'dog')
# insert(trie, 'chair', 'flesh')
# insert(trie, 'chic', 'stylish')

def print_trie(trie,root=''):
    if trie.has_key('value'):
        print('{:<{width}}: '.format(root, width=10) + trie['value'])
    else:
        listkeys=sorted(trie.keys())
        key=listkeys[0]
        print_trie(trie[key],root + key)
        for key in listkeys[1:]:
            print_trie(trie[key],'-'*len(root) + key)
    return 'Happiness be with you! :)'
    
# 30 With the help of the trie data structure, write a recursive function that processes text, locating the uniqueness point in each word, and discarding the remainder of each word. How much compression does this give? How readable is the resulting text?

# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         trie['value'] = value
            
def prune_wd(wd, trie, root='', pruned=''):
    if trie.has_key('value'):
        return pruned
    root=root+wd[0]
    if len(trie.keys())==1:
        return prune_wd(wd[1:], trie[wd[0]], root, pruned)
    return prune_wd(wd[1:], trie[wd[0]], root, root)

def trie_and_trim(raw='With the help of the trie data structure, write a recursive function that processes text, locating the uniqueness point in each word, and discarding the remainder of each word. How much compression does this give? How readable is the resulting text?'):
    txt=[ wd.lower() for wd in nltk.word_tokenize(raw) if wd.isalpha() ]
    wds=set(txt)
    trie={}
    for wd in wds:
        insert(trie,wd,wd)
    out_txt=[]
    for wd in txt:
        out_txt=out_txt+[ prune_wd(wd,trie) ]
    return 1.0*len(' '.join(out_txt))/len(' '.join(txt)), out_txt, trie
# (0.49382716049382713, ['wi', 'the', 'he', 'o', 'the', 'tr', 'da', 's', 'wr', 'a', 'rec', 'f', 'tha', 'pr', 'te', 'l', 'the', 'u', 'po', 'in', 'e', 'wo', 'a', 'di', 'the', 'rem', 'o', 'e', 'wo', 'ho', 'm', 'c', 'do', 'thi', 'g', 'ho', 'rea', 'is', 'the', 'res', 'te'], {'a': {'value': 'a', 'n': {'d': {'value': 'and'}}}, 'c': {'o': {'m': {'p': {'r': {'e': {'s': {'s': {'i': {'o': {'n': {'value': 'compression'}}}}}}}}}}}, 'e': {'a': {'c': {'h': {'value': 'each'}}}}, 'd': {'a': {'t': {'a': {'value': 'data'}}}, 'i': {'s': {'c': {'a': {'r': {'d': {'i': {'n': {'g': {'value': 'discarding'}}}}}}}}}, 'o': {'e': {'s': {'value': 'does'}}}}, 'g': {'i': {'v': {'e': {'value': 'give'}}}}, 'f': {'u': {'n': {'c': {'t': {'i': {'o': {'n': {'value': 'function'}}}}}}}}, 'i': {'s': {'value': 'is'}, 'n': {'value': 'in'}}, 'h': {'e': {'l': {'p': {'value': 'help'}}}, 'o': {'w': {'value': 'how'}}}, 'm': {'u': {'c': {'h': {'value': 'much'}}}}, 'l': {'o': {'c': {'a': {'t': {'i': {'n': {'g': {'value': 'locating'}}}}}}}}, 'o': {'f': {'value': 'of'}}, 'p': {'r': {'o': {'c': {'e': {'s': {'s': {'e': {'s': {'value': 'processes'}}}}}}}}, 'o': {'i': {'n': {'t': {'value': 'point'}}}}}, 's': {'t': {'r': {'u': {'c': {'t': {'u': {'r': {'e': {'value': 'structure'}}}}}}}}}, 'r': {'e': {'a': {'d': {'a': {'b': {'l': {'e': {'value': 'readable'}}}}}}, 'c': {'u': {'r': {'s': {'i': {'v': {'e': {'value': 'recursive'}}}}}}}, 'm': {'a': {'i': {'n': {'d': {'e': {'r': {'value': 'remainder'}}}}}}}, 's': {'u': {'l': {'t': {'i': {'n': {'g': {'value': 'resulting'}}}}}}}}}, 'u': {'n': {'i': {'q': {'u': {'e': {'n': {'e': {'s': {'s': {'value': 'uniqueness'}}}}}}}}}}, 't': {'h': {'a': {'t': {'value': 'that'}}, 'i': {'s': {'value': 'this'}}, 'e': {'value': 'the'}}, 'r': {'i': {'e': {'value': 'trie'}}}, 'e': {'x': {'t': {'value': 'text'}}}}, 'w': {'i': {'t': {'h': {'value': 'with'}}}, 'r': {'i': {'t': {'e': {'value': 'write'}}}}, 'o': {'r': {'d': {'value': 'word'}}}}})

# def lookup_trie(trie, wd):
#     if trie.has_key('value'):
#         return trie['value']
#     if wd=='' and len(trie.keys())==1:
#         return lookup_trie(trie[trie.keys()[0]], '')
#     if wd!='':
#         if trie.has_key(wd[0]):
#             return lookup_trie(trie[wd[0]], wd[1:])
#     return False

test=trie_and_trim()
lookup_trie(test[2], 'wi')
# 'with'
lookup_trie(test[2], 'he')
# 'help'
    
# 31 Obtain some raw text, in the form of a single, long string. Use Python's textwrap module to break it up into multiple lines. Now write code to add extra spaces between words, in order to justify the output. Each line must have the same width, and spaces must be approximately evenly distributed across each line. No line can begin or end with a space.

def wrappifier(txt='Obtain some raw text, in the form of a single, long string. Use Python\'s textwrap module to break it up into multiple lines. Now write code to add extra spaces between words, in order to justify the output. Each line must have the same width, and spaces must be approximately evenly distributed across each line. No line can begin or end with a space.', wid=50):
    import textwrap, random
    sents=textwrap.wrap(txt,wid)
    aux_out=[]
    for sent in sents:
        add_sp=wid-len(sent)
        sent=sent.split()
        num_sp=len(sent)-1
        tot_sp=num_sp+add_sp
        base_sp=tot_sp/num_sp
        sp_list=[base_sp]*(num_sp-(tot_sp-base_sp*num_sp)) + [base_sp+1]*(tot_sp-base_sp*num_sp)
        random.shuffle(sp_list)
        sp_list=[0]+sp_list
        aux_sent=''
        for pos in range(len(sent)):
            aux_sent=aux_sent+' '*sp_list[pos]+sent[pos]
        aux_out=aux_out+ [ aux_sent ]
    return aux_out

# 32 Develop a simple extractive summarization tool, that prints the sentences of a document which contain the highest total word frequency. Use FreqDist() to count word frequencies, and use sum to sum the frequencies of the words in each sentence. Rank the sentences according to their score. Finally, print the n highest-scoring sentences in document order. Carefully review the design of your program, especially your approach to this double sorting. Make sure the program is written as clearly as possible.

def significant_sents(txt=nltk.corpus.reuters.raw(categories='income'),num=3):
    sents=nltk.sent_tokenize(txt)
    words=nltk.word_tokenize(txt)
    fdist=nltk.FreqDist(words)
    auxout=[]
    for sent in sents:
        wds=nltk.word_tokenize(sent)
        auxout=auxout+ [ (sum([ fdist[wd] for wd in wds ]),sent) ]
    auxout=sorted(auxout,reverse=True)
    return [ sent[1] for sent in auxout[:num] ]

# import newspaper
my_art=newspaper.article.Article('http://www.theonion.com/article/states-abortion-waiting-period-allows-women-explor-51606')
my_art.download()
my_art.parse()
raw=my_art.text
significant_sents(raw)

my_art=newspaper.article.Article('http://edition.cnn.com/2015/10/22/politics/hillary-clinton-benghazi-hearing-takeaways/index.html')
my_art.download()
my_art.parse()
raw=my_art.text
significant_sents(raw)

# 33 Read the following article on semantic orientation of adjectives. Use the NetworkX package to visualize a network of adjectives with edges to indicate same vs different semantic orientation. http://www.aclweb.org/anthology/P97-1023

import networkx

def adj_network_map(txt=nltk.corpus.brown.words(),include_but=True):
    txt_tokenized_searcher=nltk.TokenSearcher(txt)
    lst=txt_tokenized_searcher.findall('<\w*>(?:<and>|<but>|<or>)<\w*>')
    adj_lst=[]
    for con in lst:
        if     (nltk.corpus.wordnet.synsets(con[0],'a') and nltk.corpus.wordnet.synsets(con[2],'a')) and \
           not (nltk.corpus.wordnet.synsets(con[0],'n') and nltk.corpus.wordnet.synsets(con[2],'n')) and \
           not (nltk.corpus.wordnet.synsets(con[0],'v') and nltk.corpus.wordnet.synsets(con[2],'v')) and \
           not (con[0].isdigit()                        or con[2].isdigit()):
            if con[1]!='but':
                adj_lst=adj_lst+[(con[0],con[2],{'color':'g'})]
            elif include_but:
                adj_lst=adj_lst+[(con[0],con[2],{'color':'r'})]
    graph=networkx.Graph()
    #adj_set=set([con[0] for con in adj_lst ] + [con[1] for con in adj_lst])
    #graph.add_nodes_from(adj_set)
    graph.add_edges_from(adj_lst)
    edgelst=graph.edges()
    edgecol=[edg[2]['color'] for edg in graph.edges(data=True)]
    networkx.draw_networkx(graph,with_labels=False,edgelist=edgelst,node_size=10,edge_color=edgecol)
    return 'Awesomeness!!!'

# 34 Design an algorithm to find the "statistically improbable phrases" of a document collection. http://www.amazon.com/gp/search-inside/sipshelp.html

# Amazon.com Statistically Improbable Phrases
# Amazon.com's Statistically Improbable Phrases, or "SIPs", are the most distinctive phrases in the text of books in the Search Inside!™ program. To identify SIPs, our computers scan the text of all books in the Search Inside! program. If they find a phrase that occurs a large number of times in a particular book relative to all Search Inside! books, that phrase is a SIP in that book.
# SIPs are not necessarily improbable within a particular book, but they are improbable relative to all books in Search Inside!. For example, most SIPs for a book on taxes are tax related. But because we display SIPs in order of their improbability score, the first SIPs will be on tax topics that this book mentions more often than other tax books. For works of fiction, SIPs tend to be distinctive word combinations that often hint at important plot elements.
# Click on a SIP to view a list of books in which the phrase occurs. You can also view a list of references to the phrase in each book. Learn more about the phrase by clicking on the A9.com search link.
# Have some ideas for improving this feature? Please send your feedback to sitb-feedback@amazon.com

# What is meant by 'phrases'?

# From https://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf
test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=['NP'])
class ChunkParser(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for _,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.TrigramTagger(train_data)
    def parse(self, sentence):
        pos_tags = [pos for (_,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
NPChunker = ChunkParser(train_sents)
print NPChunker.evaluate(test_sents)

#raw = 'Write a program to implement a brute-force algorithm for discovering word squares, a kind of n × n crossword in which the entry in the nth row is the same as the entry in the nth column.'
raw = 'The big brown fox jumped over the sleepy lazy dog.'
sents = nltk.sent_tokenize(raw)
wds_sents = [nltk.word_tokenize(sent) for sent in sents]
tag_sents = [nltk.pos_tag(sent) for sent in wds_sents]
chunks = NPChunker.parse(tag_sents)
# Fails - left for later

# 35 Write a program to implement a brute-force algorithm for discovering word squares, a kind of n × n crossword in which the entry in the nth row is the same as the entry in the nth column. For discussion, see http://itre.cis.upenn.edu/~myl/languagelog/archives/002679.html

def find_dic(root,dic):
    return [wd for wd in dic if wd[:len(root)]==root]
    
def find_wds(num,dic,wds):
    if len(wds)==num:
        return wds
    root=''
    for i in range(len(wds)):
        root=root+wds[i][len(wds)]
    reduced_dic=find_dic(root,dic)
    for wd in reduced_dic:
        aux_wds=wds+[wd]
        aux_wds=find_wds(num,dic,aux_wds)
        if len(aux_wds)==num:
            return aux_wds
    return []
        
def make_word_square(num=5,dic=nltk.corpus.words.words()):
    import random
    dic=[wd for wd in dic if len(wd)==num]
    random.shuffle(dic)
    wds=[]
    return find_wds(num,dic,wds)

dic3=['Mary', 'had', 'a', 'little', 'giant', 'BIT','ICE','TEN']
make_word_square(3, dic3)
dic5=['Mary', 'had', 'a', 'little', 'giant', 'HEART','EMBER','ABUSE','RESIN','TREND']
make_word_square(5, dic5)