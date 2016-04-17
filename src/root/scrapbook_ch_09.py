'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

def test_sent_against_grammar(sents,grammar,trace=0):
    parser = nltk.load_parser(grammar, trace)
    for sent in sents:
        print ' '.join(sent)
        num_trees = 0
        for tree in parser.parse(sent):
            num_trees = num_trees+1
            print tree
        print num_trees

# 1 What constraints are required to correctly parse word sequences like I am happy and she is happy but not
# *you is happy or *they am happy? Implement two solutions for the present tense paradigm of the verb be in English,
# first taking Grammar (6) as your starting point, and then taking Grammar (18) as the starting point.

# Person and number coordination

# % start S
# # ###################
# # Grammar Productions
# # ###################
# 
# # S expansion productions
# S -> NP_SG_1 VP_SG_1
# S -> NP_SG_2 VP_SG_2
# S -> NP_SG_3 VP_SG_3
# S -> NP_PL VP_PL
# 
# # NP expansion productions
# NP_SG_1 -> PN_SG_1
# NP_SG_2 -> PN_SG_2
# NP_SG_3 -> PN_SG_3
# NP_PL -> PN_PL
# 
# # VP expansion productions
# VP_SG_1 -> V_SG_1 ADJ
# VP_SG_2 -> V_SG_2 ADJ
# VP_SG_3 -> V_SG_3 ADJ
# VP_PL -> V_PL ADJ
# 
# # ###################
# # Lexical Productions
# # ###################
# 
# PN_SG_1 -> 'I'
# PN_SG_2 -> 'You'
# PN_SG_2 -> 'He' | 'She' | 'It'
# PN_PL -> 'We' | 'You' | 'They'
# V_SG_1 -> 'am'
# V_SG_2 -> 'are'
# V_SG_1 -> 'is'
# V_PL -> 'are'
# ADJ -> 'happy'

# test_sent_against_grammar(sents=['I am happy'.split(),
#                                  'We am happy'.split(),
#                                  'You are happy'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar01.fcfg')
# 
# I am happy
# (S[]
#   (NP_SG_1[] (PN_SG_1[] I))
#   (VP_SG_1[] (V_SG_1[] am) (ADJ[] happy)))
# 1
# We am happy
# 0
# You are happy
# (S[]
#   (NP_SG_2[] (PN_SG_2[] You))
#   (VP_SG_2[] (V_SG_2[] are) (ADJ[] happy)))
# (S[] (NP_PL[] (PN_PL[] You)) (VP_PL[] (V_PL[] are) (ADJ[] happy)))
# 2

# % start S
# # ###################
# # Grammar Productions
# # ###################
# 
# # S expansion productions
# S -> NP[AGR=?n] VP[AGR=?n]
# 
# # NP expansion productions
# NP[AGR=?n] -> PN[AGR=?n]
# 
# # VP expansion productions
# VP[AGR=?n] -> V[AGR=?n] ADJ
# 
# # ###################
# # Lexical Productions
# # ###################
# 
# PN[AGR=[NUM=SG, PERS=1]] -> 'I'
# PN[AGR=[NUM=SG, PERS=2]] -> 'You'
# PN[AGR=[NUM=SG, PERS=3]] -> 'He' | 'She' | 'It'
# PN[AGR=[NUM=PL]] -> 'We' | 'You' | 'They'
# V[AGR=[NUM=SG, PERS=1]] -> 'am'
# V[AGR=[NUM=SG, PERS=2]] -> 'are'
# V[AGR=[NUM=SG, PERS=3]] -> 'is'
# V[AGR=[NUM=PL]] -> 'are'
# ADJ -> 'happy'

# test_sent_against_grammar(sents=['I am happy'.split(),
#                                  'We am happy'.split(),
#                                  'You are happy'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar02.fcfg')
# 
# I am happy
# (S[]
#   (NP[AGR=[NUM='SG', PERS=1]] (PN[AGR=[NUM='SG', PERS=1]] I))
#   (VP[AGR=[NUM='SG', PERS=1]]
#     (V[AGR=[NUM='SG', PERS=1]] am)
#     (ADJ[] happy)))
# 1
# We am happy
# 0
# You are happy
# (S[]
#   (NP[AGR=[NUM='SG', PERS=2]] (PN[AGR=[NUM='SG', PERS=2]] You))
#   (VP[AGR=[NUM='SG', PERS=2]]
#     (V[AGR=[NUM='SG', PERS=2]] are)
#     (ADJ[] happy)))
# (S[]
#   (NP[AGR=[NUM='PL']] (PN[AGR=[NUM='PL']] You))
#   (VP[AGR=[NUM='PL']] (V[AGR=[NUM='PL']] are) (ADJ[] happy)))
# 2

# 2 Develop a variant of grammar in 1.1 that uses a feature count to make the distinctions shown below:
#   (54)
#     a. The boy sings.
#     b. *Boy sings.
#   (55)
#     a. The boys sing.
#     b. Boys sing.
#   (56)
#     a. The boys sing.
#     b. Boys sing.
#   (57)
#     a. The water is precious.
#     b. Water is precious.

# % start S
# # ###################
# # Grammar Productions
# # ###################
# # S expansion productions
# S -> NP[NUM=?n] VP[NUM=?n]
# # NP expansion productions
# NP[NUM=?n] -> PropN[NUM=?n]
# NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
# NP[NUM=sg] -> N[NUM=sg, -COUNT]
# NP[NUM=pl] -> N[NUM=pl]
# # VP expansion productions
# VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
# VP[TENSE=?t, NUM=?n] -> TV[TENSE=?t, NUM=?n] NP
# VP[TENSE=?t, NUM=?n] -> CV[TENSE=?t, NUM=?n] ADJ
# # ###################
# # Lexical Productions
# # ###################
# Det[NUM=sg] -> 'this' | 'every' | 'a'
# Det[NUM=pl] -> 'these' | 'all'
# Det -> 'the' | 'some' | 'several'
# PropN[NUM=sg]-> 'Kim' | 'Jody'
# N[NUM=sg, +COUNT] -> 'dog' | 'girl' | 'car' | 'child' | 'boy' | 'song'
# N[NUM=sg, -COUNT] -> 'water'
# N[NUM=pl] -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys' | 'songs'
# IV[TENSE=pres,  NUM=sg] -> 'disappears' | 'walks'
# TV[TENSE=pres, NUM=sg] -> 'sees' | 'likes' | 'sings'
# CV[TENSE=pres, NUM=sg] -> 'is' | 'seems'
# IV[TENSE=pres,  NUM=pl] -> 'disappear' | 'walk'
# TV[TENSE=pres, NUM=pl] -> 'see' | 'like' | 'sing'
# CV[TENSE=pres, NUM=pl] -> 'are' | 'seem'
# IV[TENSE=past] -> 'disappeared' | 'walked'
# TV[TENSE=past] -> 'saw' | 'liked' | 'sang'
# CV[TENSE=past] -> 'were' | 'seemed'
# ADJ -> 'precious' | 'happy'
# 
# test_sent_against_grammar(sents=['the boy sings a song'.split(),
#                                  'the boy sings songs'.split(),
#                                  'boy sings a song'.split(),
#                                  'the boys sing the songs'.split(),
#                                  'boys sing these songs'.split(),
#                                  'boys sang cars'.split(),
#                                  'the water is precious'.split(),
#                                  'water is precious'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar03.fcfg')
# 
# the boy sings a song
# (S[]
#   (NP[NUM='sg'] (Det[] the) (N[+COUNT, NUM='sg'] boy))
#   (VP[NUM='sg', TENSE='pres']
#     (TV[NUM='sg', TENSE='pres'] sings)
#     (NP[NUM='sg'] (Det[NUM='sg'] a) (N[+COUNT, NUM='sg'] song))))
# 1
# the boy sings songs
# (S[]
#   (NP[NUM='sg'] (Det[] the) (N[+COUNT, NUM='sg'] boy))
#   (VP[NUM='sg', TENSE='pres']
#     (TV[NUM='sg', TENSE='pres'] sings)
#     (NP[NUM='pl'] (N[NUM='pl'] songs))))
# 1
# boy sings a song
# 0
# the boys sing the songs
# (S[]
#   (NP[NUM='pl'] (Det[] the) (N[NUM='pl'] boys))
#   (VP[NUM='pl', TENSE='pres']
#     (TV[NUM='pl', TENSE='pres'] sing)
#     (NP[NUM='pl'] (Det[] the) (N[NUM='pl'] songs))))
# 1
# boys sing these songs
# (S[]
#   (NP[NUM='pl'] (N[NUM='pl'] boys))
#   (VP[NUM='pl', TENSE='pres']
#     (TV[NUM='pl', TENSE='pres'] sing)
#     (NP[NUM='pl'] (Det[NUM='pl'] these) (N[NUM='pl'] songs))))
# 1
# boys sang cars
# (S[]
#   (NP[NUM='pl'] (N[NUM='pl'] boys))
#   (VP[NUM=?n, TENSE='past']
#     (TV[TENSE='past'] sang)
#     (NP[NUM='pl'] (N[NUM='pl'] cars))))
# 1
# the water is precious
# (S[]
#   (NP[NUM='sg'] (Det[] the) (N[-COUNT, NUM='sg'] water))
#   (VP[NUM='sg', TENSE='pres']
#     (CV[NUM='sg', TENSE='pres'] is)
#     (ADJ[] precious)))
# 1
# water is precious
# (S[]
#   (NP[NUM='sg'] (N[-COUNT, NUM='sg'] water))
#   (VP[NUM='sg', TENSE='pres']
#     (CV[NUM='sg', TENSE='pres'] is)
#     (ADJ[] precious)))
# 1

# 3 Write a function subsumes() which holds of two feature structures fs1 and fs2 just in case fs1 subsumes fs2.

def subsumes(fs1=nltk.FeatStruct(CITY='Paris'), fs2=nltk.FeatStruct(NUMBER=74, STREET='rue Pascal', CITY='Paris')):
    return fs1.unify(fs2)==fs2

def ex03(fs1=nltk.FeatStruct(CITY='Paris'), fs2=nltk.FeatStruct(NUMBER=74, STREET='rue Pascal', CITY='Paris')):
    return subsumes(fs1,fs2)

# ex03(fs1=nltk.FeatStruct(CITY='Paris'), fs2=nltk.FeatStruct(NUMBER=74, STREET='rue Pascal', CITY='Paris'))
# True
# ex03(fs1=nltk.FeatStruct(NUMBER=74, STREET='rue Pascal', CITY='Paris'), fs2=nltk.FeatStruct(CITY='Paris'))
# False

# 4 Modify the grammar illustrated in (28) to incorporate a bar feature for dealing with phrasal projections.

# % start S
# # ###################
# # Grammar Productions
# # ###################
# # S expansion productions
# S -> N[BAR=2, NUM=?n] V[BAR=2, NUM=?n]
# # NP expansion productions
# N[BAR=2, NUM=?n] -> PropN[NUM=?n]
# N[BAR=2, NUM=?n] -> Det[NUM=?n] N[BAR=1, NUM=?n]
# N[BAR=2, NUM=sg] -> N[BAR=1, NUM=sg, -COUNT]
# N[BAR=2, NUM=pl] -> N[BAR=1, NUM=pl]
# N[BAR=1, NUM=?n] -> N[BAR=1, NUM=?n] P[BAR=2]
# N[BAR=1, NUM=sg, -COUNT] -> N[BAR=0, NUM=sg, -COUNT]
# N[BAR=1, NUM=?n, COUNT=?c] -> N[BAR=0, NUM=?n, COUNT=?c]
# # VP expansion productions
# V[BAR=2, TENSE=?t, NUM=?n] -> V[BAR=1, TENSE=?t, NUM=?n]
# V[BAR=1, TENSE=?t, NUM=?n] -> V[BAR=1, TENSE=?t, NUM=?n] P[BAR=2]
# V[BAR=1, SUBCAT=intrans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=intrans, TENSE=?t, NUM=?n]
# V[BAR=1, SUBCAT=trans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=trans, TENSE=?t, NUM=?n] N[BAR=2]
# V[BAR=1, SUBCAT=state, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=state, TENSE=?t, NUM=?n] ADJ
# V[BAR=1, SUBCAT=clause, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=clause, TENSE=?t, NUM=?n] SBar
# # PP expansion productions
# P[BAR=2] -> Prep P[BAR=1]
# P[BAR=1] -> P[BAR=1] P[BAR=1]
# P[BAR=1] -> Adj P[BAR=0]
# P[BAR=1] -> P[BAR=0]
# P[BAR=0] -> N[BAR=2]
# SBar -> Comp S
# # ###################
# # Lexical Productions
# # ###################
# Det[NUM=sg] -> 'this' | 'every' | 'a'
# Det[NUM=pl] -> 'these' | 'all'
# Det -> 'the' | 'some' | 'several'
# PropN[NUM=sg]-> 'Kim' | 'Jody'
# N[BAR=0, NUM=sg, +COUNT] -> 'dog' | 'girl' | 'car' | 'child' | 'boy' | 'song' | 'bike'
# N[BAR=0, NUM=sg, -COUNT] -> 'water'
# N[BAR=0, NUM=pl] -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys' | 'songs'
# V[BAR=0, SUBCAT=intrans, TENSE=pres,  NUM=sg] -> 'disappears' | 'walks'
# V[BAR=0, SUBCAT=trans, TENSE=pres, NUM=sg] -> 'sees' | 'likes' | 'sings'
# V[BAR=0, SUBCAT=state, TENSE=pres, NUM=sg] -> 'is' | 'seems'
# V[BAR=0, SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'thinks' | 'claims'
# V[BAR=0, SUBCAT=intrans, TENSE=pres,  NUM=pl] -> 'disappear' | 'walk'
# V[BAR=0, SUBCAT=trans, TENSE=pres, NUM=pl] -> 'see' | 'like' | 'sing'
# V[BAR=0, SUBCAT=state, TENSE=pres, NUM=pl] -> 'are' | 'seem'
# V[BAR=0, SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'think' | 'claim'
# V[BAR=0, SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
# V[BAR=0, SUBCAT=trans, TENSE=past] -> 'saw' | 'liked' | 'sang'
# V[BAR=0, SUBCAT=state, TENSE=past] -> 'were' | 'seemed'
# V[BAR=0, SUBCAT=clause, TENSE=past] -> 'said' | 'thought' | 'claimed'
# Prep -> 'with' | 'by' | 'on' | 'in'
# ADJ -> 'precious' | 'happy'
# Comp -> 'that'

# test_sent_against_grammar(sents=['the boy sings a song'.split(),
#                                  'the boy sings songs'.split(),
#                                  'boy sings a song'.split(),
#                                  'the boys sing the songs'.split(),
#                                  'boys sing these songs'.split(),
#                                  'boys sang cars'.split(),
#                                  'the water is precious'.split(),
#                                  'water is precious'.split(),
#                                  'the boy says that the girl walks'.split(),
#                                  'the boy in the car sees the girl with water on a bike'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar04.fcfg')
# 
# the boy sings a song
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sings)
#       (N[BAR=2, NUM='sg']
#         (Det[NUM='sg'] a)
#         (N[BAR=1, +COUNT, NUM='sg']
#           (N[BAR=0, +COUNT, NUM='sg'] song))))))
# 1
# the boy sings songs
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sings)
#       (N[BAR=2, NUM='pl']
#         (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] songs))))))
# 1
# boy sings a song
# 0
# the boys sing the songs
# (S[]
#   (N[BAR=2, NUM='pl']
#     (Det[] the)
#     (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] boys)))
#   (V[BAR=2, NUM='pl', TENSE='pres']
#     (V[BAR=1, NUM='pl', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='pl', SUBCAT='trans', TENSE='pres'] sing)
#       (N[BAR=2, NUM='pl']
#         (Det[] the)
#         (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] songs))))))
# 1
# boys sing these songs
# (S[]
#   (N[BAR=2, NUM='pl']
#     (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] boys)))
#   (V[BAR=2, NUM='pl', TENSE='pres']
#     (V[BAR=1, NUM='pl', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='pl', SUBCAT='trans', TENSE='pres'] sing)
#       (N[BAR=2, NUM='pl']
#         (Det[NUM='pl'] these)
#         (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] songs))))))
# 1
# boys sang cars
# (S[]
#   (N[BAR=2, NUM='pl']
#     (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] boys)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, SUBCAT='trans', TENSE='past'] sang)
#       (N[BAR=2, NUM='pl']
#         (N[BAR=1, COUNT=?c, NUM='pl'] (N[BAR=0, NUM='pl'] cars))))))
# 1
# the water is precious
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -COUNT, NUM='sg'] (N[BAR=0, -COUNT, NUM='sg'] water)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='state', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='state', TENSE='pres'] is)
#       (ADJ[] precious))))
# 1
# water is precious
# (S[]
#   (N[BAR=2, NUM='sg']
#     (N[BAR=1, -COUNT, NUM='sg'] (N[BAR=0, -COUNT, NUM='sg'] water)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='state', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='state', TENSE='pres'] is)
#       (ADJ[] precious))))
# 1
# the boy says that the girl walks
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='clause', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='clause', TENSE='pres'] says)
#       (SBar[]
#         (Comp[] that)
#         (S[]
#           (N[BAR=2, NUM='sg']
#             (Det[] the)
#             (N[BAR=1, +COUNT, NUM='sg']
#               (N[BAR=0, +COUNT, NUM='sg'] girl)))
#           (V[BAR=2, NUM='sg', TENSE='pres']
#             (V[BAR=1, NUM='sg', SUBCAT='intrans', TENSE='pres']
#               (V[BAR=0, NUM='sg', SUBCAT='intrans', TENSE='pres']
#                 walks))))))))
# 1
# the boy in the car sees the girl with water on a bike
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, NUM='sg']
#       (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy))
#       (P[BAR=2]
#         (Prep[] in)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[] the)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] car))))))))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sees)
#       (N[BAR=2, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, NUM='sg']
#           (N[BAR=1, NUM='sg']
#             (N[BAR=1, +COUNT, NUM='sg']
#               (N[BAR=0, +COUNT, NUM='sg'] girl))
#             (P[BAR=2]
#               (Prep[] with)
#               (P[BAR=1]
#                 (P[BAR=0]
#                   (N[BAR=2, NUM='sg']
#                     (N[BAR=1, -COUNT, NUM='sg']
#                       (N[BAR=0, -COUNT, NUM='sg'] water)))))))
#           (P[BAR=2]
#             (Prep[] on)
#             (P[BAR=1]
#               (P[BAR=0]
#                 (N[BAR=2, NUM='sg']
#                   (Det[NUM='sg'] a)
#                   (N[BAR=1, +COUNT, NUM='sg']
#                     (N[BAR=0, +COUNT, NUM='sg'] bike)))))))))))
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, NUM='sg']
#       (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy))
#       (P[BAR=2]
#         (Prep[] in)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[] the)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] car))))))))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sees)
#       (N[BAR=2, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, NUM='sg']
#           (N[BAR=1, +COUNT, NUM='sg']
#             (N[BAR=0, +COUNT, NUM='sg'] girl))
#           (P[BAR=2]
#             (Prep[] with)
#             (P[BAR=1]
#               (P[BAR=0]
#                 (N[BAR=2, NUM='sg']
#                   (N[BAR=1, NUM='sg']
#                     (N[BAR=1, -COUNT, NUM='sg']
#                       (N[BAR=0, -COUNT, NUM='sg'] water))
#                     (P[BAR=2]
#                       (Prep[] on)
#                       (P[BAR=1]
#                         (P[BAR=0]
#                           (N[BAR=2, NUM='sg']
#                             (Det[NUM='sg'] a)
#                             (N[BAR=1, +COUNT, NUM='sg']
#                               (N[BAR=0, +COUNT, NUM='sg'] bike))))))))))))))))
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, NUM='sg']
#       (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy))
#       (P[BAR=2]
#         (Prep[] in)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[] the)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] car))))))))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', TENSE='pres']
#       (V[BAR=1, NUM='sg', TENSE='pres']
#         (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#           (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sees)
#           (N[BAR=2, NUM='sg']
#             (Det[] the)
#             (N[BAR=1, +COUNT, NUM='sg']
#               (N[BAR=0, +COUNT, NUM='sg'] girl))))
#         (P[BAR=2]
#           (Prep[] with)
#           (P[BAR=1]
#             (P[BAR=0]
#               (N[BAR=2, NUM='sg']
#                 (N[BAR=1, -COUNT, NUM='sg']
#                   (N[BAR=0, -COUNT, NUM='sg'] water)))))))
#       (P[BAR=2]
#         (Prep[] on)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[NUM='sg'] a)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] bike)))))))))
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, NUM='sg']
#       (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy))
#       (P[BAR=2]
#         (Prep[] in)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[] the)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] car))))))))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', TENSE='pres']
#       (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#         (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sees)
#         (N[BAR=2, NUM='sg']
#           (Det[] the)
#           (N[BAR=1, NUM='sg']
#             (N[BAR=1, +COUNT, NUM='sg']
#               (N[BAR=0, +COUNT, NUM='sg'] girl))
#             (P[BAR=2]
#               (Prep[] with)
#               (P[BAR=1]
#                 (P[BAR=0]
#                   (N[BAR=2, NUM='sg']
#                     (N[BAR=1, -COUNT, NUM='sg']
#                       (N[BAR=0, -COUNT, NUM='sg'] water)))))))))
#       (P[BAR=2]
#         (Prep[] on)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[NUM='sg'] a)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] bike)))))))))
# (S[]
#   (N[BAR=2, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, NUM='sg']
#       (N[BAR=1, +COUNT, NUM='sg'] (N[BAR=0, +COUNT, NUM='sg'] boy))
#       (P[BAR=2]
#         (Prep[] in)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (Det[] the)
#               (N[BAR=1, +COUNT, NUM='sg']
#                 (N[BAR=0, +COUNT, NUM='sg'] car))))))))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', TENSE='pres']
#       (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#         (V[BAR=0, NUM='sg', SUBCAT='trans', TENSE='pres'] sees)
#         (N[BAR=2, NUM='sg']
#           (Det[] the)
#           (N[BAR=1, +COUNT, NUM='sg']
#             (N[BAR=0, +COUNT, NUM='sg'] girl))))
#       (P[BAR=2]
#         (Prep[] with)
#         (P[BAR=1]
#           (P[BAR=0]
#             (N[BAR=2, NUM='sg']
#               (N[BAR=1, NUM='sg']
#                 (N[BAR=1, -COUNT, NUM='sg']
#                   (N[BAR=0, -COUNT, NUM='sg'] water))
#                 (P[BAR=2]
#                   (Prep[] on)
#                   (P[BAR=1]
#                     (P[BAR=0]
#                       (N[BAR=2, NUM='sg']
#                         (Det[NUM='sg'] a)
#                         (N[BAR=1, +COUNT, NUM='sg']
#                           (N[BAR=0, +COUNT, NUM='sg'] bike))))))))))))))
# 5

# 5 Modify the German grammar in 3.2 to incorporate the treatment of subcategorization presented in 3.

# % start S
# # Grammar Productions
# S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]
# NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
# NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
# VP[AGR=?a] -> V[SUBCAT=intrans, AGR=?a]
# VP[AGR=?a] -> V[SUBCAT=trans, OBJCASE=?c, AGR=?a] NP[CASE=?c]
# # Lexical Productions
# # Singular determiners
# # masc
# Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
# Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
# Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'
# # fem
# Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
# Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
# Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
# # Plural determiners
# Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
# Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
# Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'
# # Nouns
# N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Hund'
# N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
# N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunden'
# N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
# N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Katze'
# N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Katzen'
# # Pronouns
# PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
# PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
# PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
# PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
# PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
# PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
# PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
# PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
# PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
# PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'
# # Verbs
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=1]] -> 'komme'
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=2]] -> 'kommst'
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=3]] -> 'kommt'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=1]] -> 'kommen'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=2]] -> 'kommt'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=3]] -> 'kommen'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=1]] -> 'sehe' | 'mag'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=2]] -> 'siehst' | 'magst'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=3]] -> 'sieht' | 'mag'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=1]] -> 'folge' | 'helfe'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=3]] -> 'folgt' | 'hilft'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=1]] -> 'sehen' | 'moegen'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=2]] -> 'sieht' | 'moegt'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=3]] -> 'sehen' | 'moegen'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=1]] -> 'folgen' | 'helfen'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=2]] -> 'folgt' | 'helft'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=3]] -> 'folgen' | 'helfen'

# test_sent_against_grammar(sents=['ich folge den Katzen'.split(),
#                                  'ich folge den Katze'.split(),
#                                  'die Hunde kommen'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar05.fcfg')
# 
# ich folge den Katzen
# (S[]
#   (NP[AGR=[NUM='sg', PER=1], CASE='nom']
#     (PRO[AGR=[NUM='sg', PER=1], CASE='nom'] ich))
#   (VP[AGR=[NUM='sg', PER=1]]
#     (V[AGR=[NUM='sg', PER=1], OBJCASE='dat', SUBCAT='trans'] folge)
#     (NP[AGR=[GND='fem', NUM='pl', PER=3], CASE='dat']
#       (Det[AGR=[NUM='pl', PER=3], CASE='dat'] den)
#       (N[AGR=[GND='fem', NUM='pl', PER=3]] Katzen))))
# 1
# ich folge den Katze
# 0
# die Hunde kommen
# (S[]
#   (NP[AGR=[GND='masc', NUM='pl', PER=3], CASE='nom']
#     (Det[AGR=[NUM='pl', PER=3], CASE='nom'] die)
#     (N[AGR=[GND='masc', NUM='pl', PER=3], CASE='nom'] Hunde))
#   (VP[AGR=[NUM='pl', PER=3]]
#     (V[AGR=[NUM='pl', PER=3], SUBCAT='intrans'] kommen)))
# 1

# 6 Develop a feature based grammar that will correctly describe the following Spanish noun phrases:
#   (errors on page - sentences taken from the book, v1)
#   (59) un cuadro hermos-o
#   INDEF.SG.MASC picture beautiful-SG.MASC
#   ‘a beautiful picture’
#   (60) un-os cuadro-s hermos-os
#   INDEF-PL.MASC picture-PL beautiful-PL.MASC
#   ‘beautiful pictures’
#   (61) un-a cortina hermos-a
#   INDEF-SG.FEM curtain beautiful-SG.FEM
#   ‘a beautiful curtain’
#   (62) un-as cortina-s hermos-as
#   INDEF-PL.FEM curtain beautiful-PL.FEM
#   ‘beautiful curtains’

# % start NP
# # Grammar Productions
# NP -> Det[AGR=?a] N[AGR=?a] Adj[AGR=?a]
# NP -> Det[AGR=?a] Adj[AGR=?a] N[AGR=?a]
# NP -> Det[AGR=?a] N[AGR=?a]
# # Lexical Productions
# # Determiners
# Det[AGR=[GND=masc,NUM=sg]] -> 'un'
# Det[AGR=[GND=masc,NUM=pl]] -> 'unos'
# Det[AGR=[GND=fem,NUM=sg]] -> 'una'
# Det[AGR=[GND=fem,NUM=pl]] -> 'unas'
# # Nouns
# N[AGR=[GND=masc,NUM=sg]] -> 'cuadro'
# N[AGR=[GND=masc,NUM=pl]] -> 'cuadros'
# N[AGR=[GND=fem,NUM=sg]] -> 'cortina'
# N[AGR=[GND=fem,NUM=pl]] -> 'cortinas'
# # Adjectives
# Adj[AGR=[GND=masc,NUM=sg]] -> 'hermoso'
# Adj[AGR=[GND=masc,NUM=pl]] -> 'hermosos'
# Adj[AGR=[GND=fem,NUM=sg]] -> 'hermosa'
# Adj[AGR=[GND=fem,NUM=pl]] -> 'hermosas'
# 
# test_sent_against_grammar(sents=['un cuadro hermoso'.split(),
#                                  'unas cortinas hermosas'.split(),
#                                  'una cortina'.split(),
#                                  'unos hermosos cuadros'.split(),
#                                  'un cortinas hermosa'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar06.fcfg')
# 
# un cuadro hermoso
# (NP[]
#   (Det[AGR=[GND='masc', NUM='sg']] un)
#   (N[AGR=[GND='masc', NUM='sg']] cuadro)
#   (Adj[AGR=[GND='masc', NUM='sg']] hermoso))
# 1
# unas cortinas hermosas
# (NP[]
#   (Det[AGR=[GND='fem', NUM='pl']] unas)
#   (N[AGR=[GND='fem', NUM='pl']] cortinas)
#   (Adj[AGR=[GND='fem', NUM='pl']] hermosas))
# 1
# una cortina
# (NP[]
#   (Det[AGR=[GND='fem', NUM='sg']] una)
#   (N[AGR=[GND='fem', NUM='sg']] cortina))
# 1
# unos hermosos cuadros
# (NP[]
#   (Det[AGR=[GND='masc', NUM='pl']] unos)
#   (Adj[AGR=[GND='masc', NUM='pl']] hermosos)
#   (N[AGR=[GND='masc', NUM='pl']] cuadros))
# 1
# un cortinas hermosa
# 0

# 7 Develop your own version of the EarleyChartParser which only prints a trace if the input sequence fails to parse.

class TracingIncrementalChartParser(nltk.parse.chart.ChartParser):
    """
    An *incremental* chart parser implementing Jay Earley's
    parsing algorithm:
    | For each index end in [0, 1, ..., N]:
    |   For each edge such that edge.end = end:
    |     If edge is incomplete and edge.next is not a part of speech:
    |       Apply PredictorRule to edge
    |     If edge is incomplete and edge.next is a part of speech:
    |       Apply ScannerRule to edge
    |     If edge is complete:
    |       Apply CompleterRule to edge
    | Return any complete parses in the chart
    """
    def __init__(self, grammar, strategy=nltk.parse.earleychart.BU_LC_INCREMENTAL_STRATEGY,
                 trace=0, accumulate_trace=True, trace_chart_width=50,
                 chart_class=nltk.parse.earleychart.IncrementalChart):
        """
        Create a new Earley chart parser, that uses ``grammar`` to
        parse texts.
        :type grammar: CFG
        :param grammar: The grammar used to parse texts.
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            and higher numbers will produce more verbose tracing
            output.
        :type trace_chart_width: int
        :param trace_chart_width: The default total width reserved for
            the chart in trace output.  The remainder of each line will
            be used to display edges.
        :param chart_class: The class that should be used to create
            the charts used by this parser.
        """
        self._grammar = grammar
        self._trace = trace
        self._accumulate_trace = accumulate_trace
        self._trace_chart_width = trace_chart_width
        self._chart_class = chart_class
        self._axioms = []
        self._inference_rules = []
        for rule in strategy:
            if rule.NUM_EDGES == 0:
                self._axioms.append(rule)
            elif rule.NUM_EDGES == 1:
                self._inference_rules.append(rule)
            else:
                raise ValueError("Incremental inference rules must have "
                                 "NUM_EDGES == 0 or 1")
    def _trace_new_edges(self, chart, rule, new_edges, trace, edge_width):
        if not trace: return
        print_rule_header = trace > 1
        for edge in new_edges:
            if print_rule_header:
                if self._accumulate_trace:
                    self._trace_txt=self._trace_txt+'\n{}:'.format(rule)
                else:
                    print('%s:' % rule)
                print_rule_header = False
            if self._accumulate_trace:
                self._trace_txt=self._trace_txt+'\n'+chart.pretty_format_edge(edge, edge_width)
            else:
                print(chart.pretty_format_edge(edge, edge_width))
    def chart_parse(self, tokens, trace=None):
        self._trace_txt=''
        if trace is None: trace = self._trace
        trace_new_edges = self._trace_new_edges
        tokens = list(tokens)
        self._grammar.check_coverage(tokens)
        chart = self._chart_class(tokens)
        grammar = self._grammar
        # Width, for printing trace edges.
        trace_edge_width = self._trace_chart_width // (chart.num_leaves() + 1)
        if trace:
            if self._accumulate_trace:
                self._trace_txt=self._trace_txt+'\n'+chart.pretty_format_leaves(trace_edge_width)
            else:
                print(chart.pretty_format_leaves(trace_edge_width))
        for axiom in self._axioms:
            new_edges = list(axiom.apply(chart, grammar))
            trace_new_edges(chart, axiom, new_edges, trace, trace_edge_width)
        inference_rules = self._inference_rules
        for end in range(chart.num_leaves()+1):
            if trace > 1:
                if self._accumulate_trace:
                    self._trace_txt=self._trace_txt+"\n* Processing queue: {} \n".format(end)
                else:
                    print("\n* Processing queue: {} \n".format(end))
            agenda = list(chart.select(end=end))
            while agenda:
                edge = agenda.pop()
                for rule in inference_rules:
                    new_edges = list(rule.apply(chart, grammar, edge))
                    trace_new_edges(chart, rule, new_edges, trace, trace_edge_width)
                    for new_edge in new_edges:
                        if new_edge.end()==end:
                            agenda.append(new_edge)
        if self._accumulate_trace and len(list(chart.parses(grammar.start())))==0:
            print(self._trace_txt)
        return chart

class MyEarleyChartParser(TracingIncrementalChartParser):
    def __init__(self, grammar, **parser_args):
        TracingIncrementalChartParser.__init__(self, grammar, nltk.parse.earleychart.EARLEY_STRATEGY, **parser_args)
    pass

def ex07(grammar=nltk.parse.chart.demo_grammar(),
         sent='I saw John with a dog with my cookie'.split(),
         tr=0,acc=False,
         print_trees=True):
    parser=MyEarleyChartParser(grammar,trace=tr,accumulate_trace=acc)
    chart=parser.chart_parse(sent)
    parses=list(chart.parses(grammar.start()))
    num_trees=0
    for tree in parses:
        if print_trees:
            print(tree)
        num_trees=num_trees+1
    return num_trees

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='I saw John with a dog with my cookie'.split(),
#      tr=0,acc=False,
#      print_trees=True)
# 
# (S
#   (NP I)
#   (VP
#     (Verb saw)
#     (NP
#       (NP (NP John) (PP with (NP (Det a) (Noun dog))))
#       (PP with (NP (Det my) (Noun cookie))))))
# (S
#   (NP I)
#   (VP
#     (Verb saw)
#     (NP
#       (NP John)
#       (PP
#         with
#         (NP
#           (NP (Det a) (Noun dog))
#           (PP with (NP (Det my) (Noun cookie))))))))
# (S
#   (NP I)
#   (VP
#     (VP (VP (Verb saw) (NP John)) (PP with (NP (Det a) (Noun dog))))
#     (PP with (NP (Det my) (Noun cookie)))))
# (S
#   (NP I)
#   (VP
#     (VP (Verb saw) (NP (NP John) (PP with (NP (Det a) (Noun dog)))))
#     (PP with (NP (Det my) (Noun cookie)))))
# (S
#   (NP I)
#   (VP
#     (VP (Verb saw) (NP John))
#     (PP
#       with
#       (NP
#         (NP (Det a) (Noun dog))
#         (PP with (NP (Det my) (Noun cookie)))))))
# 5

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='I saw John with a dog with my cookie'.split(),
#      tr=1,acc=False,
#      print_trees=False)
# 
# |. I  .saw .John.with. a  .dog .with. my .cook.|
# |[----]    .    .    .    .    .    .    .    .| [0:1] 'I'
# |.    [----]    .    .    .    .    .    .    .| [1:2] 'saw'
# |.    .    [----]    .    .    .    .    .    .| [2:3] 'John'
# |.    .    .    [----]    .    .    .    .    .| [3:4] 'with'
# |.    .    .    .    [----]    .    .    .    .| [4:5] 'a'
# |.    .    .    .    .    [----]    .    .    .| [5:6] 'dog'
# |.    .    .    .    .    .    [----]    .    .| [6:7] 'with'
# |.    .    .    .    .    .    .    [----]    .| [7:8] 'my'
# |.    .    .    .    .    .    .    .    [----]| [8:9] 'cookie'
# |>    .    .    .    .    .    .    .    .    .| [0:0] S  -> * NP VP
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * NP PP
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * Det Noun
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * 'I'
# |[----]    .    .    .    .    .    .    .    .| [0:1] NP -> 'I' *
# |[---->    .    .    .    .    .    .    .    .| [0:1] S  -> NP * VP
# |[---->    .    .    .    .    .    .    .    .| [0:1] NP -> NP * PP
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * VP PP
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * Verb NP
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * Verb
# |.    >    .    .    .    .    .    .    .    .| [1:1] Verb -> * 'saw'
# |.    [----]    .    .    .    .    .    .    .| [1:2] Verb -> 'saw' *
# |.    [---->    .    .    .    .    .    .    .| [1:2] VP -> Verb * NP
# |.    [----]    .    .    .    .    .    .    .| [1:2] VP -> Verb *
# |[---------]    .    .    .    .    .    .    .| [0:2] S  -> NP VP *
# |.    [---->    .    .    .    .    .    .    .| [1:2] VP -> VP * PP
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * NP PP
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * Det Noun
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * 'John'
# |.    .    [----]    .    .    .    .    .    .| [2:3] NP -> 'John' *
# |.    [---------]    .    .    .    .    .    .| [1:3] VP -> Verb NP *
# |.    .    [---->    .    .    .    .    .    .| [2:3] NP -> NP * PP
# |.    .    .    >    .    .    .    .    .    .| [3:3] PP -> * 'with' NP
# |[--------------]    .    .    .    .    .    .| [0:3] S  -> NP VP *
# |.    [--------->    .    .    .    .    .    .| [1:3] VP -> VP * PP
# |.    .    .    [---->    .    .    .    .    .| [3:4] PP -> 'with' * NP
# |.    .    .    .    >    .    .    .    .    .| [4:4] NP -> * NP PP
# |.    .    .    .    >    .    .    .    .    .| [4:4] NP -> * Det Noun
# |.    .    .    .    >    .    .    .    .    .| [4:4] Det -> * 'a'
# |.    .    .    .    [----]    .    .    .    .| [4:5] Det -> 'a' *
# |.    .    .    .    [---->    .    .    .    .| [4:5] NP -> Det * Noun
# |.    .    .    .    .    >    .    .    .    .| [5:5] Noun -> * 'dog'
# |.    .    .    .    .    [----]    .    .    .| [5:6] Noun -> 'dog' *
# |.    .    .    .    [---------]    .    .    .| [4:6] NP -> Det Noun *
# |.    .    .    [--------------]    .    .    .| [3:6] PP -> 'with' NP *
# |.    .    .    .    [--------->    .    .    .| [4:6] NP -> NP * PP
# |.    .    .    .    .    .    >    .    .    .| [6:6] PP -> * 'with' NP
# |.    .    [-------------------]    .    .    .| [2:6] NP -> NP PP *
# |.    [------------------------]    .    .    .| [1:6] VP -> VP PP *
# |[-----------------------------]    .    .    .| [0:6] S  -> NP VP *
# |.    [------------------------>    .    .    .| [1:6] VP -> VP * PP
# |.    [------------------------]    .    .    .| [1:6] VP -> Verb NP *
# |.    .    [------------------->    .    .    .| [2:6] NP -> NP * PP
# |[-----------------------------]    .    .    .| [0:6] S  -> NP VP *
# |.    [------------------------>    .    .    .| [1:6] VP -> VP * PP
# |.    .    .    .    .    .    [---->    .    .| [6:7] PP -> 'with' * NP
# |.    .    .    .    .    .    .    >    .    .| [7:7] NP -> * NP PP
# |.    .    .    .    .    .    .    >    .    .| [7:7] NP -> * Det Noun
# |.    .    .    .    .    .    .    >    .    .| [7:7] Det -> * 'my'
# |.    .    .    .    .    .    .    [----]    .| [7:8] Det -> 'my' *
# |.    .    .    .    .    .    .    [---->    .| [7:8] NP -> Det * Noun
# |.    .    .    .    .    .    .    .    >    .| [8:8] Noun -> * 'cookie'
# |.    .    .    .    .    .    .    .    [----]| [8:9] Noun -> 'cookie' *
# |.    .    .    .    .    .    .    [---------]| [7:9] NP -> Det Noun *
# |.    .    .    .    .    .    [--------------]| [6:9] PP -> 'with' NP *
# |.    .    .    .    .    .    .    [--------->| [7:9] NP -> NP * PP
# |.    .    .    .    [------------------------]| [4:9] NP -> NP PP *
# |.    [---------------------------------------]| [1:9] VP -> VP PP *
# |.    .    [----------------------------------]| [2:9] NP -> NP PP *
# |.    [---------------------------------------]| [1:9] VP -> Verb NP *
# |.    .    [---------------------------------->| [2:9] NP -> NP * PP
# |[============================================]| [0:9] S  -> NP VP *
# |.    [--------------------------------------->| [1:9] VP -> VP * PP
# |[============================================]| [0:9] S  -> NP VP *
# |.    [--------------------------------------->| [1:9] VP -> VP * PP
# |.    .    .    [-----------------------------]| [3:9] PP -> 'with' NP *
# |.    .    .    .    [------------------------>| [4:9] NP -> NP * PP
# |.    .    [----------------------------------]| [2:9] NP -> NP PP *
# |.    [---------------------------------------]| [1:9] VP -> VP PP *
# 5

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='I saw John with a dog with my cookie'.split(),
#      tr=2,acc=False,
#      print_trees=False)
# 
# |. I  .saw .John.with. a  .dog .with. my .cook.|
# Leaf Init Rule:
# |[----]    .    .    .    .    .    .    .    .| [0:1] 'I'
# |.    [----]    .    .    .    .    .    .    .| [1:2] 'saw'
# |.    .    [----]    .    .    .    .    .    .| [2:3] 'John'
# |.    .    .    [----]    .    .    .    .    .| [3:4] 'with'
# |.    .    .    .    [----]    .    .    .    .| [4:5] 'a'
# |.    .    .    .    .    [----]    .    .    .| [5:6] 'dog'
# |.    .    .    .    .    .    [----]    .    .| [6:7] 'with'
# |.    .    .    .    .    .    .    [----]    .| [7:8] 'my'
# |.    .    .    .    .    .    .    .    [----]| [8:9] 'cookie'
# Top Down Init Rule:
# |>    .    .    .    .    .    .    .    .    .| [0:0] S  -> * NP VP
# 
# * Processing queue: 0 
# 
# Predictor Rule:
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * NP PP
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * Det Noun
# |>    .    .    .    .    .    .    .    .    .| [0:0] NP -> * 'I'
# 
# * Processing queue: 1 
# 
# Scanner Rule:
# |[----]    .    .    .    .    .    .    .    .| [0:1] NP -> 'I' *
# Completer Rule:
# |[---->    .    .    .    .    .    .    .    .| [0:1] S  -> NP * VP
# |[---->    .    .    .    .    .    .    .    .| [0:1] NP -> NP * PP
# Predictor Rule:
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * VP PP
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * Verb NP
# |.    >    .    .    .    .    .    .    .    .| [1:1] VP -> * Verb
# Predictor Rule:
# |.    >    .    .    .    .    .    .    .    .| [1:1] Verb -> * 'saw'
# 
# * Processing queue: 2 
# 
# Scanner Rule:
# |.    [----]    .    .    .    .    .    .    .| [1:2] Verb -> 'saw' *
# Completer Rule:
# |.    [---->    .    .    .    .    .    .    .| [1:2] VP -> Verb * NP
# |.    [----]    .    .    .    .    .    .    .| [1:2] VP -> Verb *
# Completer Rule:
# |[---------]    .    .    .    .    .    .    .| [0:2] S  -> NP VP *
# |.    [---->    .    .    .    .    .    .    .| [1:2] VP -> VP * PP
# Predictor Rule:
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * NP PP
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * Det Noun
# |.    .    >    .    .    .    .    .    .    .| [2:2] NP -> * 'John'
# 
# * Processing queue: 3 
# 
# Scanner Rule:
# |.    .    [----]    .    .    .    .    .    .| [2:3] NP -> 'John' *
# Completer Rule:
# |.    [---------]    .    .    .    .    .    .| [1:3] VP -> Verb NP *
# |.    .    [---->    .    .    .    .    .    .| [2:3] NP -> NP * PP
# Predictor Rule:
# |.    .    .    >    .    .    .    .    .    .| [3:3] PP -> * 'with' NP
# Completer Rule:
# |[--------------]    .    .    .    .    .    .| [0:3] S  -> NP VP *
# |.    [--------->    .    .    .    .    .    .| [1:3] VP -> VP * PP
# 
# * Processing queue: 4 
# 
# Scanner Rule:
# |.    .    .    [---->    .    .    .    .    .| [3:4] PP -> 'with' * NP
# Predictor Rule:
# |.    .    .    .    >    .    .    .    .    .| [4:4] NP -> * NP PP
# |.    .    .    .    >    .    .    .    .    .| [4:4] NP -> * Det Noun
# Predictor Rule:
# |.    .    .    .    >    .    .    .    .    .| [4:4] Det -> * 'a'
# 
# * Processing queue: 5 
# 
# Scanner Rule:
# |.    .    .    .    [----]    .    .    .    .| [4:5] Det -> 'a' *
# Completer Rule:
# |.    .    .    .    [---->    .    .    .    .| [4:5] NP -> Det * Noun
# Predictor Rule:
# |.    .    .    .    .    >    .    .    .    .| [5:5] Noun -> * 'dog'
# 
# * Processing queue: 6 
# 
# Scanner Rule:
# |.    .    .    .    .    [----]    .    .    .| [5:6] Noun -> 'dog' *
# Completer Rule:
# |.    .    .    .    [---------]    .    .    .| [4:6] NP -> Det Noun *
# Completer Rule:
# |.    .    .    [--------------]    .    .    .| [3:6] PP -> 'with' NP *
# |.    .    .    .    [--------->    .    .    .| [4:6] NP -> NP * PP
# Predictor Rule:
# |.    .    .    .    .    .    >    .    .    .| [6:6] PP -> * 'with' NP
# Completer Rule:
# |.    .    [-------------------]    .    .    .| [2:6] NP -> NP PP *
# |.    [------------------------]    .    .    .| [1:6] VP -> VP PP *
# Completer Rule:
# |[-----------------------------]    .    .    .| [0:6] S  -> NP VP *
# |.    [------------------------>    .    .    .| [1:6] VP -> VP * PP
# Completer Rule:
# |.    [------------------------]    .    .    .| [1:6] VP -> Verb NP *
# |.    .    [------------------->    .    .    .| [2:6] NP -> NP * PP
# Completer Rule:
# |[-----------------------------]    .    .    .| [0:6] S  -> NP VP *
# |.    [------------------------>    .    .    .| [1:6] VP -> VP * PP
# 
# * Processing queue: 7 
# 
# Scanner Rule:
# |.    .    .    .    .    .    [---->    .    .| [6:7] PP -> 'with' * NP
# Predictor Rule:
# |.    .    .    .    .    .    .    >    .    .| [7:7] NP -> * NP PP
# |.    .    .    .    .    .    .    >    .    .| [7:7] NP -> * Det Noun
# Predictor Rule:
# |.    .    .    .    .    .    .    >    .    .| [7:7] Det -> * 'my'
# 
# * Processing queue: 8 
# 
# Scanner Rule:
# |.    .    .    .    .    .    .    [----]    .| [7:8] Det -> 'my' *
# Completer Rule:
# |.    .    .    .    .    .    .    [---->    .| [7:8] NP -> Det * Noun
# Predictor Rule:
# |.    .    .    .    .    .    .    .    >    .| [8:8] Noun -> * 'cookie'
# 
# * Processing queue: 9 
# 
# Scanner Rule:
# |.    .    .    .    .    .    .    .    [----]| [8:9] Noun -> 'cookie' *
# Completer Rule:
# |.    .    .    .    .    .    .    [---------]| [7:9] NP -> Det Noun *
# Completer Rule:
# |.    .    .    .    .    .    [--------------]| [6:9] PP -> 'with' NP *
# |.    .    .    .    .    .    .    [--------->| [7:9] NP -> NP * PP
# Completer Rule:
# |.    .    .    .    [------------------------]| [4:9] NP -> NP PP *
# |.    [---------------------------------------]| [1:9] VP -> VP PP *
# |.    .    [----------------------------------]| [2:9] NP -> NP PP *
# Completer Rule:
# |.    [---------------------------------------]| [1:9] VP -> Verb NP *
# |.    .    [---------------------------------->| [2:9] NP -> NP * PP
# Completer Rule:
# |[============================================]| [0:9] S  -> NP VP *
# |.    [--------------------------------------->| [1:9] VP -> VP * PP
# Completer Rule:
# |[============================================]| [0:9] S  -> NP VP *
# |.    [--------------------------------------->| [1:9] VP -> VP * PP
# Completer Rule:
# |.    .    .    [-----------------------------]| [3:9] PP -> 'with' NP *
# |.    .    .    .    [------------------------>| [4:9] NP -> NP * PP
# Completer Rule:
# |.    .    [----------------------------------]| [2:9] NP -> NP PP *
# |.    [---------------------------------------]| [1:9] VP -> VP PP *
# 5

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='I saw John with a dog with my cookie'.split(),
#      tr=1,acc=True,
#      print_trees=False)
# 
# 5

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='I saw John with a dog with my cookie'.split(),
#      tr=2,acc=True,
#      print_trees=False)
# 
# 5

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='saw saw saw'.split(),
#      tr=0,acc=False,
#      print_trees=False)
# 
# 0

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='saw saw saw'.split(),
#      tr=1,acc=False,
#      print_trees=False)
# 
# |.    saw    .    saw    .    saw    .|
# |[-----------]           .           .| [0:1] 'saw'
# |.           [-----------]           .| [1:2] 'saw'
# |.           .           [-----------]| [2:3] 'saw'
# |>           .           .           .| [0:0] S  -> * NP VP
# |>           .           .           .| [0:0] NP -> * NP PP
# |>           .           .           .| [0:0] NP -> * Det Noun
# 0

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='saw saw saw'.split(),
#      tr=1,acc=True,
#      print_trees=False)
# 
# |.    saw    .    saw    .    saw    .|
# |[-----------]           .           .| [0:1] 'saw'
# |.           [-----------]           .| [1:2] 'saw'
# |.           .           [-----------]| [2:3] 'saw'
# |>           .           .           .| [0:0] S  -> * NP VP
# |>           .           .           .| [0:0] NP -> * NP PP
# |>           .           .           .| [0:0] NP -> * Det Noun

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='saw saw saw'.split(),
#      tr=2,acc=False,
#      print_trees=False)
# 
# |.    saw    .    saw    .    saw    .|
# Leaf Init Rule:
# |[-----------]           .           .| [0:1] 'saw'
# |.           [-----------]           .| [1:2] 'saw'
# |.           .           [-----------]| [2:3] 'saw'
# Top Down Init Rule:
# |>           .           .           .| [0:0] S  -> * NP VP
# 
# * Processing queue: 0 
# 
# Predictor Rule:
# |>           .           .           .| [0:0] NP -> * NP PP
# |>           .           .           .| [0:0] NP -> * Det Noun
# 
# * Processing queue: 1 
# 
# 
# * Processing queue: 2 
# 
# 
# * Processing queue: 3 
# 
# 0

# ex07(grammar=nltk.parse.chart.demo_grammar(),
#      sent='saw saw saw'.split(),
#      tr=2,acc=True,
#      print_trees=False)
# 
# |.    saw    .    saw    .    saw    .|
# Leaf Init Rule:
# |[-----------]           .           .| [0:1] 'saw'
# |.           [-----------]           .| [1:2] 'saw'
# |.           .           [-----------]| [2:3] 'saw'
# Top Down Init Rule:
# |>           .           .           .| [0:0] S  -> * NP VP
# * Processing queue: 0 
# 
# Predictor Rule:
# |>           .           .           .| [0:0] NP -> * NP PP
# |>           .           .           .| [0:0] NP -> * Det Noun
# * Processing queue: 1 
# 
# * Processing queue: 2 
# 
# * Processing queue: 3 
# 
# 0

# 8 Consider the feature structures shown in 6.1.
# fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
# fs2 = nltk.FeatStruct("[B = [D = d]]")
# fs3 = nltk.FeatStruct("[B = [C = d]]")
# fs4 = nltk.FeatStruct("[A = (1)[B = b], C->(1)]")
# fs5 = nltk.FeatStruct("[A = (1)[D = ?x], C = [E -> (1), F = ?x] ]")
# fs6 = nltk.FeatStruct("[A = [D = d]]")
# fs7 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
# fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
# fs9 = nltk.FeatStruct("[A = [B = b], C = [E = [G = e]]]")
# fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")
# Work out on paper what the result is of the following unifications. (Hint: you might find it useful to draw the graph structures.)
#   fs1 and fs2  - nltk.FeatStruct("[A = ?x, B= [C = ?x,D = d]]")
#   fs1 and fs3  - nltk.FeatStruct("[A = d, B= [C = d]]")
#   fs4 and fs5  - nltk.FeatStruct("[A = (1)[B = b, D = ?x, E -> (1), F = ?x], C->(1)]")
#   fs5 and fs6  - nltk.FeatStruct("[A = (1)[D = d], C = [E -> (1), F = d] ]")
#   fs5 and fs7  - None
#   fs8 and fs9  - nltk.FeatStruct("[A = (1)[D = e, G = e, B = b], C = [B = e, E -> (1)] ]")
#   fs8 and fs10 - nltk.FeatStruct("[A = (1)[D = b, G = b, B = b, E -> (1)], C -> (1) ]")
# Check your answers using Python.
# fs1.unify(fs2)==nltk.FeatStruct("[A = ?x, B= [C = ?x,D = d]]")
# True
# fs1.unify(fs3)==nltk.FeatStruct("[A = d, B= [C = d]]")
# True
# fs4.unify(fs5)==nltk.FeatStruct("[A = (1)[B = b, D = ?x, E -> (1), F = ?x], C->(1)]")
# True
# fs5.unify(fs6)==nltk.FeatStruct("[A = (1)[D = d], C = [E -> (1), F = d] ]")
# True
# fs5.unify(fs7)==None
# True
# fs8.unify(fs9)==nltk.FeatStruct("[A = (1)[D = e, G = e, B = b], C = [B = e, E -> (1)] ]")
# True
# fs8.unify(fs10)==nltk.FeatStruct("[A = (1)[D = b, G = b, B = b, E -> (1)], C -> (1) ]")

# 9 List two feature structures that subsume [A=?x, B=?x].

def ex09(fs1=nltk.FeatStruct("[A=?x]"), fs2=nltk.FeatStruct("[A=?x, B=?x]")):
    return subsumes(fs1, fs2)

# ex09(fs1=nltk.FeatStruct("[A=?x]"), fs2=nltk.FeatStruct("[A=?x, B=?x]"))
# True
# ex09(fs1=nltk.FeatStruct("[B=?x]"), fs2=nltk.FeatStruct("[A=?x, B=?x]"))
# True

# 10 Ignoring structure sharing, give an informal algorithm for unifying two feature structures.

# # Description
# # Naming convention
# A named node is a node of the type [A='a']
# A variable node is a node of the type [A=?x]
# A link node is a node of the type [A=(1)]
# A splitter node is a node of the type [A=[A='a', B='b']]
# A path is uniquely identified by a starting node and a path name
# # Process
# Set the current nodes to the root nodes of each structures.
# Example:
#     fs1=nltk.FeatStruct("[A=(1)[B=b],C->(1)]")
#     fs2=nltk.FeatStruct("[D=(1)[C=c],C->(1)]]")
#     fs2['C'] is a link to fs2['D'], and fs1['C'] is a link:
#         Make fs2=nltk.FeatStruct("[D->(1),C=(1)[C=c]]]")
# Current node is root node.
# Walk the paths of the second structure. If any of them ends on a link to a node at the current level
# and the same path is available on the first structure and also points to a link, swap link and linked on the second
# structure.
# For each of the paths of the current node of the second structure
# - If it is not present at the current node of the first structure
#     - Copy the complete subtree (down to the leaves and the links) to the current node of structure 1
# - If it is present at the current node of the first structure, check what the paths point to
#     - Named node and Named node
#         - If the names are the same
#             - Do nothing and continue
#         - If the names are not the same
#             - Return nothing and exit
#     - Named node and Variable node
#         - Assign the value to all nodes linked to the same variable on the tree where the variable is defined
#     - Named node and Link
#         - Return nothing and exit
#     - Named node and Splitter node
#         - Return nothing and exit
#     - Variable node and Variable node
#         - Rename one set of variables so that all are linked with the same one
#     - Variable node and Link
#         - Assign the link to all nodes linked to the same variable on the tree where the variable is defined
#     - Variable node and Splitter Node
#         - Copy the splitter node into the variable node and create links on all other nodes linked to the same variable 
#     - Link and Link
#         - There should be none
#     - Splitter node and Link
#         - Swap them (and then apply the 'Link and Splitter node' rule below
#         Example:
#             fs1=nltk.FeatStruct("[A=(1)[D=?x,G=?x],C=[B=?x,E->(1)]]
#             fs2=nltk.FeatStruct("[A=(1)[B = b],C->(1)]")
#             fs1['C'] is a spliter node and fs2['C'] is a link:
#                 Make
#                     fs1=nltk.FeatStruct("[A=(1)[D=?x,G=?x],C->(1)]
#                     fs2=nltk.FeatStruct("[A=(1)[B = b],C=[B=?x,E->(1)]]")
#     - Link and Splitter node
#         - Repeat this process setting the linked and splitter nodes as starting nodes
#     - Splitter node and Splitter node
#         - Repeat this process setting the two splitter nodes as starting nodes

# Non-recursive version. Works well for two level structures, but fails on more complex ones

def ex10_get_node_v1(fs,pos):
    try:
        return reduce(lambda d, k: d[k], pos, fs)
    except:
        return None

def ex10_set_node_v1(fs,pos,val):
    ex10_get_node_v1(fs,pos[:-1])[pos[-1]]=val

def ex10_get_node_type_v1(node):
    if not node:
        return None
    elif type(node)==dict:
        return 'S'
    elif node[0]=='V':
        return 'V'
    elif node[0]=='L':
        return 'L'
    else:
        return 'N'

def ex10_prepare_fss_v1(fs1,fs2):
    for key in fs2.keys():
        n_1=ex10_get_node_v1(fs1,[ key ])
        n_2=ex10_get_node_v1(fs2,[ key ])
        if ex10_get_node_type_v1(n_1)=='L' and \
           ex10_get_node_type_v1(n_2)=='L' and \
           len(n_2[2:])==1:
                n2_aux=ex10_get_node_v1(fs2,[ n_2[2:] ])
                ex10_set_node_v1(fs2,[ n_2[2:] ],'L '+key)
                ex10_set_node_v1(fs2,[ key ],n2_aux)
        elif ex10_get_node_type_v1(n_1)=='S' and \
             ex10_get_node_type_v1(n_2)=='L':
            ex10_set_node_v1(fs1,[ key ],n_2)
            ex10_set_node_v1(fs2,[ key ],n_1)
    return fs1, fs2

def ex10_extract_frontier_v1(fs,start=[]):
    frontier=[]
    for key in fs.keys():
        frontier=frontier + [ start + [ key ] ]
        if type(fs[key])==dict:
            frontier=frontier+ex10_extract_frontier_v1(fs[key], start + [ key ] )
    return frontier

def ex10_substitute_v1(fs,n_1,value):
    for key in fs.keys():
        if fs[key]==n_1:
            ex10_set_node_v1(fs,[key],value)
        elif type(fs[key])==dict:
            ex10_set_node_v1(fs,[key],ex10_substitute_v1(fs[key],n_1,value))
    return fs

def ex10_v1(fs1={'A':{'D':'V x', 'G':'V x'},'C':{'B':'V x','E':'L A'}},
         fs2={'A':{'B':'b'},'C':'L A'}):
    import copy
    fs1, fs2=ex10_prepare_fss_v1(copy.deepcopy(fs1),copy.deepcopy(fs2))
    frontier=ex10_extract_frontier_v1(fs2)
    ignore_lst=[]
    for node in frontier:
        if not sum([set(n).issubset(set(node)) for n in ignore_lst]):
            n_1=ex10_get_node_v1(fs1,node)
            n_2=ex10_get_node_v1(fs2,node)
            if not n_1:
                ex10_set_node_v1(fs1,node,n_2)
                ignore_lst=ignore_lst+[ node ]
            elif n_1<>n_2:
                type_n_1=ex10_get_node_type_v1(n_1)
                type_n_2=ex10_get_node_type_v1(n_2)
                type_nodes=set([ type_n_1, type_n_2 ])
                if type_nodes==set(['N', 'N']) or \
                   type_nodes==set(['N', 'L']) or \
                   type_nodes==set(['N', 'S']):
                    return None
                elif type_nodes==set(['N','V']) or \
                     type_nodes==set(['V','V']) or \
                     type_nodes==set(['V','L']):
                    if type_n_1=='V':
                        var=n_1
                        val=n_2
                    else:
                        var=n_2
                        val=n_1
                    ex10_substitute_v1(fs1,var,val)
                    ex10_substitute_v1(fs2,var,val)
                elif type_nodes==set(['V','S']):
                    if type_n_1=='V':
                        var=n_1
                        ex10_set_node_v1(fs1, node, n_2)
                    else:
                        var=n_2
                        ex10_set_node_v1(fs2, node, n_1)
                    ex10_substitute_v1(fs1,var,'L '+' '.join(node))
                    ex10_substitute_v1(fs2,var,'L '+' '.join(node))
                elif type_nodes==set(['L','S']):
                    fs1=ex10_v1(fs1, {n_1[2:]:n_2})
                    ignore_lst=ignore_lst+[ node ]
                elif type_nodes==set(['S','S']):
                    pass
    return fs1

# fs1  ={'A':'V x', 'B':{'C':'V x'}}
# fs2  ={'B':{'D':'d'}}
# fs3  ={'B':{'C':'d'}}
# fs4  ={'A':{'B':'b'},'C':'L A'}
# fs5  ={'A':{'D':'V x'},'C':{'E':'L A','F':'V x'}}
# fs6  ={'A':{'D':'d'}}
# fs7  ={'A':{'D':'d'}, 'C':{'F':{'D':'d'}}}
# fs8  ={'A':{'D':'V x', 'G':'V x'},'C':{'B':'V x','E':'L A'}}
# fs9  ={'A':{'B':'b'},'C':{'E':{'G':'e'}}}
# fs10 ={'A':{'B':'b'},'C':'L A'}
# #   fs1 and fs2  - nltk.FeatStruct("[A = ?x, B= [C = ?x,D = d]]")
# ex10_v1(fs1,fs2)
# {'A': 'V x', 'B': {'C': 'V x', 'D': {'D': 'd'}}}
# #   fs1 and fs3  - nltk.FeatStruct("[A = d, B= [C = d]]")
# ex10_v1(fs1,fs3)
# {'A': 'd', 'B': {'C': 'd'}}
# #   fs4 and fs5  - nltk.FeatStruct("[A = (1)[B = b, D = ?x, E -> (1), F = ?x], C->(1)]")
# ex10_v1(fs4,fs5)
# {'A': {'B': 'b', 'E': 'L A', 'D': 'V x', 'F': 'V x'}, 'C': 'L A'}
# #   fs5 and fs6  - nltk.FeatStruct("[A = (1)[D = d], C = [E -> (1), F = d] ]")
# ex10_v1(fs5,fs6)
# {'A': {'D': 'd'}, 'C': {'E': 'L A', 'F': 'd'}}
# #   fs5 and fs7  - None
# ex10_v1(fs5,fs7)
# None
# #   fs8 and fs9  - nltk.FeatStruct("[A = (1)[D = e, G = e, B = b], C = [B = e, E -> (1)] ]")
# ex10_v1(fs8,fs9)
# {'A': {'B': 'b', 'D': 'e', 'G': 'e'}, 'C': {'B': 'e', 'E': 'L A'}}
# #   fs8 and fs10 - nltk.FeatStruct("[A = (1)[D = b, G = b, B = b, E -> (1)], C -> (1) ]")
# ex10_v1(fs8,fs10)
# {'A': {'B': 'b', 'E': 'L A', 'D': 'b', 'G': 'b'}, 'C': 'L A'}

# fs101={'A':{'C':'c'}}
# fs102={'A':{'B':'L A'}}
# ex10_v1(fs101,fs102)
# {'A': {'C': 'c', 'B': 'L A'}}
# fs103={'A':{'B':'L A'},'D':{'E':'e'}}
# fs104={'A':{'B':{'C':'c'}},'D':'L A'}
# ex10_v1(fs103,fs104)
# {'A': {'C': 'c', 'B': 'L A', 'E': 'e'}, 'D': 'L A'}
# fs105={'A':{'B':'L A'},'D':{'E':'e'}}
# fs106={'A':{'B':{'C':'c'},'D':'L A'}}
# ex10_v1(fs105,fs106)
# {'A': {'C': 'c', 'B': 'L A', 'D': 'L A'}, 'D': {'E': 'e'}}
# fs107={'A':{'B':'b'},'C':'L A'}
# fs108={'D':{'E':'e'},'C':'L D'}
# ex10_v1(fs107,fs108)
# {'A': {'B': 'b', 'E': 'e'}, 'C': 'L A', 'D': 'L C'}

# Recursive version. Should work well all the time

def ex10_get_node_v2(fs,node):
    try:
        return reduce(lambda d, k: d[k], node, fs)
    except:
        return None

def ex10_set_node_v2(fs,node,val):
    ex10_get_node_v2(fs,node[:-1])[node[-1]]=val

def ex10_get_node_type_v2(node):
    if not node:
        return None
    elif type(node)==dict:
        return 'S'
    elif node[0]=='V':
        return 'V'
    elif node[0]=='L':
        return 'L'
    else:
        return 'N'

def ex10_prepare_node_v2(fs1,node1,fs2,node2):
    for key in ex10_get_node_v2(fs2,node2).keys():
        n_1=ex10_get_node_v2(fs1,node1 + [ key ])
        type_n_1=ex10_get_node_type_v2(n_1)
        n_2=ex10_get_node_v2(fs2,node2 + [ key ])
        type_n_2=ex10_get_node_type_v2(n_2)
        if type_n_1=='L' and \
           type_n_2=='L':
                n2_aux=ex10_get_node_v2(fs2,node2 + [ n_2[2:] ])
                ex10_set_node_v2(fs2,node2 + [ n_2[2:] ],'L '+key)
                ex10_set_node_v2(fs2,node2 + [ key ],n2_aux)
        elif type_n_1=='S' and \
             type_n_2=='L':
            ex10_set_node_v2(fs1,node1 + [ key ],n_2)
            ex10_set_node_v2(fs2,node2 + [ key ],n_1)

def ex10_substitute_v2(fs,node,value):
    for key in fs.keys():
        if fs[key]==node:
            ex10_set_node_v2(fs,[key],value)
        elif type(fs[key])==dict:
            ex10_set_node_v2(fs,[key],ex10_substitute_v2(fs[key],node,value))
    return fs

def ex10_unify_node(fs1,node1,fs2,node2):
    ex10_prepare_node_v2(fs1, node1, fs2, node2)
    for key in ex10_get_node_v2(fs2,node2).keys():
        n_1=ex10_get_node_v2(fs1,node1 + [ key ])
        type_n_1=ex10_get_node_type_v2(n_1)
        n_2=ex10_get_node_v2(fs2,node2 + [ key ])
        type_n_2=ex10_get_node_type_v2(n_2)
        type_nodes=set([type_n_1,type_n_2])
        if not n_1:
            ex10_set_node_v2(fs1,node1+[ key ],n_2)
        elif n_1<>n_2:
            if type_nodes==set(['N', 'N'])  or \
               type_nodes==set(['N', 'L']) or \
               type_nodes==set(['N', 'S']):
                return False
            elif type_nodes==set(['N','V']) or \
                 type_nodes==set(['V','V']) or \
                 type_nodes==set(['V','L']):
                if type_n_1=='V':
                    var=n_1
                    val=n_2
                else:
                    var=n_2
                    val=n_1
                ex10_substitute_v2(fs1,var,val)
                ex10_substitute_v2(fs2,var,val)
            elif type_nodes==set(['V','S']):
                if type_n_1=='V':
                    var=n_1
                    ex10_set_node_v2(fs1, node1+[ key ], n_2)
                else:
                    var=n_2
                    ex10_set_node_v2(fs2, node2+[ key ], n_1)
                ex10_substitute_v2(fs1,var,'L '+' '.join(node1+[ key ]))
                ex10_substitute_v2(fs2,var,'L '+' '.join(node2+[ key ]))
            elif type_nodes==set(['L','S']):
                if not ex10_unify_node(fs1, n_1[2:].split(), fs2, node2+[ key ]):
                    return False
            elif type_nodes==set(['S','S']):
                if not ex10_unify_node(fs1, node1+[ key ], fs2, node2+[ key ]):
                    return False
    return True
    
def ex10_v2(fs1={'A':{'D':'V x', 'G':'V x'},'C':{'B':'V x','E':'L A'}},
         fs2={'A':{'B':'b'},'C':'L A'}):
    import copy
    fs1=copy.deepcopy(fs1)
    fs2=copy.deepcopy(fs2)
    if ex10_unify_node(fs1,[],fs2,[]):
        return fs1

# fs1  ={'A':'V x', 'B':{'C':'V x'}}
# fs2  ={'B':{'D':'d'}}
# fs3  ={'B':{'C':'d'}}
# fs4  ={'A':{'B':'b'},'C':'L A'}
# fs5  ={'A':{'D':'V x'},'C':{'E':'L A','F':'V x'}}
# fs6  ={'A':{'D':'d'}}
# fs7  ={'A':{'D':'d'}, 'C':{'F':{'D':'d'}}}
# fs8  ={'A':{'D':'V x', 'G':'V x'},'C':{'B':'V x','E':'L A'}}
# fs9  ={'A':{'B':'b'},'C':{'E':{'G':'e'}}}
# fs10 ={'A':{'B':'b'},'C':'L A'}
# #   fs1 and fs2  - nltk.FeatStruct("[A = ?x, B= [C = ?x,D = d]]")
# ex10_v2(fs1,fs2)
# {'A': 'V x', 'B': {'C': 'V x', 'D': 'd'}}
# #   fs1 and fs3  - nltk.FeatStruct("[A = d, B= [C = d]]")
# ex10_v2(fs1,fs3)
# {'A': 'd', 'B': {'C': 'd'}}
# #   fs4 and fs5  - nltk.FeatStruct("[A = (1)[B = b, D = ?x, E -> (1), F = ?x], C->(1)]")
# ex10_v2(fs4,fs5)
# {'A': {'B': 'b', 'E': 'L A', 'D': 'V x', 'F': 'V x'}, 'C': 'L A'}  
# #   fs5 and fs6  - nltk.FeatStruct("[A = (1)[D = d], C = [E -> (1), F = d] ]")
# ex10_v2(fs5,fs6)
# {'A': {'D': 'd'}, 'C': {'E': 'L A', 'F': 'd'}}  
# #   fs5 and fs7  - None
# ex10_v2(fs5,fs7)
# None
# #   fs8 and fs9  - nltk.FeatStruct("[A = (1)[D = e, G = e, B = b], C = [B = e, E -> (1)] ]")
# ex10_v2(fs8,fs9)
# {'A': {'B': 'b', 'D': 'e', 'G': 'e'}, 'C': {'B': 'e', 'E': 'L A'}}
# #   fs8 and fs10 - nltk.FeatStruct("[A = (1)[D = b, G = b, B = b, E -> (1)], C -> (1) ]")
# ex10_v2(fs8,fs10)
# {'A': {'B': 'b', 'E': 'L A', 'D': 'b', 'G': 'b'}, 'C': 'L A'}
  
# fs101={'A':{'C':'c'}}
# fs102={'A':{'B':'L A'}}
# ex10_v2(fs101,fs102)
# {'A': {'C': 'c', 'B': 'L A'}}
# fs103={'A':{'B':'L A'},'D':{'E':'e'}}
# fs104={'A':{'B':{'C':'c'}},'D':'L A'}
# ex10_v2(fs103,fs104)
# {'A': {'C': 'c', 'B': 'L A', 'E': 'e'}, 'D': 'L A'}
# fs105={'A':{'B':'L A'},'D':{'E':'e'}}
# fs106={'A':{'B':{'C':'c'},'D':'L A'}}
# ex10_v2(fs105,fs106)
# {'A': {'C': 'c', 'B': 'L A', 'D': 'L A'}, 'D': {'E': 'e'}}
# fs107={'A':{'B':'b'},'C':'L A'}
# fs108={'D':{'E':'e'},'C':'L D'}
# ex10_v2(fs107,fs108)
# {'A': {'B': 'b', 'E': 'e'}, 'C': 'L A', 'D': 'L C'}

# 11 Extend the German grammar in 3.2 so that it can handle so-called verb-second structures like the following:
# (58) Heute sieht der Hund die Katze.

# % start S
# # Grammar Productions
# S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]
# S -> ADV V[SUBCAT=intrans, AGR=?a] NP[CASE=nom, AGR=?a]
# S -> ADV V[SUBCAT=trans, OBJCASE=?c, AGR=?a] NP[CASE=nom, AGR=?a] NP[CASE=?c]
# NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
# NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
# VP[AGR=?a] -> V[SUBCAT=intrans, AGR=?a]
# VP[AGR=?a] -> V[SUBCAT=intrans, AGR=?a] ADV
# VP[AGR=?a] -> V[SUBCAT=trans, OBJCASE=?c, AGR=?a] NP[CASE=?c]
# VP[AGR=?a] -> V[SUBCAT=trans, OBJCASE=?c, AGR=?a] ADV NP[CASE=?c]
# # Lexical Productions
# # Singular determiners
# # masc
# Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
# Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
# Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'
# # fem
# Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
# Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
# Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
# # Plural determiners
# Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
# Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
# Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'
# # Nouns
# N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Hund'
# N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
# N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunden'
# N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
# N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Katze'
# N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Katzen'
# # Pronouns
# PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
# PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
# PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
# PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
# PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
# PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
# PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
# PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
# PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
# PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'
# # Verbs
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=1]] -> 'komme'
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=2]] -> 'kommst'
# V[SUBCAT=intrans, AGR=[NUM=sg,PER=3]] -> 'kommt'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=1]] -> 'kommen'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=2]] -> 'kommt'
# V[SUBCAT=intrans, AGR=[NUM=pl, PER=3]] -> 'kommen'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=1]] -> 'sehe' | 'mag'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=2]] -> 'siehst' | 'magst'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=3]] -> 'sieht' | 'mag'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=1]] -> 'folge' | 'helfe'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=3]] -> 'folgt' | 'hilft'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=1]] -> 'sehen' | 'moegen'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=2]] -> 'sieht' | 'moegt'
# V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=3]] -> 'sehen' | 'moegen'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=1]] -> 'folgen' | 'helfen'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=2]] -> 'folgt' | 'helft'
# V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=3]] -> 'folgen' | 'helfen'
# # Adverbs
# ADV -> 'schnell' | 'heute'

# test_sent_against_grammar(sents=['heute sieht der Hund die Katze'.split(),
#                                  'der Hund sieht heute die Katze'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar11.fcfg')
# 
# heute sieht der Hund die Katze
# (S[]
#   (ADV[] heute)
#   (V[AGR=[NUM='sg', PER=3], OBJCASE='acc', SUBCAT='trans'] sieht)
#   (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='nom']
#     (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='nom'] der)
#     (N[AGR=[GND='masc', NUM='sg', PER=3]] Hund))
#   (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#     (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#     (N[AGR=[GND='fem', NUM='sg', PER=3]] Katze)))
# 1
# der Hund sieht heute die Katze
# (S[]
#   (NP[AGR=[GND='masc', NUM='sg', PER=3], CASE='nom']
#     (Det[AGR=[GND='masc', NUM='sg', PER=3], CASE='nom'] der)
#     (N[AGR=[GND='masc', NUM='sg', PER=3]] Hund))
#   (VP[AGR=[NUM='sg', PER=3]]
#     (V[AGR=[NUM='sg', PER=3], OBJCASE='acc', SUBCAT='trans'] sieht)
#     (ADV[] heute)
#     (NP[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc']
#       (Det[AGR=[GND='fem', NUM='sg', PER=3], CASE='acc'] die)
#       (N[AGR=[GND='fem', NUM='sg', PER=3]] Katze))))
# 1

# 12 Seemingly synonymous verbs have slightly different syntactic properties (Levin, 1993). Consider the patterns of
# grammaticality for the verbs loaded, filled, and dumped below. Can you write grammar productions to handle such data?
# (59)        
# a. The farmer loaded the cart with sand
# b. The farmer loaded sand into the cart
# c. The farmer filled the cart with sand
# d. *The farmer filled sand into the cart
# e. *The farmer dumped the cart with sand
# f. The farmer dumped sand into the cart

# % start S
# # ###################
# # Grammar Productions
# # ###################
# # S expansion productions
# S -> N[BAR=2, NUM=?n] V[BAR=2, NUM=?n]
# # NP expansion productions
# N[BAR=2, NUM=?n, IN=?i, CONT=?d] -> PropN[NUM=?n, IN=?i, CONT=?d]
# N[BAR=2, NUM=?n, IN=?i, CONT=?d] -> Det[NUM=?n] N[BAR=1, NUM=?n, IN=?i, CONT=?d]
# N[BAR=2, NUM=sg, IN=?i, CONT=?d] -> N[BAR=1, NUM=sg, -COUNT, IN=?i, CONT=?d]
# N[BAR=2, NUM=pl, IN=?i, CONT=?d] -> N[BAR=1, NUM=pl, IN=?i, CONT=?d]
# N[BAR=1, NUM=?n, IN=?i, CONT=?d] -> N[BAR=1, NUM=?n, IN=?i, CONT=?d] P[BAR=2]
# N[BAR=1, NUM=sg, -COUNT, IN=?i, CONT=?d] -> N[BAR=0, NUM=sg, -COUNT, IN=?i, CONT=?d]
# N[BAR=1, NUM=?n, COUNT=?c, IN=?i, CONT=?d] -> N[BAR=0, NUM=?n, COUNT=?c, IN=?i, CONT=?d]
# # VP expansion productions
# V[BAR=2, TENSE=?t, NUM=?n] -> V[BAR=1, TENSE=?t, NUM=?n]
# V[BAR=1, TENSE=?t, NUM=?n] -> V[BAR=1, TENSE=?t, NUM=?n] P[BAR=2]
# V[BAR=1, SUBCAT=intrans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=intrans, TENSE=?t, NUM=?n]
# V[BAR=1, SUBCAT=trans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=trans, -IN, TENSE=?t, NUM=?n] N[BAR=2]
# V[BAR=1, SUBCAT=trans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=trans, +IN, +CONT, TENSE=?t, NUM=?n] N[BAR=2, +IN, +CONT] Prep[+IN, +CONT] N[BAR=2, +IN, -CONT]
# V[BAR=1, SUBCAT=trans, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=trans, +IN, -CONT, TENSE=?t, NUM=?n] N[BAR=2, +IN, -CONT] Prep[+IN, -CONT] N[BAR=2, +IN, +CONT]
# V[BAR=1, SUBCAT=state, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=state, TENSE=?t, NUM=?n] ADJ
# V[BAR=1, SUBCAT=clause, TENSE=?t, NUM=?n] -> V[BAR=0, SUBCAT=clause, TENSE=?t, NUM=?n] SBar
# # PP expansion productions
# P[BAR=2, IN=?i, CONT=?d] -> Prep[IN=?i, CONT=?d] P[BAR=1, IN=?i, CONT=?d]
# P[BAR=1, IN=?i, CONT=?d] -> P[BAR=0, IN=?i, CONT=?d]
# P[BAR=0, IN=?i, CONT=?d] -> N[BAR=2, IN=?i, CONT=?d]
# SBar -> Comp S
# # ###################
# # Lexical Productions
# # ###################
# Det[NUM=sg] -> 'this' | 'every' | 'a'
# Det[NUM=pl] -> 'these' | 'all'
# Det -> 'the' | 'some' | 'several'
# PropN[NUM=sg]-> 'Kim' | 'Jody'
# N[BAR=0, NUM=sg, +COUNT, -CONT] -> 'dog' | 'girl' | 'car' | 'child' | 'boy' | 'song' | 'bike' | 'farmer'
# N[BAR=0, NUM=sg, +COUNT, +CONT] -> 'farmer' | 'cart'
# N[BAR=0, NUM=sg, -COUNT, -CONT] -> 'water' | 'dirt' | 'sand' | 'joy'
# N[BAR=0, NUM=pl, -CONT] -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys' | 'songs' | 'farmers'
# N[BAR=0, NUM=pl, +CONT] -> 'farmers' | 'carts'
# V[BAR=0, SUBCAT=intrans, TENSE=pres,  NUM=sg] -> 'disappears' | 'walks'
# V[BAR=0, SUBCAT=trans, -IN, TENSE=pres, NUM=sg] -> 'sees' | 'likes' | 'sings'
# V[BAR=0, SUBCAT=trans, +IN, +CONT, TENSE=pres, NUM=sg] -> 'fills' | 'loads'
# V[BAR=0, SUBCAT=trans, +IN, -CONT, TENSE=pres, NUM=sg] -> 'loads' | 'dumps'
# V[BAR=0, SUBCAT=state, TENSE=pres, NUM=sg] -> 'is' | 'seems'
# V[BAR=0, SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'thinks' | 'claims'
# V[BAR=0, SUBCAT=intrans, TENSE=pres,  NUM=pl] -> 'disappear' | 'walk'
# V[BAR=0, SUBCAT=trans, -IN, TENSE=pres, NUM=pl] -> 'see' | 'like' | 'sing'
# V[BAR=0, SUBCAT=trans, +IN, +CONT, TENSE=pres, NUM=pl] -> 'fill' | 'load'
# V[BAR=0, SUBCAT=trans, +IN, -CONT, TENSE=pres, NUM=pl] -> 'load' | 'dump'
# V[BAR=0, SUBCAT=state, TENSE=pres, NUM=pl] -> 'are' | 'seem'
# V[BAR=0, SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'think' | 'claim'
# V[BAR=0, SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
# V[BAR=0, SUBCAT=trans, -IN, TENSE=past] -> 'saw' | 'liked' | 'sang'
# V[BAR=0, SUBCAT=trans, +IN, +CONT, TENSE=past] -> 'filled' | 'loaded'
# V[BAR=0, SUBCAT=trans, +IN, -CONT, TENSE=past] -> 'loaded' | 'dumped'
# V[BAR=0, SUBCAT=state, TENSE=past] -> 'were' | 'seemed'
# V[BAR=0, SUBCAT=clause, TENSE=past] -> 'said' | 'thought' | 'claimed'
# Prep[-IN] -> 'with' | 'by' | 'on' | 'in' | 'into'
# Prep[+IN, +CONT] -> 'with'
# Prep[+IN, -CONT] -> 'into'
# ADJ -> 'precious' | 'happy'
# Comp -> 'that'

# test_sent_against_grammar(sents=['the boy sings a song'.split(),
#                                  'boys sing songs'.split(),
#                                  'boy sings a song'.split(),
#                                  'water is precious'.split(),
#                                  'the boy says that the girl walks'.split(),
#                                  'the farmer loaded the cart with sand'.split(),
#                                  'the farmer loaded sand into the cart'.split(),
#                                  'girls fill the farmer with joy'.split(),
#                                  'the farmer filled sand into the cart'.split(),
#                                  'the farmer dumped the cart with sand'.split(),
#                                  'the farmer dumped sand into the cart'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar12.fcfg')
# 
# the boy sings a song
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, +COUNT, NUM='sg'] boy)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, -IN, NUM='sg', SUBCAT='trans', TENSE='pres'] sings)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (Det[NUM='sg'] a)
#         (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, +COUNT, NUM='sg'] song))))))
# 1
# boys sing songs
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='pl']
#     (N[BAR=1, -CONT, COUNT=?c, IN=?i, NUM='pl']
#       (N[BAR=0, -CONT, NUM='pl'] boys)))
#   (V[BAR=2, NUM='pl', TENSE='pres']
#     (V[BAR=1, NUM='pl', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, -IN, NUM='pl', SUBCAT='trans', TENSE='pres'] sing)
#       (N[BAR=2, -CONT, IN=?i, NUM='pl']
#         (N[BAR=1, -CONT, COUNT=?c, IN=?i, NUM='pl']
#           (N[BAR=0, -CONT, NUM='pl'] songs))))))
# 1
# boy sings a song
# 0
# water is precious
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, -COUNT, NUM='sg'] water)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='state', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='state', TENSE='pres'] is)
#       (ADJ[] precious))))
# 1
# the boy says that the girl walks
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, +COUNT, NUM='sg'] boy)))
#   (V[BAR=2, NUM='sg', TENSE='pres']
#     (V[BAR=1, NUM='sg', SUBCAT='clause', TENSE='pres']
#       (V[BAR=0, NUM='sg', SUBCAT='clause', TENSE='pres'] says)
#       (SBar[]
#         (Comp[] that)
#         (S[]
#           (N[BAR=2, -CONT, IN=?i, NUM='sg']
#             (Det[] the)
#             (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#               (N[BAR=0, -CONT, +COUNT, NUM='sg'] girl)))
#           (V[BAR=2, NUM='sg', TENSE='pres']
#             (V[BAR=1, NUM='sg', SUBCAT='intrans', TENSE='pres']
#               (V[BAR=0, NUM='sg', SUBCAT='intrans', TENSE='pres']
#                 walks))))))))
# 1
# the farmer loaded the cart with sand
# (S[]
#   (N[BAR=2, +CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, +CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, +CONT, +IN, SUBCAT='trans', TENSE='past'] loaded)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart)))
#       (Prep[+CONT, +IN] with)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand))))))
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, +CONT, +IN, SUBCAT='trans', TENSE='past'] loaded)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart)))
#       (Prep[+CONT, +IN] with)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand))))))
# 2
# the farmer loaded sand into the cart
# (S[]
#   (N[BAR=2, +CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, +CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, -CONT, +IN, SUBCAT='trans', TENSE='past'] loaded)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand)))
#       (Prep[-CONT, +IN] into)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart))))))
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, -CONT, +IN, SUBCAT='trans', TENSE='past'] loaded)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand)))
#       (Prep[-CONT, +IN] into)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart))))))
# 2
# girls fill the farmer with joy
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='pl']
#     (N[BAR=1, -CONT, COUNT=?c, IN=?i, NUM='pl']
#       (N[BAR=0, -CONT, NUM='pl'] girls)))
#   (V[BAR=2, NUM='pl', TENSE='pres']
#     (V[BAR=1, NUM='pl', SUBCAT='trans', TENSE='pres']
#       (V[BAR=0, +CONT, +IN, NUM='pl', SUBCAT='trans', TENSE='pres']
#         fill)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] farmer)))
#       (Prep[+CONT, +IN] with)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] joy))))))
# 1
# the farmer filled sand into the cart
# 0
# the farmer dumped the cart with sand
# 0
# the farmer dumped sand into the cart
# (S[]
#   (N[BAR=2, +CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, +CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, -CONT, +IN, SUBCAT='trans', TENSE='past'] dumped)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand)))
#       (Prep[-CONT, +IN] into)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart))))))
# (S[]
#   (N[BAR=2, -CONT, IN=?i, NUM='sg']
#     (Det[] the)
#     (N[BAR=1, -CONT, +COUNT, IN=?i, NUM='sg']
#       (N[BAR=0, -CONT, +COUNT, NUM='sg'] farmer)))
#   (V[BAR=2, NUM=?n, TENSE='past']
#     (V[BAR=1, NUM=?n, SUBCAT='trans', TENSE='past']
#       (V[BAR=0, -CONT, +IN, SUBCAT='trans', TENSE='past'] dumped)
#       (N[BAR=2, -CONT, IN=?i, NUM='sg']
#         (N[BAR=1, -CONT, -COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, -CONT, -COUNT, NUM='sg'] sand)))
#       (Prep[-CONT, +IN] into)
#       (N[BAR=2, +CONT, IN=?i, NUM='sg']
#         (Det[] the)
#         (N[BAR=1, +CONT, +COUNT, IN=?i, NUM='sg']
#           (N[BAR=0, +CONT, +COUNT, NUM='sg'] cart))))))
# 2

# 13 Morphological paradigms are rarely completely regular, in the sense of every cell in the matrix having a different
# realization. For example, the present tense conjugation of the lexeme walk only has two distinct forms: walks for the
# 3rd person singular, and walk for all other combinations of person and number. A successful analysis should not require
# redundantly specifying that 5 out of the 6 possible morphological combinations have the same realization.
# Propose and implement a method for dealing with this.

# % start S
# # ###################
# # Grammar Productions
# # ###################
# 
# # S expansion productions
# S -> NP[AGR=?n] VP[-REG, AGR=?n]
# S -> NP[REG_L=?m] VP[+REG, REG_L=?m]
# 
# # NP expansion productions
# NP[REG_L=?m, AGR=?n] -> PN[REG_L=?m, AGR=?n]
# 
# # VP expansion productions
# VP[REG=?r, REG_L=?l, AGR=?n] -> V[REG=?r, REG_L=?l, AGR=?n] ADJ
# VP[REG=?r, REG_L=?l, AGR=?n] -> V[REG=?r, REG_L=?l, AGR=?n] ADV
# # ###################
# # Lexical Productions
# # ###################
# 
# PN[REG_L=1, AGR=[NUM=SG, PERS=1]] -> 'I'
# PN[REG_L=1, AGR=[NUM=SG, PERS=2]] -> 'You'
# PN[REG_L=2, AGR=[NUM=SG, PERS=3]] -> 'He' | 'She' | 'It'
# PN[REG_L=1, AGR=[NUM=PL]] -> 'We' | 'You' | 'They'
# V[-REG, AGR=[NUM=SG, PERS=1]] -> 'am'
# V[-REG, AGR=[NUM=SG, PERS=2]] -> 'are'
# V[-REG, AGR=[NUM=SG, PERS=3]] -> 'is'
# V[-REG, AGR=[NUM=PL]] -> 'are'
# V[+REG, REG_L=1] -> 'walk'
# V[+REG, REG_L=2] -> 'walks'
# ADJ -> 'happy'
# ADV -> 'quickly'

# test_sent_against_grammar(sents=['I am happy'.split(),
#                                  'You are happy'.split(),
#                                  'I are happy'.split(),
#                                  'He walks quickly'.split(),
#                                  'We walk quickly'.split(),
#                                  'He walk quickly'.split()],
#                           grammar='/home/ggomarr/eclipse/projects/Natural Language Tool Kit/001 Aux/grammars/grammar13.fcfg')
# 
# I am happy
# (S[]
#   (NP[AGR=[NUM='SG', PERS=1], REG_L=1]
#     (PN[AGR=[NUM='SG', PERS=1], REG_L=1] I))
#   (VP[AGR=[NUM='SG', PERS=1], -REG, REG_L=?l]
#     (V[AGR=[NUM='SG', PERS=1], -REG] am)
#     (ADJ[] happy)))
# 1
# You are happy
# (S[]
#   (NP[AGR=[NUM='SG', PERS=2], REG_L=1]
#     (PN[AGR=[NUM='SG', PERS=2], REG_L=1] You))
#   (VP[AGR=[NUM='SG', PERS=2], -REG, REG_L=?l]
#     (V[AGR=[NUM='SG', PERS=2], -REG] are)
#     (ADJ[] happy)))
# (S[]
#   (NP[AGR=[NUM='PL'], REG_L=1] (PN[AGR=[NUM='PL'], REG_L=1] You))
#   (VP[AGR=[NUM='PL'], -REG, REG_L=?l]
#     (V[AGR=[NUM='PL'], -REG] are)
#     (ADJ[] happy)))
# 2
# I are happy
# 0
# He walks quickly
# (S[]
#   (NP[AGR=[NUM='SG', PERS=3], REG_L=2]
#     (PN[AGR=[NUM='SG', PERS=3], REG_L=2] He))
#   (VP[AGR=?n, +REG, REG_L=2]
#     (V[+REG, REG_L=2] walks)
#     (ADV[] quickly)))
# 1
# We walk quickly
# (S[]
#   (NP[AGR=[NUM='PL'], REG_L=1] (PN[AGR=[NUM='PL'], REG_L=1] We))
#   (VP[AGR=?n, +REG, REG_L=1] (V[+REG, REG_L=1] walk) (ADV[] quickly)))
# 1
# He walk quickly
# 0

# 14 So-called head features are shared between the parent node and head child. For example, TENSE is a head feature
# that is shared between a VP and its head V child. See (Gazdar, Klein, & and, 1985) for more details. Most of the
# features we have looked at are head features — exceptions are SUBCAT and SLASH. Since the sharing of head features
# is predictable, it should not need to be stated explicitly in the grammar productions. Develop an approach that
# automatically accounts for this regular behavior of head features.

# Version with a chart parser

def ex14_init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[(set(),) for i in range(numtokens+1)] for _ in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        for production in productions:
            aux_prod=production.lhs()
            aux_head=aux_prod['HEAD']
            wfst[i][i][0].add(aux_prod)
            if grammar.productions(rhs=aux_prod):
                while len(grammar.productions(rhs=aux_prod)[0].rhs())==1:
                    aux_prod=grammar.productions(rhs=aux_prod)[0]
                    aux_prod['HEAD']=aux_head
                    wfst[i][i][0].add(aux_prod)
            wfst[i][i]=wfst[i][i] + ([tokens[i]],)
    return wfst

def ex14_construct_dicts(grammar):
    import collections
    dict_grammar_rules=collections.defaultdict(set)
    dict_head_evelation_rules=dict()
    for production in grammar.productions():
        if type(production.rhs()[0])==nltk.grammar.FeatStructNonterminal:
            key=tuple([ nltk.grammar.FeatStructNonterminal(elem[nltk.Feature('type')]) for elem in production.rhs() ])
            head_elevation_lst=[True if elem.has_key('H') else False for elem in production.rhs()]
            if sum(head_elevation_lst):
                dict_head_evelation_rules[key]=head_elevation_lst.index(True)
        else:
            key=production.rhs()
        val_dict_g=production.lhs()
        dict_grammar_rules[key].add(val_dict_g)
    return dict_grammar_rules, dict_head_evelation_rules

def ex14_complete_wfst(wfst, tokens, grammar):
    import itertools
    dict_grammar_rules, head_elevation_rules = ex14_construct_dicts(grammar)
    numtokens = len(tokens)
    for span in range(1,numtokens):
        for start in range(numtokens-span):
            end = start + span
            for mid in range(start, end):
                nt_s_lst = [ wfst[start][mid][0], wfst[mid+1][end][0] ]
                for aux_key in itertools.product(nt_s_lst[0],nt_s_lst[1]):
                    key=(nltk.grammar.FeatStructNonterminal(aux_key[0][nltk.Feature('type')]),nltk.grammar.FeatStructNonterminal(aux_key[1][nltk.Feature('type')]))
                    if key in dict_grammar_rules.keys():
                        head_union = aux_key[0]['HEAD'].unify(aux_key[1]['HEAD'])
                        if head_union:
                            for rule in dict_grammar_rules[key]:
                                aux_prod=rule.copy(True)
                                if key in head_elevation_rules.keys():
                                    aux_prod['HEAD']=aux_key[head_elevation_rules[key]]['HEAD']
                                else:
                                    aux_prod['HEAD']=head_union
                                wfst[start][end][0].add(aux_prod)
                            wfst[start][end]=wfst[start][end]+([(start,mid),(mid+1,end)],)
    return wfst

def ex14_display(wfst):
    print('WFST ' + ' '.join(("%-12d" % i) for i in range(len(wfst)-1)))
    for i in range(len(wfst)-1):
        print("%-4d" % i),
        for j in range(len(wfst)-1):
            print("%-12s" % (wfst[i][j][0] or '.')),
        print('')

def ex14_wfst_to_tree(wfst,start_node=None):
    if not start_node:
        start_node=(0,len(wfst)-2)
    if wfst[start_node[0]][start_node[1]][0]:
        tree=nltk.Tree(list(wfst[start_node[0]][start_node[1]][0]),[])
        if len(wfst[start_node[0]][start_node[1]][1])==1:
            tree.append(wfst[start_node[0]][start_node[1]][1][0])
            return tree
        else:
            for leave in wfst[start_node[0]][start_node[1]][1]:
                tree.append(ex14_wfst_to_tree(wfst,leave))
            return tree

def ex14(grammar="""
                    % start S
                    # ###################
                    # Grammar Productions
                    # ###################
                    # S expansion productions
                    S -> NP VP
                    # NP expansion productions
                    NP -> PN
                    NP -> Det N
                    NP -> NP PP
                    # VP expansion productions
                    VP -> V Adj
                    VP -> VP PP
                    # PP expansion productions
                    PP -> Prep[+H] NP
                    # Lexical productions
                    Det[HEAD=[NUM=sg]]        -> 'this' | 'every' | 'a'
                    Det[HEAD=[NUM=pl]]        -> 'these' | 'all'
                    Det[HEAD=[]]              -> 'the' | 'some' | 'several'
                    PN[HEAD=[NUM=sg, PERS=1]] -> 'I'
                    PN[HEAD=[NUM=sg, PERS=2]] -> 'you'
                    PN[HEAD=[NUM=sg, PERS=3]] -> 'he' | 'she' | 'it'
                    PN[HEAD=[NUM=pl, PERS=1]] -> 'we'
                    PN[HEAD=[NUM=pl, PERS=2]] -> 'you'
                    PN[HEAD=[NUM=pl, PERS=3]] -> 'they'
                    N[HEAD=[NUM=sg, PERS=3]]  -> 'dog' | 'girl' | 'car' | 'child' | 'boy' | 'song' | 'bike'
                    N[HEAD=[NUM=pl, PERS=3]]  -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys' | 'songs'
                    V[HEAD=[NUM=sg , PERS=1]] -> 'am'
                    V[HEAD=[NUM=sg , PERS=2]] -> 'are'
                    V[HEAD=[NUM=sg , PERS=3]] -> 'is'
                    V[HEAD=[NUM=pl]]          -> 'are'
                    Adj[HEAD=[]]              -> 'happy' | 'beautiful'
                    Prep[HEAD=[]]             -> 'with' | 'by' | 'on' | 'in'""",
         sent="the girl on the car is beautiful".split()):
    fcfg_grammar=nltk.grammar.FeatureGrammar.fromstring(grammar)
    wfst=ex14_init_wfst(sent, fcfg_grammar)
    return ex14_complete_wfst(wfst, sent, fcfg_grammar)

# print(ex14_wfst_to_tree(ex14(sent="the girl on the car is happy with the dog".split())))
# ([S[HEAD=[NUM='sg', PERS=3]]]
#   ([NP[HEAD=[NUM='sg', PERS=3]]]
#     ([NP[HEAD=[NUM='sg', PERS=3]]]
#       ([Det[HEAD=[]]] the)
#       ([N[HEAD=[NUM='sg', PERS=3]]] girl))
#     ([PP[HEAD=[]]]
#       ([Prep[HEAD=[]]] on)
#       ([NP[HEAD=[NUM='sg', PERS=3]]]
#         ([Det[HEAD=[]]] the)
#         ([N[HEAD=[NUM='sg', PERS=3]]] car))))
#   ([VP[HEAD=[NUM='sg', PERS=3]]]
#     ([VP[HEAD=[NUM='sg', PERS=3]]]
#       ([V[HEAD=[NUM='sg', PERS=3]]] is)
#       ([Adj[HEAD=[]]] happy))
#     ([PP[HEAD=[]]]
#       ([Prep[HEAD=[]]] with)
#       ([NP[HEAD=[NUM='sg', PERS=3]]]
#         ([Det[HEAD=[]]] the)
#         ([N[HEAD=[NUM='sg', PERS=3]]] dog)))))
# print(ex14_wfst_to_tree(ex14(sent='the girl on the car are happy with the dog'.split())))
# None
# print(ex14_wfst_to_tree(ex14(sent='the girl by the cars is happy'.split())))
# ([S[HEAD=[NUM='sg', PERS=3]]]
#   ([NP[HEAD=[NUM='sg', PERS=3]]]
#     ([NP[HEAD=[NUM='sg', PERS=3]]]
#       ([Det[HEAD=[]]] the)
#       ([N[HEAD=[NUM='sg', PERS=3]]] girl))
#     ([PP[HEAD=[]]]
#       ([Prep[HEAD=[]]] by)
#       ([NP[HEAD=[NUM='pl', PERS=3]]]
#         ([Det[HEAD=[]]] the)
#         ([N[HEAD=[NUM='pl', PERS=3]]] cars))))
#   ([VP[HEAD=[NUM='sg', PERS=3]]]
#     ([V[HEAD=[NUM='sg', PERS=3]]] is)
#     ([Adj[HEAD=[]]] happy)))
# print(ex14_wfst_to_tree(ex14(sent='the girls are happy'.split())))
# ([S[HEAD=[NUM='pl', PERS=3]]]
#   ([NP[HEAD=[NUM='pl', PERS=3]]]
#     ([Det[HEAD=[]]] the)
#     ([N[HEAD=[NUM='pl', PERS=3]]] girls))
#   ([VP[HEAD=[NUM='sg', PERS=2]], VP[HEAD=[NUM='pl']]]
#     ([V[HEAD=[NUM='sg', PERS=2]], V[HEAD=[NUM='pl']]] are)
#     ([Adj[HEAD=[]]] happy)))

# 15 Extend NLTK's treatment of feature structures to allow unification into list-valued features, and use this to
# implement an HPSG-style analysis of subcategorization, whereby the SUBCAT of a head category is the concatenation
# its complements' categories with the SUBCAT value of its immediate parent.

# Not quite what was being asked. This list feature provides a merge method that checks whether the other
# feature structure's TYPE feature (expected to be at the root) is contained by it and
# the result is the remaining elements of the list.

class FSSubcat(nltk.featstruct.CustomFeatureValue):
    def __init__(self, lst):
        assert type(lst)==list
        self.lst = lst
    def merge(self, other):
        import copy
        if not isinstance(other, nltk.FeatStruct):
            return nltk.featstruct.UnificationFailure
        if other['TYPE'] in self.lst:
            aux_lst=copy.deepcopy(self.lst)
            aux_lst.remove(other['TYPE'])
            return FSSubcat(aux_lst)
        else:
            return nltk.featstruct.UnificationFailure
    def __repr__(self):
        return str(self.lst)
    def __eq__(self, other):
        if not isinstance(other, FSSubcat):
            return False
        return self.lst == other.lst
    def __lt__(self, other):
        if not isinstance(other, FSSubcat):
            return True
        return self.lst < other.lst

# v=nltk.FeatStruct(TYPE='V',SUBCAT=FSSubcat(['NP', 'NP', 'PP']))
# pp=nltk.FeatStruct(TYPE='PP',SUBCAT=FSSubcat(['PP']))
# np=nltk.FeatStruct(TYPE='NP',SUBCAT=FSSubcat(['NP']))
# v['SUBCAT'].merge(pp)
# ['NP', 'NP']
# v['SUBCAT'].merge(pp).merge(np)
# ['NP']
# v['SUBCAT'].merge(pp).merge(np).merge(np)
# []

# 16 Extend NLTK's treatment of feature structures to allow productions with underspecified categories, such as
# S[-INV] --> ?x S/?x.

# Maybe later

# 17 Extend NLTK's treatment of feature structures to allow typed feature structures.

# V1: each fixed level must be declared explicitly. Complete levels can be erased by changing their value to a type
# different than a Feat[Whatever]

class MyFeatDict_v1(nltk.FeatDict):
    def __init__(self, features=None, **morefeatures):
        self.locked=False
        if isinstance(features, nltk.compat.string_types):
            nltk.FeatStructReader().fromstring(features, self)
            self.update(**morefeatures)
        else:
            self.update(features, **morefeatures)
        self.locked=True
    def __setitem__(self, name_or_path, value):
        if self._frozen: raise ValueError(nltk.FeatStruct._FROZEN_ERROR)
        if isinstance(name_or_path, (nltk.compat.string_types, nltk.Feature)):
            try:
                if self.locked: id(self[name_or_path])
                return dict.__setitem__(self, name_or_path, value)
            except:
                raise ValueError('{} was not in the original structure'.format(name_or_path))
        elif isinstance(name_or_path, tuple):
            if len(name_or_path) == 0:
                raise ValueError("The path () can not be set")
            else:
                parent = self[name_or_path[:-1]]
                if not isinstance(parent, nltk.FeatStruct):
                    raise KeyError(name_or_path) # path contains base value
                parent[name_or_path[-1]] = value
        else:
            raise TypeError(self._INDEX_ERROR % name_or_path)
  
# fs=MyFeatDict_v1(TOKEN='he',TYPE='PPN',SUBCAT=MyFeatDict_v1(PERS=3,NUM='sg',GEN='M'),MISC=nltk.FeatStruct())
# fs['BLAH']=42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 31, in __setitem__
# ValueError: BLAH was not in the original structure
# fs['SUBCAT']['BLAH']=42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 31, in __setitem__
# ValueError: BLAH was not in the original structure
# fs['SUBCAT']=42
# fs
# [MISC=[], SUBCAT=42, TOKEN='he', TYPE='PPN']
# fs1=nltk.FeatStruct(A=42)
# fs['TOKEN']=fs1
# fs
# [MISC=[], SUBCAT=42, TOKEN=[A=42], TYPE='PPN']
# fs['TOKEN']='she'
# fs
# [MISC=[], SUBCAT=42, TOKEN='she', TYPE='PPN']
# fs['MISC']['BLAH']=42
# fs
# [MISC=[BLAH=42], SUBCAT=42, TOKEN='she', TYPE='PPN']

# V2: levels are frozen and their nodes cannot be deleted by assigning them differnet value types

class MyFeatDict_v2(nltk.FeatDict):
    def __init__(self, features=None, **morefeatures):
        self.locked=False
        if isinstance(features, nltk.compat.string_types):
            nltk.FeatStructReader().fromstring(features, self)
            self.update(**morefeatures)
        else:
            self.update(features, **morefeatures)
        self.fs_paths=[]
        self._extract_paths()
        self.locked=True
    def _extract_paths(self,node_lst=[],start_path=()):
        for key in self[start_path].keys():
            self.fs_paths=self.fs_paths+[ start_path+(key,) ]
            if id(self[start_path+(key,)]) not in node_lst:
                node_lst=node_lst+[ id(self[start_path+(key,)]) ]
                try:
                    node_lst=self._extract_paths(node_lst, start_path+(key,))
                except:
                    pass
        return node_lst
    def __setitem__(self, name_or_path, value):
        if self._frozen: raise ValueError(nltk.FeatStruct._FROZEN_ERROR)
        if self.locked:
            self.locked=False
            aux_fs=MyFeatDict_v2(self)
            self.locked=True
            aux_fs.locked=False
            aux_fs[name_or_path]=value
            aux_fs.fs_paths=[]
            aux_fs._extract_paths()
            if set(aux_fs.fs_paths)!=set(self.fs_paths):
                raise ValueError('The requested change does not respect the original structure')
        if isinstance(name_or_path, (nltk.compat.string_types, nltk.Feature)):
            return dict.__setitem__(self, name_or_path, value)
        elif isinstance(name_or_path, tuple):
            if len(name_or_path) == 0:
                raise ValueError("The path () can not be set")
            else:
                parent = self[name_or_path[:-1]]
                if not isinstance(parent, nltk.FeatStruct):
                    raise KeyError(name_or_path) # path contains base value
                parent[name_or_path[-1]] = value
        else:
            raise TypeError(self._INDEX_ERROR % name_or_path)

# fs=MyFeatDict_v2(TOKEN='he',TYPE='PPN',SUBCAT=MyFeatDict_v2(PERS=3,NUM='sg',GEN='M'),MISC=nltk.FeatStruct())
# fs['BLAH']=42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 32, in __setitem__
# ValueError: The requested change does not respect the original structure
# fs['SUBCAT']['BLAH']=42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 32, in __setitem__
# ValueError: The requested change does not respect the original structure
# fs['SUBCAT']=42
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 32, in __setitem__
# ValueError: The requested change does not respect the original structure
# fs1=nltk.FeatStruct(A=42)
# fs['TOKEN']=fs1
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 32, in __setitem__
# ValueError: The requested change does not respect the original structure
# fs['TOKEN']='she'
# fs
# [MISC=[], SUBCAT=[GEN='M', NUM='sg', PERS=3], TOKEN='she', TYPE='PPN']
# fs['MISC']['BLAH']=42
# fs
# [MISC=[BLAH=42], SUBCAT=[GEN='M', NUM='sg', PERS=3], TOKEN='she', TYPE='PPN']

# 18 Pick some grammatical constructions described in (Huddleston & Pullum, 2002), and develop a feature based grammar
# to account for them.

# NA
