'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# 1 The IOB format categorizes tagged tokens as I, O and B. Why are three tags necessary?
# What problem would be caused if we used I and O tags exclusively?

# NA

# 2 Write a tag pattern to match noun phrases containing plural head nouns, e.g.
# "many/JJ researchers/NNS", "two/CD weeks/NNS", "both/DT new/JJ positions/NNS".
# Try to do this by generalizing the tag pattern that handled singular noun phrases.

def ex02(grammar=r"""NP: {<DT|PP\$|CD>?<JJ>*<NNS>}""",
         sent=[("many", "JJ"), ("researchers", "NNS"), ("waited", "VB"), ("two", "CD"), ("weeks","NNS"), ("for", "IN"), ("both", "DT"), ("new","JJ"), ("positions", "NNS")]):
    chunker = nltk.RegexpParser(grammar)
    return chunker.parse(sent)

# print(ex02())
# (S
#   (NP many/JJ researchers/NNS)
#   waited/VB
#   (NP two/CD weeks/NNS)
#   for/IN
#   (NP both/DT new/JJ positions/NNS))

# 3 Pick one of the three chunk types in the CoNLL corpus. Inspect the CoNLL corpus
# and try to observe any patterns in the POS tag sequences that make up this kind of chunk.
# Develop a simple chunker using the regular expression chunker nltk.RegexpParser.
# Discuss any tag sequences that are difficult to chunk reliably.

def ex03_print_all(chunk_type='PP'):
    sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])[:50]
    for i, sent in enumerate(sents):
        for clause in sent:
            try:
                clause.label()
            except AttributeError:
                pass
            else:
                if clause.label()==chunk_type:
                    print('{} - {}'.format(i,clause))

def ex03(grammar=r"""PP: {<IN>}
                         {<TO>(?!<VB.>)}""",
        chunk_type='PP'):
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(grammar)
    return chunker, chunker.evaluate(test_sents)

# ch, ev=ex03(grammar=r"""PP:{<IN>}""",
#             chunk_type='PP')
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  96.7%
#     Precision:     81.8%
#     Recall:        86.3%
#     F-Measure:     84.0%
# map(len,[ev.guessed(),ev.missed(),ev.correct(),ev.incorrect()])
# [5071, 661, 4811, 921]

# ch, ev=ex03(grammar=r"""PP:{<IN>}
#                            {<TO>(?!<VB*>)}""",
#             chunk_type='PP')
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  97.7%
#     Precision:     82.8%
#     Recall:        96.7%
#     F-Measure:     89.2%
# map(len,[ev.guessed(),ev.missed(),ev.correct(),ev.incorrect()])
# [5616, 160, 4811, 965]

# tagged_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=['PP'])[:50]
# untagged_sents=[ tagged_sent.leaves() for tagged_sent in tagged_sents ]
# re_tagged_sents=[ ch.parse(sent) for sent in untagged_sents ]
# error_lst=[ [i, tagged, re_tagged] for (i, (tagged, re_tagged))
#              in enumerate(zip(tagged_sents, re_tagged_sents))
#              if tagged!=re_tagged ]

# ex03_print_all(chunk_type='VP'):

# ch, ev=ex03(grammar=r"""VP: {<[MVTR].*>+}""",
#             chunk_type='VP')
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  94.3%
#     Precision:     64.2%
#     Recall:        80.4%
#     F-Measure:     71.4%
# map(len,[ev.guessed(),ev.missed(),ev.correct(),ev.incorrect()])
# [5836, 911, 4658, 2089]

# ch, ev=ex03(grammar=r"""VP: {<[MVTR].*>*<[MV].*>}""",
#             chunk_type='VP')
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  97.3%
#     Precision:     83.5%
#     Recall:        88.6%
#     F-Measure:     85.9%
# map(len,[ev.guessed(),ev.missed(),ev.correct(),ev.incorrect()])
# [4943, 532, 4658, 817]

# tagged_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=['VP'])[:50]
# untagged_sents=[ tagged_sent.leaves() for tagged_sent in tagged_sents ]
# re_tagged_sents=[ ch.parse(sent) for sent in untagged_sents ]
# error_lst=[ [i, tagged, re_tagged] for (i, (tagged, re_tagged))
#              in enumerate(zip(tagged_sents, re_tagged_sents))
#              if tagged!=re_tagged ]

# 4 An early definition of chunk was the material that occurs between chinks.
# Develop a chunker that starts by putting the whole sentence in a single chunk,
# and then does the rest of its work solely by chinking.
# Determine which tags (or tag sequences) are most likely to make up chinks
# with the help of your own utility program. Compare the performance and simplicity of this approach
# relative to a chunker based entirely on chunk rules.

def ex04(grammar=r"""NP: {<.*>+}
                         }<.>{
                         }<IN>{
                         }<TO>(?!<VB.>){
                         }<[MVTR].*>*<[MV].*>{""",
        chunk_type='NP'):
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(grammar)
    return chunker, chunker.evaluate(test_sents)

# ch, ev=ex04(grammar=r"""NP: {<.*>+}
#                             }<.>{
#                             }<IN>{
#                             }<TO>(?!<VB.>){
#                             }<[MVTR].*>*<[MV].*>{""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  85.2%
#     Precision:     64.7%
#     Recall:        64.9%
#     F-Measure:     64.8%

# 5 Write a tag pattern to cover noun phrases that contain gerunds,
# e.g. "the/DT receiving/VBG end/NN", "assistant/NN managing/VBG editor/NN".
# Add these patterns to the grammar, one per line.
# Test your work using some tagged sentences of your own devising.

def ex05(grammar=r"""NP: {<DT|PP\$|CD>?<NN.*|JJ|VBG>*<NN.*>}""",
         sent=[("on", "IN"), ("the", "DT"), ("receiving", "VBG"), ("end", "NN"), ("we", "PPSS"), ("saw","VB"), ("the", "DT"), ("assistant", "NN"), ("managing","VBG"), ("director", "NN")]):
    chunker = nltk.RegexpParser(grammar)
    return chunker.parse(sent)

# print(ex05())
# (S
#   on/IN
#   (NP the/DT receiving/VBG end/NN)
#   we/PP
#   saw/VB
#   (NP the/DT assistant/NN managing/VBG director/NN))

# 6 Write one or more tag patterns to handle coordinated noun phrases,
# e.g. "July/NNP and/CC August/NNP", "all/DT your/PRP$ managers/NNS and/CC supervisors/NNS",
# "company/NN courts/NNS and/CC adjudicators/NNS".

def ex06(grammar=r"""NP: {<DT|PP\$|CD>?<NN.*|JJ|VBG>*<NN.*>}
                     CNP:{<NP><CC><NP>}""",
         sent=[("In", "IN"), ("July", "NNP"), ("and","CC"), ("August","NNP"), ("all","DT"), ("your","PRP$"), ("managers","NNS"), ("and","CC"), ("supervisors","NNS"), ("will", "VB"), ("eat", "VB"), ("the", "DT"), ("company", "NN"), ("courts","NNS"), ("and","CC"), ("adjudicators","NNS")]):
    chunker = nltk.RegexpParser(grammar)
    return chunker.parse(sent)

# print(ex06())
# (S
#   In/IN
#   (CNP (NP July/NNP) and/CC (NP August/NNP))
#   all/DT
#   your/PRP$
#   (CNP (NP managers/NNS) and/CC (NP supervisors/NNS))
#   will/VB
#   eat/VB
#   (CNP
#     (NP the/DT company/NN courts/NNS)
#     and/CC
#     (NP adjudicators/NNS)))

# 7 Carry out the following evaluation tasks for any of the chunkers you have developed earlier.
# (Note that most chunking corpora contain some internal inconsistencies,
# such that any reasonable rule-based approach will produce errors.)
# - Evaluate your chunker on 100 sentences from a chunked corpus, and report the precision,
# recall and F-measure.
# - Use the chunkscore.missed() and chunkscore.incorrect() methods to identify the errors
# made by your chunker. Discuss.
# - Compare the performance of your chunker to the baseline chunker
# discussed in the evaluation section of this chapter.

# NA - Have been doing it already (how can the previous exercises be completed otherwise, I ponder).

# 8 Develop a chunker for one of the chunk types in the CoNLL corpus
# using a regular-expression based chunk grammar RegexpChunk.
# Use any combination of rules for chunking, chinking, merging or splitting.

# NA - I have been working on the CoNLL corpus all along.
# nltk.corpus.conll2000._chunk_types
# ('NP', 'VP', 'PP')

# 9 Sometimes a word is incorrectly tagged, e.g. the head noun in "12/CD or/CC so/RB cases/VBZ".
# Instead of requiring manual correction of tagger output,
# good chunkers are able to work with the erroneous output of taggers.
# Look for other examples of correctly chunked noun phrases with incorrect tags.

def ex09(grammar=r"""NP: {<RB|DT|PP\$|PRP\$|CD>*<NN.*|JJ|VBG>*<NN.*>}
                         {<PPS*|PRP>}""",
         chunk_type='NP', likely_error='VB'):
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(grammar)
    evaluer = chunker.evaluate(test_sents)
    aux_missing=[ [i, miss] for i, miss in enumerate(evaluer.missed()) if sum([ likely_error in wrd[1] for wrd in miss])]
    return chunker, evaluer, aux_missing 

# ch,ev,le=ex09()
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  86.2%
#     Precision:     79.6%
#     Recall:        73.4%
#     F-Measure:     76.3%
# print(ev.missed()[35])
# (NP the/DT savings/NNS bank/VBP)
# print(ev.missed()[2])
# (NP so-called/JJ analog/NN integrated/VBN circuits/NNS)
# print(ev.missed()[9])
# (NP those/DT two/CD cherished/VBN national-security/NN causes/NNS)
# for l in le[:10]:
#     print l
# [2, ImmutableTree('NP', [(u'so-called', u'JJ'), (u'analog', u'NN'), (u'integrated', u'VBN'), (u'circuits', u'NNS')])]
# [9, ImmutableTree('NP', [(u'those', u'DT'), (u'two', u'CD'), (u'cherished', u'VBN'), (u'national-security', u'NN'), (u'causes', u'NNS')])]
# [23, ImmutableTree('NP', [(u'hedging', u'VBG')])]
# [26, ImmutableTree('NP', [(u'damaged', u'VBN'), (u'property', u'NN')])]
# [35, ImmutableTree('NP', [(u'the', u'DT'), (u'savings', u'NNS'), (u'bank', u'VBP')])]
# [46, ImmutableTree('NP', [(u"'s", u'POS'), (u'established', u'VBN'), (u'human', u'NN'), (u'and', u'CC'), (u'animal-health', u'NN'), (u'products', u'NNS')])]
# [51, ImmutableTree('NP', [(u'adjusted', u'VBN'), (u'gross', u'JJ'), (u'income', u'NN')])]
# [53, ImmutableTree('NP', [(u'vice', u'NN'), (u'president\\/product', u'NN'), (u'supply', u'NN'), (u',', u','), (u'purchasing', u'VBG')])]
# [59, ImmutableTree('NP', [(u'advanced', u'VBD'), (u'industrial', u'JJ'), (u'societies', u'NNS')])]
# [69, ImmutableTree('NP', [(u'separate', u'VB'), (u'bills', u'NNS')])]

# 10 The bigram chunker scores about 90% accuracy. Study its errors and try to work out
# why it doesn't get 100% accuracy. Experiment with trigram chunking.
# Are you able to improve the performance any more?

class NgramChunker(nltk.ChunkParserI):
    def __init__(self, n, train_sents, use_backoff=False):
        train_data = [[(pos_tag,chunk_tag) for _,pos_tag,chunk_tag in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        if use_backoff:
            aux_tagger=nltk.NgramTagger(1,train_data)
            for i in range(1,n):
                aux_tagger=nltk.NgramTagger(i+1,train_data,backoff=aux_tagger)
            self.tagger=aux_tagger
        else:
            self.tagger = nltk.NgramTagger(n,train_data)
    def parse(self, sentence):
        pos_tags = [pos_tag for (_,pos_tag) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunk_tags = [chunk_tag for (pos_tag, chunk_tag) in tagged_pos_tags]
        conll_tags = [(word, pos_tag, chunk_tag) for ((word,pos_tag),chunk_tag)
                     in zip(sentence, chunk_tags)]
        return nltk.chunk.conlltags2tree(conll_tags)

def ex10(n=2,backoff=False, chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker=NgramChunker(n,train_sents,use_backoff=backoff)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex10(n=2,backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.3%
#     Precision:     82.3%
#     Recall:        86.8%
#     F-Measure:     84.5%
# ch,ev=ex10(n=3,backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.3%
#     Precision:     82.5%
#     Recall:        86.8%
#     F-Measure:     84.6%

# ch,ev=ex10(n=2,backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.4%
#     Precision:     82.3%
#     Recall:        87.0%
#     F-Measure:     84.6%
#     
# ch,ev=ex10(n=3,backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.5%
#     Precision:     82.5%
#     Recall:        87.1%
#     F-Measure:     84.7%

# 11 Apply the n-gram and Brill tagging methods to IOB chunk tagging.
# Instead of assigning POS tags to words, here we will assign IOB tags to the POS tags.
# E.g. if the tag DT (determiner) often occurs at the start of a chunk,
# it will be tagged B (begin). Evaluate the performance of these chunking methods
# relative to the regular expression chunking methods covered in this chapter.

class BrillChunker(nltk.ChunkParserI):
    def __init__(self, train_sents, train_sent_num=1000,
                 max_rule=25, base_tagger=nltk.UnigramTagger,
                 brill_templates=nltk.tag.brill.nltkdemo18()):
        train_data = [[(pos_tag,chunk_tag) for _,pos_tag,chunk_tag in nltk.chunk.tree2conlltags(sent)]
                                           for sent in train_sents[:train_sent_num]]
        aux_brill_trainer = nltk.tag.BrillTaggerTrainer(base_tagger(train_data), brill_templates)
        self.tagger = aux_brill_trainer.train(train_data,max_rules=max_rule)
    def parse(self, sentence):
        pos_tags = [pos_tag for (_,pos_tag) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunk_tags = [chunk_tag for (_, chunk_tag) in tagged_pos_tags]
        conll_tags = [(word, pos_tag, chunk_tag) for ((word,pos_tag),chunk_tag)
                     in zip(sentence, chunk_tags)]
        return nltk.chunk.conlltags2tree(conll_tags)

def ex11(train_sent_num=1000, max_rule=25, chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker=BrillChunker(train_sents,max_rule)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex11(train_sent_num=1000, max_rule=25)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  90.8%
#     Precision:     77.4%
#     Recall:        82.9%
#     F-Measure:     80.1%
# ch,ev=ex11(train_sent_num=100, max_rule=150)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  92.6%
#     Precision:     80.0%
#     Recall:        84.7%
#     F-Measure:     82.3%
# ch,ev=ex11(train_sent_num=1000, max_rule=150)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  92.6%
#     Precision:     80.0%
#     Recall:        84.7%
#     F-Measure:     82.3%

# 12 We saw in 5. that it is possible to establish an upper limit to tagging performance
# by looking for ambiguous n-grams, n-grams that are tagged in more than one possible way
# in the training data. Apply the same method to determine an upper bound
# on the performance of an n-gram chunker.

def ex12(n=2, chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    train_sents=[[(pos_tag,chunk_tag) for _,pos_tag,chunk_tag in nltk.chunk.tree2conlltags(sent)]
                                      for sent in train_sents]
    contexts=[ ( tuple([ wrd[1] for wrd in wrds[:-1] ]+[wrds[-1][0]]), wrds[-1][1] )
               for sent in train_sents
               for wrds in nltk.ngrams(sent,n) ]
    cfd = nltk.ConditionalFreqDist(contexts)
    ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
    return 1.0*sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()

# ex12(n=1)
# 0.9994143401644571
# ex12(n=2)
# 0.9567929543224305
# ex12(n=3)
# 0.9237923297139762

# 13 Pick one of the three chunk types in the CoNLL corpus. Write functions to do
# the following tasks for your chosen type:
# - List all the tag sequences that occur with each instance of this chunk type.
# - Count the frequency of each tag sequence, and produce a ranked list
# in order of decreasing frequency; each line should consist of an integer (the frequency)
# and the tag sequence.
# - Inspect the high-frequency tag sequences. Use these as the basis for developing a better chunker.

def ex13_show(fd,sn=25):
    total=0
    for f in fd.most_common(sn):
        total=total+f[1]
        print "{:5} - {}".format(f[1],f[0])
    print 1.0*total/fd.N()

def ex13(chunk_type='NP',show_num=25):
    sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    sents=[ nltk.chunk.tree2conlltags(sent) for sent in sents ]
    sents=[ [ wrd for wrd in sent if wrd[2]!='O'] for sent in sents ]
    sents=[ nltk.chunk.conlltags2tree(sent) for sent in sents ]
    sequences=[ clause.leaves() for sent in sents for clause in sent ]
    sequences=[ tuple([wrd[1] for wrd in sequence]) for sequence in sequences ]
    fd=nltk.FreqDist(sequences)
    ex13_show(fd,show_num)
    return fd

# fd=ex13()
#  7223 - (u'DT', u'NN')
#  3802 - (u'PRP',)
#  3282 - (u'NNS',)
#  3249 - (u'NNP',)
#  3245 - (u'NN',)
#  2642 - (u'NNP', u'NNP')
#  2119 - (u'DT', u'JJ', u'NN')
#  1722 - (u'JJ', u'NNS')
#  1173 - (u'DT', u'NNS')
#  1143 - (u'JJ', u'NN')
#  1012 - (u'NN', u'NNS')
#   930 - (u'WDT',)
#   921 - (u'DT', u'NN', u'NN')
#   866 - (u'CD',)
#   830 - (u'CD', u'NN')
#   824 - (u'$', u'CD', u'CD')
#   690 - (u'CD', u'NNS')
#   677 - (u'NNP', u'NNP', u'NNP')
#   624 - (u'PRP$', u'NN')
#   552 - (u'POS', u'NN')
#   540 - (u'DT',)
#   509 - (u'WP',)
#   463 - (u'DT', u'NNP')
#   454 - (u'NN', u'NN')
#   446 - (u'$', u'CD')
# 0.72507761297

def ex13_chunker(grammar=r"""NP: {<[CDJNP].*>+}""",
                 chunk_type='NP'):
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(grammar)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex13_chunker(grammar = r"""NP: {<[CDJNP].*>+}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  87.7%
#     Precision:     70.6%
#     Recall:        67.8%
#     F-Measure:     69.2%

# ch,ev=ex13_chunker(grammar = r"""NP: {<[CDJNPW].*>+}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  87.7%
#     Precision:     69.1%
#     Recall:        67.1%
#     F-Measure:     68.0%

# ch,ev=ex13_chunker(grammar = r"""NP: {<[CDJNP].*>+}
#                                      {<WDT>}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  88.1%
#     Precision:     71.0%
#     Recall:        69.4%
#     F-Measure:     70.2%
    
# ch,ev=ex13_chunker(grammar=r"""NP: {<RB|DT|PP\$|PRP\$|CD>*<NN.*|JJ|VBG>*<NN.*>}
#                                    {<PPS*|PRP>}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  86.2%
#     Precision:     79.6%
#     Recall:        73.4%
#     F-Measure:     76.3%

# ch,ev=ex13_chunker(grammar=r"""NP: {<RB|DT|PP\$|PRP\$|CD>*<NN.*|JJ|VBG>*<NN.*>}
#                                    {<PPS*|PRP>}
#                                    {<WDT>}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  86.7%
#     Precision:     79.9%
#     Recall:        74.9%
#     F-Measure:     77.3%
    
# 14 The baseline chunker presented in the evaluation section tends to create larger chunks
# than it should. For example, the phrase: [every/DT time/NN] [she/PRP] sees/VBZ [a/DT newspaper/NN]
# contains two consecutive chunks, and our baseline chunker will incorrectly combine the first two:
# [every/DT time/NN she/PRP]. Write a program that finds which of these chunk-internal tags
# typically occur at the start of a chunk, then devise one or more rules that will
# split up these chunks. Combine these with the existing baseline chunker and re-evaluate it,
# to see if you have discovered an improved baseline.

def ex14_show(fd,sn=25):
    total=0
    for f in fd.most_common(sn):
        total=total+f[1]
        print "{:5} - {}".format(f[1],f[0])
    print 1.0*total/fd.N()

def ex14_v01(chunk_type='NP',show_num=25):
    sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    sents=[ nltk.chunk.tree2conlltags(sent) for sent in sents ]
    sents=[ [ (pos_tag,chunk_tag) for (_,pos_tag,chunk_tag) in sent ] for sent in sents ]
    chunker = nltk.RegexpParser(r"""NP_GROUP: {<[BI].*>+}""")
    sents=[ chunker.parse(sent) for sent in sents ]
    clauses=[ clause.leaves() for sent in sents for clause in [ subsent for subsent in sent.subtrees() if subsent.label()=='NP_GROUP' ] ]
    sequences=[ zip(*clause) for clause in clauses if zip(*clause)[1].count('B-NP')>1 ]
    sequences=[ tuple(sequence) for sequence in sequences ]
    fd=nltk.FreqDist(sequences)
    ex14_show(fd,show_num)
    return fd

# fs=ex14_v01()
#   182 - ((u'$', u'CD', u'DT', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#   148 - ((u'CD', u'NNS', u'DT', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#   143 - ((u'DT', u'NN', u'POS', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#   135 - ((u'NNP', u'POS', u'NN'), (u'B-NP', u'B-NP', u'I-NP'))
#    94 - ((u'NNP', u'NNP', u'POS', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#    80 - ((u'DT', u'NN', u'WDT'), (u'B-NP', u'I-NP', u'B-NP'))
#    58 - ((u'DT', u'NN', u'PRP'), (u'B-NP', u'I-NP', u'B-NP'))
#    55 - ((u'DT', u'NN', u'POS', u'JJ', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP', u'I-NP'))
#    52 - ((u'NNS', u'WDT'), (u'B-NP', u'B-NP'))
#    48 - ((u'NNS', u'WP'), (u'B-NP', u'B-NP'))
#    48 - ((u'DT', u'NN', u'POS', u'NNS'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#    47 - ((u'NNP', u'POS', u'NNS'), (u'B-NP', u'B-NP', u'I-NP'))
#    43 - ((u'NNP', u'POS', u'JJ', u'NN'), (u'B-NP', u'B-NP', u'I-NP', u'I-NP'))
#    42 - ((u'NNP', u'POS'), (u'B-NP', u'B-NP'))
#    41 - ((u'WP', u'PRP'), (u'B-NP', u'B-NP'))
#    36 - ((u'NNP', u'POS', u'NN', u'NN'), (u'B-NP', u'B-NP', u'I-NP', u'I-NP'))
#    32 - ((u'CD', u'NN', u'CD', u'NNS'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP'))
#    31 - ((u'NNP', u'POS', u'NNP', u'NNP'), (u'B-NP', u'B-NP', u'I-NP', u'I-NP'))
#    31 - ((u'WDT', u'PRP'), (u'B-NP', u'B-NP'))
#    30 - ((u'$', u'CD', u'CD', u'DT', u'NN'), (u'B-NP', u'I-NP', u'I-NP', u'B-NP', u'I-NP'))
#    30 - ((u'DT', u'JJ', u'NN', u'WDT'), (u'B-NP', u'I-NP', u'I-NP', u'B-NP'))
#    29 - ((u'NNS', u'POS', u'NNS'), (u'B-NP', u'B-NP', u'I-NP'))
#    28 - ((u'NN', u'WDT'), (u'B-NP', u'B-NP'))
#    28 - ((u'NNP', u'NNP', u'POS', u'JJ', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP', u'I-NP'))
#    27 - ((u'DT', u'NN', u'POS', u'NN', u'NN'), (u'B-NP', u'I-NP', u'B-NP', u'I-NP', u'I-NP'))
# 0.336660013307

def ex14_v02(chunk_type='NP',show_num=25):
    sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(r"""MANY_NPs: {<NP><NP>+}""")
    sents=[ chunker.parse(sent) for sent in sents ]
    clauses=[ clause for sent in sents for clause in [ subsent for subsent in sent.subtrees() if subsent.label()=='MANY_NPs' ] ]
    sequences=[ tuple([ tuple([ wrd[1] for wrd in sequence ]) for sequence in clause ]) for clause in clauses ]
    fd=nltk.FreqDist(sequences)
    ex14_show(fd,show_num)
    return fd

# fs=ex14_v02()
#   182 - ((u'$', u'CD'), (u'DT', u'NN'))
#   148 - ((u'CD', u'NNS'), (u'DT', u'NN'))
#   143 - ((u'DT', u'NN'), (u'POS', u'NN'))
#   135 - ((u'NNP',), (u'POS', u'NN'))
#    94 - ((u'NNP', u'NNP'), (u'POS', u'NN'))
#    80 - ((u'DT', u'NN'), (u'WDT',))
#    58 - ((u'DT', u'NN'), (u'PRP',))
#    55 - ((u'DT', u'NN'), (u'POS', u'JJ', u'NN'))
#    52 - ((u'NNS',), (u'WDT',))
#    48 - ((u'DT', u'NN'), (u'POS', u'NNS'))
#    48 - ((u'NNS',), (u'WP',))
#    47 - ((u'NNP',), (u'POS', u'NNS'))
#    43 - ((u'NNP',), (u'POS', u'JJ', u'NN'))
#    42 - ((u'NNP',), (u'POS',))
#    41 - ((u'WP',), (u'PRP',))
#    36 - ((u'NNP',), (u'POS', u'NN', u'NN'))
#    32 - ((u'CD', u'NN'), (u'CD', u'NNS'))
#    31 - ((u'WDT',), (u'PRP',))
#    31 - ((u'NNP',), (u'POS', u'NNP', u'NNP'))
#    30 - ((u'DT', u'JJ', u'NN'), (u'WDT',))
#    30 - ((u'$', u'CD', u'CD'), (u'DT', u'NN'))
#    29 - ((u'NNS',), (u'POS', u'NNS'))
#    28 - ((u'NNP', u'NNP'), (u'POS', u'JJ', u'NN'))
#    28 - ((u'NN',), (u'WDT',))
#    27 - ((u'DT', u'NN'), (u'POS', u'NN', u'NN'))
# 0.336660013307

def ex14_chunker(grammar=r"""NP: {<[CDJNP].*>+}""",
                 chunk_type='NP'):
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker = nltk.RegexpParser(grammar)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex14_chunker(grammar=r"""NP: {<[CDJNP].*>+}""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  87.7%
#     Precision:     70.6%
#     Recall:        67.8%
#     F-Measure:     69.2%

# ch,ev=ex14_chunker(grammar=r"""NP: {<[CDJNP].*>+}
#                                    }(?=<POS>){""")
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  88.6%
#     Precision:     74.4%
#     Recall:        74.1%
#     F-Measure:     74.2%

# ch,ev=ex14_chunker(grammar=r"""NP: {<[CDJNP].*>+}
#                                    }(?=<POS>){
#                                    }(<N.*>)(?=<[D].*>){""")
# 
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  88.7%
#     Precision:     74.7%
#     Recall:        74.9%
#     F-Measure:     74.8%

# 15 Develop an NP chunker that converts POS-tagged text into a list of tuples,
# where each tuple consists of a verb followed by a sequence of noun phrases and prepositions,
# e.g. the little cat sat on the mat becomes ('sat', 'on', 'NP')...

def ex15(grammar=r"""NP:     {<[CDJNP].*>+}
                     V_I_NP: {<V.*><IN>(?=<NP>)}"""):
    sents=nltk.corpus.conll2000.tagged_sents('train.txt')
    chunker = nltk.RegexpParser(grammar)
    sents=[ chunker.parse(sent) for sent in sents ]
    clauses=[ inner for sent in sents for inner in [ subsent for subsent in sent.subtrees() if subsent.label()=='V_I_NP' ] ]
    sequences=[ tuple([ wrd[0] for wrd in clause ]) for clause in clauses ]
    return sequences

# There is something I am not getting; this seems no different from finding all 'verb+preposition'.
# What is then the point of NP-chunking first?

# 16 The Penn Treebank contains a section of tagged Wall Street Journal text that has been chunked
# into noun phrases. The format uses square brackets, and we have encountered it
# several times during this chapter. The Treebank corpus can be accessed using:
# for sent in nltk.corpus.treebank_chunk.chunked_sents(fileid).
# These are flat trees, just as we got using nltk.corpus.conll2000.chunked_sents().
# - The functions nltk.tree.pprint() and nltk.chunk.tree2conllstr() can be used to create
# Treebank and IOB strings from a tree. Write functions chunk2brackets() and chunk2iob()
# that take a single chunk tree as their sole argument, and return the required multi-line
# string representation.
# - Write command-line conversion utilities bracket2iob.py and iob2bracket.py that take a file
# in Treebank or CoNLL format (resp) and convert it to the other format.
# (Obtain some raw Treebank or CoNLL data from the NLTK Corpora, save it to a file,
# and then use for line in open(filename) to access it from Python.)

def ex16_read_first(filenom='/usr/share/nltk_data/corpora/conll2000/train.txt'):
    f=open(filenom)
    aux_str=''
    s='\n'
    while s=='\n':
        s=f.readline()
    while s!='\n':
        aux_str=aux_str+s
        s=f.readline()
    f.close()
    return aux_str[:-1]
  
# print(ex16_read_first(filenom='/usr/share/nltk_data/corpora/conll2000/train.txt'))
# Confidence NN B-NP
# in IN B-PP
# the DT B-NP
# pound NN I-NP
# is VBZ B-VP
# widely RB I-VP
# expected VBN I-VP
# to TO I-VP
# take VB I-VP
# another DT B-NP
# sharp JJ I-NP
# dive NN I-NP
# if IN B-SBAR
# trade NN B-NP
# figures NNS I-NP
# for IN B-PP
# September NNP B-NP
# , , O
# due JJ B-ADJP
# for IN B-PP
# release NN B-NP
# tomorrow NN B-NP
# , , O
# fail VB B-VP
# to TO I-VP
# show VB I-VP
# a DT B-NP
# substantial JJ I-NP
# improvement NN I-NP
# from IN B-PP
# July NNP B-NP
# and CC I-NP
# August NNP I-NP
# 's POS B-NP
# near-record JJ I-NP
# deficits NNS I-NP
# . . O

# s1=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=['NP'])[0]

# print(nltk.chunk.tree2conllstr(s1))
# Confidence NN B-NP
# in IN O
# the DT B-NP
# pound NN I-NP
# is VBZ O
# widely RB O
# expected VBN O
# to TO O
# take VB O
# another DT B-NP
# sharp JJ I-NP
# dive NN I-NP
# if IN O
# trade NN B-NP
# figures NNS I-NP
# for IN O
# September NNP B-NP
# , , O
# due JJ O
# for IN O
# release NN B-NP
# tomorrow NN B-NP
# , , O
# fail VB O
# to TO O
# show VB O
# a DT B-NP
# substantial JJ I-NP
# improvement NN I-NP
# from IN O
# July NNP B-NP
# and CC I-NP
# August NNP I-NP
# 's POS B-NP
# near-record JJ I-NP
# deficits NNS I-NP
# . . O

# s1.pprint()
# (S
#   (NP Confidence/NN)
#   in/IN
#   (NP the/DT pound/NN)
#   is/VBZ
#   widely/RB
#   expected/VBN
#   to/TO
#   take/VB
#   (NP another/DT sharp/JJ dive/NN)
#   if/IN
#   (NP trade/NN figures/NNS)
#   for/IN
#   (NP September/NNP)
#   ,/,
#   due/JJ
#   for/IN
#   (NP release/NN)
#   (NP tomorrow/NN)
#   ,/,
#   fail/VB
#   to/TO
#   show/VB
#   (NP a/DT substantial/JJ improvement/NN)
#   from/IN
#   (NP July/NNP and/CC August/NNP)
#   (NP 's/POS near-record/JJ deficits/NNS)
#   ./.)

# print(ex16_read_first(filenom='/usr/share/nltk_data/corpora/treebank/tagged/wsj_0001.pos'))
# [ Pierre/NNP Vinken/NNP ]
# ,/, 
# [ 61/CD years/NNS ]
# old/JJ ,/, will/MD join/VB 
# [ the/DT board/NN ]
# as/IN 
# [ a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ]
# ./. 
# 
# s2=nltk.corpus.treebank_chunk.chunked_sents('wsj_0001.pos')[0]
# 
# print(nltk.chunk.tree2conllstr(s2))
# Pierre NNP B-NP
# Vinken NNP I-NP
# , , O
# 61 CD B-NP
# years NNS I-NP
# old JJ O
# , , O
# will MD O
# join VB O
# the DT B-NP
# board NN I-NP
# as IN O
# a DT B-NP
# nonexecutive JJ I-NP
# director NN I-NP
# Nov. NNP I-NP
# 29 CD I-NP
# . . O
# 
# s2.pprint()
# (S
#   (NP Pierre/NNP Vinken/NNP)
#   ,/,
#   (NP 61/CD years/NNS)
#   old/JJ
#   ,/,
#   will/MD
#   join/VB
#   (NP the/DT board/NN)
#   as/IN
#   (NP a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD)
#   ./.)

# This is assumed to be the brackets structure:
# [ Pierre/NNP Vinken/NNP ]
# ,/, 
# [ 61/CD years/NNS ]
# old/JJ ,/, will/MD join/VB 
# [ the/DT board/NN ]
# as/IN 
# [ a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ]
# ./.

def ex16_chunk2brackets(my_tree):
    aux_str=u''
    last_clause_NP=''
    for clause in my_tree:
        try:
            clause.label()
            if aux_str!='':
                aux_str=aux_str+' \n'
            aux_str=aux_str+'[ '+' '.join([ wrd[0]+'/'+wrd[1] for wrd in clause ])+' ]'
            last_clause_NP=True
        except AttributeError:
            if aux_str!='':
                if last_clause_NP:
                    aux_str=aux_str+'\n'
                else:
                    aux_str=aux_str+' '
            aux_str=aux_str+clause[0]+'/'+clause[1]
            last_clause_NP=False
    if not last_clause_NP:
        aux_str=aux_str+' '
    return aux_str

# ex16_chunk2brackets(s2)==ex16_read_first(filenom='/usr/share/nltk_data/corpora/treebank/tagged/wsj_0001.pos')
# True

def ex16_chunk2iob_v01(my_tree):
    return nltk.chunk.tree2conllstr(my_tree)

# ex16_chunk2iob_v01(s1)==nltk.chunk.tree2conllstr(s1)
# True

# There is something I am not getting: is tree2conllstr not exactly what is being requested?
# In any case, here is the code that does the same thing

def ex16_chunk2iob_v02(my_tree):
    aux_str=''
    for clause in my_tree:
        if aux_str!='':
            aux_str=aux_str+'\n'
        try:
            clause.label()
        except AttributeError:
            aux_str=aux_str+clause[0]+' '+clause[1]+' O'
        else:
            aux_str=aux_str+clause[0][0]+' '+clause[0][1]+' B-NP'
            if len(clause)>1:
                aux_str=aux_str+'\n'+'\n'.join([wrd[0]+' '+wrd[1]+' I-NP' for wrd in clause[1:] ])
    return aux_str

# ex16_chunk2iob_v02(s1)==ex16_chunk2iob_v01(s1)
# True

def ex16_bracket2tree(my_str):
    aux_leaves=[]
    for clause in my_str.split('\n'):
        if clause[0]=='[':
            clause=clause[2:-2].split(' ')
            clause=[( wrd[:wrd.rfind('/')],wrd[wrd.rfind('/')+1:]) for wrd in clause ]
            aux_leaves=aux_leaves+[ nltk.Tree('NP',clause) ]
        else:
            clause=clause.strip().split(' ')
            clause=[( wrd[:wrd.rfind('/')],wrd[wrd.rfind('/')+1:]) for wrd in clause ]
            aux_leaves=aux_leaves+clause
    return nltk.Tree('S', aux_leaves)

# s2==ex16_bracket2tree(ex16_read_first(filenom='/usr/share/nltk_data/corpora/treebank/tagged/wsj_0001.pos'))
# True

def ex16_bracket2iob(my_str):
    my_tree=ex16_bracket2tree(my_str)
    return nltk.chunk.tree2conllstr(my_tree)

# ex16_bracket2iob(ex16_read_first(filenom='/usr/share/nltk_data/corpora/treebank/tagged/wsj_0001.pos'))==nltk.chunk.tree2conllstr(s2)
# True

def ex16_iob2bracket(my_str):
    my_tree=nltk.chunk.conllstr2tree(my_str)
    return ex16_chunk2brackets(my_tree)

# ex16_iob2bracket(nltk.chunk.tree2conllstr(s2))==ex16_read_first(filenom='/usr/share/nltk_data/corpora/treebank/tagged/wsj_0001.pos')
# True

# 17 An n-gram chunker can use information other than the current part-of-speech tag
# and the n-1 previous chunk tags. Investigate other models of the context,
# such as the n-1 previous part-of-speech tags, or some combination of previous chunk tags
# along with previous and following part-of-speech tags.

class PimpedGramChunker(nltk.ChunkParserI):
    def __init__(self, n, pos_lst, use_backoff, train_sents):
        self.pos_lst=pos_lst
        train_sents=[ nltk.chunk.tree2conlltags(sent) for sent in train_sents ]
        train_feats=[ self._extract_features([ (word, pos_tag) for (word, pos_tag, _) in sent ])
                      for sent in train_sents ]
        train_tags= [ [ chk_tag for (_, _, chk_tag) in sent ]
                      for sent in train_sents ]
        train_data=[ zip(train_feats[i],train_tags[i]) for i in range(len(train_sents))]
        if use_backoff:
            aux_tagger=nltk.NgramTagger(1,train_data)
            for i in range(1,n):
                aux_tagger=nltk.NgramTagger(i+1,train_data,backoff=aux_tagger)
            self.tagger=aux_tagger
        else:
            self.tagger = nltk.NgramTagger(n,train_data)
    def parse(self, sentence):
        featured_sent = self._extract_features(sentence)
        tagged_feats = self.tagger.tag(featured_sent)
        chunk_tags = [chunk_tag for (_, chunk_tag) in tagged_feats]
        conll_tags = [(word, pos_tag, chunk_tag) for ((word,pos_tag),chunk_tag)
                     in zip(sentence, chunk_tags)]
        return nltk.chunk.conlltags2tree(conll_tags)
    def _extract_features(self,sentence):
        feats=[]
        for i in range(len(sentence)):
            i_feats=[]
            for j in self.pos_lst:
                if i+j<0:
                    feat='<START>'
                elif i+j>=len(sentence):
                    feat='<END>'
                else:
                    feat=sentence[i+j][1]
                i_feats=i_feats+[ feat ]
            feats=feats+[ tuple(i_feats) ]
        return feats

def ex17(n=2,pos_lst=[0],backoff=False,chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker=PimpedGramChunker(n,pos_lst,backoff,train_sents)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex17(n=1,pos_lst=[0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  92.9%
#     Precision:     79.9%
#     Recall:        86.8%
#     F-Measure:     83.2%
#     
# ch,ev=ex17(n=1,pos_lst=[-1, 0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  94.1%
#     Precision:     83.8%
#     Recall:        88.0%
#     F-Measure:     85.8%
# 
# ch,ev=ex17(n=1,pos_lst=[-2, -1, 0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.5%
#     Precision:     84.0%
#     Recall:        86.9%
#     F-Measure:     85.5%
# 
# ch,ev=ex17(n=1,pos_lst=[-1, 0, 1],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  94.8%
#     Precision:     86.5%
#     Recall:        88.2%
#     F-Measure:     87.3%
# 
# ch,ev=ex17(n=2,pos_lst=[0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.3%
#     Precision:     82.3%
#     Recall:        86.8%
#     F-Measure:     84.5%
#     
# ch,ev=ex17(n=2,pos_lst=[-1, 0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  92.3%
#     Precision:     86.6%
#     Recall:        85.4%
#     F-Measure:     86.0%
# 
# ch,ev=ex17(n=2,pos_lst=[-2, -1, 0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  83.9%
#     Precision:     87.2%
#     Recall:        70.5%
#     F-Measure:     78.0%
#     
# ch,ev=ex17(n=2,pos_lst=[-1, 0, 1],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  85.7%
#     Precision:     91.1%
#     Recall:        72.9%
#     F-Measure:     81.0%
# 
# ch,ev=ex17(n=2,pos_lst=[0],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.4%
#     Precision:     82.3%
#     Recall:        87.0%
#     F-Measure:     84.6%
#      
# ch,ev=ex17(n=2,pos_lst=[-1, 0],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  94.3%
#     Precision:     86.5%
#     Recall:        88.7%
#     F-Measure:     87.6%
#     
# ch,ev=ex17(n=2,pos_lst=[-2, -1, 0],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  93.5%
#     Precision:     84.8%
#     Recall:        87.0%
#     F-Measure:     85.9%
# 
# ch,ev=ex17(n=2,pos_lst=[-1, 0, 1],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  95.2%
#     Precision:     89.6%
#     Recall:        89.0%
#     F-Measure:     89.3%
    
# 18 Consider the way an n-gram tagger uses recent tags to inform its tagging choice.
# Now observe how a chunker may re-use this sequence information.
# For example, both tasks will make use of the information that nouns tend to follow adjectives
# (in English). It would appear that the same information is being maintained in two places.
# Is this likely to become a problem as the size of the rule sets grows?
# If so, speculate about any ways that this problem might be addressed.

# Train a single classifier to estimate both POS tags and chunk tags from the same inputs?
# The tags would then be a tuple of (POS tag, Chunk tag). To be explored

# Whatever! The results seem promising, but a larger training set would be needed
# to see the method performing to its fullest.

class NgramTAndC_Chunker(nltk.ChunkParserI):
    def __init__(self, n, wrd_lst, use_backoff, train_sents):
        self.wrd_lst=wrd_lst
        train_sents=[ nltk.chunk.tree2conlltags(sent) for sent in train_sents ]
        train_feats=[ self._extract_features([ word for (word, _, _) in sent ])
                      for sent in train_sents ]
        train_tags= [ [ (pos_tag, chk_tag) for (_, pos_tag, chk_tag) in sent ]
                      for sent in train_sents ]
        train_data=[ zip(train_feats[i],train_tags[i]) for i in range(len(train_sents))]
        if use_backoff:
            aux_tagger=nltk.NgramTagger(1,train_data)
            for i in range(1,n):
                aux_tagger=nltk.NgramTagger(i+1,train_data,backoff=aux_tagger)
            self.tagger=aux_tagger
        else:
            self.tagger = nltk.NgramTagger(n,train_data)
    def parse(self, sentence):
        featured_sent = self._extract_features([ word for (word, _) in sentence ])
        tagged_feats = self.tagger.tag(featured_sent)
        chunk_tags = [tags[1] if tags!=None else None for (_, tags) in tagged_feats]
        conll_tags = [(word, pos_tag, chunk_tag) for ((word,pos_tag),chunk_tag)
                     in zip(sentence, chunk_tags)]
        return nltk.chunk.conlltags2tree(conll_tags)
    def _extract_features(self,sentence):
        feats=[]
        for i in range(len(sentence)):
            i_feats=[]
            for j in self.wrd_lst:
                if i+j<0:
                    feat='<START>'
                elif i+j>=len(sentence):
                    feat='<END>'
                else:
                    feat=sentence[i+j]
                i_feats=i_feats+[ feat ]
            feats=feats+[ tuple(i_feats) ]
        return feats

def ex18_chunker(n=1,wrd_lst=[0],backoff=False,chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=[chunk_type])
    chunker=NgramTAndC_Chunker(n,wrd_lst,backoff,train_sents)
    return chunker, chunker.evaluate(test_sents)

# ch,ev=ex18_chunker(n=1,wrd_lst=[0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  83.0%
#     Precision:     54.7%
#     Recall:        64.3%
#     F-Measure:     59.1%
#     
# ch,ev=ex18_chunker(n=1,wrd_lst=[-1,0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  83.0%
#     Precision:     54.7%
#     Recall:        64.3%
#     F-Measure:     59.1%
#     
# ch,ev=ex18_chunker(n=2,wrd_lst=[0],backoff=False)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  53.9%
#     Precision:     70.4%
#     Recall:        16.9%
#     F-Measure:     27.2%
#     
# ch,ev=ex18_chunker(n=2,wrd_lst=[0],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  86.0%
#     Precision:     64.4%
#     Recall:        70.5%
#     F-Measure:     67.3%
# 
# ch,ev=ex18_chunker(n=2,wrd_lst=[-1,0],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  69.1%
#     Precision:     47.8%
#     Recall:        35.8%
#     F-Measure:     40.9%
#     
# ch,ev=ex18_chunker(n=2,wrd_lst=[0,1],backoff=True)
# print(ev)
# ChunkParse score:
#     IOB Accuracy:  64.8%
#     Precision:     45.3%
#     Recall:        33.9%
#     F-Measure:     38.8%

class NgramTAndC_Tagger(nltk.TaggerI):
    def __init__(self, n, wrd_lst, use_backoff, train_sents):
        self.wrd_lst=wrd_lst
        train_sents=[ nltk.chunk.tree2conlltags(sent) for sent in train_sents ]
        train_feats=[ self._extract_features([ word for (word, _, _) in sent ])
                      for sent in train_sents ]
        train_tags= [ [ (pos_tag, chk_tag) for (_, pos_tag, chk_tag) in sent ]
                      for sent in train_sents ]
        train_data=[ zip(train_feats[i],train_tags[i]) for i in range(len(train_sents))]
        if use_backoff:
            aux_tagger=nltk.NgramTagger(1,train_data)
            for i in range(1,n):
                aux_tagger=nltk.NgramTagger(i+1,train_data,backoff=aux_tagger)
            self.tagger=aux_tagger
        else:
            self.tagger = nltk.NgramTagger(n,train_data)
    def tag(self, sentence):
        featured_sent = self._extract_features(sentence)
        tagged_feats = self.tagger.tag(featured_sent)
        pos_tags = [tags[0] if tags!=None else None for (_, tags) in tagged_feats]
        return zip(sentence,pos_tags)
    def _extract_features(self,sentence):
        feats=[]
        for i in range(len(sentence)):
            i_feats=[]
            for j in self.wrd_lst:
                if i+j<0:
                    feat='<START>'
                elif i+j>=len(sentence):
                    feat='<END>'
                else:
                    feat=sentence[i+j]
                i_feats=i_feats+[ feat ]
            feats=feats+[ tuple(i_feats) ]
        return feats

def ex18_tagger(n=1,wrd_lst=[0],backoff=False,chunk_type='NP'):
    train_sents=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=[chunk_type])
    test_sents=nltk.corpus.conll2000.tagged_sents('test.txt')
    tagger=NgramTAndC_Tagger(n,wrd_lst,backoff,train_sents)
    return tagger, tagger.evaluate(test_sents)

# ch,ev=ex18_tagger(n=1,wrd_lst=[0],backoff=False)
# print(ev)
# 0.892796082487
# 
# ch,ev=ex18_tagger(n=1,wrd_lst=[-1,0],backoff=False)
# print(ev)
# 0.554340713848
# 
# ch,ev=ex18_tagger(n=2,wrd_lst=[0],backoff=True)
# print(ev)
# 0.903898516158