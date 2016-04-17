'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# Chapter 5

# 1 Search the web for "spoof newspaper headlines", to find such gems as: British Left Waffles on Falkland Islands, and Juvenile Court to Try Shooting Defendant. Manually tag these headlines to see if knowledge of the part-of-speech tags removes the ambiguity.

# NA

# 2 Working with someone else, take turns to pick a word that can be either a noun or a verb (e.g. contest); the opponent has to predict which one is likely to be the most frequent in the Brown corpus; check the opponent's prediction, and tally the score over several turns.

# NA

# 3 Tokenize and tag the following sentence: They wind back the clock, while we chase after the wind. What different pronunciations and parts of speech are involved?

# NA

# 4 Review the mappings in 3.1. Discuss any other examples of mappings you can think of. What type of information do they map from and to?

# NA

# 5 Using the Python interpreter in interactive mode, experiment with the dictionary examples in this chapter. Create a dictionary d, and add some entries. What happens if you try to access a non-existent entry, e.g. d['xyz']?

def ex05(my_dict={'a':1,'b':2},test_key='xyz'):
    return my_dict[test_key]

# 6 Try deleting an element from a dictionary d, using the syntax del d['abc']. Check that the item was deleted.

def ex06(my_dict={'a':1,'b':2,'c':3},del_key='a'):
    del my_dict[del_key]
    return my_dict

# 7 Create two dictionaries, d1 and d2, and add some entries to each. Now issue the command d1.update(d2). What did this do? What might it be useful for?

def ex07(dict1={'a':1,'b':2,'c':3},dict2={'d':4,'e':5,'f':6,'a':0}):
    dict1.update(dict2)
    return dict1

# 8 Create a dictionary e, to represent a single lexical entry for some word of your choice. Define keys like headword, part-of-speech, sense, and example, and assign them suitable values.

# NA

# 9 Satisfy yourself that there are restrictions on the distribution of go and went, in the sense that they cannot be freely interchanged in the kinds of contexts illustrated in (3d) in 7.

# NA

# 10 Train a unigram tagger and run it on some new text. Observe that some words are not assigned a tag. Why not?

def ex10(train_sents=nltk.corpus.brown.tagged_sents(categories='news',tagset='universal'),
         test_sents=nltk.corpus.brown.sents(categories='romance'),
         count_tag=None):
    my_tagger=nltk.UnigramTagger(train_sents)
    tagged_test_sents=my_tagger.tag_sents(test_sents)
    num_tags=sum(map(lambda s: [v2 for (_, v2) in s].count(count_tag), tagged_test_sents))
    return num_tags

# 11 Learn about the affix tagger (type help(nltk.AffixTagger)). Train an affix tagger and run it on some new text. Experiment with different settings for the affix length and the minimum word length. Discuss your findings.

def ex11(train_sents=nltk.corpus.brown.tagged_sents(categories='news',tagset='universal'),
         evaluate_sents=nltk.corpus.brown.tagged_sents(categories='romance',tagset='universal'),
         affix_len=-3, min_stem_len=3):
    my_tagger=nltk.AffixTagger(train=train_sents, affix_length=affix_len, min_stem_length=min_stem_len)
    return my_tagger.evaluate(evaluate_sents)

def ex11_test(affix_lens=[-1,-2,-3,-4],stem_lens=[1,2,3,4]):
    import itertools
    param_list=itertools.product(affix_lens,stem_lens)
    return [(a_l, s_l, ex11(affix_len=a_l,min_stem_len=s_l)) for (a_l, s_l) in param_list]
    
# 12 Train a bigram tagger with no backoff tagger, and run it on some of the training data. Next, run it on some new data. What happens to the performance of the tagger? Why?

def ex12(train_sents=nltk.corpus.brown.tagged_sents(categories='news',tagset='universal'),
         evaluate_sents=nltk.corpus.brown.tagged_sents(categories='romance',tagset='universal')):
    my_tagger=nltk.BigramTagger(train_sents)
    return my_tagger.evaluate(evaluate_sents)

# 13 We can use a dictionary to specify the values to be substituted into a formatting string. Read Python's library documentation for formatting strings http://docs.python.org/lib/typesseq-strings.html and use this method to display today's date in two different formats.

# Web page not available. If the point is to use a dictionary to contain the formatting strings and give them human
# readable names, then NA

# 14 Use sorted() and set() to get a sorted list of tags used in the Brown corpus, removing duplicates.

def ex14(tokens=nltk.corpus.brown.tagged_words()):
    return sorted(set([v2 for (_, v2) in tokens]))

# 15 Write programs to process the Brown Corpus and find answers to the following questions:

# - Which nouns are more common in their plural form, rather than their singular form? (Only consider regular plurals, formed with the -s suffix.)

def ex15_a(tokens=nltk.corpus.brown.tagged_words()):
    cand_pl=nltk.FreqDist([ v1.lower() for (v1, v2) in tokens if v2=='NNS' and v1.endswith('s') ])
    cand_sg=nltk.FreqDist([ v1.lower() for (v1, v2) in tokens if v2=='NN' ])
    return sorted([ [ cand_pl[key], cand_sg[key[:-1]], key ] for key in cand_pl.keys() if cand_pl[key]>cand_sg[key[:-1]] ], reverse=True)

# - Which word has the greatest number of distinct tags. What are they, and what do they represent?

def ex15_b(tokens=nltk.corpus.brown.tagged_words()):
    tokens=list(set([ (v1.lower(),v2) for (v1,v2) in tokens ]))
    aux_list=nltk.Index(tokens).items()
    return sorted(aux_list, key=lambda entry: len(entry[1]), reverse=True)

# - List tags in order of decreasing frequency. What do the 20 most frequent tags represent?

def ex15_c(tokens=nltk.corpus.brown.tagged_words()):
    tok_tags=[v2 for (_, v2) in tokens]
    return nltk.FreqDist(tok_tags)

# - Which tags are nouns most commonly found after? What do these tags represent?

def ex15_d(tokens=nltk.corpus.brown.tagged_words()):
    tokens=[ v2 for (_, v2) in tokens ]
    tokens=nltk.bigrams(tokens)
    tag_NN=[ v1 for (v1, v2) in tokens if v2.startswith('NN')]
    return nltk.FreqDist(tag_NN)

# 16 Explore the following issues that arise in connection with the lookup tagger:

# - What happens to the tagger performance for the various model sizes when a backoff tagger is omitted?

def ex16_performance(cfd, wordlist, category, tags):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt)
    return baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories=category, tagset=tags))

def ex16_display(category='news',tags=None):
    import pylab
    word_freqs = nltk.FreqDist(nltk.corpus.brown.words(categories=category)).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(nltk.corpus.brown.tagged_words(categories=category, tagset=tags))
    sizes = 4 ** pylab.arange(8)
    perfs = [ex16_performance(cfd, words_by_freq[:size], category, tags) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
    return zip(sizes,perfs)

# (1, 0.05527378324084571)
# (4, 0.1732303041152018)
# (16, 0.3012311792668616)
# (64, 0.42333472562006486)
# (256, 0.5264832826143166)
# (1024, 0.6589991447381507)
# (4096, 0.8073075163593691)
# (16384, 0.9349006503968017)

# - Consider the curve in 4.2; suggest a good size for a lookup tagger that balances memory and performance. Can you come up with scenarios where it would be preferable to minimize memory usage, or to maximize performance with no regard for memory usage?

# NA

# 17 What is the upper limit of performance for a lookup tagger, assuming no limit to the size of its table? (Hint: write a program to work out what percentage of tokens of a word are assigned the most likely tag for that word, on average.)

def ex17(train_tokens=nltk.corpus.brown.tagged_words(categories='news'),
         train_sents=nltk.corpus.brown.tagged_sents(categories='news')):
    cfd = nltk.ConditionalFreqDist(train_tokens)
    my_cfd = [ cfd[entry].values() for entry in cfd.keys() ]
    correct=sum([ max(vals) for vals in my_cfd ])
    total=sum([ sum(vals) for vals in my_cfd ])
    perf1=1.0*correct/total
    my_tagger=nltk.UnigramTagger(train_sents)
    perf2=my_tagger.evaluate(train_sents)
    return [perf1, perf2]

# [0.9349006503968017, 0.9349006503968017]

# 18 Generate some statistics for tagged data to answer the following questions:

# - What proportion of word types are always assigned the same part-of-speech tag?

def ex18_a(tokens=nltk.corpus.brown.tagged_words()):
    cfd = nltk.ConditionalFreqDist(tokens)
    my_cfd = [ cfd[entry].values() for entry in cfd.keys() ]
    single=sum([ len(vals)==1 for vals in my_cfd ])
    total=len(my_cfd)
    return 1.0*single/total

# 0.8442834971546819

# - How many words are ambiguous, in the sense that they appear with at least two tags?

def ex18_b(tokens=nltk.corpus.brown.tagged_words()):
    cfd = nltk.ConditionalFreqDist(tokens)
    my_cfd = [ cfd[entry].values() for entry in cfd.keys() ]
    single=sum([ len(vals)==1 for vals in my_cfd ])
    total=len(my_cfd)
    return [total-single, total]

# [8729, 56057]

# - What percentage of word tokens in the Brown Corpus involve these ambiguous words?

def ex18_c(tokens=nltk.corpus.brown.tagged_words()):
    cfd = nltk.ConditionalFreqDist(tokens)
    my_cfd = [ cfd[entry].values() for entry in cfd.keys() ]
    ambig_num=sum([ sum(vals) for vals in my_cfd if len(vals)>1 ])
    total=len(tokens)
    return 1.0*ambig_num/total

# 0.7864892283102192

# 19 The evaluate() method works out how accurately the tagger performs on this text. For example, if the supplied tagged text was [('the', 'DT'), ('dog', 'NN')] and the tagger produced the output [('the', 'NN'), ('dog', 'NN')], then the score would be 0.5. Let's try to figure out how the evaluation method works:
# - A tagger t takes a list of words as input, and produces a list of tagged words as output. However, t.evaluate() is given correctly tagged text as its only parameter. What must it do with this input before performing the tagging?
# - Once the tagger has created newly tagged text, how might the evaluate() method go about comparing it with the original tagged text and computing the accuracy score?
# - Now examine the source code to see how the method is implemented. Inspect nltk.tag.api.__file__ to discover the location of the source code, and open this file using an editor (be sure to use the api.py file and not the compiled api.pyc binary file).

# NA

# 20 Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the following questions:

# - Produce an alphabetically sorted list of the distinct words tagged as MD.

def ex20_a(tokens=nltk.corpus.brown.tagged_words(), tag='MD'):
    return sorted(set([ v1.lower() for (v1, v2) in tokens if v2==tag ]))

# - Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).

def ex20_b(tokens=nltk.corpus.brown.tagged_words(), tag_lst=['VBZ', 'NNS']):
    tokens=list(set([ (v1.lower(),v2) for (v1,v2) in tokens if v2 in tag_lst]))
    aux_list=nltk.Index(tokens).items()
    return sorted([ elem[0] for elem in aux_list if set(tag_lst)-set(elem[1])==set([]) ])

# - Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).

def ex20_c(tokens=nltk.corpus.brown.tagged_words(), tag_lst=['IN', 'DT', 'NN']):
    tokens=[ (v0.lower(), v1) for (v0, v1) in tokens ]
    tokens=nltk.trigrams(tokens)
    return [ [w0[0], w1[0], w2[0]] for (w0, w1, w2) in tokens if w0[1].startswith(tag_lst[0]) and
                                                                 w1[1].startswith(tag_lst[1]) and
                                                                 w2[1].startswith(tag_lst[2])]

# - What is the ratio of masculine to feminine pronouns?

def ex20_d(tokens=nltk.corpus.brown.tagged_words(),
           tag_lst= ['PP$$','PPL',    'PPO','PPS','PPS+BEZ','PPS+HVZ','PPS+HVD','PPS+MD'],
           masc_lst=['his', 'himself','him','he', 'he\'s',            'he\'d',  'he\'ll'],
           fem_lst=['hers','herself','her','she','she\'s',           'she\'d', 'she\'ll']):
    tokens=[ v0.lower() for (v0, v1) in tokens if v1 in tag_lst and v0 in masc_lst + fem_lst ]
    num_masc=len([ 1 for v in tokens if v in masc_lst ])
    num_fem=len(tokens)-num_masc
    return 1.0*num_masc/num_fem

# 21 In 3.1 we saw a table involving frequency counts for the verbs adore, love, like, prefer and preceding qualifiers absolutely and definitely. Investigate the full range of adverbs that appear before these four verbs.

def ex21(tokens  = nltk.corpus.brown.tagged_words(),
         verb_lst= ['adore','love','like','prefer'],
         tag_lst = ['RB']):
    tokens=[ (v0.lower(), v1) for (v0, v1) in tokens ]
    tokens=nltk.bigrams(tokens)
    tokens=[(w0[0], w1[0]) for (w0, w1) in tokens if w0[1] in tag_lst and w1[0] in verb_lst]
    return nltk.FreqDist(tokens)

def ex21_print(FD=ex21()):
    adv=sorted(set([v[0] for v in FD.keys()]))
    max_len=max([len(ad) for ad in adv])
    vrb=sorted(set([v[1] for v in FD.keys()]))
    print "\t".join([" "*max_len] + vrb)
    for ad in adv:
        row=['{0:<{1}}'.format(ad,max_len)]
        for vr in vrb:
            row=row+[str(FD[(ad,vr)])]
        print "\t".join(row)
    return "Done!"

# 22 We defined the regexp_tagger that can be used as a fall-back tagger for unknown words. This tagger only checks for cardinal numbers. By testing for particular prefix or suffix strings, it should be possible to guess other tags. For example, we could tag any word that ends with -s as a plural noun. Define a regular expression tagger (using RegexpTagger()) that tests for at least five other patterns in the spelling of words. (Use inline documentation to explain the rules.)

def ex22(test_sents=nltk.corpus.brown.tagged_sents(categories='news'),
         new_sent=nltk.word_tokenize("The big brown dog jumped over the 314 lazy foxes.")):
    patterns = [
                (r'.*ing$', 'VBG'),               # gerunds
                (r'.*ed$', 'VBD'),                # simple past
                (r'.*es$', 'VBZ'),                # 3rd singular present
                (r'.*ould$', 'MD'),               # modals
                (r'.*\'s$', 'NN$'),               # possessive nouns
                (r'.*s$', 'NNS'),                 # plural nouns
                (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
                (r'.*', 'NN')                     # nouns (default)
               ]
    regexp_tagger = nltk.RegexpTagger(patterns)
    return regexp_tagger.tag(new_sent)

# 23 Consider the regular expression tagger developed in the exercises in the previous section. Evaluate the tagger using its accuracy() method, and try to come up with ways to improve its performance. Discuss your findings. How does objective evaluation help in the development process?

def ex23(test_sents=nltk.corpus.brown.tagged_sents(categories='news'),
         new_sent=nltk.word_tokenize("The big brown dog jumped over the 314 lazy foxes.")):
    patterns = [
                (r'.*ing$', 'VBG'),               # gerunds
                (r'.*ed$', 'VBD'),                # simple past
                (r'.*es$', 'VBZ'),                # 3rd singular present
                (r'.*ould$', 'MD'),               # modals
                (r'.*\'s$', 'NN$'),               # possessive nouns
                (r'.*s$', 'NNS'),                 # plural nouns
                (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
                (r'.*', 'NN')                     # nouns (default)
               ]
    regexp_tagger = nltk.RegexpTagger(patterns)
    return regexp_tagger.evaluate(test_sents)

# 24 How serious is the sparse data problem? Investigate the performance of n-gram taggers as n increases from 1 to 6. Tabulate the accuracy score. Estimate the training data required for these taggers, assuming a vocabulary size of 105 and a tagset size of 102.

def ex24_perf(train_sents, test_sents, n):
    my_tagger=nltk.NgramTagger(n, train_sents)
    return my_tagger.evaluate(test_sents)

def ex24(all_sents=nltk.corpus.brown.tagged_sents(categories='news'), train_frac=0.8, n_range=range(1,6)):
    train_sents=all_sents[:int(train_frac*len(all_sents))]
    test_sents=all_sents[int(train_frac*len(all_sents)):]
    return [ ex24_perf(train_sents,test_sents,n) for n in n_range ]

# [0.802158100101161, 0.09205645744014644, 0.059010549641119514, 0.05265186184305602, 0.05159208054337878]

# 25 Obtain some tagged data for another language, and train and evaluate a variety of taggers on it. If the language is morphologically complex, or if there are any orthographic clues (e.g. capitalization) to word classes, consider developing a regular expression tagger for it (ordered after the unigram tagger, and before the default tagger). How does the accuracy of your tagger(s) compare with the same taggers run on English data? Discuss any issues you encounter in applying these methods to the language.

def ex25_train(train_sents, n, use_backoffs):
    my_taggers=[ nltk.DefaultTagger(None) ]
    for i in range(n):
        my_tagger=nltk.NgramTagger(i+1,train=train_sents,backoff=my_taggers[i*use_backoffs])
        my_taggers=my_taggers+[my_tagger]
    return my_taggers

def ex25(all_sents=nltk.corpus.cess_esp.tagged_sents(), train_frac=0.8, n=3, use_backoffs=True):
    train_sents=all_sents[:int(train_frac*len(all_sents))]
    test_sents=all_sents[int(train_frac*len(all_sents)):]
    my_taggers=ex25_train(train_sents,n,use_backoffs)
    return [ my_tagger.evaluate(test_sents) for my_tagger in my_taggers ]

# cess_esp corpus
# use_backoffs=True:  [0.0, 0.8146301990613368, 0.8281275287263311,  0.8280627933322544]
# use_backoffs=False: [0.0, 0.8146301990613368, 0.10315585046123968, 0.06486486486486487]

# brown corpus
# use_backoffs=True:  [0.0, 0.8771110352197239, 0.8999647472265982,  0.90029524197724]
# use_backoffs=False: [0.0, 0.8771110352197239, 0.3391757460918996,  0.19181364502660483]

# brown(categories='news') corpus
# use_backoffs=True:  [0.0, 0.802158100101161,  0.8113107567801917,  0.8093838816898694]
# use_backoffs=False: [0.0, 0.802158100101161,  0.09205645744014644, 0.059010549641119514]

# 26 4.1 plotted a curve showing change in the performance of a lookup tagger as the model size was increased. Plot the performance curve for a unigram tagger, as the amount of training data is varied.

def ex26_train(train_sents, num_sents):
    return [ nltk.NgramTagger(1, train=train_sents[:num_sent]) for num_sent in num_sents ]

def ex26_perfs(test_sents, taggers):
    return [ tagger.evaluate(test_sents) for tagger in taggers ]

def ex26_display(sizes, perfs):
    import pylab
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('1-Gram Tagger Performance with Varying Training Size')
    pylab.xlabel('Training Size (sentences)')
    pylab.ylabel('Performance')
    pylab.show()

def ex26(all_sents=nltk.corpus.brown.tagged_sents(), train_frac=0.8, n=5):
    train_sents=all_sents[:int(train_frac*len(all_sents))]
    num_bas=len(train_sents) ** (1.0/n)
    num_sents=[ int(num_bas ** ex) for ex in range(n+1) ]
    my_taggers=ex26_train(train_sents,num_sents)
    test_sents=all_sents[int(train_frac*len(all_sents)):]
    perfs=ex26_perfs(test_sents,my_taggers)
    ex26_display(num_sents,perfs)
    return zip(num_sents,perfs)

# [(1,     0.12119793330615931),
#  (8,     0.3478732662796206),
#  (73,    0.48878521146155796),
#  (626,   0.666145219393432),
#  (5360,  0.8042038932281625),
#  (45872, 0.8771110352197239)]

# 27 Inspect the confusion matrix for the bigram tagger t2 defined in 5, and identify one or more sets of tags to collapse. Define a dictionary to do the mapping, and evaluate the tagger on the simplified data.

def ex27_train(train_sents):
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    return t2

def ex27_post_process(my_tags, my_dict):
    return [ my_dict[my_tag] if my_tag in my_dict.keys() else my_tag for my_tag in my_tags ]

def ex27(my_corpus=nltk.corpus.brown, train_category='news', test_category='editorial',
         my_dict={'NNS':'NN', 'NP':'NN', 'NN-TL':'NN'}):
    my_tagger = ex27_train(my_corpus.tagged_sents(categories=train_category))
    gold_tags_1 = [tag for (_, tag) in my_corpus.tagged_words(categories=test_category)]
    test_tags_1 = [tag for sent in my_corpus.sents(categories=test_category)
                       for (_, tag) in my_tagger.tag(sent)]
    conf_mat_1 = nltk.ConfusionMatrix(gold_tags_1, test_tags_1)
    gold_tags_2 = ex27_post_process(gold_tags_1, my_dict)
    test_tags_2 = ex27_post_process(test_tags_1, my_dict)
    conf_mat_2 = nltk.ConfusionMatrix(gold_tags_2, test_tags_2)    
    return [[1.0*conf_mat_1._correct/conf_mat_1._total, 1.0*conf_mat_2._correct/conf_mat_2._total],
            [conf_mat_1, conf_mat_2]]

# [[0.8499772742029739, 0.8776540484384131], [<ConfusionMatrix: 52362/61604 correct>, <ConfusionMatrix: 54067/61604 correct>]]

# 28 Experiment with taggers using the simplified tagset (or make one of your own by discarding all but the first character of each tag name). Such a tagger has fewer distinctions to make, but much less information on which to base its work. Discuss your findings.

# ex26(all_sents=nltk.corpus.brown.tagged_sents(categories='news',tagset='universal'), train_frac=0.8, n=5)
# [(1,    0.09933041090611301),
#  (5,    0.3339274531528494),
#  (26,   0.4367744110988005),
#  (138,  0.5758947926200684),
#  (715,  0.7126065802784335),
#  (3698, 0.8348668047593815)]

# ex26(all_sents=nltk.corpus.brown.tagged_sents(categories='news'), train_frac=0.8, n=5)
# [(1,    0.09721084830675851),
#  (5,    0.32891757791801146),
#  (26,   0.4298858326508984),
#  (138,  0.5583120574208776),
#  (715,  0.6866419384363409),
#  (3698, 0.802158100101161)]

# ex16_display(category='news',tags='universal')
# [(1,     0.05549257115579689),
#  (4,     0.17549774250651393),
#  (16,    0.30492073910535633),
#  (64,    0.4297392445849991),
#  (256,   0.5388746345247329),
#  (1024,  0.6800922887204885),
#  (4096,  0.8367444358255266),
#  (16384, 0.9666746225908467)]

# ex16_display(category='news',tags=None)
# [(1,     0.05527378324084571)
#  (4,     0.1732303041152018)
#  (16,    0.3012311792668616)
#  (64,    0.42333472562006486)
#  (256,   0.5264832826143166)
#  (1024,  0.6589991447381507)
#  (4096,  0.8073075163593691)
#  (16384, 0.9349006503968017)

# 29 Recall the example of a bigram tagger which encountered a word it hadn't seen during training, and tagged the rest of the sentence as None. It is possible for a bigram tagger to fail part way through a sentence even if it contains no unseen words (even if the sentence was used during training). In what circumstance can this happen? Can you write a program to find some examples of this?

def ex29_count_none_tag(sent):
    return sum([ 1 for (_, v1) in sent if v1==None ])

def ex29(target_corpus=nltk.corpus.brown, category='news'):
    all_tagged_sents=target_corpus.tagged_sents(categories=category)
    my_tagger=nltk.BigramTagger(all_tagged_sents)
    all_sents=target_corpus.sents(categories=category)
    my_tagged_sents=my_tagger.tag_sents(all_sents)
    return [ (all_tagged_sents[i], my_tagged_sents[i])
             for i in range(len(all_sents))
             if ex29_count_none_tag(all_tagged_sents[i]) < ex29_count_none_tag(my_tagged_sents[i]) ]

# 30 Preprocess the Brown News data by replacing low frequency words with UNK, but leaving the tags untouched. Now train and evaluate a bigram tagger on this data. How much does this help? What is the contribution of the unigram tagger and default tagger now?

def ex30_pre_process(sents,remove_list):
    aux_sents=[]
    for sent in sents:
        aux_sents=aux_sents + [ [('UNK' if word[0] in remove_list else word[0], word[1]) for word in sent] ]
    return aux_sents

def ex30_create_remove_lists(FD,n_range):
    return [ [ v0 for (v0, _) in FD.most_common() ][-n:] if n > 0 else [] for n in n_range ]
    
def ex30_train(train_sents, use_backoffs):
    if use_backoffs:
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
    else:
        t2 = nltk.BigramTagger(train_sents)
    return t2

def ex30_perf(sents, tagger):
    return tagger.evaluate(sents)
 
def ex30_display(sizes, perfs):
    import pylab
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('2-Gram Tagger Performance with Varying Removal Size')
    pylab.xlabel('Removal Size (words)')
    pylab.ylabel('Performance')
    pylab.show()

def ex30_display_results(results=[(0, 0),
                                  (1, 1)]):
    num_words=[v0 for (v0, _) in results]
    perfs    =[v1 for (_, v1) in results]
    ex30_display(num_words,perfs)

def ex30(target_corpus=nltk.corpus.brown, category='news',
         train_frac=0.8, use_backoffs=True,
         removal_frac=[0, 0.2, 0.4, 0.45, 0.5, 0.525, 0.55, 0.6, 0.8]):
    all_sents=target_corpus.tagged_sents(categories=category)
    train_sents_orig=all_sents[:int(train_frac*len(all_sents))]
    test_sents_orig =all_sents[int(train_frac*len(all_sents)):]
    FD=nltk.FreqDist(target_corpus.words(categories=category))
    num_words=[ int(len(FD)*frac) for frac in removal_frac ]
    remove_lists=ex30_create_remove_lists(FD, num_words)
    train_sents=[ ex30_pre_process(train_sents_orig, remove_lists[num]) for num in range(len(removal_frac))  ]
    my_taggers =[ ex30_train(train_sent_list, use_backoffs) for train_sent_list in train_sents ]
    test_sents =[ ex30_pre_process(test_sents_orig,  remove_lists[num]) for num in range(len(removal_frac))  ]
    perfs      =[ ex30_perf(test_sent_list, tagger) for (test_sent_list, tagger) in  zip(test_sents,my_taggers)]
    ex30_display(num_words,perfs)
    return zip(num_words,perfs)

# ex30(use_backoffs=True, removal_frac=[0, 0.2, 0.4, 0.45, 0.5, 0.525, 0.55, 0.6, 0.8])
# [(0,     0.835300351654704),
#  (2878,  0.8381906642901874),
#  (5757,  0.8401175393805097),
#  (6477,  0.8408882894166385),
#  (7197,  0.8406474300303483),
#  (7556,  0.8409846331711547),
#  (7916,  0.8399248518714775),
#  (8636,  0.8360711016908329),
#  (11515, 0.8135748350113204)]

# ex30_display_results_1(results=[(0,     0.835300351654704),
#                                 (2878,  0.8381906642901874),
#                                 (5757,  0.8401175393805097),
#                                 (6477,  0.8408882894166385),
#                                 (7197,  0.8406474300303483),
#                                 (7556,  0.8409846331711547),
#                                 (7916,  0.8399248518714775),
#                                 (8636,  0.8360711016908329),
#                                 (11515, 0.8135748350113204)])

# ex30(use_backoffs=False, removal_frac=[0, 0.2, 0.4, 0.45, 0.5, 0.525, 0.55, 0.6, 0.8,
#                                        0.85,0.9,0.95,
#                                        0.96,0.97,0.98,0.99,
#                                        0.992,0.994,0.996,0.998,
#                                        1])

# [(0,     0.09205645744014644),
#  (2878,  0.09976395780143552),
#  (5757,  0.10819403632159545),
#  (6477,  0.11055445830724023),
#  (7197,  0.11378197408353004),
#  (7556,  0.11570884917385231),
#  (7916,  0.11787658365046486),
#  (8636,  0.12476516209836698),
#  (11515, 0.1581482730382003),
#  (12234, 0.17549014885110073),
#  (12954, 0.21157088491738524),
#  (13674, 0.2728455127896334),
#  (13818, 0.287778794739631),
#  (13962, 0.33281949997591403),
#  (14106, 0.386242111855099),
#  (14250, 0.42015511344477097),
#  (14278, 0.4344621609904138),
#  (14307, 0.4478057709908955),
#  (14336, 0.4400500987523484),
#  (14365, 0.41167686304735296),
#  (14394, 0.11065080206175634)]

# ex30_display_results(results=[(0,     0.09205645744014644),
#                               (2878,  0.09976395780143552),
#                               (5757,  0.10819403632159545),
#                               (6477,  0.11055445830724023),
#                               (7197,  0.11378197408353004),
#                               (7556,  0.11570884917385231),
#                               (7916,  0.11787658365046486),
#                               (8636,  0.12476516209836698),
#                               (11515, 0.1581482730382003),
#                               (12234, 0.17549014885110073),
#                               (12954, 0.21157088491738524),
#                               (13674, 0.2728455127896334),
#                               (13818, 0.287778794739631),
#                               (13962, 0.33281949997591403),
#                               (14106, 0.386242111855099),
#                               (14250, 0.42015511344477097),
#                               (14278, 0.4344621609904138),
#                               (14307, 0.4478057709908955),
#                               (14336, 0.4400500987523484),
#                               (14365, 0.41167686304735296),
#                               (14394, 0.11065080206175634)])

# 31 Modify the program in 4.1 to use a logarithmic scale on the x-axis, by replacing pylab.plot() with pylab.semilogx(). What do you notice about the shape of the resulting plot? Does the gradient tell you anything?

def ex31_performance(cfd, wordlist, category, tags):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt)
    return baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories=category, tagset=tags))

def ex31_display(category='news',tags=None):
    import pylab
    word_freqs = nltk.FreqDist(nltk.corpus.brown.words(categories=category)).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(nltk.corpus.brown.tagged_words(categories=category, tagset=tags))
    sizes = 4 ** pylab.arange(8)
    perfs = [ex31_performance(cfd, words_by_freq[:size], category, tags) for size in sizes]
    pylab.semilogx(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
    return zip(sizes,perfs)

# The result is a straight line. The slope is the factor F of the relationship:
# model_size = Const1 ^ ( F * model_performance )

# 32 Consult the documentation for the Brill tagger demo function, using help(nltk.tag.brill.demo). Experiment with the tagger by setting different values for the parameters. Is there any trade-off between training time (corpus size) and performance?

def ex32_train_base_tagger(train_sents):
    import time
    start_time=time.time()
    tagger=nltk.UnigramTagger(train_sents)
    train_time=time.time()-start_time
    return tagger, train_time

def ex32_setup_brill_trainer(base_tagger, brill_templates=nltk.tag.brill.nltkdemo18()):
    return nltk.tag.BrillTaggerTrainer(base_tagger, brill_templates)

def ex32_train_brill_tagger(brill_trainer, train_sents, max_rule):
    import time
    start_time=time.time()
    tagger=brill_trainer.train(train_sents,max_rules=max_rule)
    train_time=time.time()-start_time
    return tagger, train_time
    
def ex32_perf(tagger,test_sents):
    return tagger.evaluate(test_sents)

def ex32_display_results(results=[[0.5,   0, 0.5, 0.766],
                                  [0.05, 25,   4, 0.819],
                                  [0.05, 50,   5, 0.822],
                                  [0.1,  25,   9, 0.824],
                                  [0.1,  50,  11, 0.829]]):
    import pylab
    results=results[1:]
    frac_set=sorted(set([res[0] for res in results ]))
    frac_x=[ [ res[2] for res in results if res[0]==frac_i ] for frac_i in frac_set ]
    frac_y=[ [ res[3] for res in results if res[0]==frac_i ] for frac_i in frac_set ]
    rule_set=sorted(set([res[1] for res in results ]))
    rule_x=[ [ res[2] for res in results if res[1]==rule_i ] for rule_i in rule_set ]
    rule_y=[ [ res[3] for res in results if res[1]==rule_i ] for rule_i in rule_set ]
    for frac in range(len(frac_set)):
        pylab.plot(frac_x[frac],frac_y[frac],'-bo')
        pylab.annotate(str(frac_set[frac]), xy=(frac_x[frac][-1],frac_y[frac][-1]))
    for rule in range(len(rule_set)):
        pylab.plot(rule_x[rule],rule_y[rule],'-ro')
        pylab.annotate(str(rule_set[rule]), xy=(rule_x[rule][-1],rule_y[rule][-1]))
    pylab.title('Brill Tagger Performance vs Train Time with Varying Model Size')
    pylab.xlabel('Train Time')
    pylab.ylabel('Performance')
    pylab.show()

def ex32(all_sents=nltk.corpus.brown.tagged_sents(categories='news'),
         base_train_frac=0.5,
         brill_train_fracs=[0.05,0.1,0.15,0.2,0.25,0.3],
         test_frac=0.2,
         max_rules=[25,50,75,100,125,150]):
    end_base_train=int(base_train_frac*len(all_sents))
    base_train_sents=all_sents[:end_base_train]
    test_sents=all_sents[int(base_train_frac*len(all_sents)):]
    base_tagger, train_time=ex32_train_base_tagger(base_train_sents)
    brill_trainer=ex32_setup_brill_trainer(base_tagger)
    aux_out=[[base_train_frac, 0, train_time, ex32_perf(base_tagger,test_sents)]]
    case_list=[ (btf, mr) for btf in brill_train_fracs for mr in max_rules ]
    for case in case_list:
        train_frac=case[0]
        max_rule=case[1]
        brill_train_sents=all_sents[end_base_train:end_base_train+int(train_frac*len(all_sents))]
        brill_tagger, train_time=ex32_train_brill_tagger(brill_trainer, brill_train_sents, max_rule)
        aux_out=aux_out+[[train_frac, max_rule, train_time, ex32_perf(brill_tagger,test_sents)]]
    return aux_out

# [[0.5, 0, 0.30856895446777344, 0.7661015614231989],
#  [0.05, 25, 4.115216970443726, 0.8193829129501644],
#  [0.05, 50, 4.699591875076294, 0.8222576643629276],
#  [0.05, 75, 4.7758049964904785, 0.8241085317108708],
#  [0.05, 100, 5.357706069946289, 0.8241479118672101],
#  [0.05, 125, 5.853008985519409, 0.8256246677299309],
#  [0.05, 150, 5.713151931762695, 0.8256246677299309],
#  [0.1, 25, 9.328532934188843, 0.8240297713981924],
#  [0.1, 50, 11.05479097366333, 0.8293460925039873],
#  [0.1, 75, 11.974913120269775, 0.831984562978715],
#  [0.1, 100, 13.12317180633545, 0.8344261326717467],
#  [0.1, 125, 13.739800930023193, 0.8351743556421919],
#  [0.1, 150, 14.738219022750854, 0.836178549628842],
#  [0.15, 25, 15.179649829864502, 0.8260775395278319],
#  [0.15, 50, 17.41165590286255, 0.8314332407899659],
#  [0.15, 75, 19.497020959854126, 0.8339535707956761],
#  [0.15, 100, 21.928075075149536, 0.8361982397070117],
#  [0.15, 125, 24.598634958267212, 0.8379112765077678],
#  [0.15, 150, 26.377384901046753, 0.8398015240120503],
#  [0.2, 25, 24.429016828536987, 0.8235375194439521],
#  [0.2, 50, 32.35071778297424, 0.8289522909405951],
#  [0.2, 75, 36.21369409561157, 0.8320042530568846],
#  [0.2, 100, 41.75600504875183, 0.8340520211865241],
#  [0.2, 125, 44.75836420059204, 0.836434520645047],
#  [0.2, 150, 49.36854290962219, 0.8383444582274991],
#  [0.25, 25, 29.66509699821472, 0.8280268572666234],
#  [0.25, 50, 35.44471502304077, 0.8339338807175064],
#  [0.25, 75, 41.1855788230896, 0.8382066276803118],
#  [0.25, 100, 47.721441984176636, 0.8406678874515132],
#  [0.25, 125, 53.76896095275879, 0.8431685273790537],
#  [0.25, 150, 59.43853712081909, 0.844724043554453],
#  [0.3, 25, 35.96728205680847, 0.8281646878138106],
#  [0.3, 50, 44.910569190979004, 0.835016835016835],
#  [0.3, 75, 51.840336084365845, 0.8393880323704885],
#  [0.3, 100, 61.368995904922485, 0.8423021639395908],
#  [0.3, 125, 70.89899802207947, 0.8448815641798098],
#  [0.3, 150, 81.22834801673889, 0.8471262330911453]]

# ex32_display_results(results=res)
# ex32_display_results(results=[ r for r in res if r[0]<>0.2 ])

# 33 Write code that builds a dictionary of dictionaries of sets. Use it to store the set of POS tags that can follow a given word having a given POS tag, i.e. wordi → tagi → tagi+1.

def ex33(all_sents=nltk.corpus.brown.tagged_sents(categories='news')):
    import collections
    my_dict=collections.defaultdict(lambda : collections.defaultdict(list))
    for sent in all_sents:
        for i in range(len(sent)-1):
            if sent[i+1][1] not in my_dict[sent[i][0]][sent[i][1]]: 
                my_dict[sent[i][0]][sent[i][1]]=my_dict[sent[i][0]][sent[i][1]] + [ sent[i+1][1] ]
    return my_dict

# 34 There are 264 distinct words in the Brown Corpus having exactly three possible tags.

# - Print a table with the integers 1..10 in one column, and the number of distinct words in the corpus having 1..10 distinct tags in the other column.

def ex34_a(all_words=nltk.corpus.brown.tagged_words(),num_cnt=10):
    my_index=nltk.Index(set(all_words))
    FD=nltk.FreqDist([ len(wrd[1]) for wrd in my_index.items()])
    return [ [i+1, FD[i+1]] for i in range(num_cnt) ]

# - For the word with the greatest number of distinct tags, print out sentences from the corpus containing the word, one for each possible tag.

def ex34_b(target_corpus=nltk.corpus.brown,num_cnt=12):
    my_index=nltk.Index(set(target_corpus.tagged_words()))
    my_index=nltk.Index([ (len(wrd[1]),wrd[0]) for wrd in my_index.items() ])
    wrd=my_index[num_cnt]
    nltk.Text(target_corpus.words()).concordance(wrd[0])
    return wrd

# 35 Write a program to classify contexts involving the word must according to the tag of the following word. Can this be used to discriminate between the epistemic and deontic uses of must?

def ex35_process(sent, my_dict):
    return ' '.join([ wrd if wrd<>'must' else wrd+' ['+my_dict[tag[:2]]+']' for ((wrd,_),(_,tag)) in nltk.bigrams(sent)] )

def ex35(all_sents=nltk.corpus.brown.tagged_sents(),
         my_dict={'BE':'Epistemic','HV':'Epistemic','RB':'Epistemic','VB':'Deontic'}):
    import collections
    my_dict=collections.defaultdict(str,my_dict)
    must_sents=[sent for sent in all_sents if 'must' in [ wrd for (wrd,_) in sent ] ]
    return [ ex35_process(sent, my_dict) for sent in must_sents ]

# 36 Create a regular expression tagger and various unigram and n-gram taggers, incorporating backoff, and train them on part of the Brown corpus.
# - Create three different combinations of the taggers. Test the accuracy of each combined tagger. Which combination works best?
# - Try varying the size of the training corpus. How does it affect your results?

def ex36_train(train_sents,regex_rules):
    return [ [nltk.BigramTagger(train_set,backoff=nltk.UnigramTagger(train_set,backoff=nltk.DefaultTagger('NN'))),
              nltk.BigramTagger(train_set,backoff=nltk.UnigramTagger(train_set,backoff=nltk.RegexpTagger(regex_rules)))]
             for train_set in train_sents ]

def ex36_perf(test_sents,taggers):
    return [ [ tagger[0].evaluate(test_sents), tagger[1].evaluate(test_sents) ] for tagger in taggers ]
    
def ex36(all_sents=nltk.corpus.brown.tagged_sents(), train_fracs=[0.2,0.4,0.6,0.8], test_frac=0.05,
         regex_rules=[(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
                      (r'(The|the|A|a|An|an)$', 'AT'),   # articles
                      (r'.*able$', 'JJ'),                # adjectives
                      (r'.*ness$', 'NN'),                # nouns formed from adjectives  
                      (r'.*ly$', 'RB'),                  # adverbs
                      (r'.*s$', 'NNS'),                  # plural nouns  
                      (r'.*ing$', 'VBG'),                # gerunds   
                      (r'.*ed$', 'VBD'),                 # past tense verbs
                      (r'.*', 'NN')                      # nouns (default)
                     ]):
    num_sents=len(all_sents)
    train_sents=[ all_sents[:int(num_sents*frac)] for frac in train_fracs ]
    my_taggers=ex36_train(train_sents,regex_rules)
    test_sents=all_sents[-int(num_sents*test_frac):]
    perfs=ex36_perf(test_sents,my_taggers)
    return [ [ train_fracs[i], perfs[i][0], perfs[i][1] ] for i in range(len(train_fracs)) ]

# [[0.2, 0.8769840459215983, 0.8922435805772884],
#  [0.4, 0.8946132004167262, 0.9043163851040794],
#  [0.6, 0.900312544685719, 0.9082180867362573],
#  [0.8, 0.908401936551386, 0.9139174310052499]]

# 37 Our approach for tagging an unknown word has been to consider the letters of the word (using RegexpTagger()), or to ignore the word altogether and tag it as a noun (using nltk.DefaultTagger()). These methods will not do well for texts having new words that are not nouns. Consider the sentence I like to blog on Kim's blog. If blog is a new word, then looking at the previous tag (TO versus NP$) would probably be helpful. I.e. we need a default tagger that is sensitive to the preceding tag.
# - Create a new kind of unigram tagger that looks at the tag of the previous word, and ignores the current word. (The best way to do this is to modify the source code for UnigramTagger(), which presumes knowledge of object-oriented programming in Python.)
# - Add this tagger to the sequence of backoff taggers (including ordinary trigram and bigram taggers that look at words), right before the usual default tagger.
# - Evaluate the contribution of this new unigram tagger.

def ex37_train(train_sents):
    class MyUnigramTagger(nltk.UnigramTagger):
        @classmethod
        def context(self, tokens, index, history):
            return '<START>' if index==0 else history[index-1]
    t0=nltk.DefaultTagger('NN')
    t1_1=MyUnigramTagger(train_sents,    backoff=t0)
    t1_2=nltk.UnigramTagger(train_sents, backoff=t0)
    t1_3=nltk.UnigramTagger(train_sents, backoff=t1_1)
    t2_0=nltk.BigramTagger(train_sents,  backoff=t0)
    t2_1=nltk.BigramTagger(train_sents,  backoff=t1_1)
    t2_2=nltk.BigramTagger(train_sents,  backoff=t1_2)
    t2_3=nltk.BigramTagger(train_sents,  backoff=t1_3)
    return [ t2_0, t2_1, t2_2, t2_3 ]

def ex37_perf(test_sents,taggers):
    return [ tagger.evaluate(test_sents) for tagger in taggers ]

def ex37(all_sents=nltk.corpus.brown.tagged_sents(categories='news'), train_frac=0.8, test_frac=0.2):
    train_sents=all_sents[:int(train_frac*len(all_sents))]
    taggers=ex37_train(train_sents)
    test_sents=all_sents[int(train_frac*len(all_sents)):]
    perfs=ex37_perf(test_sents, taggers)
    return perfs

# train_sent=[ [ (u'The', u'AT'),(u'Fulton', u'NP'),(u'County', u'NN'),(u'Grand', u'JJ'),(u'Jury', u'NN'),
#                (u'said', u'VBD'),(u'Friday', u'NR'),(u'an', u'AT'),(u'investigation', u'NN'),(u'of', u'IN'),
#                (u"Atlanta's", u'NP$'),(u'recent', u'JJ'),(u'primary', u'NN'),(u'election', u'NN'),
#                (u'produced', u'VBD'),(u'no', u'AT'),(u'evidence', u'NN'),(u'that', u'CS'),
#                (u'any', u'DTI'),(u'irregularities', u'NNS'),(u'took', u'VBD'),(u'place', u'NN'),(u'.', u'.') ] ]
# test_sent1=[u'The', u'Fulton', u'County', u'Grand', u'Jury',
#             u'said', 'Friday', u'.']
# test_sent2=[u'The', u'BAZINGA', u'County', u'Grand', u'Jury',
#             u'said', 'Friday', u'.']
# class MyUnigramTagger(nltk.UnigramTagger):
#     @classmethod
#     def context(self, tokens, index, history):
#         return '<START>' if index==0 else history[index-1]
# tg=nltk.BigramTagger(train_sent, backoff=MyUnigramTagger(train_sent,backoff=nltk.DefaultTagger('NN')))
# ts1=tg.tag(test_sent1)
# ts2=tg.tag(test_sent2)

# t0=nltk.DefaultTagger('NN')
# t1_1=MyUnigramTagger(train_sents,    backoff=t0)
# t1_2=nltk.UnigramTagger(train_sents, backoff=t0)
# t1_3=nltk.UnigramTagger(train_sents, backoff=t1_1)
# t2_0=nltk.BigramTagger(train_sents,  backoff=t0)
# t2_1=nltk.BigramTagger(train_sents,  backoff=t1_1)
# t2_2=nltk.BigramTagger(train_sents,  backoff=t1_2)
# t2_3=nltk.BigramTagger(train_sents,  backoff=t1_3)
# s=['The', 'actor', 'wants', 'to', 'blog', 'in', 'his', 'blog']
# t0.tag(s)
# [('The', 'NN'), ('actor', 'NN'), ('wants', 'NN'), ('to', 'NN'), ('blog', 'NN'), ('in', 'NN'), ('his', 'NN'), ('blog', 'NN')]
# t1_1.tag(s)
# [('The', u'AT'), ('actor', u'NN'), ('wants', u'IN'), ('to', u'AT'), ('blog', u'NN'), ('in', u'IN'), ('his', u'AT'), ('blog', u'NN')]
# t1_2.tag(s)
# [('The', u'AT'), ('actor', 'NN'), ('wants', u'VBZ'), ('to', u'TO'), ('blog', 'NN'), ('in', u'IN'), ('his', u'PP$'), ('blog', 'NN')]
# t1_3.tag(s)
# [('The', u'AT'), ('actor', u'NN'), ('wants', u'VBZ'), ('to', u'TO'), ('blog', u'VB'), ('in', u'IN'), ('his', u'PP$'), ('blog', u'NN')]
# t2_1.tag(s)
# [('The', u'AT'), ('actor', u'NN'), ('wants', u'IN'), ('to', u'IN'), ('blog', u'AT'), ('in', u'NN'), ('his', u'PP$'), ('blog', u'NN')]
# t2_2.tag(s)
# [('The', u'AT'), ('actor', 'NN'), ('wants', u'VBZ'), ('to', u'TO'), ('blog', 'NN'), ('in', u'IN'), ('his', u'PP$'), ('blog', 'NN')]
# t2_3.tag(s)
# [('The', u'AT'), ('actor', u'NN'), ('wants', u'VBZ'), ('to', u'TO'), ('blog', u'VB'), ('in', u'IN'), ('his', u'PP$'), ('blog', u'NN')]

# 38 Consider the code in 5 which determines the upper bound for accuracy of a trigram tagger. Review Abney's discussion concerning the impossibility of exact tagging (Church, Young, & Bloothooft, 1996). Explain why correct tagging of these examples requires access to other kinds of information than just words and tags. How might you estimate the scale of this problem?

# NA

# 39 Use some of the estimation techniques in nltk.probability, such as Lidstone or Laplace estimation, to develop a statistical tagger that does a better job than n-gram backoff taggers in cases where contexts encountered during testing were not seen during training.

# Maybe later

# 40 Inspect the diagnostic files created by the Brill tagger rules.out and errors.out. Obtain the demonstration code by accessing the source code (at http://www.nltk.org/code) and create your own version of the Brill tagger. Delete some of the rule templates, based on what you learned from inspecting rules.out. Add some new rule templates which employ contexts that might help to correct the errors you saw in errors.out.

# Maybe later

# 41 Develop an n-gram backoff tagger that permits "anti-n-grams" such as ["the", "the"] to be specified when a tagger is initialized. An anti-ngram is assigned a count of zero and is used to prevent backoff for this n-gram (e.g. to avoid estimating P(the | the) as just P(the)).

# Maybe later

# 42 Investigate three different ways to define the split between training and testing data when developing a tagger using the Brown Corpus: genre (category), source (fileid), and sentence. Compare their relative performance and discuss which method is the most legitimate. (You might use n-fold cross validation, discussed in 3, to improve the accuracy of the evaluations.)

# Maybe later

# 43 Develop your own NgramTagger class that inherits from NLTK's class, and which encapsulates the method of collapsing the vocabulary of the tagged training and testing data that was described in this chapter. Make sure that the unigram and default backoff taggers have access to the full vocabulary.

# Maybe later