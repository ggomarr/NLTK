'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# Chapter 3

# 1 Define a string s = 'colorless'. Write a Python statement
# that changes this to "colourless" using only the slice and concatenation operations.

s = 'colorless'
s = s[:4] + 'u' + s[4:]

# 2 We can use the slice notation to remove morphological endings on words.
# For example, 'dogs'[:-1] removes the last character of dogs, leaving dog.
# Use slice notation to remove the affixes from these words
# (we've inserted a hyphen to indicate the affix boundary, but omit this from your strings):
# dish-es, run-ning, nation-ality, un-do, pre-heat.

l = [ 'dishes', 'running', 'nationality', 'undo', 'preheat' ]
endings = ['es', 'ning', 'ality', 'do', 'heat'] # Some weird choices for affixes there
l = [ l[i][:-len(endings[i])] for i in range(len(l))]

# 3 We saw how we can generate an IndexError by indexing beyond the end of a string.
# Is it possible to construct an index that goes too far to the left, before the start of the string?

my_str = 'Is it possible to construct an index that goes too far to the left, before the start of the string?'
my_str[-len(my_str)]
my_str[-len(my_str)-1] # IndexError

# 4 We can specify a "step" size for the slice. The following returns every second character
# within the slice: monty[6:11:2]. It also works in the reverse direction: monty[10:5:-2]
# Try these for yourself, then experiment with different step values.

# NA

# 5 What happens if you ask the interpreter to evaluate monty[::-1]?
# Explain why this is a reasonable result.

monty = 'Monty Python'
if monty[::-1]=='nohtyP ytnoM':
    print('This statement is definitely true.')

# 6 Describe the class of strings matched by the following regular expressions.
# [a-zA-Z]+
# [A-Z][a-z]*
# p[aeiou]{,2}t
# \d+(\.\d+)?
# ([^aeiou][aeiou][^aeiou])*
# \w+|[^\w\s]+
# Test your answers using nltk.re_show().

print('[a-zA-Z]+')
nltk.re_show('[a-zA-Z]+','Matches all groups of characters, but not the number 3.')
print('[A-Z][a-z]*')
nltk.re_show('[A-Z][a-z]*','Matches Matches, Aitor, Joaquin, or Abba, but not chainsaw, or nyu.')
print('p[aeiou]{,2}t')
nltk.re_show('p[aeiou]{,2}t','Matches pt., Sengupta., put, paet, piit, or pot.')
print('\d+(\.\d+)?')
nltk.re_show('\d+(\.\d+)?','Matches numbers with decimals or not, like 0.1, 1000, or 1000.1.')
print('([^aeiou][aeiou][^aeiou])*')
nltk.re_show('([^aeiou][aeiou][^aeiou])*','Matches ?a_-ex+ih, tiptaptok, or (iptakto) (and some other unexpected shit).')
print('\w+|[^\w\s]+')
nltk.re_show('\w+|[^\w\s]+','Matches groups of characters and of non-(characters or spaces).')

# 7 Write regular expressions to match the following classes of strings:
#   A single determiner (assume that a, an, and the are the only determiners).
#   An arithmetic expression using integers, addition, and multiplication, such as 2*3+8.

print('((?<=\s)|^)(a|A|an|An|the|The)(?=\s|$)')
nltk.re_show('((?<=\s)|^)(a|A|an|An|the|The)(?=\s|$)','The big brown fox jumped over a big black ant carrying an umbrella.')

print('\d+[(\*|\+)\d+]+')
nltk.re_show('\d+[(\*|\+)\d+]+','2*3+8, 15+4*10+6000')

# 8 Write a utility function that takes a URL as its argument, and returns the contents of the URL,
# with all HTML markup removed. Use from urllib import request and then
# request.urlopen('http://nltk.org/').read().decode('utf8') to access the contents of the URL.

def html_reader(urladd='http://nltk.org/'):
    import urllib, bs4
    return bs4.BeautifulSoup(urllib.urlopen(urladd).read().decode('utf8')).get_text()

# 9 Save some text into a file corpus.txt. Define a function load(f) that reads from the file
# named in its sole argument, and returns a string containing the text of the file.
# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation
# in this text. Use one multi-line regular expression, with inline comments,
# using the verbose flag (?x).
# Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression:
# monetary amounts; dates; names of people and organizations.

#     pattern = r'''(?x)             # set flag to allow verbose, multiline regexps
#                   ([A-Z]\.)+       # abbreviations, e.g. U.S.A.
#                 | \w+(-\w+)*       # words with optional internal hyphens
#                 | \$?\d+(\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
#                 | \.\.\.           # ellipsis
#                 | [][.,;"'?():-_`] # these are separate tokens; includes ], [
#                '''

#     pattern = r'''(?x)                # set flag to allow verbose, multiline regexps
#                   [\[\].,;"'?():\-_`] # punctuation
#                '''

#     pattern = r'''(?x)                # set flag to allow verbose, multiline regexps
#                   [$€£]?              # currency symbol (optional)
#                   \d+                 # number
#                   (\.\d{,2})?         # decimal places (optional)
#                '''

def load_txt(filenom='/home/ggomarr/eclipse/workspace/Natural Language Tool Kit/001 Aux/test_text.txt'):
    f = open(filenom)
    raw = f.read().decode('utf8')
    pattern = r'''(?x)                # set flag to allow verbose, multiline regexps
                  [$€£]?              # currency symbol (optional)
                  \d+                 # number
                  (\.\d{,2})?         # decimal places (optional)
               '''
    raw = nltk.regexp_tokenize(raw, pattern)
    return raw
    
# 10 Rewrite the following loop as a list comprehension:
# >>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# >>> result = []
# >>> for word in sent:
# ...     word_len = (word, len(word))
# ...     result.append(word_len)
# >>> result
# [('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [ (wd, len(wd)) for wd in sent ]

# 11 Define a string raw containing a sentence of your own choosing.
# Now, split raw on some character other than space, such as 's'.

sent = 'The big brown fox jumped over a big black ant carrying an umbrella.'
sent.split('a')

# 12 Write a for loop to print out the characters of a string, one per line.

sent = 'The big brown fox jumped over a big black ant carrying an umbrella.'
for ch in sent:
    print(ch)
 
# 13 What is the difference between calling split on a string with no argument
# or with ' ' as the argument, e.g. sent.split() versus sent.split(' ')?
# What happens when the string being split contains tab characters, consecutive space characters,
# or a sequence of tabs and spaces? (In IDLE you will need to use '\t' to enter a tab character.)
 
sent = 'The big brown fox jumped over\na\tbig black ant carrying an umbrella.'
sent.split()
sent.split(' ') 
 
# 14 Create a variable words containing a list of words. Experiment with words.sort()
# and sorted(words). What is the difference?
 
words = 'The big brown fox jumped over\na\tbig black ant carrying an umbrella.'.split()
words.sort()  # words gets modified
sorted(words) # the sorted list gets returned, but words stays the same
 
# 15 Explore the difference between strings and integers by typing the following at a Python prompt:
# "3" * 7 and 3 * 7. Try converting between strings and integers using int("3") and str(3).
 
# NA
 
# 16 Use a text editor to create a file called prog.py containing the single line
# monty = 'Monty Python'. Next, start up a new session with the Python interpreter,
# and enter the expression monty at the prompt. You will get an error from the interpreter.
# Now, try the following (note that you have to leave off the .py part of the filename):
# >>> from prog import monty
# >>> monty
# This time, Python should return with a value. You can also try import prog, in which case Python
# should be able to evaluate the expression prog.monty at the prompt.

# NA
 
# 17 What happens when the formatting strings %6s and %-6s are used to display strings
# that are longer than six characters?

'%6s' % 'Test'
'%6s' % 'Testing'
'%-6s' % 'Test'
'%-6s' % 'Testing'

# 18 Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur.
# (wh-words in English are used in questions, relative clauses and exclamations:
# who, which, what, and so on.) Print them in order. Are any words duplicated in this list,
# because of the presence of case distinctions or punctuation?

raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
tokens = nltk.regexp_tokenize(raw,'(?<=\s)((?:wh|Wh|WH)\w+)') # Finds a whole lot of whatever
# [u'What', u'whim', u'wholesomeness', u'whoever', u'whisper', u'When', u'whatever', u'whiten', ...

# 19 Create a file consisting of words and (made up) frequencies, where each line consists of a word,
# the space character, and a positive integer, e.g. fuzzy 53. Read the file into a Python list
# using open(filename).readlines(). Next, break each line into its two fields using split(),
# and convert the number into an integer using int(). The result should be a list of the form:
# [['fuzzy', 53], ...].

import re

filenom='/home/ggomarr/eclipse/workspace/Natural Language Tool Kit/001 Aux/freq_dict.txt'
raw = open(filenom).readlines()
freq_dict=[ [ re.findall('\w+',lin)[0], int(re.findall('\w+',lin)[1]) ] for lin in raw ]

# 20 Write code to access a favorite webpage and extract some text from it. For example,
# access a weather site and extract the forecast top temperature for your town or city today.
 
def html_grabber(urladd='http://www.elmundo.es/'):
    import urllib, bs4
    return bs4.BeautifulSoup(urllib.urlopen(urladd).read()).get_text()
    
# 21 Write a function unknown() that takes a URL as its argument, and returns a list of unknown words
# that occur on that webpage. In order to do this, extract all substrings consisting of
# lowercase letters (using re.findall()) and remove any items from this set that occur in the
# Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings. 

def html_unknown(urladd='http://nltk.org/'):
    import urllib, bs4
    raw = bs4.BeautifulSoup(urllib.urlopen(urladd).read()).get_text()
    tokens = nltk.regexp_tokenize(raw,'(?<=\s)[a-z]+')
    my_dict = nltk.corpus.words.words()
    unknown_tokens = [ wd for wd in tokens if wd not in my_dict ]
    return sorted(unknown_tokens)
# [u'analyzing', u'announcements', u'called', u'categorizing', u'creators', u'didn', u'educators', ...

# 22 Examine the results of processing the URL http://news.bbc.co.uk/ using the regular expressions
# suggested above. You will see that there is still a fair amount of non-textual data there,
# particularly Javascript commands. You may also find that sentence breaks have not been
# properly preserved. Define further regular expressions that improve the extraction of text
# from this web page.

# NA

# 23 Are you able to write a regular expression to tokenize text in such a way that the word don't
# is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+»

nltk.regexp_tokenize('You shouldn\'t do that! Please don\'t!','n\'t|\w+')
# ['You', 'shouldn', 't', 'do', 'that', 'Please', 'don', 't']
nltk.regexp_tokenize('You shouldn\'t do that! Please don\'t!','\w+(?=n\'t)|n\'t|\w+')
# ['You', 'should', "n't", 'do', 'that', 'Please', 'do', "n't"]

# 24 Try to write code to convert text into hAck3r, using regular expressions and substitution,
# where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to lowercase
# before converting it. Add more substitutions of your own. Now try to map s to two different values:
# $ for word-initial s, and 5 for word-internal s.

def hackerizator(raw='The soup ate the substrate in position number one at one sharp.',
                 mapeator=[['ate', '8'],
                           ['\ss', ' $'],
                           ['^s', '$'],
                           ['s', '5'],
                           ['e', '3'],
                           ['i', '1'],
                           ['o', '0'],
                           ['\.', '5w33t!']]
                 ):
    raw=raw.lower()
    for mapp3r in mapeator:
        raw=re.sub(mapp3r[0],mapp3r[1],raw)
    return raw

# 25 Pig Latin is a simple transformation of English text. Each word of the text is converted
# as follows: move any consonant (or consonant cluster) that appears at the start of the word
# to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin
# Write a function to convert a word to Pig Latin.
# Write code that converts text, instead of individual words.
# Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay),
# and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

def latin_pigs(wd='string'):
#    cons_pat='^[^aeiou\W]*'
    cons_pat='^([^aeiouy\W]*?(?:qu|ye)?[^aeiouy\W]*)'
    cons=re.findall(cons_pat,wd)
    return wd[len(cons[0]):] + cons[0] + 'ay' 

# 26 Download some text from a language that has vowel harmony (e.g. Hungarian),
# extract the vowel sequences of words, and create a vowel bigram table.

# Maybe later

# 27 Python's random module includes a function choice() which randomly chooses an item
# from a sequence, e.g. choice("aehh ") will produce one of four possible characters,
# with the letter h being twice as frequent as the others. Write a generator expression
# that produces a sequence of 500 randomly chosen letters drawn from the string "aehh ",
# and put this expression inside a call to the ''.join() function, to concatenate them
# into one long string. You should get a result that looks like uncontrolled sneezing
# or maniacal laughter: he haha ee heheeh eha. Use split() and join() again to normalize
# the whitespace in this string.

def maniacal_laughter(seed_chars='aehh ', length=500):
    import random
    raw=[]
    for _ in range(length):
        raw.append(random.choice(seed_chars))
    laughter=''.join(raw)
    laughter=' '.join(laughter.split())
    return laughter

# 28 Consider the numeric expressions in the following sentence from the MedLine Corpus:
# The corresponding free cortisol fractions in these sera were 4.53 +/- 0.15% and 8.16 +/- 0.23%,
# respectively. Should we say that the numeric expression 4.53 +/- 0.15% is three words?
# Or should we say that it's a single compound word? Or should we say that it is actually nine words,
# since it's read "four point five three, plus or minus zero point fifteen percent"?
# Or should we say that it's not a "real" word at all, since it wouldn't appear in any dictionary?
# Discuss these different possibilities. Can you think of application domains that motivate
# at least two of these answers?

# NA

# 29 Readability measures are used to score the reading difficulty of a text, for the purposes
# of selecting texts of appropriate difficulty for language learners. Let us define μw to be
# the average number of letters per word, and μs to be the average number of words per sentence,
# in a given text. The Automated Readability Index (ARI) of the text is defined to be:
# 4.71 μw + 0.5 μs - 21.43. Compute the ARI score for various sections of the Brown Corpus,
# including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words()
# produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences.

def compute_ari_brown(genres=['lore','learned']):
    output=[]
    for genre in genres:
        wds=nltk.corpus.brown.words(categories=genre)
        wd_len=[ len(wd) for wd in wds if wd.isalpha()]
        cpw=1.0*sum(wd_len)/len(wd_len)
        num_wds=len(wds)
        num_sents=len(nltk.corpus.brown.sents(categories=genre))
        wps=1.0*num_wds/num_sents
        ari=4.71*cpw+0.5*wps-21.43
        output=output + [ [genre,ari] ]
    return output

# 30 Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word.
# Do the same thing with the Lancaster Stemmer and see if you observe any differences.

import newspaper
hot_topics=newspaper.hot()
news_sources=newspaper.popular_urls()
cnn_paper = newspaper.build('http://cnn.com')
my_art=cnn_paper.articles[25]
my_art.download()
my_art.parse()
my_art.nlp()
raw=my_art.text
tokens=nltk.word_tokenize(raw)
port_stem = [ nltk.PorterStemmer().stem(wd).lower() for wd in tokens ]
lanc_stem = [ nltk.LancasterStemmer().stem(wd).lower() for wd in tokens ]
port_set=set(port_stem)
lanc_set=set(lanc_stem)
in_port_not_lanc = port_set-lanc_set
in_lanc_not_port = lanc_set-port_set

# 31 Define the variable saying to contain the list
# ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.'].
# Process this list using a for loop, and store the length of each word in a new list lengths.
# Hint: begin by assigning the empty list to lengths, using lengths = [].
# Then each time through the loop, use append() to add another length value to the list.
# Now do the same thing using a list comprehension.

saying=['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
lengths1=[]
for wd in saying:
    lengths1=lengths1+[ len(wd) ]
lengths2=[ len(wd) for wd in saying ]
print(lengths1==lengths2)

# 32 Define a variable silly to contain the string:
# 'newly formed bland ideas are inexpressible in an infuriating way'. (This happens to be the
# legitimate interpretation that bilingual English-Spanish speakers can assign to
# Chomsky's famous nonsense phrase, colorless green ideas sleep furiously according to Wikipedia).
# Now write code to perform the following tasks:
# Split silly into a list of strings, one per word, using Python's split() operation,
# and save this to a variable called bland.
# Extract the second letter of each word in silly and join them into a string, to get 'eoldrnnnna'.
# Combine the words in bland back into a single string, using join().
# Make sure the words in the resulting string are separated with whitespace.
# Print the words of silly in alphabetical order, one per line.

silly='newly formed bland ideas are inexpressible in an infuriating way'
bland=silly.split()
''.join([ wd[1] for wd in silly.split() ])
' '.join(bland)
for wd in sorted(silly.split()):
    print wd

# 33 The index() function can be used to look up items in sequences. For example,
# 'inexpressible'.index('e') tells us the index of the first position of the letter e.
# What happens when you look up a substring, e.g. 'inexpressible'.index('re')?
# Define a variable words containing a list of words. Now use words.index() to look up
# the position of an individual word.
# Define a variable silly as in the exercise above. Use the index() function
# in combination with list slicing to build a list phrase consisting of
# all the words up to (but not including) in in silly.

'inexpressible'.index('e')
'inexpressible'.index('re')

silly='newly formed bland ideas are inexpressible in an infuriating way'
bland=silly.split()
bland.index('in')
silly[:silly.index(' in ')]

# 34 Write code to convert nationality adjectives like Canadian and Australian
# to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names).

# Maybe later

# 35 Read the LanguageLog post on phrases of the form as best as p can and as best p can,
# where p is a pronoun. Investigate this phenomenon with the help of a corpus and the findall()
# method for searching tokenized text described in 3.5. http://itre.cis.upenn.edu/~myl/languagelog/archives/002733.html

nltk.Text(nltk.corpus.brown.words()).findall('<(?:A|a)s><best><as>?<\w*>(?:<can>|<could>)')
# as best he could; as best I could; as best Mike could; As best as I could; as best I could
nltk.Text(nltk.corpus.webtext.words()).findall('<(?:A|a)s><best><as>?<\w*>(?:<can>|<could>)')
# as best you can

nltk.Text(nltk.corpus.gutenberg.words()).findall('<(?:A|a)s><best>')
# None
nltk.Text(nltk.corpus.reuters.words()).findall('<(?:A|a)s><best>')
# None
nltk.Text(nltk.corpus.inaugural.words()).findall('<(?:A|a)s><best>')
# None
nltk.Text(nltk.corpus.nps_chat.words()).findall('<(?:A|a)s><best>')
# None

# 36 tudy the lolcat version of the book of Genesis, accessible as
# nltk.corpus.genesis.words('lolcat.txt'), and the rules for converting text into lolspeak at
# http://www.lolcatbible.com/index.php?title=How_to_speak_lolcat. Define regular expressions
# to convert English words into corresponding lolspeak words.

# Maybe later

# 37 Read about the re.sub() function for string substitution using regular expressions,
# using help(re.sub) and by consulting the further readings for this chapter. Use re.sub in writing
# code to remove HTML tags from an HTML file, and to normalize whitespace.

def remove_html_tags(urladd='http://nltk.org/'):
    import urllib
    raw_html = urllib.urlopen(urladd).read()
    raw_txt=re.sub('<[^>]*>',' ',raw_html)
    raw_txt=' '.join(raw_txt.split())
    return raw_txt
# See http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

# 38 An interesting challenge for tokenization is words that have been split across a line-break.
# E.g. if long-term is split, then we have the string long-\nterm.
# Write a regular expression that identifies words that are hyphenated at a line-break.
# The expression will need to include the \n character.
# Use re.sub() to remove the \n character from these words.
# How might you identify words that should not remain hyphenated once the newline is removed,
# e.g. 'encyclo-\npedia'?

def de_hyphen(raw="This text was cre-\nated so that the long-\nterm effects of heavy rain can be es-\ntablished."):
    wds=re.findall('\w*-\n\w*',raw)
    for wd_dirty in wds:
        wd_clean=re.sub('-\n','',wd_dirty)
        wd_aux = nltk.WordNetLemmatizer().lemmatize(wd_clean)
        if wd_aux!=wd_clean:
            can_be_Lemmatized=True
        else:
            can_be_Lemmatized=False
        wd_aux = nltk.PorterStemmer().stem(wd_clean)
        if wd_aux!=wd_clean:
            can_be_PorterStemmed=True
        else:
            can_be_PorterStemmed=False
        wd_aux = nltk.LancasterStemmer().stem(wd_clean)
        if wd_aux!=wd_clean:
            can_be_LancasterStemmed=True
        else:
            can_be_LancasterStemmed=False
        if wd_aux in nltk.corpus.words.words():
            is_in_dict=True
        else:
            is_in_dict=False
        if not can_be_Lemmatized and \
           not can_be_PorterStemmed and \
           not can_be_LancasterStemmed and \
           not is_in_dict:
            wd_clean=re.sub('-\n','-',wd_dirty)
        raw=re.sub(wd_dirty, wd_clean, raw)
    return raw

# 39 Read the Wikipedia entry on Soundex. Implement this algorithm in Python.

def soundex(nom='Robert'):
    aux_nom=nom[0]+re.sub('[hw]','',nom[1:])
    aux_nom=re.sub('[BbFfPpVv]+','1',aux_nom)
    aux_nom=re.sub('[CcGgJjKkQqSsXxZz]+','2',aux_nom)
    aux_nom=re.sub('[DdTt]+','3',aux_nom)
    aux_nom=re.sub('[Ll]+','4',aux_nom)
    aux_nom=re.sub('[MmNn]+','5',aux_nom)
    aux_nom=re.sub('[Rr]+','6',aux_nom)
    aux_nom=re.sub('[aeiouy]','',aux_nom)
    aux_nom=nom[0]+'{:0<3}'.format(aux_nom[1:])[:3]
    return aux_nom

# 40 Obtain raw texts from two or more genres and compute their respective reading difficulty scores
# as in the earlier exercise on reading difficulty. E.g. compare ABC Rural News and ABC Science News
# (nltk.corpus.abc). Use Punkt to perform sentence segmentation.

def compute_ari_raw(txt=nltk.corpus.abc.raw()):
    wds=nltk.word_tokenize(txt)
    wd_len=[ len(wd) for wd in wds if wd.isalpha()]
    cpw=1.0*sum(wd_len)/len(wd_len)
    num_wds=len(wds)
    num_sents=len(nltk.PunktSentenceTokenizer().tokenize(txt))
    wps=1.0*num_wds/num_sents
    ari=4.71*cpw+0.5*wps-21.43
    return ari

# 41 Rewrite the following nested loop as a nested list comprehension:
# >>> words = ['attribution', 'confabulation', 'elocution',
# ...          'sequoia', 'tenacious', 'unidirectional']
# >>> vsequences = set()
# >>> for word in words:
# ...     vowels = []
# ...     for char in word:
# ...         if char in 'aeiou':
# ...             vowels.append(char)
# ...     vsequences.add(''.join(vowels))
# >>> sorted(vsequences)
# ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
[ ''.join(vow_list) for vow_list in [ re.findall('[aeiou]',wd) for wd in words ] ]

# 42 Use WordNet to create a semantic index for a text collection. Extend the concordance
# search program in 3.6, indexing each word using the offset of its first synset,
# e.g. wn.synsets('dog')[0].offset (and optionally the offset of some of its ancestors
# in the hypernym hierarchy).

# Concordance search program in 3.6

# class IndexedText(object):
# 
#     def __init__(self, stemmer, text):
#         self._text = text
#         self._stemmer = stemmer
#         self._index = nltk.Index((self._stem(word), i)
#                                  for (i, word) in enumerate(text))
# 
#     def concordance(self, word, width=40):
#         key = self._stem(word)
#         wc = int(width/4)                # words of context
#         for i in self._index[key]:
#             lcontext = ' '.join(self._text[i-wc:i])
#             rcontext = ' '.join(self._text[i:i+wc])
#             ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
#             rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
#             print(ldisplay, rdisplay)
# 
#     def _stem(self, word):
#         return self._stemmer.stem(word).lower()
#      
# >>> porter = nltk.PorterStemmer()
# >>> grail = nltk.corpus.webtext.words('grail.txt')
# >>> text = IndexedText(porter, grail)
# >>> text.concordance('lie')
# r king ! DENNIS : Listen , strange women lying in ponds distributing swords is no
#  beat a very brave retreat . ROBIN : All lies ! MINSTREL : [ singing ] Bravest of
#        Nay . Nay . Come . Come . You may lie here . Oh , but you are wounded !
# doctors immediately ! No , no , please ! Lie down . [ clap clap ] PIGLET : Well
# ere is much danger , for beyond the cave lies the Gorge of Eternal Peril , which
#    you . Oh ... TIM : To the north there lies a cave -- the cave of Caerbannog --
# h it and lived ! Bones of full fifty men lie strewn about its lair . So , brave k
# not stop our fight ' til each one of you lies dead , and the Holy Grail returns t

class IndexedText():
    def __init__(self, text):
        self._text = text
        self._index = nltk.Index((self._offsetter(word), i)
                                 for (i, word) in enumerate(text)
                                 if nltk.corpus.wordnet.synsets(word.lower())!=[])
    def concordance(self, word, width=40):
        key = self._offsetter(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay + ' ' + rdisplay)
    def _offsetter(self, word):
        return nltk.corpus.wordnet.synsets(word.lower())[0].offset

grail = nltk.corpus.webtext.words('grail.txt')
txt = IndexedText(grail)
txt.concordance('animal')
# a talk to you no more , you empty headed animal food trough wiper ! I fart in you
# he entrance to this cave is guarded by a creature so foul , so cruel that no man 
# r ] MAYNARD : It ' s the legendary Black Beast of Aaauugh ! [ Black Beast of Aaau
# gendary Black Beast of Aaauugh ! [ Black Beast of Aaauugh eats BROTHER MAYNARD ] 
# agh ! NARRATOR : As the horrendous Black Beast lunged forward , escape for Arthur

# 43  With the help of a multilingual corpus such as the Universal Declaration of Human Rights Corpus
# (nltk.corpus.udhr), and NLTK's frequency distribution and rank correlation functionality
# (nltk.FreqDist, nltk.spearman_correlation), develop a system that guesses the language
# of a previously unseen text. For simplicity, work with a single character encoding and just a few
# languages.

def detect_lang(text):
    langlist = ['English-Latin1', 'Spanish-Latin1', 'German_Deutsch-Latin1', 'French_Francais-Latin1']
    langfdist = [ nltk.FreqDist(nltk.corpus.udhr.words(lang)) for lang in langlist ]
    fdist=nltk.FreqDist(nltk.word_tokenize(text))
    SC = [ nltk.spearman_correlation(fdist, lfdist) for lfdist in langfdist ]
    return langlist[SC.index(max(SC))], SC

detect_lang(nltk.corpus.udhr.raw('English-Latin1'))
# ('English-Latin1', [0.9999975811329509, 0.668421052631579, 0.9281423804226919, 0.9942533322691356])

my_art=newspaper.article.Article('http://www.theonion.com/article/states-abortion-waiting-period-allows-women-explor-51606')
my_art.download()
my_art.parse()
raw=my_art.text
detect_lang(raw)
# ('English-Latin1', [-5.391138273491214, -1878.8, -2858.25, -1223.4])

my_art=newspaper.article.Article('http://www.elmundo.es/motor/2015/10/19/5624df3b46163fb10a8b45a7.html')
my_art.download()
my_art.parse()
raw=my_art.text
detect_lang(raw)
# ('Spanish-Latin1', [-342.4, -0.041353383458646586, -130.66071428571428, -23.603715170278637])

my_art=newspaper.article.Article('http://www.lefigaro.fr/international/2015/10/19/01003-20151019ARTFIG00206-en-suisse-la-crise-des-refugies-offre-un-score-record-aux-populistes.php')
my_art.download()
my_art.parse()
raw=my_art.text
detect_lang(raw)
# ('French_Francais-Latin1', [-55.04761904761905, -22.535539215686274, -42.35, 0.7608933787731256])

my_art=newspaper.article.Article('http://www.zeit.de/gesellschaft/zeitgeschehen/2015-10/hardheim-fluechtlinge-benimmregeln-willkommenskultur-ehrenamt-integration')
my_art.download()
my_art.parse()
raw=my_art.text
detect_lang(raw)
# ('German_Deutsch-Latin1', [-94.92857142857143, -202.05714285714285, 0.7719218122031422, -158.0857142857143])

# 44 Write a program that processes a text and discovers cases where a word has been used with a novel
# sense. For each word, compute the WordNet similarity between all synsets of the word and all synsets
# of the words in its context. (Note that this is a crude approach; doing it well is a difficult, open
# research problem.)

def context_similarity(wd='election', txt=nltk.corpus.brown.words(), ctx_width=5, width=40):
    pos_lst = [pos for pos, word in enumerate(txt) if word == wd]
    syn_wd = nltk.corpus.wordnet.synsets(wd)
    auxout=[]
    for pos in pos_lst:
        lcontext = txt[max(pos-ctx_width,0):pos]
        rcontext = txt[pos+1:min(pos+ctx_width+1,len(txt))]
        context = lcontext + rcontext
        syn_ctx = [ nltk.corpus.wordnet.synsets(word) for word in context if nltk.corpus.wordnet.synsets(word)!=[] ]
        syn_ctx = [ inner for outer in syn_ctx for inner in outer ]
        dist_pairs = [ (syn1, syn2) for syn1 in syn_wd for syn2 in syn_ctx ]
        distances = [ syn[0].path_similarity(syn[1]) for syn in dist_pairs ]
        distances = [ 0 if val is None else val for val in distances ]
        dist = sum(distances)/len(distances)
        ldisplay = '{:>{width}}'.format(' '.join(lcontext)[-width:], width=width)
        rdisplay = '{:{width}}'.format(' '.join(rcontext)[:width], width=width)
        auxout=auxout + [ ( dist , ldisplay + ' ' + wd + ' ' + rdisplay ) ]
    return auxout

# 45 Read the article on normalization of non-standard words (Sproat et al, 2001), and implement
# a similar system for text normalization.

# Maybe later