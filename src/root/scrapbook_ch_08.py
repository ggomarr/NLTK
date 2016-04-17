'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# 1 Can you come up with grammatical sentences that have probably never been uttered before?
# (Take turns with a partner.) What does this tell you about human language?

# NA

# 2 Recall Strunk and White's prohibition against sentence-initial however used to mean "although".
# Do a web search for however used at the start of the sentence. How widely used is this construction?

# NA

# 3 Consider the sentence Kim arrived or Dana left and everyone cheered. Write down the parenthesized
# forms to show the relative scope of and and or. Generate tree structures corresponding to both
# of these interpretations.

def ex03_v01(grammar="""
                        S   -> CS C CSS | CSS C CS
                        CSS -> CS | CS C CS
                        CS  -> NP VP
                        NP  -> N
                        VP  -> V
                        C   -> 'and' | 'or'
                        V   -> 'arrived' | 'left' | 'cheered'
                        N   -> 'Kim' | 'Dana' | 'everyone'""",
             sent='Kim arrived or Dana left and everyone cheered'.split(),
             print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    rd_parser = nltk.RecursiveDescentParser(cfg_grammar)
    num_trees=0
    for tree in rd_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# ex03_v01()
# (S
#   (CS (NP (N Kim)) (VP (V arrived)))
#   (C or)
#   (CSS
#     (CS (NP (N Dana)) (VP (V left)))
#     (C and)
#     (CS (NP (N everyone)) (VP (V cheered)))))
# (S
#   (CSS
#     (CS (NP (N Kim)) (VP (V arrived)))
#     (C or)
#     (CS (NP (N Dana)) (VP (V left))))
#   (C and)
#   (CS (NP (N everyone)) (VP (V cheered))))
# 2

def ex03_v02(grammar="""
                        S   -> NP VP | S C S
                        NP  -> N
                        VP  -> V
                        C   -> 'and' | 'or'
                        V   -> 'arrived' | 'left' | 'cheered'
                        N   -> 'Kim' | 'Dana' | 'everyone'""",
             sent='Kim arrived or Dana left and everyone cheered'.split(),
             print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    tdc_parser = nltk.parse.chart.TopDownChartParser(cfg_grammar)
    num_trees=0
    for tree in tdc_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# ex03_v02()
# (S
#   (S (NP (N Kim)) (VP (V arrived)))
#   (C or)
#   (S
#     (S (NP (N Dana)) (VP (V left)))
#     (C and)
#     (S (NP (N everyone)) (VP (V cheered)))))
# (S
#   (S
#     (S (NP (N Kim)) (VP (V arrived)))
#     (C or)
#     (S (NP (N Dana)) (VP (V left))))
#   (C and)
#   (S (NP (N everyone)) (VP (V cheered))))
# 2

# 4 The Tree class implements a variety of other useful methods. See the Tree help documentation
# for more details, i.e. import the Tree class and then type help(Tree).

# NA

# 5 In this exercise you will manually construct some parse trees.
# - Write code to produce two trees, one for each reading of the phrase old men and women
# - Encode any of the trees presented in this chapter as a labeled bracketing and use nltk.Tree() to check that it is well-formed. Now use draw() to display the tree.
# - As in (a) above, draw a tree for The woman saw a man last Thursday.

def ex05_arborize(grammar="""
                             S   -> NP VP | NP
                             NP  -> N | DT NP | A NP | NP C NP
                             VP  -> V NP | VP NP
                             C   -> 'and'
                             DT  -> 'The' | 'a'
                             V   -> 'saw'
                             N   -> 'man' | 'men' | 'woman' | 'women' | 'Thursday'
                             A   -> 'Old' | 'last'
                          """,
                  sent='Old men and women'.split(),
                  print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    tdc_parser = nltk.parse.chart.TopDownChartParser(cfg_grammar)
    num_trees=0
    for tree in tdc_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# ex05_arborize(sent='Old men and women'.split())
# (S (NP (A Old) (NP (NP (N men)) (C and) (NP (N women)))))
# (S (NP (NP (A Old) (NP (N men))) (C and) (NP (N women))))
# 2

def ex05_str_to_drawn_tree(sent_str ='(S (NP (A Old) (NP (NP (N men)) (C and) (NP (N women)))))'):
    sent_tree=nltk.Tree.fromstring(sent_str)
    sent_tree.draw()

# ex05_arborize(sent='The woman saw a man last Thursday'.split())
# (S
#   (NP (DT The) (NP (N woman)))
#   (VP
#     (VP (V saw) (NP (DT a) (NP (N man))))
#     (NP (A last) (NP (N Thursday)))))
# 1

# 6 Write a recursive function to traverse a tree and return the depth of the tree,
# such that a tree with a single node would have depth zero. (Hint: the depth of a subtree
# is the maximum depth of its children, plus one.)

def ex06(my_tree=nltk.Tree.fromstring('(S (NP (DT The) (NP (N woman))) (VP (VP (V saw) (NP (DT a) (NP (N man)))) (NP (A last) (NP (N Thursday)))))')):
    depth=[]
    for branch in my_tree:
        aux_depth=0
        try:
            branch.label()
            aux_depth=aux_depth+ex06(branch)
        except AttributeError:
            pass
        depth=depth+[aux_depth]
    return max(depth)

# ex06()
# 6 #i.e., (S (VP (VP (NP (NP (N man))))))

# 7 Analyze the A.A. Milne sentence about Piglet, by underlining all of the sentences it contains
# then replacing these with S (e.g. the first sentence becomes S when:lx` S). Draw a tree structure
# for this "compressed" sentence. What are the main syntactic constructions used for building
# such a long sentence?

# NA

# 8 In the recursive descent parser demo, experiment with changing the sentence to be parsed
# by selecting Edit Text in the Edit menu.

# NA

# 9 Can the grammar in grammar1 be used to describe sentences that are more than 20 words in length?

# Yes: S -> NP VP -> Det N PP V NP PP -> Det N P NP V Det N PP P NP -> ...

def ex08(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
             sent='a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a telescope'.split(),
             print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    rd_parser = nltk.RecursiveDescentParser(cfg_grammar)
    num_trees=0
    for tree in rd_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# len('a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a telescope')
# 26
# ex08(print_trees=False)
# 5

# 10 Use the graphical chart-parser interface to experiment with different rule invocation strategies.
# Come up with your own strategy that you can execute manually using the graphical interface.
# Describe the steps, and report any efficiency improvements it has (e.g. in terms of the size
# of the resulting chart). Do these improvements depend on the structure of the grammar?
# What do you think of the prospects for significant performance boosts from cleverer
# rule invocation strategies?

# To obtain the smallest chart, the 'most compressing rules' should be applied first.
# Maybe think about it more later?

# 11 With pen and paper, manually trace the execution of a recursive descent parser
# and a shift-reduce parser, for a CFG you have already seen, or one of your own devising.

# NA

# 12 We have seen that a chart parser adds but never removes edges from a chart. Why?

# Because they may be used again. Maybe think about it more later?

# 13 Consider the sequence of words: Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.
# This is a grammatically correct sentence, as explained at
# http://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo.
# Consider the tree diagram presented on this Wikipedia page, and write down a suitable grammar.
# Normalize case to lowercase, to simulate the problem that a listener has when hearing this sentence.
# Can you find other parses for this sentence? How does the number of parse trees grow as the sentence
# gets longer? (More examples of these sentences can be found at http://en.wikipedia.org/wiki/List_of_homophonous_phrases).

def ex13(grammar="""
                    S -> NP VP
                    VP -> V | V NP
                    RC -> NP V
                    NP -> N | PN N | NP RC
                    V  -> "buffalo"
                    N  -> "buffalo"
                    PN -> "buffalo"
                    """,
             sent=['buffalo']*8,
             print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    tdc_parser = nltk.TopDownChartParser(cfg_grammar)
    num_trees=0
    for tree in tdc_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# map(lambda n: ex13(sent=['buffalo']*n,print_trees=False), range(20))
# [0, 1, 2, 3, 5, 9, 17, 33, 66, 134, 277, 579, 1224, 2610, 5609, 12135, 26408, 57770, 126962]
# Aprox. doubles each time

# 14 You can modify the grammar in the recursive descent parser demo by selecting Edit Grammar
# in the Edit menu. Change the second expansion production, namely NP -> Det N PP, to NP -> NP PP.
# Using the Step button, try to build a parse tree. What happens?

# Recursive grammar and recursive descent: should go into infinite loop.
# Hence the 'weird' grammar on ex03

def ex14(grammar="""
                    S   -> NP VP | S C S
                    NP  -> N
                    VP  -> V
                    C   -> 'and' | 'or'
                    V   -> 'arrived' | 'left' | 'cheered'
                    N   -> 'Kim' | 'Dana' | 'everyone'""",
         sent='Kim arrived or Dana left and everyone cheered'.split(),
         print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    rd_parser = nltk.RecursiveDescentParser(cfg_grammar)
    num_trees=0
    for tree in rd_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# ex14()
# (S
#   (S (NP (N Kim)) (VP (V arrived)))
#   (C or)
#   (S
#     (S (NP (N Dana)) (VP (V left)))
#     (C and)
#     (S (NP (N everyone)) (VP (V cheered)))))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 13, in ex14
#   File "/usr/local/lib/python2.7/dist-packages/nltk/parse/recursivedescent.py", line 127, in _parse
#     for result in self._expand(remaining_text, tree, frontier):
#   File "/usr/local/lib/python2.7/dist-packages/nltk/parse/recursivedescent.py", line 227, in _expand
#     new_frontier + frontier[1:]):
# [--- A LOT OF THE SAME ---]
# RuntimeError: maximum recursion depth exceeded while calling a Python object

# 15 Extend the grammar in grammar2 with productions that expand prepositions as intransitive,
# transitive and requiring a PP complement. Based on these productions,
# use the method of the preceding exercise to draw a tree for the sentence Lee ran away home.

def ex15(grammar="""
                  S         -> NP VP
                  NP        -> Det Nom | PropN
                  Nom       -> Adj Nom | N
                  VP        -> VPTrans | VPIntrans| VPCop | VPSent | VP PP
                  VPTrans   -> VTrans NP | VTrans PTrans NP
                  VPIntrans -> VIntrans | VIntrans PIntrans | VIntrans PIntrans N
                  VPCop     -> VCop Adj | VCop NP
                  VPSent    -> VSent S
                  PP        -> PPP NP
                  PropN     -> 'Buster' | 'Chatterer' | 'Joe' | 'Lee'
                  Det       -> 'the' | 'a'
                  Adj       -> 'angry' | 'frightened' |  'little' | 'tall'
                  N         -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log' | 'home'
                  VTrans    -> 'chased' | 'saw' | 'put' | 'took'
                  VIntrans  -> 'ran'
                  VCop      -> 'was' | 'became' | 'looked'
                  VSent     -> 'said' | 'thought' | 'saw'
                  PTrans    -> 'away' | 'in' | 'out'
                  PIntrans  -> 'away' | 'around' | 'in'
                  PPP       -> 'on' | 'to' | 'from' | 'in' | 'into' | 'for'
                  """,
             sent='Lee ran away home'.split(),
             print_trees=True):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    tdc_parser = nltk.TopDownChartParser(cfg_grammar)
    num_trees=0
    for tree in tdc_parser.parse(sent):
        if print_trees:
            print tree
        num_trees=num_trees+1
    return num_trees

# ex15(sent='Lee ran away home'.split(), print_trees=True)
# (S
#   (NP (PropN Lee))
#   (VP (VPIntrans (VIntrans ran) (PIntrans away) (N home))))
# 1
# ex15(sent='Lee saw the angry bear on the tall log'.split(), print_trees=True)
# (S
#   (NP (PropN Lee))
#   (VP
#     (VP
#       (VPTrans
#         (VTrans saw)
#         (NP (Det the) (Nom (Adj angry) (Nom (N bear))))))
#     (PP (PPP on) (NP (Det the) (Nom (Adj tall) (Nom (N log)))))))
# 1
# ex15(sent='Lee took Buster to the tree into the litle log'.split(), print_trees=True)
# (S
#   (NP (PropN Lee))
#   (VP
#     (VP
#       (VP (VPTrans (VTrans took) (NP (PropN Buster))))
#       (PP (PPP to) (NP (Det the) (Nom (N tree)))))
#     (PP (PPP into) (NP (Det the) (Nom (Adj little) (Nom (N log)))))))
# 1
# ex15(sent='Lee chased away a frightened squirrel'.split(), print_trees=True)
# (S
#   (NP (PropN Lee))
#   (VP
#     (VPTrans
#       (VTrans chased)
#       (PTrans away)
#       (NP (Det a) (Nom (Adj frightened) (Nom (N squirrel)))))))
# 1
# ex15(sent='Lee said Buster chased away a frightened squirrel'.split(), print_trees=True)
# (S
#   (NP (PropN Lee))
#   (VP
#     (VPSent
#       (VSent said)
#       (S
#         (NP (PropN Buster))
#         (VP
#           (VPTrans
#             (VTrans chased)
#             (PTrans away)
#             (NP (Det a) (Nom (Adj frightened) (Nom (N squirrel))))))))))
# 1

# 16 Pick some common verbs and complete the following tasks:
# - Write a program to find those verbs in the Prepositional Phrase Attachment Corpus nltk.corpus.ppattach.
# Find any cases where the same verb exhibits two different attachments, but where the first noun, or second noun,
# or preposition, stay unchanged (as we saw in our discussion of syntactic ambiguity in 2).
# - Devise CFG grammar productions to cover some of these cases.

def ex16(att='noun1'):
    import collections
    entries = nltk.corpus.ppattach.attachments('training')
    aux_out=collections.defaultdict(lambda: collections.defaultdict(set))
    for entry in entries:
        key=entry.verb+' - '+getattr(entry,att)
        aux_out[key][entry.attachment].add(entry)
    return [aux_out[key] for key in aux_out.keys() if len(aux_out[key])==2]

# for i in ex16(att='noun1')[:25]:
#     for j in i['N']:
#         print j
#     for j in i['V']:
#         print j
# PPAttachment(sent=u'19465', verb=u'paid', noun1=u'million', prep=u'in', noun2=u'taxes', attachment=u'N')
# PPAttachment(sent=u'38039', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'PLC', attachment=u'N')
# PPAttachment(sent=u'26218', verb=u'paid', noun1=u'million', prep=u'of', noun2=u'cost', attachment=u'N')
# PPAttachment(sent=u'10698', verb=u'paid', noun1=u'million', prep=u'of', noun2=u'shares', attachment=u'N')
# PPAttachment(sent=u'22042', verb=u'paid', noun1=u'million', prep=u'in', noun2=u'cash', attachment=u'N')
# PPAttachment(sent=u'10698', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'Falcon', attachment=u'V')
# PPAttachment(sent=u'30516', verb=u'paid', noun1=u'million', prep=u'to', noun2=u'creditors', attachment=u'V')
# PPAttachment(sent=u'31817', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'backing', attachment=u'V')
# PPAttachment(sent=u'8301', verb=u'paid', noun1=u'million', prep=u'to', noun2=u'hospitals', attachment=u'V')
# PPAttachment(sent=u'26861', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'stake', attachment=u'V')
# PPAttachment(sent=u'5012', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'Tower', attachment=u'V')
# PPAttachment(sent=u'22042', verb=u'paid', noun1=u'million', prep=u'for', noun2=u'share', attachment=u'V')
# PPAttachment(sent=u'9144', verb=u'viewed', noun1=u'creation', prep=u'of', noun2=u'plans', attachment=u'N')
# PPAttachment(sent=u'9144', verb=u'viewed', noun1=u'creation', prep=u'as', noun2=u'abuse', attachment=u'V')
# PPAttachment(sent=u'2139', verb=u'take', noun1=u'charge', prep=u'of', noun2=u'operations', attachment=u'N')
# PPAttachment(sent=u'4585', verb=u'take', noun1=u'charge', prep=u'against', noun2=u'earnings', attachment=u'N')
# PPAttachment(sent=u'4585', verb=u'take', noun1=u'charge', prep=u'in', noun2=u'quarter', attachment=u'V')
# PPAttachment(sent=u'3702', verb=u'presented', noun1=u'claims', prep=u'for', noun2=u'damages', attachment=u'N')
# PPAttachment(sent=u'3702', verb=u'presented', noun1=u'claims', prep=u'in', noun2=u'court', attachment=u'V')
# PPAttachment(sent=u'31052', verb=u'refinancing', noun1=u'debt', prep=u'of', noun2=u'concern', attachment=u'N')
# PPAttachment(sent=u'31052', verb=u'refinancing', noun1=u'debt', prep=u'at', noun2=u'rates', attachment=u'V')
# PPAttachment(sent=u'3423', verb=u'raised', noun1=u'price', prep=u'for', noun2=u'jeweler', attachment=u'N')
# PPAttachment(sent=u'3423', verb=u'raised', noun1=u'price', prep=u'to', noun2=u'57.50', attachment=u'V')
# PPAttachment(sent=u'38685', verb=u'take', noun1=u'look', prep=u'at', noun2=u'2', attachment=u'N')
# PPAttachment(sent=u'7524', verb=u'take', noun1=u'look', prep=u'at', noun2=u'issue', attachment=u'N')
# PPAttachment(sent=u'2162', verb=u'take', noun1=u'look', prep=u'at', noun2=u'businesses', attachment=u'N')
# PPAttachment(sent=u'546', verb=u'take', noun1=u'look', prep=u'at', noun2=u'Lights', attachment=u'N')
# PPAttachment(sent=u'38023', verb=u'take', noun1=u'look', prep=u'at', noun2=u'business', attachment=u'N')
# PPAttachment(sent=u'14944', verb=u'take', noun1=u'look', prep=u'at', noun2=u'newspaper', attachment=u'N')
# PPAttachment(sent=u'37065', verb=u'take', noun1=u'look', prep=u'at', noun2=u'stocks', attachment=u'V')
# PPAttachment(sent=u'7524', verb=u'take', noun1=u'look', prep=u'during', noun2=u'days', attachment=u'V')
# PPAttachment(sent=u'15286', verb=u'take', noun1=u'look', prep=u'at', noun2=u'competition', attachment=u'V')
# PPAttachment(sent=u'12685', verb=u'selling', noun1=u'parts', prep=u'of', noun2=u'portfolios', attachment=u'N')
# PPAttachment(sent=u'16237', verb=u'selling', noun1=u'parts', prep=u'of', noun2=u'company', attachment=u'N')
# PPAttachment(sent=u'16038', verb=u'selling', noun1=u'parts', prep=u'to', noun2=u'the', attachment=u'V')
# PPAttachment(sent=u'26880', verb=u'satisfy', noun1=u'need', prep=u'for', noun2=u'DRAMs', attachment=u'N')
# PPAttachment(sent=u'26880', verb=u'satisfy', noun1=u'need', prep=u'from', noun2=u'market', attachment=u'V')
# PPAttachment(sent=u'6213', verb=u'be', noun1=u'bids', prep=u'for', noun2=u'companies', attachment=u'N')
# PPAttachment(sent=u'6213', verb=u'be', noun1=u'bids', prep=u'within', noun2=u'months', attachment=u'V')
# PPAttachment(sent=u'3056', verb=u'increasing', noun1=u'size', prep=u'of', noun2=u'bond', attachment=u'N')
# PPAttachment(sent=u'33036', verb=u'increasing', noun1=u'size', prep=u'to', noun2=u'members', attachment=u'V')
# PPAttachment(sent=u'22912', verb=u'exceed', noun1=u'supply', prep=u'for', noun2=u'Fujis', attachment=u'N')
# PPAttachment(sent=u'22912', verb=u'exceed', noun1=u'supply', prep=u'for', noun2=u'10', attachment=u'V')
# PPAttachment(sent=u'8690', verb=u'combine', noun1=u'controls', prep=u'of', noun2=u'the', attachment=u'N')
# PPAttachment(sent=u'8690', verb=u'combine', noun1=u'controls', prep=u'with', noun2=u'benefits', attachment=u'V')
# PPAttachment(sent=u'7216', verb=u'hitting', noun1=u'low', prep=u'of', noun2=u'2102.2', attachment=u'N')
# PPAttachment(sent=u'7216', verb=u'hitting', noun1=u'low', prep=u'within', noun2=u'minutes', attachment=u'V')
# PPAttachment(sent=u'13433', verb=u'reach', noun1=u'goal', prep=u'of', noun2=u'schools', attachment=u'N')
# PPAttachment(sent=u'13433', verb=u'reach', noun1=u'goal', prep=u'before', noun2=u'end', attachment=u'V')
# PPAttachment(sent=u'36452', verb=u'showed', noun1=u'growth', prep=u'in', noun2=u'lending', attachment=u'N')
# PPAttachment(sent=u'39273', verb=u'showed', noun1=u'growth', prep=u'in', noun2=u'lines', attachment=u'V')
# PPAttachment(sent=u'26839', verb=u'consider', noun1=u'proposal', prep=u'from', noun2=u'group', attachment=u'N')
# PPAttachment(sent=u'33686', verb=u'consider', noun1=u'proposal', prep=u'at', noun2=u'hearing', attachment=u'V')
# PPAttachment(sent=u'7981', verb=u'provided', noun1=u'information', prep=u'about', noun2=u'plans', attachment=u'N')
# PPAttachment(sent=u'5082', verb=u'provided', noun1=u'information', prep=u'during', noun2=u'inquiry', attachment=u'V')
# PPAttachment(sent=u'24274', verb=u'provided', noun1=u'information', prep=u'to', noun2=u'Pentagon', attachment=u'V')
# PPAttachment(sent=u'9678', verb=u'provided', noun1=u'information', prep=u'to', noun2=u'Force', attachment=u'V')
# PPAttachment(sent=u'2380', verb=u'offered', noun1=u'tickets', prep=u'on', noun2=u'Airlines', attachment=u'N')
# PPAttachment(sent=u'2380', verb=u'offered', noun1=u'tickets', prep=u'to', noun2=u'buyers', attachment=u'V')
# PPAttachment(sent=u'37774', verb=u'manufacture', noun1=u'line', prep=u'of', noun2=u'trucks', attachment=u'N')
# PPAttachment(sent=u'37774', verb=u'manufacture', noun1=u'line', prep=u'in', noun2=u'Britain', attachment=u'V')
# PPAttachment(sent=u'9098', verb=u'trade', noun1=u'some', prep=u'of', noun2=u'it', attachment=u'N')
# PPAttachment(sent=u'4489', verb=u'trade', noun1=u'some', prep=u'of', noun2=u'stake', attachment=u'N')
# PPAttachment(sent=u'4489', verb=u'trade', noun1=u'some', prep=u'for', noun2=u'%', attachment=u'V')
# PPAttachment(sent=u'9098', verb=u'trade', noun1=u'some', prep=u'for', noun2=u'cocaine', attachment=u'V')
# PPAttachment(sent=u'6105', verb=u'provide', noun1=u'level', prep=u'of', noun2=u'insurance', attachment=u'N')
# PPAttachment(sent=u'6105', verb=u'provide', noun1=u'level', prep=u'to', noun2=u'workers', attachment=u'V')
# PPAttachment(sent=u'17797', verb=u'was', noun1=u'cause', prep=u'of', noun2=u'death', attachment=u'N')
# PPAttachment(sent=u'17797', verb=u'was', noun1=u'cause', prep=u'in', noun2=u'%', attachment=u'V')
# PPAttachment(sent=u'11593', verb=u'slowed', noun1=u'progress', prep=u'of', noun2=u'legislation', attachment=u'N')
# PPAttachment(sent=u'11593', verb=u'slowed', noun1=u'progress', prep=u'to', noun2=u'halt', attachment=u'V')
# PPAttachment(sent=u'11722', verb=u'put', noun1=u'money', prep=u'at', noun2=u'risk', attachment=u'N')
# PPAttachment(sent=u'33699', verb=u'put', noun1=u'money', prep=u'into', noun2=u'funds', attachment=u'V')
# PPAttachment(sent=u'18144', verb=u'put', noun1=u'money', prep=u'in', noun2=u'IRA', attachment=u'V')
# PPAttachment(sent=u'32905', verb=u'put', noun1=u'money', prep=u'into', noun2=u'policy', attachment=u'V')
        
def ex16_preps():
    import collections
    entries = nltk.corpus.ppattach.attachments('training')
    aux_out=collections.defaultdict(lambda: collections.defaultdict(set))
    for entry in entries:
        aux_out[entry.prep.lower()][entry.attachment].add(entry)
    return [ [key, len(aux_out[key]['N']), len(aux_out[key]['V'])] for key in aux_out.keys() ]

# for i in a[:25]:
#     print i
# [u'among', 29, 39]
# [u'via', 1, 19]
# [u'past', 0, 4]
# [u'into', 24, 270]
# [u'within', 9, 41]
# [u'while', 0, 1]
# [u'except', 1, 2]
# [u'down', 0, 3]
# [u'as', 94, 380]
# [u'because', 7, 17]
# [u'through', 15, 121]
# [u'at', 136, 552]
# [u'in', 1552, 1948]
# [u'notwithstanding', 0, 1]
# [u'throughout', 2, 11]
# [u'before', 5, 56]
# [u'beyond', 3, 8]
# [u'from', 292, 644]
# [u'for', 1045, 1136]
# [u'since', 11, 44]
# [u'below', 12, 8]
# [u'per', 14, 3]
# [u'than', 64, 10]
# [u'beside', 0, 1]
# [u'to', 501, 2172]

# 17 Write a program to compare the efficiency of a top-down chart parser compared with a recursive descent parser
# (4). Use the same grammar and input sentences for both. Compare their performance using the timeit module
# (see 4.7 for an example of how to do this).

def ex17(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
             sent='a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a telescope'.split(),
             parsers=[ nltk.TopDownChartParser, nltk.RecursiveDescentParser ],
             loops=1000):
    import timeit
    cfg_grammar = nltk.CFG.fromstring(grammar)
    aux_out=[]
    for parser in parsers:
        t_pars=parser(cfg_grammar)
        tim_out=timeit.Timer(lambda: t_pars.parse(sent)).timeit(number=loops)
        num_trees=sum([1 for _ in t_pars.parse(sent)])
        aux_out=aux_out+[[num_trees,tim_out]]
    return aux_out

# ex17()
# [[5, 6.9965150356292725],
#  [5, 0.010149002075195312]]

# 18 Compare the performance of the top-down, bottom-up, and left-corner parsers using the same grammar and three
# grammatical test sentences. Use timeit to log the amount of time each parser takes on the same sentence.
# Write a function that runs all three parsers on all three sentences, and prints a 3-by-3 grid of times,
# as well as row and column totals. Discuss your findings.

def ex18(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
             sents=[ 'a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a telescope'.split(),
                     'a cat on a dog with a man in a park saw a cat on a dog'.split(),
                     'a cat saw a cat'.split()],
             parsers=[ nltk.TopDownChartParser, nltk.RecursiveDescentParser, nltk.ShiftReduceParser ],
             loops=1000):
    import timeit
    cfg_grammar = nltk.CFG.fromstring(grammar)
    aux_out=[]
    for parser in parsers:
        t_pars=parser(cfg_grammar)
        aux_out=aux_out+[ [ timeit.Timer(lambda: t_pars.parse(sent)).timeit(number=loops) for sent in sents ] ]
    return aux_out

# ex18()
# [[6.775464057922363,     4.00439190864563,     1.1771330833435059],
#  [0.009818077087402344,  0.007216215133666992, 0.003948211669921875],
#  [0.0004749298095703125, 0.0004730224609375,   0.00047016143798828125]]

# 19 Read up on "garden path" sentences. How might the computational work of a parser relate to the difficulty
# humans have with processing these sentences? http://en.wikipedia.org/wiki/Garden_path_sentence

# A parser would not have such issues: it would generate all trees anyway. Issues may arise from the way the rules
# of the grammar are constructed and the order in which they apply - these have been defined by what we consider
# to be acceptable, which means a lot of 'expected trees' may be explored before the 'real tree' of the
# intended meaning is reached. However, if all trees are going to be searched anyway, this makes
# little difference on the outcome.

# 20 To compare multiple trees in a single window, we can use the draw_trees() method. Define some trees
# and try it out:
# >>> from nltk.draw.tree import draw_trees
# >>> draw_trees(tree1, tree2, tree3)                    

# NA

# 21 Using tree positions, list the subjects of the first 100 sentences in the Penn treebank;
# to make the results easier to view, limit the extracted subjects to subtrees whose height is 2.

def ex21(num=100, search_tag='SBJ'):
    sents=nltk.corpus.treebank.parsed_sents()[:num]
    return [tree for sent in sents for tree in sent if search_tag in tree.label()]

# for sbj in ex21()[:10]:
#     print sbj
# (NP-SBJ
#   (NP (NNP Pierre) (NNP Vinken))
#   (, ,)
#   (ADJP (NP (CD 61) (NNS years)) (JJ old))
#   (, ,))
# (NP-SBJ (NNP Mr.) (NNP Vinken))
# (NP-SBJ-1
#   (NP (NNP Rudolph) (NNP Agnew))
#   (, ,)
#   (UCP
#     (ADJP (NP (CD 55) (NNS years)) (JJ old))
#     (CC and)
#     (NP
#       (NP (JJ former) (NN chairman))
#       (PP
#         (IN of)
#         (NP (NNP Consolidated) (NNP Gold) (NNP Fields) (NNP PLC)))))
#   (, ,))
# (NP-SBJ (NNS researchers))
# (NP-SBJ (NNS researchers))
# (NP-SBJ
#   (NP (NNP Lorillard) (NNP Inc.))
#   (, ,)
#   (NP
#     (NP (DT the) (NN unit))
#     (PP
#       (IN of)
#       (NP (ADJP (JJ New) (JJ York-based)) (NNP Loews) (NNP Corp.)))
#     (SBAR
#       (WHNP-2 (WDT that))
#       (S
#         (NP-SBJ (-NONE- *T*-2))
#         (VP (VBZ makes) (NP (NNP Kent) (NNS cigarettes))))))
#   (, ,))
# (NP-SBJ (DT the) (JJS latest) (NNS results))
# (NP-SBJ (DT A) (NNP Lorillard) (NN spokewoman))
# (NP-SBJ (PRP We))
# (NP-SBJ (EX There))

# 22 Inspect the Prepositional Phrase Attachment Corpus and try to suggest some factors
# that influence PP attachment.

# Already addressed in ex16

# 23 In this section we claimed that there are linguistic regularities that cannot be described simply
# in terms of n-grams. Consider the following sentence, particularly the position of the phrase in his turn.
# Does this illustrate a problem for an approach based on n-grams?
# What was more, the in his turn somewhat youngish Nikolay Parfenovich also turned out to be the only person
# in the entire world to acquire a sincere liking to our "discriminated-against" public procurator.
# (Dostoevsky: The Brothers Karamazov)

# n-grams miss the 'semantical unit' level altogether; they would have a hard time parsing meaningfully subordinate
# constructions of any kind, which can be arbitrarily long, and would fail miserably with those such as
# 'the in his turn somewhat youngish Nikolay Parfenovich'

# 24 Write a recursive function that produces a nested bracketing for a tree, leaving out the leaf nodes,
# and displaying the non-terminal labels after their subtrees. So the above example about Pierre Vinken
# would produce:
# [[[NNP NNP]NP , [ADJP [CD NNS]NP JJ]ADJP ,]NP-SBJ MD [VB [DT NN]NP [IN [DT JJ NN]NP]PP-CLR [NNP CD]NP-TMP]VP .]S
# Consecutive categories should be separated by space.


# print(nltk.corpus.treebank.parsed_sents()[0])
# (S
#   (NP-SBJ
#     (NP (NNP Pierre) (NNP Vinken))
#     (, ,)
#     (ADJP (NP (CD 61) (NNS years)) (JJ old))
#     (, ,))
#   (VP
#     (MD will)
#     (VP
#       (VB join)
#       (NP (DT the) (NN board))
#       (PP-CLR (IN as) (NP (DT a) (JJ nonexecutive) (NN director)))
#       (NP-TMP (NNP Nov.) (CD 29))))
#   (. .))

def ex24(tree_sent=nltk.corpus.treebank.parsed_sents()[0]):
    aux_str=''
    try:
        node_label=tree_sent.label()
        for branch in tree_sent:
            aux_txt=ex24(branch)
            if aux_txt:
                if aux_str:
                    aux_str=aux_str+' '+aux_txt
                else:
                    aux_str=aux_txt
            else:
                if aux_str:
                    aux_str=aux_str+' '+branch.label()
                else:
                    aux_str=branch.label()
        return '['+aux_str+']'+node_label
    except AttributeError:
        pass

# ex24()
# u'[[[NNP NNP]NP , [[CD NNS]NP JJ]ADJP ,]NP-SBJ [MD [VB [DT NN]NP [IN [DT JJ NN]NP]PP-CLR [NNP CD]NP-TMP]VP]VP .]S'

# 25 Download several electronic books from Project Gutenberg. Write a program to scan these texts for any extremely
# long sentences. What is the longest sentence you can find? What syntactic construction(s) are responsible
# for such long sentences?

def ex25(sents=nltk.corpus.gutenberg.sents(),num=10):
    return sorted(sents,key=len,reverse=True)[:num]

# for s in ex25():
#     print len(s), s
# 1378 [u'By', u'the', u'city', u"'", u's', u'quadrangular', u'houses', u'--', u'in', u'log', u'huts', u',', u'camping', u'with', u'lumber', u'-', u'men', u',', u'Along', u'the', u'ruts', u'of', u'the', u'turnpike', u',', u'along', u'the', u'dry', u'gulch', u'and', u'rivulet', u'bed', u',', u'Weeding', u'my', u'onion', u'-', u'patch', u'or', u'hosing', u'rows', u'of', u'carrots', u'and', u'parsnips', u',', u'crossing', u'savannas', u',', u'trailing', u'in', u'forests', u',', u'Prospecting', u',', u'gold', u'-', u'digging', u',', u'girdling', u'the', u'trees', u'of', u'a', u'new', u'purchase', u',', u'Scorch', u"'", u'd', u'ankle', u'-', u'deep', u'by', u'the', u'hot', u'sand', u',', u'hauling', u'my', u'boat', u'down', u'the', u'shallow', u'river', u',', u'Where', u'the', u'panther', u'walks', u'to', u'and', u'fro', u'on', u'a', u'limb', u'overhead', u',', u'where', u'the', u'buck', u'turns', u'furiously', u'at', u'the', u'hunter', u',', u'Where', u'the', u'rattlesnake', u'suns', u'his', u'flabby', u'length', u'on', u'a', u'rock', u',', u'where', u'the', u'otter', u'is', u'feeding', u'on', u'fish', u',', u'Where', u'the', u'alligator', u'in', u'his', u'tough', u'pimples', u'sleeps', u'by', u'the', u'bayou', u',', u'Where', u'the', u'black', u'bear', u'is', u'searching', u'for', u'roots', u'or', u'honey', u',', u'where', u'the', u'beaver', u'pats', u'the', u'mud', u'with', u'his', u'paddle', u'-', u'shaped', u'tall', u';', u'Over', u'the', u'growing', u'sugar', u',', u'over', u'the', u'yellow', u'-', u'flower', u"'", u'd', u'cotton', u'plant', u',', u'over', u'the', u'rice', u'in', u'its', u'low', u'moist', u'field', u',', u'Over', u'the', u'sharp', u'-', u'peak', u"'", u'd', u'farm', u'house', u',', u'with', u'its', u'scallop', u"'", u'd', u'scum', u'and', u'slender', u'shoots', u'from', u'the', u'gutters', u',', u'Over', u'the', u'western', u'persimmon', u',', u'over', u'the', u'long', u'-', u'leav', u"'", u'd', u'corn', u',', u'over', u'the', u'delicate', u'blue', u'-', u'flower', u'flax', u',', u'Over', u'the', u'white', u'and', u'brown', u'buckwheat', u',', u'a', u'hummer', u'and', u'buzzer', u'there', u'with', u'the', u'rest', u',', u'Over', u'the', u'dusky', u'green', u'of', u'the', u'rye', u'as', u'it', u'ripples', u'and', u'shades', u'in', u'the', u'breeze', u';', u'Scaling', u'mountains', u',', u'pulling', u'myself', u'cautiously', u'up', u',', u'holding', u'on', u'by', u'low', u'scragged', u'limbs', u',', u'Walking', u'the', u'path', u'worn', u'in', u'the', u'grass', u'and', u'beat', u'through', u'the', u'leaves', u'of', u'the', u'brush', u',', u'Where', u'the', u'quail', u'is', u'whistling', u'betwixt', u'the', u'woods', u'and', u'the', u'wheat', u'-', u'lot', u',', u'Where', u'the', u'bat', u'flies', u'in', u'the', u'Seventh', u'-', u'month', u'eve', u',', u'where', u'the', u'great', u'goldbug', u'drops', u'through', u'the', u'dark', u',', u'Where', u'the', u'brook', u'puts', u'out', u'of', u'the', u'roots', u'of', u'the', u'old', u'tree', u'and', u'flows', u'to', u'the', u'meadow', u',', u'Where', u'cattle', u'stand', u'and', u'shake', u'away', u'flies', u'with', u'the', u'tremulous', u'shuddering', u'of', u'their', u'hides', u',', u'Where', u'the', u'cheese', u'-', u'cloth', u'hangs', u'in', u'the', u'kitchen', u',', u'where', u'andirons', u'straddle', u'the', u'hearth', u'-', u'slab', u',', u'where', u'cobwebs', u'fall', u'in', u'festoons', u'from', u'the', u'rafters', u';', u'Where', u'trip', u'-', u'hammers', u'crash', u',', u'where', u'the', u'press', u'is', u'whirling', u'its', u'cylinders', u',', u'Wherever', u'the', u'human', u'heart', u'beats', u'with', u'terrible', u'throes', u'under', u'its', u'ribs', u',', u'Where', u'the', u'pear', u'-', u'shaped', u'balloon', u'is', u'floating', u'aloft', u',', u'(', u'floating', u'in', u'it', u'myself', u'and', u'looking', u'composedly', u'down', u',)', u'Where', u'the', u'life', u'-', u'car', u'is', u'drawn', u'on', u'the', u'slip', u'-', u'noose', u',', u'where', u'the', u'heat', u'hatches', u'pale', u'-', u'green', u'eggs', u'in', u'the', u'dented', u'sand', u',', u'Where', u'the', u'she', u'-', u'whale', u'swims', u'with', u'her', u'calf', u'and', u'never', u'forsakes', u'it', u',', u'Where', u'the', u'steam', u'-', u'ship', u'trails', u'hind', u'-', u'ways', u'its', u'long', u'pennant', u'of', u'smoke', u',', u'Where', u'the', u'fin', u'of', u'the', u'shark', u'cuts', u'like', u'a', u'black', u'chip', u'out', u'of', u'the', u'water', u',', u'Where', u'the', u'half', u'-', u'burn', u"'", u'd', u'brig', u'is', u'riding', u'on', u'unknown', u'currents', u',', u'Where', u'shells', u'grow', u'to', u'her', u'slimy', u'deck', u',', u'where', u'the', u'dead', u'are', u'corrupting', u'below', u';', u'Where', u'the', u'dense', u'-', u'starr', u"'", u'd', u'flag', u'is', u'borne', u'at', u'the', u'head', u'of', u'the', u'regiments', u',', u'Approaching', u'Manhattan', u'up', u'by', u'the', u'long', u'-', u'stretching', u'island', u',', u'Under', u'Niagara', u',', u'the', u'cataract', u'falling', u'like', u'a', u'veil', u'over', u'my', u'countenance', u',', u'Upon', u'a', u'door', u'-', u'step', u',', u'upon', u'the', u'horse', u'-', u'block', u'of', u'hard', u'wood', u'outside', u',', u'Upon', u'the', u'race', u'-', u'course', u',', u'or', u'enjoying', u'picnics', u'or', u'jigs', u'or', u'a', u'good', u'game', u'of', u'base', u'-', u'ball', u',', u'At', u'he', u'-', u'festivals', u',', u'with', u'blackguard', u'gibes', u',', u'ironical', u'license', u',', u'bull', u'-', u'dances', u',', u'drinking', u',', u'laughter', u',', u'At', u'the', u'cider', u'-', u'mill', u'tasting', u'the', u'sweets', u'of', u'the', u'brown', u'mash', u',', u'sucking', u'the', u'juice', u'through', u'a', u'straw', u',', u'At', u'apple', u'-', u'peelings', u'wanting', u'kisses', u'for', u'all', u'the', u'red', u'fruit', u'I', u'find', u',', u'At', u'musters', u',', u'beach', u'-', u'parties', u',', u'friendly', u'bees', u',', u'huskings', u',', u'house', u'-', u'raisings', u';', u'Where', u'the', u'mocking', u'-', u'bird', u'sounds', u'his', u'delicious', u'gurgles', u',', u'cackles', u',', u'screams', u',', u'weeps', u',', u'Where', u'the', u'hay', u'-', u'rick', u'stands', u'in', u'the', u'barn', u'-', u'yard', u',', u'where', u'the', u'dry', u'-', u'stalks', u'are', u'scatter', u"'", u'd', u',', u'where', u'the', u'brood', u'-', u'cow', u'waits', u'in', u'the', u'hovel', u',', u'Where', u'the', u'bull', u'advances', u'to', u'do', u'his', u'masculine', u'work', u',', u'where', u'the', u'stud', u'to', u'the', u'mare', u',', u'where', u'the', u'cock', u'is', u'treading', u'the', u'hen', u',', u'Where', u'the', u'heifers', u'browse', u',', u'where', u'geese', u'nip', u'their', u'food', u'with', u'short', u'jerks', u',', u'Where', u'sun', u'-', u'down', u'shadows', u'lengthen', u'over', u'the', u'limitless', u'and', u'lonesome', u'prairie', u',', u'Where', u'herds', u'of', u'buffalo', u'make', u'a', u'crawling', u'spread', u'of', u'the', u'square', u'miles', u'far', u'and', u'near', u',', u'Where', u'the', u'humming', u'-', u'bird', u'shimmers', u',', u'where', u'the', u'neck', u'of', u'the', u'long', u'-', u'lived', u'swan', u'is', u'curving', u'and', u'winding', u',', u'Where', u'the', u'laughing', u'-', u'gull', u'scoots', u'by', u'the', u'shore', u',', u'where', u'she', u'laughs', u'her', u'near', u'-', u'human', u'laugh', u',', u'Where', u'bee', u'-', u'hives', u'range', u'on', u'a', u'gray', u'bench', u'in', u'the', u'garden', u'half', u'hid', u'by', u'the', u'high', u'weeds', u',', u'Where', u'band', u'-', u'neck', u"'", u'd', u'partridges', u'roost', u'in', u'a', u'ring', u'on', u'the', u'ground', u'with', u'their', u'heads', u'out', u',', u'Where', u'burial', u'coaches', u'enter', u'the', u'arch', u"'", u'd', u'gates', u'of', u'a', u'cemetery', u',', u'Where', u'winter', u'wolves', u'bark', u'amid', u'wastes', u'of', u'snow', u'and', u'icicled', u'trees', u',', u'Where', u'the', u'yellow', u'-', u'crown', u"'", u'd', u'heron', u'comes', u'to', u'the', u'edge', u'of', u'the', u'marsh', u'at', u'night', u'and', u'feeds', u'upon', u'small', u'crabs', u',', u'Where', u'the', u'splash', u'of', u'swimmers', u'and', u'divers', u'cools', u'the', u'warm', u'noon', u',', u'Where', u'the', u'katy', u'-', u'did', u'works', u'her', u'chromatic', u'reed', u'on', u'the', u'walnut', u'-', u'tree', u'over', u'the', u'well', u',', u'Through', u'patches', u'of', u'citrons', u'and', u'cucumbers', u'with', u'silver', u'-', u'wired', u'leaves', u',', u'Through', u'the', u'salt', u'-', u'lick', u'or', u'orange', u'glade', u',', u'or', u'under', u'conical', u'firs', u',', u'Through', u'the', u'gymnasium', u',', u'through', u'the', u'curtain', u"'", u'd', u'saloon', u',', u'through', u'the', u'office', u'or', u'public', u'hall', u';', u'Pleas', u"'", u'd', u'with', u'the', u'native', u'and', u'pleas', u"'", u'd', u'with', u'the', u'foreign', u',', u'pleas', u"'", u'd', u'with', u'the', u'new', u'and', u'old', u',', u'Pleas', u"'", u'd', u'with', u'the', u'homely', u'woman', u'as', u'well', u'as', u'the', u'handsome', u',', u'Pleas', u"'", u'd', u'with', u'the', u'quakeress', u'as', u'she', u'puts', u'off', u'her', u'bonnet', u'and', u'talks', u'melodiously', u',', u'Pleas', u"'", u'd', u'with', u'the', u'tune', u'of', u'the', u'choir', u'of', u'the', u'whitewash', u"'", u'd', u'church', u',', u'Pleas', u"'", u'd', u'with', u'the', u'earnest', u'words', u'of', u'the', u'sweating', u'Methodist', u'preacher', u',', u'impress', u"'", u'd', u'seriously', u'at', u'the', u'camp', u'-', u'meeting', u';', u'Looking', u'in', u'at', u'the', u'shop', u'-', u'windows', u'of', u'Broadway', u'the', u'whole', u'forenoon', u',', u'flatting', u'the', u'flesh', u'of', u'my', u'nose', u'on', u'the', u'thick', u'plate', u'glass', u',', u'Wandering', u'the', u'same', u'afternoon', u'with', u'my', u'face', u'turn', u"'", u'd', u'up', u'to', u'the', u'clouds', u',', u'or', u'down', u'a', u'lane', u'or', u'along', u'the', u'beach', u',', u'My', u'right', u'and', u'left', u'arms', u'round', u'the', u'sides', u'of', u'two', u'friends', u',', u'and', u'I', u'in', u'the', u'middle', u';', u'Coming', u'home', u'with', u'the', u'silent', u'and', u'dark', u'-', u'cheek', u"'", u'd', u'bush', u'-', u'boy', u',', u'(', u'behind', u'me', u'he', u'rides', u'at', u'the', u'drape', u'of', u'the', u'day', u',)', u'Far', u'from', u'the', u'settlements', u'studying', u'the', u'print', u'of', u'animals', u"'", u'feet', u',', u'or', u'the', u'moccasin', u'print', u',', u'By', u'the', u'cot', u'in', u'the', u'hospital', u'reaching', u'lemonade', u'to', u'a', u'feverish', u'patient', u',', u'Nigh', u'the', u'coffin', u"'", u'd', u'corpse', u'when', u'all', u'is', u'still', u',', u'examining', u'with', u'a', u'candle', u';', u'Voyaging', u'to', u'every', u'port', u'to', u'dicker', u'and', u'adventure', u',', u'Hurrying', u'with', u'the', u'modern', u'crowd', u'as', u'eager', u'and', u'fickle', u'as', u'any', u',', u'Hot', u'toward', u'one', u'I', u'hate', u',', u'ready', u'in', u'my', u'madness', u'to', u'knife', u'him', u',', u'Solitary', u'at', u'midnight', u'in', u'my', u'back', u'yard', u',', u'my', u'thoughts', u'gone', u'from', u'me', u'a', u'long', u'while', u',', u'Walking', u'the', u'old', u'hills', u'of', u'Judaea', u'with', u'the', u'beautiful', u'gentle', u'God', u'by', u'my', u'side', u',', u'Speeding', u'through', u'space', u',', u'speeding', u'through', u'heaven', u'and', u'the', u'stars', u',', u'Speeding', u'amid', u'the', u'seven', u'satellites', u'and', u'the', u'broad', u'ring', u',', u'and', u'the', u'diameter', u'of', u'eighty', u'thousand', u'miles', u',', u'Speeding', u'with', u'tail', u"'", u'd', u'meteors', u',', u'throwing', u'fire', u'-', u'balls', u'like', u'the', u'rest', u',', u'Carrying', u'the', u'crescent', u'child', u'that', u'carries', u'its', u'own', u'full', u'mother', u'in', u'its', u'belly', u',', u'Storming', u',', u'enjoying', u',', u'planning', u',', u'loving', u',', u'cautioning', u',', u'Backing', u'and', u'filling', u',', u'appearing', u'and', u'disappearing', u',', u'I', u'tread', u'day', u'and', u'night', u'such', u'roads', u'.']
# 1102 [u'3', u'The', u'log', u'at', u'the', u'wood', u'-', u'pile', u',', u'the', u'axe', u'supported', u'by', u'it', u',', u'The', u'sylvan', u'hut', u',', u'the', u'vine', u'over', u'the', u'doorway', u',', u'the', u'space', u'clear', u"'", u'd', u'for', u'garden', u',', u'The', u'irregular', u'tapping', u'of', u'rain', u'down', u'on', u'the', u'leaves', u'after', u'the', u'storm', u'is', u'lull', u"'", u'd', u',', u'The', u'walling', u'and', u'moaning', u'at', u'intervals', u',', u'the', u'thought', u'of', u'the', u'sea', u',', u'The', u'thought', u'of', u'ships', u'struck', u'in', u'the', u'storm', u'and', u'put', u'on', u'their', u'beam', u'ends', u',', u'and', u'the', u'cutting', u'away', u'of', u'masts', u',', u'The', u'sentiment', u'of', u'the', u'huge', u'timbers', u'of', u'old', u'-', u'fashion', u"'", u'd', u'houses', u'and', u'barns', u',', u'The', u'remember', u"'", u'd', u'print', u'or', u'narrative', u',', u'the', u'voyage', u'at', u'a', u'venture', u'of', u'men', u',', u'families', u',', u'goods', u',', u'The', u'disembarkation', u',', u'the', u'founding', u'of', u'a', u'new', u'city', u',', u'The', u'voyage', u'of', u'those', u'who', u'sought', u'a', u'New', u'England', u'and', u'found', u'it', u',', u'the', u'outset', u'anywhere', u',', u'The', u'settlements', u'of', u'the', u'Arkansas', u',', u'Colorado', u',', u'Ottawa', u',', u'Willamette', u',', u'The', u'slow', u'progress', u',', u'the', u'scant', u'fare', u',', u'the', u'axe', u',', u'rifle', u',', u'saddle', u'-', u'bags', u';', u'The', u'beauty', u'of', u'all', u'adventurous', u'and', u'daring', u'persons', u',', u'The', u'beauty', u'of', u'wood', u'-', u'boys', u'and', u'wood', u'-', u'men', u'with', u'their', u'clear', u'untrimm', u"'", u'd', u'faces', u',', u'The', u'beauty', u'of', u'independence', u',', u'departure', u',', u'actions', u'that', u'rely', u'on', u'themselves', u',', u'The', u'American', u'contempt', u'for', u'statutes', u'and', u'ceremonies', u',', u'the', u'boundless', u'impatience', u'of', u'restraint', u',', u'The', u'loose', u'drift', u'of', u'character', u',', u'the', u'inkling', u'through', u'random', u'types', u',', u'the', u'solidification', u';', u'The', u'butcher', u'in', u'the', u'slaughter', u'-', u'house', u',', u'the', u'hands', u'aboard', u'schooners', u'and', u'sloops', u',', u'the', u'raftsman', u',', u'the', u'pioneer', u',', u'Lumbermen', u'in', u'their', u'winter', u'camp', u',', u'daybreak', u'in', u'the', u'woods', u',', u'stripes', u'of', u'snow', u'on', u'the', u'limbs', u'of', u'trees', u',', u'the', u'occasional', u'snapping', u',', u'The', u'glad', u'clear', u'sound', u'of', u'one', u"'", u's', u'own', u'voice', u',', u'the', u'merry', u'song', u',', u'the', u'natural', u'life', u'of', u'the', u'woods', u',', u'the', u'strong', u'day', u"'", u's', u'work', u',', u'The', u'blazing', u'fire', u'at', u'night', u',', u'the', u'sweet', u'taste', u'of', u'supper', u',', u'the', u'talk', u',', u'the', u'bed', u'of', u'hemlock', u'-', u'boughs', u'and', u'the', u'bear', u'-', u'skin', u';', u'The', u'house', u'-', u'builder', u'at', u'work', u'in', u'cities', u'or', u'anywhere', u',', u'The', u'preparatory', u'jointing', u',', u'squaring', u',', u'sawing', u',', u'mortising', u',', u'The', u'hoist', u'-', u'up', u'of', u'beams', u',', u'the', u'push', u'of', u'them', u'in', u'their', u'places', u',', u'laying', u'them', u'regular', u',', u'Setting', u'the', u'studs', u'by', u'their', u'tenons', u'in', u'the', u'mortises', u'according', u'as', u'they', u'were', u'prepared', u',', u'The', u'blows', u'of', u'mallets', u'and', u'hammers', u',', u'the', u'attitudes', u'of', u'the', u'men', u',', u'their', u'curv', u"'", u'd', u'limbs', u',', u'Bending', u',', u'standing', u',', u'astride', u'the', u'beams', u',', u'driving', u'in', u'pins', u',', u'holding', u'on', u'by', u'posts', u'and', u'braces', u',', u'The', u'hook', u"'", u'd', u'arm', u'over', u'the', u'plate', u',', u'the', u'other', u'arm', u'wielding', u'the', u'axe', u',', u'The', u'floor', u'-', u'men', u'forcing', u'the', u'planks', u'close', u'to', u'be', u'nail', u"'", u'd', u',', u'Their', u'postures', u'bringing', u'their', u'weapons', u'downward', u'on', u'the', u'bearers', u',', u'The', u'echoes', u'resounding', u'through', u'the', u'vacant', u'building', u':', u'The', u'huge', u'storehouse', u'carried', u'up', u'in', u'the', u'city', u'well', u'under', u'way', u',', u'The', u'six', u'framing', u'-', u'men', u',', u'two', u'in', u'the', u'middle', u'and', u'two', u'at', u'each', u'end', u',', u'carefully', u'bearing', u'on', u'their', u'shoulders', u'a', u'heavy', u'stick', u'for', u'a', u'cross', u'-', u'beam', u',', u'The', u'crowded', u'line', u'of', u'masons', u'with', u'trowels', u'in', u'their', u'right', u'hands', u'rapidly', u'laying', u'the', u'long', u'side', u'-', u'wall', u',', u'two', u'hundred', u'feet', u'from', u'front', u'to', u'rear', u',', u'The', u'flexible', u'rise', u'and', u'fall', u'of', u'backs', u',', u'the', u'continual', u'click', u'of', u'the', u'trowels', u'striking', u'the', u'bricks', u',', u'The', u'bricks', u'one', u'after', u'another', u'each', u'laid', u'so', u'workmanlike', u'in', u'its', u'place', u',', u'and', u'set', u'with', u'a', u'knock', u'of', u'the', u'trowel', u'-', u'handle', u',', u'The', u'piles', u'of', u'materials', u',', u'the', u'mortar', u'on', u'the', u'mortar', u'-', u'boards', u',', u'and', u'the', u'steady', u'replenishing', u'by', u'the', u'hod', u'-', u'men', u';', u'Spar', u'-', u'makers', u'in', u'the', u'spar', u'-', u'yard', u',', u'the', u'swarming', u'row', u'of', u'well', u'-', u'grown', u'apprentices', u',', u'The', u'swing', u'of', u'their', u'axes', u'on', u'the', u'square', u'-', u'hew', u"'", u'd', u'log', u'shaping', u'it', u'toward', u'the', u'shape', u'of', u'a', u'mast', u',', u'The', u'brisk', u'short', u'crackle', u'of', u'the', u'steel', u'driven', u'slantingly', u'into', u'the', u'pine', u',', u'The', u'butter', u'-', u'color', u"'", u'd', u'chips', u'flying', u'off', u'in', u'great', u'flakes', u'and', u'slivers', u',', u'The', u'limber', u'motion', u'of', u'brawny', u'young', u'arms', u'and', u'hips', u'in', u'easy', u'costumes', u',', u'The', u'constructor', u'of', u'wharves', u',', u'bridges', u',', u'piers', u',', u'bulk', u'-', u'heads', u',', u'floats', u',', u'stays', u'against', u'the', u'sea', u';', u'The', u'city', u'fireman', u',', u'the', u'fire', u'that', u'suddenly', u'bursts', u'forth', u'in', u'the', u'close', u'-', u'pack', u"'", u'd', u'square', u',', u'The', u'arriving', u'engines', u',', u'the', u'hoarse', u'shouts', u',', u'the', u'nimble', u'stepping', u'and', u'daring', u',', u'The', u'strong', u'command', u'through', u'the', u'fire', u'-', u'trumpets', u',', u'the', u'falling', u'in', u'line', u',', u'the', u'rise', u'and', u'fall', u'of', u'the', u'arms', u'forcing', u'the', u'water', u',', u'The', u'slender', u',', u'spasmic', u',', u'blue', u'-', u'white', u'jets', u',', u'the', u'bringing', u'to', u'bear', u'of', u'the', u'hooks', u'and', u'ladders', u'and', u'their', u'execution', u',', u'The', u'crash', u'and', u'cut', u'away', u'of', u'connecting', u'wood', u'-', u'work', u',', u'or', u'through', u'floors', u'if', u'the', u'fire', u'smoulders', u'under', u'them', u',', u'The', u'crowd', u'with', u'their', u'lit', u'faces', u'watching', u',', u'the', u'glare', u'and', u'dense', u'shadows', u';', u'The', u'forger', u'at', u'his', u'forge', u'-', u'furnace', u'and', u'the', u'user', u'of', u'iron', u'after', u'him', u',', u'The', u'maker', u'of', u'the', u'axe', u'large', u'and', u'small', u',', u'and', u'the', u'welder', u'and', u'temperer', u',', u'The', u'chooser', u'breathing', u'his', u'breath', u'on', u'the', u'cold', u'steel', u'and', u'trying', u'the', u'edge', u'with', u'his', u'thumb', u',', u'The', u'one', u'who', u'clean', u'-', u'shapes', u'the', u'handle', u'and', u'sets', u'it', u'firmly', u'in', u'the', u'socket', u';', u'The', u'shadowy', u'processions', u'of', u'the', u'portraits', u'of', u'the', u'past', u'users', u'also', u',', u'The', u'primal', u'patient', u'mechanics', u',', u'the', u'architects', u'and', u'engineers', u',', u'The', u'far', u'-', u'off', u'Assyrian', u'edifice', u'and', u'Mizra', u'edifice', u',', u'The', u'Roman', u'lictors', u'preceding', u'the', u'consuls', u',', u'The', u'antique', u'European', u'warrior', u'with', u'his', u'axe', u'in', u'combat', u',', u'The', u'uplifted', u'arm', u',', u'the', u'clatter', u'of', u'blows', u'on', u'the', u'helmeted', u'head', u',', u'The', u'death', u'-', u'howl', u',', u'the', u'limpsy', u'tumbling', u'body', u',', u'the', u'rush', u'of', u'friend', u'and', u'foe', u'thither', u',', u'The', u'siege', u'of', u'revolted', u'lieges', u'determin', u"'", u'd', u'for', u'liberty', u',', u'The', u'summons', u'to', u'surrender', u',', u'the', u'battering', u'at', u'castle', u'gates', u',', u'the', u'truce', u'and', u'parley', u',', u'The', u'sack', u'of', u'an', u'old', u'city', u'in', u'its', u'time', u',', u'The', u'bursting', u'in', u'of', u'mercenaries', u'and', u'bigots', u'tumultuously', u'and', u'disorderly', u',', u'Roar', u',', u'flames', u',', u'blood', u',', u'drunkenness', u',', u'madness', u',', u'Goods', u'freely', u'rifled', u'from', u'houses', u'and', u'temples', u',', u'screams', u'of', u'women', u'in', u'the', u'gripe', u'of', u'brigands', u',', u'Craft', u'and', u'thievery', u'of', u'camp', u'-', u'followers', u',', u'men', u'running', u',', u'old', u'persons', u'despairing', u',', u'The', u'hell', u'of', u'war', u',', u'the', u'cruelties', u'of', u'creeds', u',', u'The', u'list', u'of', u'all', u'executive', u'deeds', u'and', u'words', u'just', u'or', u'unjust', u',', u'The', u'power', u'of', u'personality', u'just', u'or', u'unjust', u'.']
# 944 [u'Always', u'Florida', u"'", u's', u'green', u'peninsula', u'--', u'always', u'the', u'priceless', u'delta', u'of', u'Louisiana', u'--', u'always', u'the', u'cotton', u'-', u'fields', u'of', u'Alabama', u'and', u'Texas', u',', u'Always', u'California', u"'", u's', u'golden', u'hills', u'and', u'hollows', u',', u'and', u'the', u'silver', u'mountains', u'of', u'New', u'Mexico', u'--', u'always', u'soft', u'-', u'breath', u"'", u'd', u'Cuba', u',', u'Always', u'the', u'vast', u'slope', u'drain', u"'", u'd', u'by', u'the', u'Southern', u'sea', u',', u'inseparable', u'with', u'the', u'slopes', u'drain', u"'", u'd', u'by', u'the', u'Eastern', u'and', u'Western', u'seas', u',', u'The', u'area', u'the', u'eighty', u'-', u'third', u'year', u'of', u'these', u'States', u',', u'the', u'three', u'and', u'a', u'half', u'millions', u'of', u'square', u'miles', u',', u'The', u'eighteen', u'thousand', u'miles', u'of', u'sea', u'-', u'coast', u'and', u'bay', u'-', u'coast', u'on', u'the', u'main', u',', u'the', u'thirty', u'thousand', u'miles', u'of', u'river', u'navigation', u',', u'The', u'seven', u'millions', u'of', u'distinct', u'families', u'and', u'the', u'same', u'number', u'of', u'dwellings', u'--', u'always', u'these', u',', u'and', u'more', u',', u'branching', u'forth', u'into', u'numberless', u'branches', u',', u'Always', u'the', u'free', u'range', u'and', u'diversity', u'--', u'always', u'the', u'continent', u'of', u'Democracy', u';', u'Always', u'the', u'prairies', u',', u'pastures', u',', u'forests', u',', u'vast', u'cities', u',', u'travelers', u',', u'Kanada', u',', u'the', u'snows', u';', u'Always', u'these', u'compact', u'lands', u'tied', u'at', u'the', u'hips', u'with', u'the', u'belt', u'stringing', u'the', u'huge', u'oval', u'lakes', u';', u'Always', u'the', u'West', u'with', u'strong', u'native', u'persons', u',', u'the', u'increasing', u'density', u'there', u',', u'the', u'habitans', u',', u'friendly', u',', u'threatening', u',', u'ironical', u',', u'scorning', u'invaders', u';', u'All', u'sights', u',', u'South', u',', u'North', u',', u'East', u'--', u'all', u'deeds', u',', u'promiscuously', u'done', u'at', u'all', u'times', u',', u'All', u'characters', u',', u'movements', u',', u'growths', u',', u'a', u'few', u'noticed', u',', u'myriads', u'unnoticed', u',', u'Through', u'Mannahatta', u"'", u's', u'streets', u'I', u'walking', u',', u'these', u'things', u'gathering', u',', u'On', u'interior', u'rivers', u'by', u'night', u'in', u'the', u'glare', u'of', u'pine', u'knots', u',', u'steamboats', u'wooding', u'up', u',', u'Sunlight', u'by', u'day', u'on', u'the', u'valley', u'of', u'the', u'Susquehanna', u',', u'and', u'on', u'the', u'valleys', u'of', u'the', u'Potomac', u'and', u'Rappahannock', u',', u'and', u'the', u'valleys', u'of', u'the', u'Roanoke', u'and', u'Delaware', u',', u'In', u'their', u'northerly', u'wilds', u'beasts', u'of', u'prey', u'haunting', u'the', u'Adirondacks', u'the', u'hills', u',', u'or', u'lapping', u'the', u'Saginaw', u'waters', u'to', u'drink', u',', u'In', u'a', u'lonesome', u'inlet', u'a', u'sheldrake', u'lost', u'from', u'the', u'flock', u',', u'sitting', u'on', u'the', u'water', u'rocking', u'silently', u',', u'In', u'farmers', u"'", u'barns', u'oxen', u'in', u'the', u'stable', u',', u'their', u'harvest', u'labor', u'done', u',', u'they', u'rest', u'standing', u',', u'they', u'are', u'too', u'tired', u',', u'Afar', u'on', u'arctic', u'ice', u'the', u'she', u'-', u'walrus', u'lying', u'drowsily', u'while', u'her', u'cubs', u'play', u'around', u',', u'The', u'hawk', u'sailing', u'where', u'men', u'have', u'not', u'yet', u'sail', u"'", u'd', u',', u'the', u'farthest', u'polar', u'sea', u',', u'ripply', u',', u'crystalline', u',', u'open', u',', u'beyond', u'the', u'floes', u',', u'White', u'drift', u'spooning', u'ahead', u'where', u'the', u'ship', u'in', u'the', u'tempest', u'dashes', u',', u'On', u'solid', u'land', u'what', u'is', u'done', u'in', u'cities', u'as', u'the', u'bells', u'strike', u'midnight', u'together', u',', u'In', u'primitive', u'woods', u'the', u'sounds', u'there', u'also', u'sounding', u',', u'the', u'howl', u'of', u'the', u'wolf', u',', u'the', u'scream', u'of', u'the', u'panther', u',', u'and', u'the', u'hoarse', u'bellow', u'of', u'the', u'elk', u',', u'In', u'winter', u'beneath', u'the', u'hard', u'blue', u'ice', u'of', u'Moosehead', u'lake', u',', u'in', u'summer', u'visible', u'through', u'the', u'clear', u'waters', u',', u'the', u'great', u'trout', u'swimming', u',', u'In', u'lower', u'latitudes', u'in', u'warmer', u'air', u'in', u'the', u'Carolinas', u'the', u'large', u'black', u'buzzard', u'floating', u'slowly', u'high', u'beyond', u'the', u'tree', u'tops', u',', u'Below', u',', u'the', u'red', u'cedar', u'festoon', u"'", u'd', u'with', u'tylandria', u',', u'the', u'pines', u'and', u'cypresses', u'growing', u'out', u'of', u'the', u'white', u'sand', u'that', u'spreads', u'far', u'and', u'flat', u',', u'Rude', u'boats', u'descending', u'the', u'big', u'Pedee', u',', u'climbing', u'plants', u',', u'parasites', u'with', u'color', u"'", u'd', u'flowers', u'and', u'berries', u'enveloping', u'huge', u'trees', u',', u'The', u'waving', u'drapery', u'on', u'the', u'live', u'-', u'oak', u'trailing', u'long', u'and', u'low', u',', u'noiselessly', u'waved', u'by', u'the', u'wind', u',', u'The', u'camp', u'of', u'Georgia', u'wagoners', u'just', u'after', u'dark', u',', u'the', u'supper', u'-', u'fires', u'and', u'the', u'cooking', u'and', u'eating', u'by', u'whites', u'and', u'negroes', u',', u'Thirty', u'or', u'forty', u'great', u'wagons', u',', u'the', u'mules', u',', u'cattle', u',', u'horses', u',', u'feeding', u'from', u'troughs', u',', u'The', u'shadows', u',', u'gleams', u',', u'up', u'under', u'the', u'leaves', u'of', u'the', u'old', u'sycamore', u'-', u'trees', u',', u'the', u'flames', u'with', u'the', u'black', u'smoke', u'from', u'the', u'pitch', u'-', u'pine', u'curling', u'and', u'rising', u';', u'Southern', u'fishermen', u'fishing', u',', u'the', u'sounds', u'and', u'inlets', u'of', u'North', u'Carolina', u"'", u's', u'coast', u',', u'the', u'shad', u'-', u'fishery', u'and', u'the', u'herring', u'-', u'fishery', u',', u'the', u'large', u'sweep', u'-', u'seines', u',', u'the', u'windlasses', u'on', u'shore', u'work', u"'", u'd', u'by', u'horses', u',', u'the', u'clearing', u',', u'curing', u',', u'and', u'packing', u'-', u'houses', u';', u'Deep', u'in', u'the', u'forest', u'in', u'piney', u'woods', u'turpentine', u'dropping', u'from', u'the', u'incisions', u'in', u'the', u'trees', u',', u'there', u'are', u'the', u'turpentine', u'works', u',', u'There', u'are', u'the', u'negroes', u'at', u'work', u'in', u'good', u'health', u',', u'the', u'ground', u'in', u'all', u'directions', u'is', u'cover', u"'", u'd', u'with', u'pine', u'straw', u';', u'In', u'Tennessee', u'and', u'Kentucky', u'slaves', u'busy', u'in', u'the', u'coalings', u',', u'at', u'the', u'forge', u',', u'by', u'the', u'furnace', u'-', u'blaze', u',', u'or', u'at', u'the', u'corn', u'-', u'shucking', u',', u'In', u'Virginia', u',', u'the', u'planter', u"'", u's', u'son', u'returning', u'after', u'a', u'long', u'absence', u',', u'joyfully', u'welcom', u"'", u'd', u'and', u'kiss', u"'", u'd', u'by', u'the', u'aged', u'mulatto', u'nurse', u',', u'On', u'rivers', u'boatmen', u'safely', u'moor', u"'", u'd', u'at', u'nightfall', u'in', u'their', u'boats', u'under', u'shelter', u'of', u'high', u'banks', u',', u'Some', u'of', u'the', u'younger', u'men', u'dance', u'to', u'the', u'sound', u'of', u'the', u'banjo', u'or', u'fiddle', u',', u'others', u'sit', u'on', u'the', u'gunwale', u'smoking', u'and', u'talking', u';', u'Late', u'in', u'the', u'afternoon', u'the', u'mocking', u'-', u'bird', u',', u'the', u'American', u'mimic', u',', u'singing', u'in', u'the', u'Great', u'Dismal', u'Swamp', u',', u'There', u'are', u'the', u'greenish', u'waters', u',', u'the', u'resinous', u'odor', u',', u'the', u'plenteous', u'moss', u',', u'the', u'cypress', u'-', u'tree', u',', u'and', u'the', u'juniper', u'-', u'tree', u';', u'Northward', u',', u'young', u'men', u'of', u'Mannahatta', u',', u'the', u'target', u'company', u'from', u'an', u'excursion', u'returning', u'home', u'at', u'evening', u',', u'the', u'musket', u'-', u'muzzles', u'all', u'bear', u'bunches', u'of', u'flowers', u'presented', u'by', u'women', u';', u'Children', u'at', u'play', u',', u'or', u'on', u'his', u'father', u"'", u's', u'lap', u'a', u'young', u'boy', u'fallen', u'asleep', u',', u'(', u'how', u'his', u'lips', u'move', u'!']
# 827 [u'Spontaneous', u'me', u',', u'Nature', u',', u'The', u'loving', u'day', u',', u'the', u'mounting', u'sun', u',', u'the', u'friend', u'I', u'am', u'happy', u'with', u',', u'The', u'arm', u'of', u'my', u'friend', u'hanging', u'idly', u'over', u'my', u'shoulder', u',', u'The', u'hillside', u'whiten', u"'", u'd', u'with', u'blossoms', u'of', u'the', u'mountain', u'ash', u',', u'The', u'same', u'late', u'in', u'autumn', u',', u'the', u'hues', u'of', u'red', u',', u'yellow', u',', u'drab', u',', u'purple', u',', u'and', u'light', u'and', u'dark', u'green', u',', u'The', u'rich', u'coverlet', u'of', u'the', u'grass', u',', u'animals', u'and', u'birds', u',', u'the', u'private', u'untrimm', u"'", u'd', u'bank', u',', u'the', u'primitive', u'apples', u',', u'the', u'pebble', u'-', u'stones', u',', u'Beautiful', u'dripping', u'fragments', u',', u'the', u'negligent', u'list', u'of', u'one', u'after', u'another', u'as', u'I', u'happen', u'to', u'call', u'them', u'to', u'me', u'or', u'think', u'of', u'them', u',', u'The', u'real', u'poems', u',', u'(', u'what', u'we', u'call', u'poems', u'being', u'merely', u'pictures', u',)', u'The', u'poems', u'of', u'the', u'privacy', u'of', u'the', u'night', u',', u'and', u'of', u'men', u'like', u'me', u',', u'This', u'poem', u'drooping', u'shy', u'and', u'unseen', u'that', u'I', u'always', u'carry', u',', u'and', u'that', u'all', u'men', u'carry', u',', u'(', u'Know', u'once', u'for', u'all', u',', u'avow', u"'", u'd', u'on', u'purpose', u',', u'wherever', u'are', u'men', u'like', u'me', u',', u'are', u'our', u'lusty', u'lurking', u'masculine', u'poems', u',)', u'Love', u'-', u'thoughts', u',', u'love', u'-', u'juice', u',', u'love', u'-', u'odor', u',', u'love', u'-', u'yielding', u',', u'love', u'-', u'climbers', u',', u'and', u'the', u'climbing', u'sap', u',', u'Arms', u'and', u'hands', u'of', u'love', u',', u'lips', u'of', u'love', u',', u'phallic', u'thumb', u'of', u'love', u',', u'breasts', u'of', u'love', u',', u'bellies', u'press', u"'", u'd', u'and', u'glued', u'together', u'with', u'love', u',', u'Earth', u'of', u'chaste', u'love', u',', u'life', u'that', u'is', u'only', u'life', u'after', u'love', u',', u'The', u'body', u'of', u'my', u'love', u',', u'the', u'body', u'of', u'the', u'woman', u'I', u'love', u',', u'the', u'body', u'of', u'the', u'man', u',', u'the', u'body', u'of', u'the', u'earth', u',', u'Soft', u'forenoon', u'airs', u'that', u'blow', u'from', u'the', u'south', u'-', u'west', u',', u'The', u'hairy', u'wild', u'-', u'bee', u'that', u'murmurs', u'and', u'hankers', u'up', u'and', u'down', u',', u'that', u'gripes', u'the', u'full', u'-', u'grown', u'lady', u'-', u'flower', u',', u'curves', u'upon', u'her', u'with', u'amorous', u'firm', u'legs', u',', u'takes', u'his', u'will', u'of', u'her', u',', u'and', u'holds', u'himself', u'tremulous', u'and', u'tight', u'till', u'he', u'is', u'satisfied', u';', u'The', u'wet', u'of', u'woods', u'through', u'the', u'early', u'hours', u',', u'Two', u'sleepers', u'at', u'night', u'lying', u'close', u'together', u'as', u'they', u'sleep', u',', u'one', u'with', u'an', u'arm', u'slanting', u'down', u'across', u'and', u'below', u'the', u'waist', u'of', u'the', u'other', u',', u'The', u'smell', u'of', u'apples', u',', u'aromas', u'from', u'crush', u"'", u'd', u'sage', u'-', u'plant', u',', u'mint', u',', u'birch', u'-', u'bark', u',', u'The', u'boy', u"'", u's', u'longings', u',', u'the', u'glow', u'and', u'pressure', u'as', u'he', u'confides', u'to', u'me', u'what', u'he', u'was', u'dreaming', u',', u'The', u'dead', u'leaf', u'whirling', u'its', u'spiral', u'whirl', u'and', u'falling', u'still', u'and', u'content', u'to', u'the', u'ground', u',', u'The', u'no', u'-', u'form', u"'", u'd', u'stings', u'that', u'sights', u',', u'people', u',', u'objects', u',', u'sting', u'me', u'with', u',', u'The', u'hubb', u"'", u'd', u'sting', u'of', u'myself', u',', u'stinging', u'me', u'as', u'much', u'as', u'it', u'ever', u'can', u'any', u'one', u',', u'The', u'sensitive', u',', u'orbic', u',', u'underlapp', u"'", u'd', u'brothers', u',', u'that', u'only', u'privileged', u'feelers', u'may', u'be', u'intimate', u'where', u'they', u'are', u',', u'The', u'curious', u'roamer', u'the', u'hand', u'roaming', u'all', u'over', u'the', u'body', u',', u'the', u'bashful', u'withdrawing', u'of', u'flesh', u'where', u'the', u'fingers', u'soothingly', u'pause', u'and', u'edge', u'themselves', u',', u'The', u'limpid', u'liquid', u'within', u'the', u'young', u'man', u',', u'The', u'vex', u"'", u'd', u'corrosion', u'so', u'pensive', u'and', u'so', u'painful', u',', u'The', u'torment', u',', u'the', u'irritable', u'tide', u'that', u'will', u'not', u'be', u'at', u'rest', u',', u'The', u'like', u'of', u'the', u'same', u'I', u'feel', u',', u'the', u'like', u'of', u'the', u'same', u'in', u'others', u',', u'The', u'young', u'man', u'that', u'flushes', u'and', u'flushes', u',', u'and', u'the', u'young', u'woman', u'that', u'flushes', u'and', u'flushes', u',', u'The', u'young', u'man', u'that', u'wakes', u'deep', u'at', u'night', u',', u'the', u'hot', u'hand', u'seeking', u'to', u'repress', u'what', u'would', u'master', u'him', u',', u'The', u'mystic', u'amorous', u'night', u',', u'the', u'strange', u'half', u'-', u'welcome', u'pangs', u',', u'visions', u',', u'sweats', u',', u'The', u'pulse', u'pounding', u'through', u'palms', u'and', u'trembling', u'encircling', u'fingers', u',', u'the', u'young', u'man', u'all', u'color', u"'", u'd', u',', u'red', u',', u'ashamed', u',', u'angry', u';', u'The', u'souse', u'upon', u'me', u'of', u'my', u'lover', u'the', u'sea', u',', u'as', u'I', u'lie', u'willing', u'and', u'naked', u',', u'The', u'merriment', u'of', u'the', u'twin', u'babes', u'that', u'crawl', u'over', u'the', u'grass', u'in', u'the', u'sun', u',', u'the', u'mother', u'never', u'turning', u'her', u'vigilant', u'eyes', u'from', u'them', u',', u'The', u'walnut', u'-', u'trunk', u',', u'the', u'walnut', u'-', u'husks', u',', u'and', u'the', u'ripening', u'or', u'ripen', u"'", u'd', u'long', u'-', u'round', u'walnuts', u',', u'The', u'continence', u'of', u'vegetables', u',', u'birds', u',', u'animals', u',', u'The', u'consequent', u'meanness', u'of', u'me', u'should', u'I', u'skulk', u'or', u'find', u'myself', u'indecent', u',', u'while', u'birds', u'and', u'animals', u'never', u'once', u'skulk', u'or', u'find', u'themselves', u'indecent', u',', u'The', u'great', u'chastity', u'of', u'paternity', u',', u'to', u'match', u'the', u'great', u'chastity', u'of', u'maternity', u',', u'The', u'oath', u'of', u'procreation', u'I', u'have', u'sworn', u',', u'my', u'Adamic', u'and', u'fresh', u'daughters', u',', u'The', u'greed', u'that', u'eats', u'me', u'day', u'and', u'night', u'with', u'hungry', u'gnaw', u',', u'till', u'I', u'saturate', u'what', u'shall', u'produce', u'boys', u'to', u'fill', u'my', u'place', u'when', u'I', u'am', u'through', u',', u'The', u'wholesome', u'relief', u',', u'repose', u',', u'content', u',', u'And', u'this', u'bunch', u'pluck', u"'", u'd', u'at', u'random', u'from', u'myself', u',', u'It', u'has', u'done', u'its', u'work', u'--', u'I', u'toss', u'it', u'carelessly', u'to', u'fall', u'where', u'it', u'may', u'.']
# 687 [u'House', u'-', u'building', u',', u'measuring', u',', u'sawing', u'the', u'boards', u',', u'Blacksmithing', u',', u'glass', u'-', u'blowing', u',', u'nail', u'-', u'making', u',', u'coopering', u',', u'tin', u'-', u'roofing', u',', u'shingle', u'-', u'dressing', u',', u'Ship', u'-', u'joining', u',', u'dock', u'-', u'building', u',', u'fish', u'-', u'curing', u',', u'flagging', u'of', u'sidewalks', u'by', u'flaggers', u',', u'The', u'pump', u',', u'the', u'pile', u'-', u'driver', u',', u'the', u'great', u'derrick', u',', u'the', u'coal', u'-', u'kiln', u'and', u'brickkiln', u',', u'Coal', u'-', u'mines', u'and', u'all', u'that', u'is', u'down', u'there', u',', u'the', u'lamps', u'in', u'the', u'darkness', u',', u'echoes', u',', u'songs', u',', u'what', u'meditations', u',', u'what', u'vast', u'native', u'thoughts', u'looking', u'through', u'smutch', u"'", u'd', u'faces', u',', u'Iron', u'-', u'works', u',', u'forge', u'-', u'fires', u'in', u'the', u'mountains', u'or', u'by', u'river', u'-', u'banks', u',', u'men', u'around', u'feeling', u'the', u'melt', u'with', u'huge', u'crowbars', u',', u'lumps', u'of', u'ore', u',', u'the', u'due', u'combining', u'of', u'ore', u',', u'limestone', u',', u'coal', u',', u'The', u'blast', u'-', u'furnace', u'and', u'the', u'puddling', u'-', u'furnace', u',', u'the', u'loup', u'-', u'lump', u'at', u'the', u'bottom', u'of', u'the', u'melt', u'at', u'last', u',', u'the', u'rolling', u'-', u'mill', u',', u'the', u'stumpy', u'bars', u'of', u'pig', u'-', u'iron', u',', u'the', u'strong', u'clean', u'-', u'shaped', u'Trail', u'for', u'railroads', u',', u'Oil', u'-', u'works', u',', u'silk', u'-', u'works', u',', u'white', u'-', u'lead', u'-', u'works', u',', u'the', u'sugar', u'-', u'house', u',', u'steam', u'-', u'saws', u',', u'the', u'great', u'mills', u'and', u'factories', u',', u'Stone', u'-', u'cutting', u',', u'shapely', u'trimmings', u'for', u'facades', u'or', u'window', u'or', u'door', u'-', u'lintels', u',', u'the', u'mallet', u',', u'the', u'tooth', u'-', u'chisel', u',', u'the', u'jib', u'to', u'protect', u'the', u'thumb', u',', u'The', u'calking', u'-', u'iron', u',', u'the', u'kettle', u'of', u'boiling', u'vault', u'-', u'cement', u',', u'and', u'the', u'fire', u'under', u'the', u'kettle', u',', u'The', u'cotton', u'-', u'bale', u',', u'the', u'stevedore', u"'", u's', u'hook', u',', u'the', u'saw', u'and', u'buck', u'of', u'the', u'sawyer', u',', u'the', u'mould', u'of', u'the', u'moulder', u',', u'the', u'working', u'-', u'knife', u'of', u'the', u'butcher', u',', u'the', u'ice', u'-', u'saw', u',', u'and', u'all', u'the', u'work', u'with', u'ice', u',', u'The', u'work', u'and', u'tools', u'of', u'the', u'rigger', u',', u'grappler', u',', u'sail', u'-', u'maker', u',', u'block', u'-', u'maker', u',', u'Goods', u'of', u'gutta', u'-', u'percha', u',', u'papier', u'-', u'mache', u',', u'colors', u',', u'brushes', u',', u'brush', u'-', u'making', u',', u'glazier', u"'", u's', u'implements', u',', u'The', u'veneer', u'and', u'glue', u'-', u'pot', u',', u'the', u'confectioner', u"'", u's', u'ornaments', u',', u'the', u'decanter', u'and', u'glasses', u',', u'the', u'shears', u'and', u'flat', u'-', u'iron', u',', u'The', u'awl', u'and', u'knee', u'-', u'strap', u',', u'the', u'pint', u'measure', u'and', u'quart', u'measure', u',', u'the', u'counter', u'and', u'stool', u',', u'the', u'writing', u'-', u'pen', u'of', u'quill', u'or', u'metal', u',', u'the', u'making', u'of', u'all', u'sorts', u'of', u'edged', u'tools', u',', u'The', u'brewery', u',', u'brewing', u',', u'the', u'malt', u',', u'the', u'vats', u',', u'every', u'thing', u'that', u'is', u'done', u'by', u'brewers', u',', u'wine', u'-', u'makers', u',', u'vinegar', u'-', u'makers', u',', u'Leather', u'-', u'dressing', u',', u'coach', u'-', u'making', u',', u'boiler', u'-', u'making', u',', u'rope', u'-', u'twisting', u',', u'distilling', u',', u'sign', u'-', u'painting', u',', u'lime', u'-', u'burning', u',', u'cotton', u'-', u'picking', u',', u'electroplating', u',', u'electrotyping', u',', u'stereotyping', u',', u'Stave', u'-', u'machines', u',', u'planing', u'-', u'machines', u',', u'reaping', u'-', u'machines', u',', u'ploughing', u'-', u'machines', u',', u'thrashing', u'-', u'machines', u',', u'steam', u'wagons', u',', u'The', u'cart', u'of', u'the', u'carman', u',', u'the', u'omnibus', u',', u'the', u'ponderous', u'dray', u',', u'Pyrotechny', u',', u'letting', u'off', u'color', u"'", u'd', u'fireworks', u'at', u'night', u',', u'fancy', u'figures', u'and', u'jets', u';', u'Beef', u'on', u'the', u'butcher', u"'", u's', u'stall', u',', u'the', u'slaughter', u'-', u'house', u'of', u'the', u'butcher', u',', u'the', u'butcher', u'in', u'his', u'killing', u'-', u'clothes', u',', u'The', u'pens', u'of', u'live', u'pork', u',', u'the', u'killing', u'-', u'hammer', u',', u'the', u'hog', u'-', u'hook', u',', u'the', u'scalder', u"'", u's', u'tub', u',', u'gutting', u',', u'the', u'cutter', u"'", u's', u'cleaver', u',', u'the', u'packer', u"'", u's', u'maul', u',', u'and', u'the', u'plenteous', u'winterwork', u'of', u'pork', u'-', u'packing', u',', u'Flour', u'-', u'works', u',', u'grinding', u'of', u'wheat', u',', u'rye', u',', u'maize', u',', u'rice', u',', u'the', u'barrels', u'and', u'the', u'half', u'and', u'quarter', u'barrels', u',', u'the', u'loaded', u'barges', u',', u'the', u'high', u'piles', u'on', u'wharves', u'and', u'levees', u',', u'The', u'men', u'and', u'the', u'work', u'of', u'the', u'men', u'on', u'ferries', u',', u'railroads', u',', u'coasters', u',', u'fish', u'-', u'boats', u',', u'canals', u';', u'The', u'hourly', u'routine', u'of', u'your', u'own', u'or', u'any', u'man', u"'", u's', u'life', u',', u'the', u'shop', u',', u'yard', u',', u'store', u',', u'or', u'factory', u',', u'These', u'shows', u'all', u'near', u'you', u'by', u'day', u'and', u'night', u'--', u'workman', u'!']
# 657 [u'15', u'The', u'pure', u'contralto', u'sings', u'in', u'the', u'organ', u'loft', u',', u'The', u'carpenter', u'dresses', u'his', u'plank', u',', u'the', u'tongue', u'of', u'his', u'foreplane', u'whistles', u'its', u'wild', u'ascending', u'lisp', u',', u'The', u'married', u'and', u'unmarried', u'children', u'ride', u'home', u'to', u'their', u'Thanksgiving', u'dinner', u',', u'The', u'pilot', u'seizes', u'the', u'king', u'-', u'pin', u',', u'he', u'heaves', u'down', u'with', u'a', u'strong', u'arm', u',', u'The', u'mate', u'stands', u'braced', u'in', u'the', u'whale', u'-', u'boat', u',', u'lance', u'and', u'harpoon', u'are', u'ready', u',', u'The', u'duck', u'-', u'shooter', u'walks', u'by', u'silent', u'and', u'cautious', u'stretches', u',', u'The', u'deacons', u'are', u'ordain', u"'", u'd', u'with', u'cross', u"'", u'd', u'hands', u'at', u'the', u'altar', u',', u'The', u'spinning', u'-', u'girl', u'retreats', u'and', u'advances', u'to', u'the', u'hum', u'of', u'the', u'big', u'wheel', u',', u'The', u'farmer', u'stops', u'by', u'the', u'bars', u'as', u'he', u'walks', u'on', u'a', u'First', u'-', u'day', u'loafe', u'and', u'looks', u'at', u'the', u'oats', u'and', u'rye', u',', u'The', u'lunatic', u'is', u'carried', u'at', u'last', u'to', u'the', u'asylum', u'a', u'confirm', u"'", u'd', u'case', u',', u'(', u'He', u'will', u'never', u'sleep', u'any', u'more', u'as', u'he', u'did', u'in', u'the', u'cot', u'in', u'his', u'mother', u"'", u's', u'bed', u'-', u'room', u';)', u'The', u'jour', u'printer', u'with', u'gray', u'head', u'and', u'gaunt', u'jaws', u'works', u'at', u'his', u'case', u',', u'He', u'turns', u'his', u'quid', u'of', u'tobacco', u'while', u'his', u'eyes', u'blurr', u'with', u'the', u'manuscript', u';', u'The', u'malform', u"'", u'd', u'limbs', u'are', u'tied', u'to', u'the', u'surgeon', u"'", u's', u'table', u',', u'What', u'is', u'removed', u'drops', u'horribly', u'in', u'a', u'pail', u';', u'The', u'quadroon', u'girl', u'is', u'sold', u'at', u'the', u'auction', u'-', u'stand', u',', u'the', u'drunkard', u'nods', u'by', u'the', u'bar', u'-', u'room', u'stove', u',', u'The', u'machinist', u'rolls', u'up', u'his', u'sleeves', u',', u'the', u'policeman', u'travels', u'his', u'beat', u',', u'the', u'gate', u'-', u'keeper', u'marks', u'who', u'pass', u',', u'The', u'young', u'fellow', u'drives', u'the', u'express', u'-', u'wagon', u',', u'(', u'I', u'love', u'him', u',', u'though', u'I', u'do', u'not', u'know', u'him', u';)', u'The', u'half', u'-', u'breed', u'straps', u'on', u'his', u'light', u'boots', u'to', u'compete', u'in', u'the', u'race', u',', u'The', u'western', u'turkey', u'-', u'shooting', u'draws', u'old', u'and', u'young', u',', u'some', u'lean', u'on', u'their', u'rifles', u',', u'some', u'sit', u'on', u'logs', u',', u'Out', u'from', u'the', u'crowd', u'steps', u'the', u'marksman', u',', u'takes', u'his', u'position', u',', u'levels', u'his', u'piece', u';', u'The', u'groups', u'of', u'newly', u'-', u'come', u'immigrants', u'cover', u'the', u'wharf', u'or', u'levee', u',', u'As', u'the', u'woolly', u'-', u'pates', u'hoe', u'in', u'the', u'sugar', u'-', u'field', u',', u'the', u'overseer', u'views', u'them', u'from', u'his', u'saddle', u',', u'The', u'bugle', u'calls', u'in', u'the', u'ball', u'-', u'room', u',', u'the', u'gentlemen', u'run', u'for', u'their', u'partners', u',', u'the', u'dancers', u'bow', u'to', u'each', u'other', u',', u'The', u'youth', u'lies', u'awake', u'in', u'the', u'cedar', u'-', u'roof', u"'", u'd', u'garret', u'and', u'harks', u'to', u'the', u'musical', u'rain', u',', u'The', u'Wolverine', u'sets', u'traps', u'on', u'the', u'creek', u'that', u'helps', u'fill', u'the', u'Huron', u',', u'The', u'squaw', u'wrapt', u'in', u'her', u'yellow', u'-', u'hemm', u"'", u'd', u'cloth', u'is', u'offering', u'moccasins', u'and', u'bead', u'-', u'bags', u'for', u'sale', u',', u'The', u'connoisseur', u'peers', u'along', u'the', u'exhibition', u'-', u'gallery', u'with', u'half', u'-', u'shut', u'eyes', u'bent', u'sideways', u',', u'As', u'the', u'deck', u'-', u'hands', u'make', u'fast', u'the', u'steamboat', u'the', u'plank', u'is', u'thrown', u'for', u'the', u'shore', u'-', u'going', u'passengers', u',', u'The', u'young', u'sister', u'holds', u'out', u'the', u'skein', u'while', u'the', u'elder', u'sister', u'winds', u'it', u'off', u'in', u'a', u'ball', u',', u'and', u'stops', u'now', u'and', u'then', u'for', u'the', u'knots', u',', u'The', u'one', u'-', u'year', u'wife', u'is', u'recovering', u'and', u'happy', u'having', u'a', u'week', u'ago', u'borne', u'her', u'first', u'child', u',', u'The', u'clean', u'-', u'hair', u"'", u'd', u'Yankee', u'girl', u'works', u'with', u'her', u'sewing', u'-', u'machine', u'or', u'in', u'the', u'factory', u'or', u'mill', u',', u'The', u'paving', u'-', u'man', u'leans', u'on', u'his', u'two', u'-', u'handed', u'rammer', u',', u'the', u'reporter', u"'", u's', u'lead', u'flies', u'swiftly', u'over', u'the', u'note', u'-', u'book', u',', u'the', u'sign', u'-', u'painter', u'is', u'lettering', u'with', u'blue', u'and', u'gold', u',', u'The', u'canal', u'boy', u'trots', u'on', u'the', u'tow', u'-', u'path', u',', u'the', u'book', u'-', u'keeper', u'counts', u'at', u'his', u'desk', u',', u'the', u'shoemaker', u'waxes', u'his', u'thread', u',', u'The', u'conductor', u'beats', u'time', u'for', u'the', u'band', u'and', u'all', u'the', u'performers', u'follow', u'him', u',', u'The', u'child', u'is', u'baptized', u',', u'the', u'convert', u'is', u'making', u'his', u'first', u'professions', u',', u'The', u'regatta', u'is', u'spread', u'on', u'the', u'bay', u',', u'the', u'race', u'is', u'begun', u',', u'(', u'how', u'the', u'white', u'sails', u'sparkle', u'!)']
# 653 [u'I', u'dare', u'not', u'desert', u'the', u'likes', u'of', u'you', u'in', u'other', u'men', u'and', u'women', u',', u'nor', u'the', u'likes', u'of', u'the', u'parts', u'of', u'you', u',', u'I', u'believe', u'the', u'likes', u'of', u'you', u'are', u'to', u'stand', u'or', u'fall', u'with', u'the', u'likes', u'of', u'the', u'soul', u',', u'(', u'and', u'that', u'they', u'are', u'the', u'soul', u',)', u'I', u'believe', u'the', u'likes', u'of', u'you', u'shall', u'stand', u'or', u'fall', u'with', u'my', u'poems', u',', u'and', u'that', u'they', u'are', u'my', u'poems', u',', u'Man', u"'", u's', u',', u'woman', u"'", u's', u',', u'child', u',', u'youth', u"'", u's', u',', u'wife', u"'", u's', u',', u'husband', u"'", u's', u',', u'mother', u"'", u's', u',', u'father', u"'", u's', u',', u'young', u'man', u"'", u's', u',', u'young', u'woman', u"'", u's', u'poems', u',', u'Head', u',', u'neck', u',', u'hair', u',', u'ears', u',', u'drop', u'and', u'tympan', u'of', u'the', u'ears', u',', u'Eyes', u',', u'eye', u'-', u'fringes', u',', u'iris', u'of', u'the', u'eye', u',', u'eyebrows', u',', u'and', u'the', u'waking', u'or', u'sleeping', u'of', u'the', u'lids', u',', u'Mouth', u',', u'tongue', u',', u'lips', u',', u'teeth', u',', u'roof', u'of', u'the', u'mouth', u',', u'jaws', u',', u'and', u'the', u'jaw', u'-', u'hinges', u',', u'Nose', u',', u'nostrils', u'of', u'the', u'nose', u',', u'and', u'the', u'partition', u',', u'Cheeks', u',', u'temples', u',', u'forehead', u',', u'chin', u',', u'throat', u',', u'back', u'of', u'the', u'neck', u',', u'neck', u'-', u'slue', u',', u'Strong', u'shoulders', u',', u'manly', u'beard', u',', u'scapula', u',', u'hind', u'-', u'shoulders', u',', u'and', u'the', u'ample', u'side', u'-', u'round', u'of', u'the', u'chest', u',', u'Upper', u'-', u'arm', u',', u'armpit', u',', u'elbow', u'-', u'socket', u',', u'lower', u'-', u'arm', u',', u'arm', u'-', u'sinews', u',', u'arm', u'-', u'bones', u',', u'Wrist', u'and', u'wrist', u'-', u'joints', u',', u'hand', u',', u'palm', u',', u'knuckles', u',', u'thumb', u',', u'forefinger', u',', u'finger', u'-', u'joints', u',', u'finger', u'-', u'nails', u',', u'Broad', u'breast', u'-', u'front', u',', u'curling', u'hair', u'of', u'the', u'breast', u',', u'breast', u'-', u'bone', u',', u'breast', u'-', u'side', u',', u'Ribs', u',', u'belly', u',', u'backbone', u',', u'joints', u'of', u'the', u'backbone', u',', u'Hips', u',', u'hip', u'-', u'sockets', u',', u'hip', u'-', u'strength', u',', u'inward', u'and', u'outward', u'round', u',', u'man', u'-', u'balls', u',', u'man', u'-', u'root', u',', u'Strong', u'set', u'of', u'thighs', u',', u'well', u'carrying', u'the', u'trunk', u'above', u',', u'Leg', u'-', u'fibres', u',', u'knee', u',', u'knee', u'-', u'pan', u',', u'upper', u'-', u'leg', u',', u'under', u'-', u'leg', u',', u'Ankles', u',', u'instep', u',', u'foot', u'-', u'ball', u',', u'toes', u',', u'toe', u'-', u'joints', u',', u'the', u'heel', u';', u'All', u'attitudes', u',', u'all', u'the', u'shapeliness', u',', u'all', u'the', u'belongings', u'of', u'my', u'or', u'your', u'body', u'or', u'of', u'any', u'one', u"'", u's', u'body', u',', u'male', u'or', u'female', u',', u'The', u'lung', u'-', u'sponges', u',', u'the', u'stomach', u'-', u'sac', u',', u'the', u'bowels', u'sweet', u'and', u'clean', u',', u'The', u'brain', u'in', u'its', u'folds', u'inside', u'the', u'skull', u'-', u'frame', u',', u'Sympathies', u',', u'heart', u'-', u'valves', u',', u'palate', u'-', u'valves', u',', u'sexuality', u',', u'maternity', u',', u'Womanhood', u',', u'and', u'all', u'that', u'is', u'a', u'woman', u',', u'and', u'the', u'man', u'that', u'comes', u'from', u'woman', u',', u'The', u'womb', u',', u'the', u'teats', u',', u'nipples', u',', u'breast', u'-', u'milk', u',', u'tears', u',', u'laughter', u',', u'weeping', u',', u'love', u'-', u'looks', u',', u'love', u'-', u'perturbations', u'and', u'risings', u',', u'The', u'voice', u',', u'articulation', u',', u'language', u',', u'whispering', u',', u'shouting', u'aloud', u',', u'Food', u',', u'drink', u',', u'pulse', u',', u'digestion', u',', u'sweat', u',', u'sleep', u',', u'walking', u',', u'swimming', u',', u'Poise', u'on', u'the', u'hips', u',', u'leaping', u',', u'reclining', u',', u'embracing', u',', u'arm', u'-', u'curving', u'and', u'tightening', u',', u'The', u'continual', u'changes', u'of', u'the', u'flex', u'of', u'the', u'mouth', u',', u'and', u'around', u'the', u'eyes', u',', u'The', u'skin', u',', u'the', u'sunburnt', u'shade', u',', u'freckles', u',', u'hair', u',', u'The', u'curious', u'sympathy', u'one', u'feels', u'when', u'feeling', u'with', u'the', u'hand', u'the', u'naked', u'meat', u'of', u'the', u'body', u',', u'The', u'circling', u'rivers', u'the', u'breath', u',', u'and', u'breathing', u'it', u'in', u'and', u'out', u',', u'The', u'beauty', u'of', u'the', u'waist', u',', u'and', u'thence', u'of', u'the', u'hips', u',', u'and', u'thence', u'downward', u'toward', u'the', u'knees', u',', u'The', u'thin', u'red', u'jellies', u'within', u'you', u'or', u'within', u'me', u',', u'the', u'bones', u'and', u'the', u'marrow', u'in', u'the', u'bones', u',', u'The', u'exquisite', u'realization', u'of', u'health', u';', u'O', u'I', u'say', u'these', u'are', u'not', u'the', u'parts', u'and', u'poems', u'of', u'the', u'body', u'only', u',', u'but', u'of', u'the', u'soul', u',', u'O', u'I', u'say', u'now', u'these', u'are', u'the', u'soul', u'!']
# 644 [u'15', u':', u'21', u'And', u'the', u'uttermost', u'cities', u'of', u'the', u'tribe', u'of', u'the', u'children', u'of', u'Judah', u'toward', u'the', u'coast', u'of', u'Edom', u'southward', u'were', u'Kabzeel', u',', u'and', u'Eder', u',', u'and', u'Jagur', u',', u'15', u':', u'22', u'And', u'Kinah', u',', u'and', u'Dimonah', u',', u'and', u'Adadah', u',', u'15', u':', u'23', u'And', u'Kedesh', u',', u'and', u'Hazor', u',', u'and', u'Ithnan', u',', u'15', u':', u'24', u'Ziph', u',', u'and', u'Telem', u',', u'and', u'Bealoth', u',', u'15', u':', u'25', u'And', u'Hazor', u',', u'Hadattah', u',', u'and', u'Kerioth', u',', u'and', u'Hezron', u',', u'which', u'is', u'Hazor', u',', u'15', u':', u'26', u'Amam', u',', u'and', u'Shema', u',', u'and', u'Moladah', u',', u'15', u':', u'27', u'And', u'Hazargaddah', u',', u'and', u'Heshmon', u',', u'and', u'Bethpalet', u',', u'15', u':', u'28', u'And', u'Hazarshual', u',', u'and', u'Beersheba', u',', u'and', u'Bizjothjah', u',', u'15', u':', u'29', u'Baalah', u',', u'and', u'Iim', u',', u'and', u'Azem', u',', u'15', u':', u'30', u'And', u'Eltolad', u',', u'and', u'Chesil', u',', u'and', u'Hormah', u',', u'15', u':', u'31', u'And', u'Ziklag', u',', u'and', u'Madmannah', u',', u'and', u'Sansannah', u',', u'15', u':', u'32', u'And', u'Lebaoth', u',', u'and', u'Shilhim', u',', u'and', u'Ain', u',', u'and', u'Rimmon', u':', u'all', u'the', u'cities', u'are', u'twenty', u'and', u'nine', u',', u'with', u'their', u'villages', u':', u'15', u':', u'33', u'And', u'in', u'the', u'valley', u',', u'Eshtaol', u',', u'and', u'Zoreah', u',', u'and', u'Ashnah', u',', u'15', u':', u'34', u'And', u'Zanoah', u',', u'and', u'Engannim', u',', u'Tappuah', u',', u'and', u'Enam', u',', u'15', u':', u'35', u'Jarmuth', u',', u'and', u'Adullam', u',', u'Socoh', u',', u'and', u'Azekah', u',', u'15', u':', u'36', u'And', u'Sharaim', u',', u'and', u'Adithaim', u',', u'and', u'Gederah', u',', u'and', u'Gederothaim', u';', u'fourteen', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'37', u'Zenan', u',', u'and', u'Hadashah', u',', u'and', u'Migdalgad', u',', u'15', u':', u'38', u'And', u'Dilean', u',', u'and', u'Mizpeh', u',', u'and', u'Joktheel', u',', u'15', u':', u'39', u'Lachish', u',', u'and', u'Bozkath', u',', u'and', u'Eglon', u',', u'15', u':', u'40', u'And', u'Cabbon', u',', u'and', u'Lahmam', u',', u'and', u'Kithlish', u',', u'15', u':', u'41', u'And', u'Gederoth', u',', u'Bethdagon', u',', u'and', u'Naamah', u',', u'and', u'Makkedah', u';', u'sixteen', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'42', u'Libnah', u',', u'and', u'Ether', u',', u'and', u'Ashan', u',', u'15', u':', u'43', u'And', u'Jiphtah', u',', u'and', u'Ashnah', u',', u'and', u'Nezib', u',', u'15', u':', u'44', u'And', u'Keilah', u',', u'and', u'Achzib', u',', u'and', u'Mareshah', u';', u'nine', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'45', u'Ekron', u',', u'with', u'her', u'towns', u'and', u'her', u'villages', u':', u'15', u':', u'46', u'From', u'Ekron', u'even', u'unto', u'the', u'sea', u',', u'all', u'that', u'lay', u'near', u'Ashdod', u',', u'with', u'their', u'villages', u':', u'15', u':', u'47', u'Ashdod', u'with', u'her', u'towns', u'and', u'her', u'villages', u',', u'Gaza', u'with', u'her', u'towns', u'and', u'her', u'villages', u',', u'unto', u'the', u'river', u'of', u'Egypt', u',', u'and', u'the', u'great', u'sea', u',', u'and', u'the', u'border', u'thereof', u':', u'15', u':', u'48', u'And', u'in', u'the', u'mountains', u',', u'Shamir', u',', u'and', u'Jattir', u',', u'and', u'Socoh', u',', u'15', u':', u'49', u'And', u'Dannah', u',', u'and', u'Kirjathsannah', u',', u'which', u'is', u'Debir', u',', u'15', u':', u'50', u'And', u'Anab', u',', u'and', u'Eshtemoh', u',', u'and', u'Anim', u',', u'15', u':', u'51', u'And', u'Goshen', u',', u'and', u'Holon', u',', u'and', u'Giloh', u';', u'eleven', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'52', u'Arab', u',', u'and', u'Dumah', u',', u'and', u'Eshean', u',', u'15', u':', u'53', u'And', u'Janum', u',', u'and', u'Bethtappuah', u',', u'and', u'Aphekah', u',', u'15', u':', u'54', u'And', u'Humtah', u',', u'and', u'Kirjatharba', u',', u'which', u'is', u'Hebron', u',', u'and', u'Zior', u';', u'nine', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'55', u'Maon', u',', u'Carmel', u',', u'and', u'Ziph', u',', u'and', u'Juttah', u',', u'15', u':', u'56', u'And', u'Jezreel', u',', u'and', u'Jokdeam', u',', u'and', u'Zanoah', u',', u'15', u':', u'57', u'Cain', u',', u'Gibeah', u',', u'and', u'Timnah', u';', u'ten', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'58', u'Halhul', u',', u'Bethzur', u',', u'and', u'Gedor', u',', u'15', u':', u'59', u'And', u'Maarath', u',', u'and', u'Bethanoth', u',', u'and', u'Eltekon', u';', u'six', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'60', u'Kirjathbaal', u',', u'which', u'is', u'Kirjathjearim', u',', u'and', u'Rabbah', u';', u'two', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'61', u'In', u'the', u'wilderness', u',', u'Betharabah', u',', u'Middin', u',', u'and', u'Secacah', u',', u'15', u':', u'62', u'And', u'Nibshan', u',', u'and', u'the', u'city', u'of', u'Salt', u',', u'and', u'Engedi', u';', u'six', u'cities', u'with', u'their', u'villages', u'.']
# 636 [u'Of', u'them', u'standing', u'among', u'them', u',', u'one', u'lifts', u'to', u'the', u'light', u'a', u'west', u'-', u'bred', u'face', u',', u'To', u'him', u'the', u'hereditary', u'countenance', u'bequeath', u"'", u'd', u'both', u'mother', u"'", u's', u'and', u'father', u"'", u's', u',', u'His', u'first', u'parts', u'substances', u',', u'earth', u',', u'water', u',', u'animals', u',', u'trees', u',', u'Built', u'of', u'the', u'common', u'stock', u',', u'having', u'room', u'for', u'far', u'and', u'near', u',', u'Used', u'to', u'dispense', u'with', u'other', u'lands', u',', u'incarnating', u'this', u'land', u',', u'Attracting', u'it', u'body', u'and', u'soul', u'to', u'himself', u',', u'hanging', u'on', u'its', u'neck', u'with', u'incomparable', u'love', u',', u'Plunging', u'his', u'seminal', u'muscle', u'into', u'its', u'merits', u'and', u'demerits', u',', u'Making', u'its', u'cities', u',', u'beginnings', u',', u'events', u',', u'diversities', u',', u'wars', u',', u'vocal', u'in', u'him', u',', u'Making', u'its', u'rivers', u',', u'lakes', u',', u'bays', u',', u'embouchure', u'in', u'him', u',', u'Mississippi', u'with', u'yearly', u'freshets', u'and', u'changing', u'chutes', u',', u'Columbia', u',', u'Niagara', u',', u'Hudson', u',', u'spending', u'themselves', u'lovingly', u'in', u'him', u',', u'If', u'the', u'Atlantic', u'coast', u'stretch', u'or', u'the', u'Pacific', u'coast', u'stretch', u',', u'he', u'stretching', u'with', u'them', u'North', u'or', u'South', u',', u'Spanning', u'between', u'them', u'East', u'and', u'West', u',', u'and', u'touching', u'whatever', u'is', u'between', u'them', u',', u'Growths', u'growing', u'from', u'him', u'to', u'offset', u'the', u'growths', u'of', u'pine', u',', u'cedar', u',', u'hemlock', u',', u'live', u'-', u'oak', u',', u'locust', u',', u'chestnut', u',', u'hickory', u',', u'cottonwood', u',', u'orange', u',', u'magnolia', u',', u'Tangles', u'as', u'tangled', u'in', u'him', u'as', u'any', u'canebrake', u'or', u'swamp', u',', u'He', u'likening', u'sides', u'and', u'peaks', u'of', u'mountains', u',', u'forests', u'coated', u'with', u'northern', u'transparent', u'ice', u',', u'Off', u'him', u'pasturage', u'sweet', u'and', u'natural', u'as', u'savanna', u',', u'upland', u',', u'prairie', u',', u'Through', u'him', u'flights', u',', u'whirls', u',', u'screams', u',', u'answering', u'those', u'of', u'the', u'fish', u'-', u'hawk', u',', u'mocking', u'-', u'bird', u',', u'night', u'-', u'heron', u',', u'and', u'eagle', u',', u'His', u'spirit', u'surrounding', u'his', u'country', u"'", u's', u'spirit', u',', u'unclosed', u'to', u'good', u'and', u'evil', u',', u'Surrounding', u'the', u'essences', u'of', u'real', u'things', u',', u'old', u'times', u'and', u'present', u'times', u',', u'Surrounding', u'just', u'found', u'shores', u',', u'islands', u',', u'tribes', u'of', u'red', u'aborigines', u',', u'Weather', u'-', u'beaten', u'vessels', u',', u'landings', u',', u'settlements', u',', u'embryo', u'stature', u'and', u'muscle', u',', u'The', u'haughty', u'defiance', u'of', u'the', u'Year', u'One', u',', u'war', u',', u'peace', u',', u'the', u'formation', u'of', u'the', u'Constitution', u',', u'The', u'separate', u'States', u',', u'the', u'simple', u'elastic', u'scheme', u',', u'the', u'immigrants', u',', u'The', u'Union', u'always', u'swarming', u'with', u'blatherers', u'and', u'always', u'sure', u'and', u'impregnable', u',', u'The', u'unsurvey', u"'", u'd', u'interior', u',', u'log', u'-', u'houses', u',', u'clearings', u',', u'wild', u'animals', u',', u'hunters', u',', u'trappers', u',', u'Surrounding', u'the', u'multiform', u'agriculture', u',', u'mines', u',', u'temperature', u',', u'the', u'gestation', u'of', u'new', u'States', u',', u'Congress', u'convening', u'every', u'Twelfth', u'-', u'month', u',', u'the', u'members', u'duly', u'coming', u'up', u'from', u'the', u'uttermost', u'parts', u',', u'Surrounding', u'the', u'noble', u'character', u'of', u'mechanics', u'and', u'farmers', u',', u'especially', u'the', u'young', u'men', u',', u'Responding', u'their', u'manners', u',', u'speech', u',', u'dress', u',', u'friendships', u',', u'the', u'gait', u'they', u'have', u'of', u'persons', u'who', u'never', u'knew', u'how', u'it', u'felt', u'to', u'stand', u'in', u'the', u'presence', u'of', u'superiors', u',', u'The', u'freshness', u'and', u'candor', u'of', u'their', u'physiognomy', u',', u'the', u'copiousness', u'and', u'decision', u'of', u'their', u'phrenology', u',', u'The', u'picturesque', u'looseness', u'of', u'their', u'carriage', u',', u'their', u'fierceness', u'when', u'wrong', u"'", u'd', u',', u'The', u'fluency', u'of', u'their', u'speech', u',', u'their', u'delight', u'in', u'music', u',', u'their', u'curiosity', u',', u'good', u'temper', u'and', u'open', u'-', u'handedness', u',', u'the', u'whole', u'composite', u'make', u',', u'The', u'prevailing', u'ardor', u'and', u'enterprise', u',', u'the', u'large', u'amativeness', u',', u'The', u'perfect', u'equality', u'of', u'the', u'female', u'with', u'the', u'male', u',', u'the', u'fluid', u'movement', u'of', u'the', u'population', u',', u'The', u'superior', u'marine', u',', u'free', u'commerce', u',', u'fisheries', u',', u'whaling', u',', u'gold', u'-', u'digging', u',', u'Wharf', u'-', u'hemm', u"'", u'd', u'cities', u',', u'railroad', u'and', u'steamboat', u'lines', u'intersecting', u'all', u'points', u',', u'Factories', u',', u'mercantile', u'life', u',', u'labor', u'-', u'saving', u'machinery', u',', u'the', u'Northeast', u',', u'Northwest', u',', u'Southwest', u',', u'Manhattan', u'firemen', u',', u'the', u'Yankee', u'swap', u',', u'southern', u'plantation', u'life', u',', u'Slavery', u'--', u'the', u'murderous', u',', u'treacherous', u'conspiracy', u'to', u'raise', u'it', u'upon', u'the', u'ruins', u'of', u'all', u'the', u'rest', u',', u'On', u'and', u'on', u'to', u'the', u'grapple', u'with', u'it', u'--', u'Assassin', u'!']
# 596 [u'3', u':', u'23', u'And', u'Jesus', u'himself', u'began', u'to', u'be', u'about', u'thirty', u'years', u'of', u'age', u',', u'being', u'(', u'as', u'was', u'supposed', u')', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Heli', u',', u'3', u':', u'24', u'Which', u'was', u'the', u'son', u'of', u'Matthat', u',', u'which', u'was', u'the', u'son', u'of', u'Levi', u',', u'which', u'was', u'the', u'son', u'of', u'Melchi', u',', u'which', u'was', u'the', u'son', u'of', u'Janna', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'3', u':', u'25', u'Which', u'was', u'the', u'son', u'of', u'Mattathias', u',', u'which', u'was', u'the', u'son', u'of', u'Amos', u',', u'which', u'was', u'the', u'son', u'of', u'Naum', u',', u'which', u'was', u'the', u'son', u'of', u'Esli', u',', u'which', u'was', u'the', u'son', u'of', u'Nagge', u',', u'3', u':', u'26', u'Which', u'was', u'the', u'son', u'of', u'Maath', u',', u'which', u'was', u'the', u'son', u'of', u'Mattathias', u',', u'which', u'was', u'the', u'son', u'of', u'Semei', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'3', u':', u'27', u'Which', u'was', u'the', u'son', u'of', u'Joanna', u',', u'which', u'was', u'the', u'son', u'of', u'Rhesa', u',', u'which', u'was', u'the', u'son', u'of', u'Zorobabel', u',', u'which', u'was', u'the', u'son', u'of', u'Salathiel', u',', u'which', u'was', u'the', u'son', u'of', u'Neri', u',', u'3', u':', u'28', u'Which', u'was', u'the', u'son', u'of', u'Melchi', u',', u'which', u'was', u'the', u'son', u'of', u'Addi', u',', u'which', u'was', u'the', u'son', u'of', u'Cosam', u',', u'which', u'was', u'the', u'son', u'of', u'Elmodam', u',', u'which', u'was', u'the', u'son', u'of', u'Er', u',', u'3', u':', u'29', u'Which', u'was', u'the', u'son', u'of', u'Jose', u',', u'which', u'was', u'the', u'son', u'of', u'Eliezer', u',', u'which', u'was', u'the', u'son', u'of', u'Jorim', u',', u'which', u'was', u'the', u'son', u'of', u'Matthat', u',', u'which', u'was', u'the', u'son', u'of', u'Levi', u',', u'3', u':', u'30', u'Which', u'was', u'the', u'son', u'of', u'Simeon', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Jonan', u',', u'which', u'was', u'the', u'son', u'of', u'Eliakim', u',', u'3', u':', u'31', u'Which', u'was', u'the', u'son', u'of', u'Melea', u',', u'which', u'was', u'the', u'son', u'of', u'Menan', u',', u'which', u'was', u'the', u'son', u'of', u'Mattatha', u',', u'which', u'was', u'the', u'son', u'of', u'Nathan', u',', u'which', u'was', u'the', u'son', u'of', u'David', u',', u'3', u':', u'32', u'Which', u'was', u'the', u'son', u'of', u'Jesse', u',', u'which', u'was', u'the', u'son', u'of', u'Obed', u',', u'which', u'was', u'the', u'son', u'of', u'Booz', u',', u'which', u'was', u'the', u'son', u'of', u'Salmon', u',', u'which', u'was', u'the', u'son', u'of', u'Naasson', u',', u'3', u':', u'33', u'Which', u'was', u'the', u'son', u'of', u'Aminadab', u',', u'which', u'was', u'the', u'son', u'of', u'Aram', u',', u'which', u'was', u'the', u'son', u'of', u'Esrom', u',', u'which', u'was', u'the', u'son', u'of', u'Phares', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'3', u':', u'34', u'Which', u'was', u'the', u'son', u'of', u'Jacob', u',', u'which', u'was', u'the', u'son', u'of', u'Isaac', u',', u'which', u'was', u'the', u'son', u'of', u'Abraham', u',', u'which', u'was', u'the', u'son', u'of', u'Thara', u',', u'which', u'was', u'the', u'son', u'of', u'Nachor', u',', u'3', u':', u'35', u'Which', u'was', u'the', u'son', u'of', u'Saruch', u',', u'which', u'was', u'the', u'son', u'of', u'Ragau', u',', u'which', u'was', u'the', u'son', u'of', u'Phalec', u',', u'which', u'was', u'the', u'son', u'of', u'Heber', u',', u'which', u'was', u'the', u'son', u'of', u'Sala', u',', u'3', u':', u'36', u'Which', u'was', u'the', u'son', u'of', u'Cainan', u',', u'which', u'was', u'the', u'son', u'of', u'Arphaxad', u',', u'which', u'was', u'the', u'son', u'of', u'Sem', u',', u'which', u'was', u'the', u'son', u'of', u'Noe', u',', u'which', u'was', u'the', u'son', u'of', u'Lamech', u',', u'3', u':', u'37', u'Which', u'was', u'the', u'son', u'of', u'Mathusala', u',', u'which', u'was', u'the', u'son', u'of', u'Enoch', u',', u'which', u'was', u'the', u'son', u'of', u'Jared', u',', u'which', u'was', u'the', u'son', u'of', u'Maleleel', u',', u'which', u'was', u'the', u'son', u'of', u'Cainan', u',', u'3', u':', u'38', u'Which', u'was', u'the', u'son', u'of', u'Enos', u',', u'which', u'was', u'the', u'son', u'of', u'Seth', u',', u'which', u'was', u'the', u'son', u'of', u'Adam', u',', u'which', u'was', u'the', u'son', u'of', u'God', u'.']
# 1378 [u'By', u'the', u'city', u"'", u's', u'quadrangular', u'houses', u'--', u'in', u'log', u'huts', u',', u'camping', u'with', u'lumber', u'-', u'men', u',', u'Along', u'the', u'ruts', u'of', u'the', u'turnpike', u',', u'along', u'the', u'dry', u'gulch', u'and', u'rivulet', u'bed', u',', u'Weeding', u'my', u'onion', u'-', u'patch', u'or', u'hosing', u'rows', u'of', u'carrots', u'and', u'parsnips', u',', u'crossing', u'savannas', u',', u'trailing', u'in', u'forests', u',', u'Prospecting', u',', u'gold', u'-', u'digging', u',', u'girdling', u'the', u'trees', u'of', u'a', u'new', u'purchase', u',', u'Scorch', u"'", u'd', u'ankle', u'-', u'deep', u'by', u'the', u'hot', u'sand', u',', u'hauling', u'my', u'boat', u'down', u'the', u'shallow', u'river', u',', u'Where', u'the', u'panther', u'walks', u'to', u'and', u'fro', u'on', u'a', u'limb', u'overhead', u',', u'where', u'the', u'buck', u'turns', u'furiously', u'at', u'the', u'hunter', u',', u'Where', u'the', u'rattlesnake', u'suns', u'his', u'flabby', u'length', u'on', u'a', u'rock', u',', u'where', u'the', u'otter', u'is', u'feeding', u'on', u'fish', u',', u'Where', u'the', u'alligator', u'in', u'his', u'tough', u'pimples', u'sleeps', u'by', u'the', u'bayou', u',', u'Where', u'the', u'black', u'bear', u'is', u'searching', u'for', u'roots', u'or', u'honey', u',', u'where', u'the', u'beaver', u'pats', u'the', u'mud', u'with', u'his', u'paddle', u'-', u'shaped', u'tall', u';', u'Over', u'the', u'growing', u'sugar', u',', u'over', u'the', u'yellow', u'-', u'flower', u"'", u'd', u'cotton', u'plant', u',', u'over', u'the', u'rice', u'in', u'its', u'low', u'moist', u'field', u',', u'Over', u'the', u'sharp', u'-', u'peak', u"'", u'd', u'farm', u'house', u',', u'with', u'its', u'scallop', u"'", u'd', u'scum', u'and', u'slender', u'shoots', u'from', u'the', u'gutters', u',', u'Over', u'the', u'western', u'persimmon', u',', u'over', u'the', u'long', u'-', u'leav', u"'", u'd', u'corn', u',', u'over', u'the', u'delicate', u'blue', u'-', u'flower', u'flax', u',', u'Over', u'the', u'white', u'and', u'brown', u'buckwheat', u',', u'a', u'hummer', u'and', u'buzzer', u'there', u'with', u'the', u'rest', u',', u'Over', u'the', u'dusky', u'green', u'of', u'the', u'rye', u'as', u'it', u'ripples', u'and', u'shades', u'in', u'the', u'breeze', u';', u'Scaling', u'mountains', u',', u'pulling', u'myself', u'cautiously', u'up', u',', u'holding', u'on', u'by', u'low', u'scragged', u'limbs', u',', u'Walking', u'the', u'path', u'worn', u'in', u'the', u'grass', u'and', u'beat', u'through', u'the', u'leaves', u'of', u'the', u'brush', u',', u'Where', u'the', u'quail', u'is', u'whistling', u'betwixt', u'the', u'woods', u'and', u'the', u'wheat', u'-', u'lot', u',', u'Where', u'the', u'bat', u'flies', u'in', u'the', u'Seventh', u'-', u'month', u'eve', u',', u'where', u'the', u'great', u'goldbug', u'drops', u'through', u'the', u'dark', u',', u'Where', u'the', u'brook', u'puts', u'out', u'of', u'the', u'roots', u'of', u'the', u'old', u'tree', u'and', u'flows', u'to', u'the', u'meadow', u',', u'Where', u'cattle', u'stand', u'and', u'shake', u'away', u'flies', u'with', u'the', u'tremulous', u'shuddering', u'of', u'their', u'hides', u',', u'Where', u'the', u'cheese', u'-', u'cloth', u'hangs', u'in', u'the', u'kitchen', u',', u'where', u'andirons', u'straddle', u'the', u'hearth', u'-', u'slab', u',', u'where', u'cobwebs', u'fall', u'in', u'festoons', u'from', u'the', u'rafters', u';', u'Where', u'trip', u'-', u'hammers', u'crash', u',', u'where', u'the', u'press', u'is', u'whirling', u'its', u'cylinders', u',', u'Wherever', u'the', u'human', u'heart', u'beats', u'with', u'terrible', u'throes', u'under', u'its', u'ribs', u',', u'Where', u'the', u'pear', u'-', u'shaped', u'balloon', u'is', u'floating', u'aloft', u',', u'(', u'floating', u'in', u'it', u'myself', u'and', u'looking', u'composedly', u'down', u',)', u'Where', u'the', u'life', u'-', u'car', u'is', u'drawn', u'on', u'the', u'slip', u'-', u'noose', u',', u'where', u'the', u'heat', u'hatches', u'pale', u'-', u'green', u'eggs', u'in', u'the', u'dented', u'sand', u',', u'Where', u'the', u'she', u'-', u'whale', u'swims', u'with', u'her', u'calf', u'and', u'never', u'forsakes', u'it', u',', u'Where', u'the', u'steam', u'-', u'ship', u'trails', u'hind', u'-', u'ways', u'its', u'long', u'pennant', u'of', u'smoke', u',', u'Where', u'the', u'fin', u'of', u'the', u'shark', u'cuts', u'like', u'a', u'black', u'chip', u'out', u'of', u'the', u'water', u',', u'Where', u'the', u'half', u'-', u'burn', u"'", u'd', u'brig', u'is', u'riding', u'on', u'unknown', u'currents', u',', u'Where', u'shells', u'grow', u'to', u'her', u'slimy', u'deck', u',', u'where', u'the', u'dead', u'are', u'corrupting', u'below', u';', u'Where', u'the', u'dense', u'-', u'starr', u"'", u'd', u'flag', u'is', u'borne', u'at', u'the', u'head', u'of', u'the', u'regiments', u',', u'Approaching', u'Manhattan', u'up', u'by', u'the', u'long', u'-', u'stretching', u'island', u',', u'Under', u'Niagara', u',', u'the', u'cataract', u'falling', u'like', u'a', u'veil', u'over', u'my', u'countenance', u',', u'Upon', u'a', u'door', u'-', u'step', u',', u'upon', u'the', u'horse', u'-', u'block', u'of', u'hard', u'wood', u'outside', u',', u'Upon', u'the', u'race', u'-', u'course', u',', u'or', u'enjoying', u'picnics', u'or', u'jigs', u'or', u'a', u'good', u'game', u'of', u'base', u'-', u'ball', u',', u'At', u'he', u'-', u'festivals', u',', u'with', u'blackguard', u'gibes', u',', u'ironical', u'license', u',', u'bull', u'-', u'dances', u',', u'drinking', u',', u'laughter', u',', u'At', u'the', u'cider', u'-', u'mill', u'tasting', u'the', u'sweets', u'of', u'the', u'brown', u'mash', u',', u'sucking', u'the', u'juice', u'through', u'a', u'straw', u',', u'At', u'apple', u'-', u'peelings', u'wanting', u'kisses', u'for', u'all', u'the', u'red', u'fruit', u'I', u'find', u',', u'At', u'musters', u',', u'beach', u'-', u'parties', u',', u'friendly', u'bees', u',', u'huskings', u',', u'house', u'-', u'raisings', u';', u'Where', u'the', u'mocking', u'-', u'bird', u'sounds', u'his', u'delicious', u'gurgles', u',', u'cackles', u',', u'screams', u',', u'weeps', u',', u'Where', u'the', u'hay', u'-', u'rick', u'stands', u'in', u'the', u'barn', u'-', u'yard', u',', u'where', u'the', u'dry', u'-', u'stalks', u'are', u'scatter', u"'", u'd', u',', u'where', u'the', u'brood', u'-', u'cow', u'waits', u'in', u'the', u'hovel', u',', u'Where', u'the', u'bull', u'advances', u'to', u'do', u'his', u'masculine', u'work', u',', u'where', u'the', u'stud', u'to', u'the', u'mare', u',', u'where', u'the', u'cock', u'is', u'treading', u'the', u'hen', u',', u'Where', u'the', u'heifers', u'browse', u',', u'where', u'geese', u'nip', u'their', u'food', u'with', u'short', u'jerks', u',', u'Where', u'sun', u'-', u'down', u'shadows', u'lengthen', u'over', u'the', u'limitless', u'and', u'lonesome', u'prairie', u',', u'Where', u'herds', u'of', u'buffalo', u'make', u'a', u'crawling', u'spread', u'of', u'the', u'square', u'miles', u'far', u'and', u'near', u',', u'Where', u'the', u'humming', u'-', u'bird', u'shimmers', u',', u'where', u'the', u'neck', u'of', u'the', u'long', u'-', u'lived', u'swan', u'is', u'curving', u'and', u'winding', u',', u'Where', u'the', u'laughing', u'-', u'gull', u'scoots', u'by', u'the', u'shore', u',', u'where', u'she', u'laughs', u'her', u'near', u'-', u'human', u'laugh', u',', u'Where', u'bee', u'-', u'hives', u'range', u'on', u'a', u'gray', u'bench', u'in', u'the', u'garden', u'half', u'hid', u'by', u'the', u'high', u'weeds', u',', u'Where', u'band', u'-', u'neck', u"'", u'd', u'partridges', u'roost', u'in', u'a', u'ring', u'on', u'the', u'ground', u'with', u'their', u'heads', u'out', u',', u'Where', u'burial', u'coaches', u'enter', u'the', u'arch', u"'", u'd', u'gates', u'of', u'a', u'cemetery', u',', u'Where', u'winter', u'wolves', u'bark', u'amid', u'wastes', u'of', u'snow', u'and', u'icicled', u'trees', u',', u'Where', u'the', u'yellow', u'-', u'crown', u"'", u'd', u'heron', u'comes', u'to', u'the', u'edge', u'of', u'the', u'marsh', u'at', u'night', u'and', u'feeds', u'upon', u'small', u'crabs', u',', u'Where', u'the', u'splash', u'of', u'swimmers', u'and', u'divers', u'cools', u'the', u'warm', u'noon', u',', u'Where', u'the', u'katy', u'-', u'did', u'works', u'her', u'chromatic', u'reed', u'on', u'the', u'walnut', u'-', u'tree', u'over', u'the', u'well', u',', u'Through', u'patches', u'of', u'citrons', u'and', u'cucumbers', u'with', u'silver', u'-', u'wired', u'leaves', u',', u'Through', u'the', u'salt', u'-', u'lick', u'or', u'orange', u'glade', u',', u'or', u'under', u'conical', u'firs', u',', u'Through', u'the', u'gymnasium', u',', u'through', u'the', u'curtain', u"'", u'd', u'saloon', u',', u'through', u'the', u'office', u'or', u'public', u'hall', u';', u'Pleas', u"'", u'd', u'with', u'the', u'native', u'and', u'pleas', u"'", u'd', u'with', u'the', u'foreign', u',', u'pleas', u"'", u'd', u'with', u'the', u'new', u'and', u'old', u',', u'Pleas', u"'", u'd', u'with', u'the', u'homely', u'woman', u'as', u'well', u'as', u'the', u'handsome', u',', u'Pleas', u"'", u'd', u'with', u'the', u'quakeress', u'as', u'she', u'puts', u'off', u'her', u'bonnet', u'and', u'talks', u'melodiously', u',', u'Pleas', u"'", u'd', u'with', u'the', u'tune', u'of', u'the', u'choir', u'of', u'the', u'whitewash', u"'", u'd', u'church', u',', u'Pleas', u"'", u'd', u'with', u'the', u'earnest', u'words', u'of', u'the', u'sweating', u'Methodist', u'preacher', u',', u'impress', u"'", u'd', u'seriously', u'at', u'the', u'camp', u'-', u'meeting', u';', u'Looking', u'in', u'at', u'the', u'shop', u'-', u'windows', u'of', u'Broadway', u'the', u'whole', u'forenoon', u',', u'flatting', u'the', u'flesh', u'of', u'my', u'nose', u'on', u'the', u'thick', u'plate', u'glass', u',', u'Wandering', u'the', u'same', u'afternoon', u'with', u'my', u'face', u'turn', u"'", u'd', u'up', u'to', u'the', u'clouds', u',', u'or', u'down', u'a', u'lane', u'or', u'along', u'the', u'beach', u',', u'My', u'right', u'and', u'left', u'arms', u'round', u'the', u'sides', u'of', u'two', u'friends', u',', u'and', u'I', u'in', u'the', u'middle', u';', u'Coming', u'home', u'with', u'the', u'silent', u'and', u'dark', u'-', u'cheek', u"'", u'd', u'bush', u'-', u'boy', u',', u'(', u'behind', u'me', u'he', u'rides', u'at', u'the', u'drape', u'of', u'the', u'day', u',)', u'Far', u'from', u'the', u'settlements', u'studying', u'the', u'print', u'of', u'animals', u"'", u'feet', u',', u'or', u'the', u'moccasin', u'print', u',', u'By', u'the', u'cot', u'in', u'the', u'hospital', u'reaching', u'lemonade', u'to', u'a', u'feverish', u'patient', u',', u'Nigh', u'the', u'coffin', u"'", u'd', u'corpse', u'when', u'all', u'is', u'still', u',', u'examining', u'with', u'a', u'candle', u';', u'Voyaging', u'to', u'every', u'port', u'to', u'dicker', u'and', u'adventure', u',', u'Hurrying', u'with', u'the', u'modern', u'crowd', u'as', u'eager', u'and', u'fickle', u'as', u'any', u',', u'Hot', u'toward', u'one', u'I', u'hate', u',', u'ready', u'in', u'my', u'madness', u'to', u'knife', u'him', u',', u'Solitary', u'at', u'midnight', u'in', u'my', u'back', u'yard', u',', u'my', u'thoughts', u'gone', u'from', u'me', u'a', u'long', u'while', u',', u'Walking', u'the', u'old', u'hills', u'of', u'Judaea', u'with', u'the', u'beautiful', u'gentle', u'God', u'by', u'my', u'side', u',', u'Speeding', u'through', u'space', u',', u'speeding', u'through', u'heaven', u'and', u'the', u'stars', u',', u'Speeding', u'amid', u'the', u'seven', u'satellites', u'and', u'the', u'broad', u'ring', u',', u'and', u'the', u'diameter', u'of', u'eighty', u'thousand', u'miles', u',', u'Speeding', u'with', u'tail', u"'", u'd', u'meteors', u',', u'throwing', u'fire', u'-', u'balls', u'like', u'the', u'rest', u',', u'Carrying', u'the', u'crescent', u'child', u'that', u'carries', u'its', u'own', u'full', u'mother', u'in', u'its', u'belly', u',', u'Storming', u',', u'enjoying', u',', u'planning', u',', u'loving', u',', u'cautioning', u',', u'Backing', u'and', u'filling', u',', u'appearing', u'and', u'disappearing', u',', u'I', u'tread', u'day', u'and', u'night', u'such', u'roads', u'.']
# 1102 [u'3', u'The', u'log', u'at', u'the', u'wood', u'-', u'pile', u',', u'the', u'axe', u'supported', u'by', u'it', u',', u'The', u'sylvan', u'hut', u',', u'the', u'vine', u'over', u'the', u'doorway', u',', u'the', u'space', u'clear', u"'", u'd', u'for', u'garden', u',', u'The', u'irregular', u'tapping', u'of', u'rain', u'down', u'on', u'the', u'leaves', u'after', u'the', u'storm', u'is', u'lull', u"'", u'd', u',', u'The', u'walling', u'and', u'moaning', u'at', u'intervals', u',', u'the', u'thought', u'of', u'the', u'sea', u',', u'The', u'thought', u'of', u'ships', u'struck', u'in', u'the', u'storm', u'and', u'put', u'on', u'their', u'beam', u'ends', u',', u'and', u'the', u'cutting', u'away', u'of', u'masts', u',', u'The', u'sentiment', u'of', u'the', u'huge', u'timbers', u'of', u'old', u'-', u'fashion', u"'", u'd', u'houses', u'and', u'barns', u',', u'The', u'remember', u"'", u'd', u'print', u'or', u'narrative', u',', u'the', u'voyage', u'at', u'a', u'venture', u'of', u'men', u',', u'families', u',', u'goods', u',', u'The', u'disembarkation', u',', u'the', u'founding', u'of', u'a', u'new', u'city', u',', u'The', u'voyage', u'of', u'those', u'who', u'sought', u'a', u'New', u'England', u'and', u'found', u'it', u',', u'the', u'outset', u'anywhere', u',', u'The', u'settlements', u'of', u'the', u'Arkansas', u',', u'Colorado', u',', u'Ottawa', u',', u'Willamette', u',', u'The', u'slow', u'progress', u',', u'the', u'scant', u'fare', u',', u'the', u'axe', u',', u'rifle', u',', u'saddle', u'-', u'bags', u';', u'The', u'beauty', u'of', u'all', u'adventurous', u'and', u'daring', u'persons', u',', u'The', u'beauty', u'of', u'wood', u'-', u'boys', u'and', u'wood', u'-', u'men', u'with', u'their', u'clear', u'untrimm', u"'", u'd', u'faces', u',', u'The', u'beauty', u'of', u'independence', u',', u'departure', u',', u'actions', u'that', u'rely', u'on', u'themselves', u',', u'The', u'American', u'contempt', u'for', u'statutes', u'and', u'ceremonies', u',', u'the', u'boundless', u'impatience', u'of', u'restraint', u',', u'The', u'loose', u'drift', u'of', u'character', u',', u'the', u'inkling', u'through', u'random', u'types', u',', u'the', u'solidification', u';', u'The', u'butcher', u'in', u'the', u'slaughter', u'-', u'house', u',', u'the', u'hands', u'aboard', u'schooners', u'and', u'sloops', u',', u'the', u'raftsman', u',', u'the', u'pioneer', u',', u'Lumbermen', u'in', u'their', u'winter', u'camp', u',', u'daybreak', u'in', u'the', u'woods', u',', u'stripes', u'of', u'snow', u'on', u'the', u'limbs', u'of', u'trees', u',', u'the', u'occasional', u'snapping', u',', u'The', u'glad', u'clear', u'sound', u'of', u'one', u"'", u's', u'own', u'voice', u',', u'the', u'merry', u'song', u',', u'the', u'natural', u'life', u'of', u'the', u'woods', u',', u'the', u'strong', u'day', u"'", u's', u'work', u',', u'The', u'blazing', u'fire', u'at', u'night', u',', u'the', u'sweet', u'taste', u'of', u'supper', u',', u'the', u'talk', u',', u'the', u'bed', u'of', u'hemlock', u'-', u'boughs', u'and', u'the', u'bear', u'-', u'skin', u';', u'The', u'house', u'-', u'builder', u'at', u'work', u'in', u'cities', u'or', u'anywhere', u',', u'The', u'preparatory', u'jointing', u',', u'squaring', u',', u'sawing', u',', u'mortising', u',', u'The', u'hoist', u'-', u'up', u'of', u'beams', u',', u'the', u'push', u'of', u'them', u'in', u'their', u'places', u',', u'laying', u'them', u'regular', u',', u'Setting', u'the', u'studs', u'by', u'their', u'tenons', u'in', u'the', u'mortises', u'according', u'as', u'they', u'were', u'prepared', u',', u'The', u'blows', u'of', u'mallets', u'and', u'hammers', u',', u'the', u'attitudes', u'of', u'the', u'men', u',', u'their', u'curv', u"'", u'd', u'limbs', u',', u'Bending', u',', u'standing', u',', u'astride', u'the', u'beams', u',', u'driving', u'in', u'pins', u',', u'holding', u'on', u'by', u'posts', u'and', u'braces', u',', u'The', u'hook', u"'", u'd', u'arm', u'over', u'the', u'plate', u',', u'the', u'other', u'arm', u'wielding', u'the', u'axe', u',', u'The', u'floor', u'-', u'men', u'forcing', u'the', u'planks', u'close', u'to', u'be', u'nail', u"'", u'd', u',', u'Their', u'postures', u'bringing', u'their', u'weapons', u'downward', u'on', u'the', u'bearers', u',', u'The', u'echoes', u'resounding', u'through', u'the', u'vacant', u'building', u':', u'The', u'huge', u'storehouse', u'carried', u'up', u'in', u'the', u'city', u'well', u'under', u'way', u',', u'The', u'six', u'framing', u'-', u'men', u',', u'two', u'in', u'the', u'middle', u'and', u'two', u'at', u'each', u'end', u',', u'carefully', u'bearing', u'on', u'their', u'shoulders', u'a', u'heavy', u'stick', u'for', u'a', u'cross', u'-', u'beam', u',', u'The', u'crowded', u'line', u'of', u'masons', u'with', u'trowels', u'in', u'their', u'right', u'hands', u'rapidly', u'laying', u'the', u'long', u'side', u'-', u'wall', u',', u'two', u'hundred', u'feet', u'from', u'front', u'to', u'rear', u',', u'The', u'flexible', u'rise', u'and', u'fall', u'of', u'backs', u',', u'the', u'continual', u'click', u'of', u'the', u'trowels', u'striking', u'the', u'bricks', u',', u'The', u'bricks', u'one', u'after', u'another', u'each', u'laid', u'so', u'workmanlike', u'in', u'its', u'place', u',', u'and', u'set', u'with', u'a', u'knock', u'of', u'the', u'trowel', u'-', u'handle', u',', u'The', u'piles', u'of', u'materials', u',', u'the', u'mortar', u'on', u'the', u'mortar', u'-', u'boards', u',', u'and', u'the', u'steady', u'replenishing', u'by', u'the', u'hod', u'-', u'men', u';', u'Spar', u'-', u'makers', u'in', u'the', u'spar', u'-', u'yard', u',', u'the', u'swarming', u'row', u'of', u'well', u'-', u'grown', u'apprentices', u',', u'The', u'swing', u'of', u'their', u'axes', u'on', u'the', u'square', u'-', u'hew', u"'", u'd', u'log', u'shaping', u'it', u'toward', u'the', u'shape', u'of', u'a', u'mast', u',', u'The', u'brisk', u'short', u'crackle', u'of', u'the', u'steel', u'driven', u'slantingly', u'into', u'the', u'pine', u',', u'The', u'butter', u'-', u'color', u"'", u'd', u'chips', u'flying', u'off', u'in', u'great', u'flakes', u'and', u'slivers', u',', u'The', u'limber', u'motion', u'of', u'brawny', u'young', u'arms', u'and', u'hips', u'in', u'easy', u'costumes', u',', u'The', u'constructor', u'of', u'wharves', u',', u'bridges', u',', u'piers', u',', u'bulk', u'-', u'heads', u',', u'floats', u',', u'stays', u'against', u'the', u'sea', u';', u'The', u'city', u'fireman', u',', u'the', u'fire', u'that', u'suddenly', u'bursts', u'forth', u'in', u'the', u'close', u'-', u'pack', u"'", u'd', u'square', u',', u'The', u'arriving', u'engines', u',', u'the', u'hoarse', u'shouts', u',', u'the', u'nimble', u'stepping', u'and', u'daring', u',', u'The', u'strong', u'command', u'through', u'the', u'fire', u'-', u'trumpets', u',', u'the', u'falling', u'in', u'line', u',', u'the', u'rise', u'and', u'fall', u'of', u'the', u'arms', u'forcing', u'the', u'water', u',', u'The', u'slender', u',', u'spasmic', u',', u'blue', u'-', u'white', u'jets', u',', u'the', u'bringing', u'to', u'bear', u'of', u'the', u'hooks', u'and', u'ladders', u'and', u'their', u'execution', u',', u'The', u'crash', u'and', u'cut', u'away', u'of', u'connecting', u'wood', u'-', u'work', u',', u'or', u'through', u'floors', u'if', u'the', u'fire', u'smoulders', u'under', u'them', u',', u'The', u'crowd', u'with', u'their', u'lit', u'faces', u'watching', u',', u'the', u'glare', u'and', u'dense', u'shadows', u';', u'The', u'forger', u'at', u'his', u'forge', u'-', u'furnace', u'and', u'the', u'user', u'of', u'iron', u'after', u'him', u',', u'The', u'maker', u'of', u'the', u'axe', u'large', u'and', u'small', u',', u'and', u'the', u'welder', u'and', u'temperer', u',', u'The', u'chooser', u'breathing', u'his', u'breath', u'on', u'the', u'cold', u'steel', u'and', u'trying', u'the', u'edge', u'with', u'his', u'thumb', u',', u'The', u'one', u'who', u'clean', u'-', u'shapes', u'the', u'handle', u'and', u'sets', u'it', u'firmly', u'in', u'the', u'socket', u';', u'The', u'shadowy', u'processions', u'of', u'the', u'portraits', u'of', u'the', u'past', u'users', u'also', u',', u'The', u'primal', u'patient', u'mechanics', u',', u'the', u'architects', u'and', u'engineers', u',', u'The', u'far', u'-', u'off', u'Assyrian', u'edifice', u'and', u'Mizra', u'edifice', u',', u'The', u'Roman', u'lictors', u'preceding', u'the', u'consuls', u',', u'The', u'antique', u'European', u'warrior', u'with', u'his', u'axe', u'in', u'combat', u',', u'The', u'uplifted', u'arm', u',', u'the', u'clatter', u'of', u'blows', u'on', u'the', u'helmeted', u'head', u',', u'The', u'death', u'-', u'howl', u',', u'the', u'limpsy', u'tumbling', u'body', u',', u'the', u'rush', u'of', u'friend', u'and', u'foe', u'thither', u',', u'The', u'siege', u'of', u'revolted', u'lieges', u'determin', u"'", u'd', u'for', u'liberty', u',', u'The', u'summons', u'to', u'surrender', u',', u'the', u'battering', u'at', u'castle', u'gates', u',', u'the', u'truce', u'and', u'parley', u',', u'The', u'sack', u'of', u'an', u'old', u'city', u'in', u'its', u'time', u',', u'The', u'bursting', u'in', u'of', u'mercenaries', u'and', u'bigots', u'tumultuously', u'and', u'disorderly', u',', u'Roar', u',', u'flames', u',', u'blood', u',', u'drunkenness', u',', u'madness', u',', u'Goods', u'freely', u'rifled', u'from', u'houses', u'and', u'temples', u',', u'screams', u'of', u'women', u'in', u'the', u'gripe', u'of', u'brigands', u',', u'Craft', u'and', u'thievery', u'of', u'camp', u'-', u'followers', u',', u'men', u'running', u',', u'old', u'persons', u'despairing', u',', u'The', u'hell', u'of', u'war', u',', u'the', u'cruelties', u'of', u'creeds', u',', u'The', u'list', u'of', u'all', u'executive', u'deeds', u'and', u'words', u'just', u'or', u'unjust', u',', u'The', u'power', u'of', u'personality', u'just', u'or', u'unjust', u'.']
# 944 [u'Always', u'Florida', u"'", u's', u'green', u'peninsula', u'--', u'always', u'the', u'priceless', u'delta', u'of', u'Louisiana', u'--', u'always', u'the', u'cotton', u'-', u'fields', u'of', u'Alabama', u'and', u'Texas', u',', u'Always', u'California', u"'", u's', u'golden', u'hills', u'and', u'hollows', u',', u'and', u'the', u'silver', u'mountains', u'of', u'New', u'Mexico', u'--', u'always', u'soft', u'-', u'breath', u"'", u'd', u'Cuba', u',', u'Always', u'the', u'vast', u'slope', u'drain', u"'", u'd', u'by', u'the', u'Southern', u'sea', u',', u'inseparable', u'with', u'the', u'slopes', u'drain', u"'", u'd', u'by', u'the', u'Eastern', u'and', u'Western', u'seas', u',', u'The', u'area', u'the', u'eighty', u'-', u'third', u'year', u'of', u'these', u'States', u',', u'the', u'three', u'and', u'a', u'half', u'millions', u'of', u'square', u'miles', u',', u'The', u'eighteen', u'thousand', u'miles', u'of', u'sea', u'-', u'coast', u'and', u'bay', u'-', u'coast', u'on', u'the', u'main', u',', u'the', u'thirty', u'thousand', u'miles', u'of', u'river', u'navigation', u',', u'The', u'seven', u'millions', u'of', u'distinct', u'families', u'and', u'the', u'same', u'number', u'of', u'dwellings', u'--', u'always', u'these', u',', u'and', u'more', u',', u'branching', u'forth', u'into', u'numberless', u'branches', u',', u'Always', u'the', u'free', u'range', u'and', u'diversity', u'--', u'always', u'the', u'continent', u'of', u'Democracy', u';', u'Always', u'the', u'prairies', u',', u'pastures', u',', u'forests', u',', u'vast', u'cities', u',', u'travelers', u',', u'Kanada', u',', u'the', u'snows', u';', u'Always', u'these', u'compact', u'lands', u'tied', u'at', u'the', u'hips', u'with', u'the', u'belt', u'stringing', u'the', u'huge', u'oval', u'lakes', u';', u'Always', u'the', u'West', u'with', u'strong', u'native', u'persons', u',', u'the', u'increasing', u'density', u'there', u',', u'the', u'habitans', u',', u'friendly', u',', u'threatening', u',', u'ironical', u',', u'scorning', u'invaders', u';', u'All', u'sights', u',', u'South', u',', u'North', u',', u'East', u'--', u'all', u'deeds', u',', u'promiscuously', u'done', u'at', u'all', u'times', u',', u'All', u'characters', u',', u'movements', u',', u'growths', u',', u'a', u'few', u'noticed', u',', u'myriads', u'unnoticed', u',', u'Through', u'Mannahatta', u"'", u's', u'streets', u'I', u'walking', u',', u'these', u'things', u'gathering', u',', u'On', u'interior', u'rivers', u'by', u'night', u'in', u'the', u'glare', u'of', u'pine', u'knots', u',', u'steamboats', u'wooding', u'up', u',', u'Sunlight', u'by', u'day', u'on', u'the', u'valley', u'of', u'the', u'Susquehanna', u',', u'and', u'on', u'the', u'valleys', u'of', u'the', u'Potomac', u'and', u'Rappahannock', u',', u'and', u'the', u'valleys', u'of', u'the', u'Roanoke', u'and', u'Delaware', u',', u'In', u'their', u'northerly', u'wilds', u'beasts', u'of', u'prey', u'haunting', u'the', u'Adirondacks', u'the', u'hills', u',', u'or', u'lapping', u'the', u'Saginaw', u'waters', u'to', u'drink', u',', u'In', u'a', u'lonesome', u'inlet', u'a', u'sheldrake', u'lost', u'from', u'the', u'flock', u',', u'sitting', u'on', u'the', u'water', u'rocking', u'silently', u',', u'In', u'farmers', u"'", u'barns', u'oxen', u'in', u'the', u'stable', u',', u'their', u'harvest', u'labor', u'done', u',', u'they', u'rest', u'standing', u',', u'they', u'are', u'too', u'tired', u',', u'Afar', u'on', u'arctic', u'ice', u'the', u'she', u'-', u'walrus', u'lying', u'drowsily', u'while', u'her', u'cubs', u'play', u'around', u',', u'The', u'hawk', u'sailing', u'where', u'men', u'have', u'not', u'yet', u'sail', u"'", u'd', u',', u'the', u'farthest', u'polar', u'sea', u',', u'ripply', u',', u'crystalline', u',', u'open', u',', u'beyond', u'the', u'floes', u',', u'White', u'drift', u'spooning', u'ahead', u'where', u'the', u'ship', u'in', u'the', u'tempest', u'dashes', u',', u'On', u'solid', u'land', u'what', u'is', u'done', u'in', u'cities', u'as', u'the', u'bells', u'strike', u'midnight', u'together', u',', u'In', u'primitive', u'woods', u'the', u'sounds', u'there', u'also', u'sounding', u',', u'the', u'howl', u'of', u'the', u'wolf', u',', u'the', u'scream', u'of', u'the', u'panther', u',', u'and', u'the', u'hoarse', u'bellow', u'of', u'the', u'elk', u',', u'In', u'winter', u'beneath', u'the', u'hard', u'blue', u'ice', u'of', u'Moosehead', u'lake', u',', u'in', u'summer', u'visible', u'through', u'the', u'clear', u'waters', u',', u'the', u'great', u'trout', u'swimming', u',', u'In', u'lower', u'latitudes', u'in', u'warmer', u'air', u'in', u'the', u'Carolinas', u'the', u'large', u'black', u'buzzard', u'floating', u'slowly', u'high', u'beyond', u'the', u'tree', u'tops', u',', u'Below', u',', u'the', u'red', u'cedar', u'festoon', u"'", u'd', u'with', u'tylandria', u',', u'the', u'pines', u'and', u'cypresses', u'growing', u'out', u'of', u'the', u'white', u'sand', u'that', u'spreads', u'far', u'and', u'flat', u',', u'Rude', u'boats', u'descending', u'the', u'big', u'Pedee', u',', u'climbing', u'plants', u',', u'parasites', u'with', u'color', u"'", u'd', u'flowers', u'and', u'berries', u'enveloping', u'huge', u'trees', u',', u'The', u'waving', u'drapery', u'on', u'the', u'live', u'-', u'oak', u'trailing', u'long', u'and', u'low', u',', u'noiselessly', u'waved', u'by', u'the', u'wind', u',', u'The', u'camp', u'of', u'Georgia', u'wagoners', u'just', u'after', u'dark', u',', u'the', u'supper', u'-', u'fires', u'and', u'the', u'cooking', u'and', u'eating', u'by', u'whites', u'and', u'negroes', u',', u'Thirty', u'or', u'forty', u'great', u'wagons', u',', u'the', u'mules', u',', u'cattle', u',', u'horses', u',', u'feeding', u'from', u'troughs', u',', u'The', u'shadows', u',', u'gleams', u',', u'up', u'under', u'the', u'leaves', u'of', u'the', u'old', u'sycamore', u'-', u'trees', u',', u'the', u'flames', u'with', u'the', u'black', u'smoke', u'from', u'the', u'pitch', u'-', u'pine', u'curling', u'and', u'rising', u';', u'Southern', u'fishermen', u'fishing', u',', u'the', u'sounds', u'and', u'inlets', u'of', u'North', u'Carolina', u"'", u's', u'coast', u',', u'the', u'shad', u'-', u'fishery', u'and', u'the', u'herring', u'-', u'fishery', u',', u'the', u'large', u'sweep', u'-', u'seines', u',', u'the', u'windlasses', u'on', u'shore', u'work', u"'", u'd', u'by', u'horses', u',', u'the', u'clearing', u',', u'curing', u',', u'and', u'packing', u'-', u'houses', u';', u'Deep', u'in', u'the', u'forest', u'in', u'piney', u'woods', u'turpentine', u'dropping', u'from', u'the', u'incisions', u'in', u'the', u'trees', u',', u'there', u'are', u'the', u'turpentine', u'works', u',', u'There', u'are', u'the', u'negroes', u'at', u'work', u'in', u'good', u'health', u',', u'the', u'ground', u'in', u'all', u'directions', u'is', u'cover', u"'", u'd', u'with', u'pine', u'straw', u';', u'In', u'Tennessee', u'and', u'Kentucky', u'slaves', u'busy', u'in', u'the', u'coalings', u',', u'at', u'the', u'forge', u',', u'by', u'the', u'furnace', u'-', u'blaze', u',', u'or', u'at', u'the', u'corn', u'-', u'shucking', u',', u'In', u'Virginia', u',', u'the', u'planter', u"'", u's', u'son', u'returning', u'after', u'a', u'long', u'absence', u',', u'joyfully', u'welcom', u"'", u'd', u'and', u'kiss', u"'", u'd', u'by', u'the', u'aged', u'mulatto', u'nurse', u',', u'On', u'rivers', u'boatmen', u'safely', u'moor', u"'", u'd', u'at', u'nightfall', u'in', u'their', u'boats', u'under', u'shelter', u'of', u'high', u'banks', u',', u'Some', u'of', u'the', u'younger', u'men', u'dance', u'to', u'the', u'sound', u'of', u'the', u'banjo', u'or', u'fiddle', u',', u'others', u'sit', u'on', u'the', u'gunwale', u'smoking', u'and', u'talking', u';', u'Late', u'in', u'the', u'afternoon', u'the', u'mocking', u'-', u'bird', u',', u'the', u'American', u'mimic', u',', u'singing', u'in', u'the', u'Great', u'Dismal', u'Swamp', u',', u'There', u'are', u'the', u'greenish', u'waters', u',', u'the', u'resinous', u'odor', u',', u'the', u'plenteous', u'moss', u',', u'the', u'cypress', u'-', u'tree', u',', u'and', u'the', u'juniper', u'-', u'tree', u';', u'Northward', u',', u'young', u'men', u'of', u'Mannahatta', u',', u'the', u'target', u'company', u'from', u'an', u'excursion', u'returning', u'home', u'at', u'evening', u',', u'the', u'musket', u'-', u'muzzles', u'all', u'bear', u'bunches', u'of', u'flowers', u'presented', u'by', u'women', u';', u'Children', u'at', u'play', u',', u'or', u'on', u'his', u'father', u"'", u's', u'lap', u'a', u'young', u'boy', u'fallen', u'asleep', u',', u'(', u'how', u'his', u'lips', u'move', u'!']
# 827 [u'Spontaneous', u'me', u',', u'Nature', u',', u'The', u'loving', u'day', u',', u'the', u'mounting', u'sun', u',', u'the', u'friend', u'I', u'am', u'happy', u'with', u',', u'The', u'arm', u'of', u'my', u'friend', u'hanging', u'idly', u'over', u'my', u'shoulder', u',', u'The', u'hillside', u'whiten', u"'", u'd', u'with', u'blossoms', u'of', u'the', u'mountain', u'ash', u',', u'The', u'same', u'late', u'in', u'autumn', u',', u'the', u'hues', u'of', u'red', u',', u'yellow', u',', u'drab', u',', u'purple', u',', u'and', u'light', u'and', u'dark', u'green', u',', u'The', u'rich', u'coverlet', u'of', u'the', u'grass', u',', u'animals', u'and', u'birds', u',', u'the', u'private', u'untrimm', u"'", u'd', u'bank', u',', u'the', u'primitive', u'apples', u',', u'the', u'pebble', u'-', u'stones', u',', u'Beautiful', u'dripping', u'fragments', u',', u'the', u'negligent', u'list', u'of', u'one', u'after', u'another', u'as', u'I', u'happen', u'to', u'call', u'them', u'to', u'me', u'or', u'think', u'of', u'them', u',', u'The', u'real', u'poems', u',', u'(', u'what', u'we', u'call', u'poems', u'being', u'merely', u'pictures', u',)', u'The', u'poems', u'of', u'the', u'privacy', u'of', u'the', u'night', u',', u'and', u'of', u'men', u'like', u'me', u',', u'This', u'poem', u'drooping', u'shy', u'and', u'unseen', u'that', u'I', u'always', u'carry', u',', u'and', u'that', u'all', u'men', u'carry', u',', u'(', u'Know', u'once', u'for', u'all', u',', u'avow', u"'", u'd', u'on', u'purpose', u',', u'wherever', u'are', u'men', u'like', u'me', u',', u'are', u'our', u'lusty', u'lurking', u'masculine', u'poems', u',)', u'Love', u'-', u'thoughts', u',', u'love', u'-', u'juice', u',', u'love', u'-', u'odor', u',', u'love', u'-', u'yielding', u',', u'love', u'-', u'climbers', u',', u'and', u'the', u'climbing', u'sap', u',', u'Arms', u'and', u'hands', u'of', u'love', u',', u'lips', u'of', u'love', u',', u'phallic', u'thumb', u'of', u'love', u',', u'breasts', u'of', u'love', u',', u'bellies', u'press', u"'", u'd', u'and', u'glued', u'together', u'with', u'love', u',', u'Earth', u'of', u'chaste', u'love', u',', u'life', u'that', u'is', u'only', u'life', u'after', u'love', u',', u'The', u'body', u'of', u'my', u'love', u',', u'the', u'body', u'of', u'the', u'woman', u'I', u'love', u',', u'the', u'body', u'of', u'the', u'man', u',', u'the', u'body', u'of', u'the', u'earth', u',', u'Soft', u'forenoon', u'airs', u'that', u'blow', u'from', u'the', u'south', u'-', u'west', u',', u'The', u'hairy', u'wild', u'-', u'bee', u'that', u'murmurs', u'and', u'hankers', u'up', u'and', u'down', u',', u'that', u'gripes', u'the', u'full', u'-', u'grown', u'lady', u'-', u'flower', u',', u'curves', u'upon', u'her', u'with', u'amorous', u'firm', u'legs', u',', u'takes', u'his', u'will', u'of', u'her', u',', u'and', u'holds', u'himself', u'tremulous', u'and', u'tight', u'till', u'he', u'is', u'satisfied', u';', u'The', u'wet', u'of', u'woods', u'through', u'the', u'early', u'hours', u',', u'Two', u'sleepers', u'at', u'night', u'lying', u'close', u'together', u'as', u'they', u'sleep', u',', u'one', u'with', u'an', u'arm', u'slanting', u'down', u'across', u'and', u'below', u'the', u'waist', u'of', u'the', u'other', u',', u'The', u'smell', u'of', u'apples', u',', u'aromas', u'from', u'crush', u"'", u'd', u'sage', u'-', u'plant', u',', u'mint', u',', u'birch', u'-', u'bark', u',', u'The', u'boy', u"'", u's', u'longings', u',', u'the', u'glow', u'and', u'pressure', u'as', u'he', u'confides', u'to', u'me', u'what', u'he', u'was', u'dreaming', u',', u'The', u'dead', u'leaf', u'whirling', u'its', u'spiral', u'whirl', u'and', u'falling', u'still', u'and', u'content', u'to', u'the', u'ground', u',', u'The', u'no', u'-', u'form', u"'", u'd', u'stings', u'that', u'sights', u',', u'people', u',', u'objects', u',', u'sting', u'me', u'with', u',', u'The', u'hubb', u"'", u'd', u'sting', u'of', u'myself', u',', u'stinging', u'me', u'as', u'much', u'as', u'it', u'ever', u'can', u'any', u'one', u',', u'The', u'sensitive', u',', u'orbic', u',', u'underlapp', u"'", u'd', u'brothers', u',', u'that', u'only', u'privileged', u'feelers', u'may', u'be', u'intimate', u'where', u'they', u'are', u',', u'The', u'curious', u'roamer', u'the', u'hand', u'roaming', u'all', u'over', u'the', u'body', u',', u'the', u'bashful', u'withdrawing', u'of', u'flesh', u'where', u'the', u'fingers', u'soothingly', u'pause', u'and', u'edge', u'themselves', u',', u'The', u'limpid', u'liquid', u'within', u'the', u'young', u'man', u',', u'The', u'vex', u"'", u'd', u'corrosion', u'so', u'pensive', u'and', u'so', u'painful', u',', u'The', u'torment', u',', u'the', u'irritable', u'tide', u'that', u'will', u'not', u'be', u'at', u'rest', u',', u'The', u'like', u'of', u'the', u'same', u'I', u'feel', u',', u'the', u'like', u'of', u'the', u'same', u'in', u'others', u',', u'The', u'young', u'man', u'that', u'flushes', u'and', u'flushes', u',', u'and', u'the', u'young', u'woman', u'that', u'flushes', u'and', u'flushes', u',', u'The', u'young', u'man', u'that', u'wakes', u'deep', u'at', u'night', u',', u'the', u'hot', u'hand', u'seeking', u'to', u'repress', u'what', u'would', u'master', u'him', u',', u'The', u'mystic', u'amorous', u'night', u',', u'the', u'strange', u'half', u'-', u'welcome', u'pangs', u',', u'visions', u',', u'sweats', u',', u'The', u'pulse', u'pounding', u'through', u'palms', u'and', u'trembling', u'encircling', u'fingers', u',', u'the', u'young', u'man', u'all', u'color', u"'", u'd', u',', u'red', u',', u'ashamed', u',', u'angry', u';', u'The', u'souse', u'upon', u'me', u'of', u'my', u'lover', u'the', u'sea', u',', u'as', u'I', u'lie', u'willing', u'and', u'naked', u',', u'The', u'merriment', u'of', u'the', u'twin', u'babes', u'that', u'crawl', u'over', u'the', u'grass', u'in', u'the', u'sun', u',', u'the', u'mother', u'never', u'turning', u'her', u'vigilant', u'eyes', u'from', u'them', u',', u'The', u'walnut', u'-', u'trunk', u',', u'the', u'walnut', u'-', u'husks', u',', u'and', u'the', u'ripening', u'or', u'ripen', u"'", u'd', u'long', u'-', u'round', u'walnuts', u',', u'The', u'continence', u'of', u'vegetables', u',', u'birds', u',', u'animals', u',', u'The', u'consequent', u'meanness', u'of', u'me', u'should', u'I', u'skulk', u'or', u'find', u'myself', u'indecent', u',', u'while', u'birds', u'and', u'animals', u'never', u'once', u'skulk', u'or', u'find', u'themselves', u'indecent', u',', u'The', u'great', u'chastity', u'of', u'paternity', u',', u'to', u'match', u'the', u'great', u'chastity', u'of', u'maternity', u',', u'The', u'oath', u'of', u'procreation', u'I', u'have', u'sworn', u',', u'my', u'Adamic', u'and', u'fresh', u'daughters', u',', u'The', u'greed', u'that', u'eats', u'me', u'day', u'and', u'night', u'with', u'hungry', u'gnaw', u',', u'till', u'I', u'saturate', u'what', u'shall', u'produce', u'boys', u'to', u'fill', u'my', u'place', u'when', u'I', u'am', u'through', u',', u'The', u'wholesome', u'relief', u',', u'repose', u',', u'content', u',', u'And', u'this', u'bunch', u'pluck', u"'", u'd', u'at', u'random', u'from', u'myself', u',', u'It', u'has', u'done', u'its', u'work', u'--', u'I', u'toss', u'it', u'carelessly', u'to', u'fall', u'where', u'it', u'may', u'.']
# 687 [u'House', u'-', u'building', u',', u'measuring', u',', u'sawing', u'the', u'boards', u',', u'Blacksmithing', u',', u'glass', u'-', u'blowing', u',', u'nail', u'-', u'making', u',', u'coopering', u',', u'tin', u'-', u'roofing', u',', u'shingle', u'-', u'dressing', u',', u'Ship', u'-', u'joining', u',', u'dock', u'-', u'building', u',', u'fish', u'-', u'curing', u',', u'flagging', u'of', u'sidewalks', u'by', u'flaggers', u',', u'The', u'pump', u',', u'the', u'pile', u'-', u'driver', u',', u'the', u'great', u'derrick', u',', u'the', u'coal', u'-', u'kiln', u'and', u'brickkiln', u',', u'Coal', u'-', u'mines', u'and', u'all', u'that', u'is', u'down', u'there', u',', u'the', u'lamps', u'in', u'the', u'darkness', u',', u'echoes', u',', u'songs', u',', u'what', u'meditations', u',', u'what', u'vast', u'native', u'thoughts', u'looking', u'through', u'smutch', u"'", u'd', u'faces', u',', u'Iron', u'-', u'works', u',', u'forge', u'-', u'fires', u'in', u'the', u'mountains', u'or', u'by', u'river', u'-', u'banks', u',', u'men', u'around', u'feeling', u'the', u'melt', u'with', u'huge', u'crowbars', u',', u'lumps', u'of', u'ore', u',', u'the', u'due', u'combining', u'of', u'ore', u',', u'limestone', u',', u'coal', u',', u'The', u'blast', u'-', u'furnace', u'and', u'the', u'puddling', u'-', u'furnace', u',', u'the', u'loup', u'-', u'lump', u'at', u'the', u'bottom', u'of', u'the', u'melt', u'at', u'last', u',', u'the', u'rolling', u'-', u'mill', u',', u'the', u'stumpy', u'bars', u'of', u'pig', u'-', u'iron', u',', u'the', u'strong', u'clean', u'-', u'shaped', u'Trail', u'for', u'railroads', u',', u'Oil', u'-', u'works', u',', u'silk', u'-', u'works', u',', u'white', u'-', u'lead', u'-', u'works', u',', u'the', u'sugar', u'-', u'house', u',', u'steam', u'-', u'saws', u',', u'the', u'great', u'mills', u'and', u'factories', u',', u'Stone', u'-', u'cutting', u',', u'shapely', u'trimmings', u'for', u'facades', u'or', u'window', u'or', u'door', u'-', u'lintels', u',', u'the', u'mallet', u',', u'the', u'tooth', u'-', u'chisel', u',', u'the', u'jib', u'to', u'protect', u'the', u'thumb', u',', u'The', u'calking', u'-', u'iron', u',', u'the', u'kettle', u'of', u'boiling', u'vault', u'-', u'cement', u',', u'and', u'the', u'fire', u'under', u'the', u'kettle', u',', u'The', u'cotton', u'-', u'bale', u',', u'the', u'stevedore', u"'", u's', u'hook', u',', u'the', u'saw', u'and', u'buck', u'of', u'the', u'sawyer', u',', u'the', u'mould', u'of', u'the', u'moulder', u',', u'the', u'working', u'-', u'knife', u'of', u'the', u'butcher', u',', u'the', u'ice', u'-', u'saw', u',', u'and', u'all', u'the', u'work', u'with', u'ice', u',', u'The', u'work', u'and', u'tools', u'of', u'the', u'rigger', u',', u'grappler', u',', u'sail', u'-', u'maker', u',', u'block', u'-', u'maker', u',', u'Goods', u'of', u'gutta', u'-', u'percha', u',', u'papier', u'-', u'mache', u',', u'colors', u',', u'brushes', u',', u'brush', u'-', u'making', u',', u'glazier', u"'", u's', u'implements', u',', u'The', u'veneer', u'and', u'glue', u'-', u'pot', u',', u'the', u'confectioner', u"'", u's', u'ornaments', u',', u'the', u'decanter', u'and', u'glasses', u',', u'the', u'shears', u'and', u'flat', u'-', u'iron', u',', u'The', u'awl', u'and', u'knee', u'-', u'strap', u',', u'the', u'pint', u'measure', u'and', u'quart', u'measure', u',', u'the', u'counter', u'and', u'stool', u',', u'the', u'writing', u'-', u'pen', u'of', u'quill', u'or', u'metal', u',', u'the', u'making', u'of', u'all', u'sorts', u'of', u'edged', u'tools', u',', u'The', u'brewery', u',', u'brewing', u',', u'the', u'malt', u',', u'the', u'vats', u',', u'every', u'thing', u'that', u'is', u'done', u'by', u'brewers', u',', u'wine', u'-', u'makers', u',', u'vinegar', u'-', u'makers', u',', u'Leather', u'-', u'dressing', u',', u'coach', u'-', u'making', u',', u'boiler', u'-', u'making', u',', u'rope', u'-', u'twisting', u',', u'distilling', u',', u'sign', u'-', u'painting', u',', u'lime', u'-', u'burning', u',', u'cotton', u'-', u'picking', u',', u'electroplating', u',', u'electrotyping', u',', u'stereotyping', u',', u'Stave', u'-', u'machines', u',', u'planing', u'-', u'machines', u',', u'reaping', u'-', u'machines', u',', u'ploughing', u'-', u'machines', u',', u'thrashing', u'-', u'machines', u',', u'steam', u'wagons', u',', u'The', u'cart', u'of', u'the', u'carman', u',', u'the', u'omnibus', u',', u'the', u'ponderous', u'dray', u',', u'Pyrotechny', u',', u'letting', u'off', u'color', u"'", u'd', u'fireworks', u'at', u'night', u',', u'fancy', u'figures', u'and', u'jets', u';', u'Beef', u'on', u'the', u'butcher', u"'", u's', u'stall', u',', u'the', u'slaughter', u'-', u'house', u'of', u'the', u'butcher', u',', u'the', u'butcher', u'in', u'his', u'killing', u'-', u'clothes', u',', u'The', u'pens', u'of', u'live', u'pork', u',', u'the', u'killing', u'-', u'hammer', u',', u'the', u'hog', u'-', u'hook', u',', u'the', u'scalder', u"'", u's', u'tub', u',', u'gutting', u',', u'the', u'cutter', u"'", u's', u'cleaver', u',', u'the', u'packer', u"'", u's', u'maul', u',', u'and', u'the', u'plenteous', u'winterwork', u'of', u'pork', u'-', u'packing', u',', u'Flour', u'-', u'works', u',', u'grinding', u'of', u'wheat', u',', u'rye', u',', u'maize', u',', u'rice', u',', u'the', u'barrels', u'and', u'the', u'half', u'and', u'quarter', u'barrels', u',', u'the', u'loaded', u'barges', u',', u'the', u'high', u'piles', u'on', u'wharves', u'and', u'levees', u',', u'The', u'men', u'and', u'the', u'work', u'of', u'the', u'men', u'on', u'ferries', u',', u'railroads', u',', u'coasters', u',', u'fish', u'-', u'boats', u',', u'canals', u';', u'The', u'hourly', u'routine', u'of', u'your', u'own', u'or', u'any', u'man', u"'", u's', u'life', u',', u'the', u'shop', u',', u'yard', u',', u'store', u',', u'or', u'factory', u',', u'These', u'shows', u'all', u'near', u'you', u'by', u'day', u'and', u'night', u'--', u'workman', u'!']
# 657 [u'15', u'The', u'pure', u'contralto', u'sings', u'in', u'the', u'organ', u'loft', u',', u'The', u'carpenter', u'dresses', u'his', u'plank', u',', u'the', u'tongue', u'of', u'his', u'foreplane', u'whistles', u'its', u'wild', u'ascending', u'lisp', u',', u'The', u'married', u'and', u'unmarried', u'children', u'ride', u'home', u'to', u'their', u'Thanksgiving', u'dinner', u',', u'The', u'pilot', u'seizes', u'the', u'king', u'-', u'pin', u',', u'he', u'heaves', u'down', u'with', u'a', u'strong', u'arm', u',', u'The', u'mate', u'stands', u'braced', u'in', u'the', u'whale', u'-', u'boat', u',', u'lance', u'and', u'harpoon', u'are', u'ready', u',', u'The', u'duck', u'-', u'shooter', u'walks', u'by', u'silent', u'and', u'cautious', u'stretches', u',', u'The', u'deacons', u'are', u'ordain', u"'", u'd', u'with', u'cross', u"'", u'd', u'hands', u'at', u'the', u'altar', u',', u'The', u'spinning', u'-', u'girl', u'retreats', u'and', u'advances', u'to', u'the', u'hum', u'of', u'the', u'big', u'wheel', u',', u'The', u'farmer', u'stops', u'by', u'the', u'bars', u'as', u'he', u'walks', u'on', u'a', u'First', u'-', u'day', u'loafe', u'and', u'looks', u'at', u'the', u'oats', u'and', u'rye', u',', u'The', u'lunatic', u'is', u'carried', u'at', u'last', u'to', u'the', u'asylum', u'a', u'confirm', u"'", u'd', u'case', u',', u'(', u'He', u'will', u'never', u'sleep', u'any', u'more', u'as', u'he', u'did', u'in', u'the', u'cot', u'in', u'his', u'mother', u"'", u's', u'bed', u'-', u'room', u';)', u'The', u'jour', u'printer', u'with', u'gray', u'head', u'and', u'gaunt', u'jaws', u'works', u'at', u'his', u'case', u',', u'He', u'turns', u'his', u'quid', u'of', u'tobacco', u'while', u'his', u'eyes', u'blurr', u'with', u'the', u'manuscript', u';', u'The', u'malform', u"'", u'd', u'limbs', u'are', u'tied', u'to', u'the', u'surgeon', u"'", u's', u'table', u',', u'What', u'is', u'removed', u'drops', u'horribly', u'in', u'a', u'pail', u';', u'The', u'quadroon', u'girl', u'is', u'sold', u'at', u'the', u'auction', u'-', u'stand', u',', u'the', u'drunkard', u'nods', u'by', u'the', u'bar', u'-', u'room', u'stove', u',', u'The', u'machinist', u'rolls', u'up', u'his', u'sleeves', u',', u'the', u'policeman', u'travels', u'his', u'beat', u',', u'the', u'gate', u'-', u'keeper', u'marks', u'who', u'pass', u',', u'The', u'young', u'fellow', u'drives', u'the', u'express', u'-', u'wagon', u',', u'(', u'I', u'love', u'him', u',', u'though', u'I', u'do', u'not', u'know', u'him', u';)', u'The', u'half', u'-', u'breed', u'straps', u'on', u'his', u'light', u'boots', u'to', u'compete', u'in', u'the', u'race', u',', u'The', u'western', u'turkey', u'-', u'shooting', u'draws', u'old', u'and', u'young', u',', u'some', u'lean', u'on', u'their', u'rifles', u',', u'some', u'sit', u'on', u'logs', u',', u'Out', u'from', u'the', u'crowd', u'steps', u'the', u'marksman', u',', u'takes', u'his', u'position', u',', u'levels', u'his', u'piece', u';', u'The', u'groups', u'of', u'newly', u'-', u'come', u'immigrants', u'cover', u'the', u'wharf', u'or', u'levee', u',', u'As', u'the', u'woolly', u'-', u'pates', u'hoe', u'in', u'the', u'sugar', u'-', u'field', u',', u'the', u'overseer', u'views', u'them', u'from', u'his', u'saddle', u',', u'The', u'bugle', u'calls', u'in', u'the', u'ball', u'-', u'room', u',', u'the', u'gentlemen', u'run', u'for', u'their', u'partners', u',', u'the', u'dancers', u'bow', u'to', u'each', u'other', u',', u'The', u'youth', u'lies', u'awake', u'in', u'the', u'cedar', u'-', u'roof', u"'", u'd', u'garret', u'and', u'harks', u'to', u'the', u'musical', u'rain', u',', u'The', u'Wolverine', u'sets', u'traps', u'on', u'the', u'creek', u'that', u'helps', u'fill', u'the', u'Huron', u',', u'The', u'squaw', u'wrapt', u'in', u'her', u'yellow', u'-', u'hemm', u"'", u'd', u'cloth', u'is', u'offering', u'moccasins', u'and', u'bead', u'-', u'bags', u'for', u'sale', u',', u'The', u'connoisseur', u'peers', u'along', u'the', u'exhibition', u'-', u'gallery', u'with', u'half', u'-', u'shut', u'eyes', u'bent', u'sideways', u',', u'As', u'the', u'deck', u'-', u'hands', u'make', u'fast', u'the', u'steamboat', u'the', u'plank', u'is', u'thrown', u'for', u'the', u'shore', u'-', u'going', u'passengers', u',', u'The', u'young', u'sister', u'holds', u'out', u'the', u'skein', u'while', u'the', u'elder', u'sister', u'winds', u'it', u'off', u'in', u'a', u'ball', u',', u'and', u'stops', u'now', u'and', u'then', u'for', u'the', u'knots', u',', u'The', u'one', u'-', u'year', u'wife', u'is', u'recovering', u'and', u'happy', u'having', u'a', u'week', u'ago', u'borne', u'her', u'first', u'child', u',', u'The', u'clean', u'-', u'hair', u"'", u'd', u'Yankee', u'girl', u'works', u'with', u'her', u'sewing', u'-', u'machine', u'or', u'in', u'the', u'factory', u'or', u'mill', u',', u'The', u'paving', u'-', u'man', u'leans', u'on', u'his', u'two', u'-', u'handed', u'rammer', u',', u'the', u'reporter', u"'", u's', u'lead', u'flies', u'swiftly', u'over', u'the', u'note', u'-', u'book', u',', u'the', u'sign', u'-', u'painter', u'is', u'lettering', u'with', u'blue', u'and', u'gold', u',', u'The', u'canal', u'boy', u'trots', u'on', u'the', u'tow', u'-', u'path', u',', u'the', u'book', u'-', u'keeper', u'counts', u'at', u'his', u'desk', u',', u'the', u'shoemaker', u'waxes', u'his', u'thread', u',', u'The', u'conductor', u'beats', u'time', u'for', u'the', u'band', u'and', u'all', u'the', u'performers', u'follow', u'him', u',', u'The', u'child', u'is', u'baptized', u',', u'the', u'convert', u'is', u'making', u'his', u'first', u'professions', u',', u'The', u'regatta', u'is', u'spread', u'on', u'the', u'bay', u',', u'the', u'race', u'is', u'begun', u',', u'(', u'how', u'the', u'white', u'sails', u'sparkle', u'!)']
# 653 [u'I', u'dare', u'not', u'desert', u'the', u'likes', u'of', u'you', u'in', u'other', u'men', u'and', u'women', u',', u'nor', u'the', u'likes', u'of', u'the', u'parts', u'of', u'you', u',', u'I', u'believe', u'the', u'likes', u'of', u'you', u'are', u'to', u'stand', u'or', u'fall', u'with', u'the', u'likes', u'of', u'the', u'soul', u',', u'(', u'and', u'that', u'they', u'are', u'the', u'soul', u',)', u'I', u'believe', u'the', u'likes', u'of', u'you', u'shall', u'stand', u'or', u'fall', u'with', u'my', u'poems', u',', u'and', u'that', u'they', u'are', u'my', u'poems', u',', u'Man', u"'", u's', u',', u'woman', u"'", u's', u',', u'child', u',', u'youth', u"'", u's', u',', u'wife', u"'", u's', u',', u'husband', u"'", u's', u',', u'mother', u"'", u's', u',', u'father', u"'", u's', u',', u'young', u'man', u"'", u's', u',', u'young', u'woman', u"'", u's', u'poems', u',', u'Head', u',', u'neck', u',', u'hair', u',', u'ears', u',', u'drop', u'and', u'tympan', u'of', u'the', u'ears', u',', u'Eyes', u',', u'eye', u'-', u'fringes', u',', u'iris', u'of', u'the', u'eye', u',', u'eyebrows', u',', u'and', u'the', u'waking', u'or', u'sleeping', u'of', u'the', u'lids', u',', u'Mouth', u',', u'tongue', u',', u'lips', u',', u'teeth', u',', u'roof', u'of', u'the', u'mouth', u',', u'jaws', u',', u'and', u'the', u'jaw', u'-', u'hinges', u',', u'Nose', u',', u'nostrils', u'of', u'the', u'nose', u',', u'and', u'the', u'partition', u',', u'Cheeks', u',', u'temples', u',', u'forehead', u',', u'chin', u',', u'throat', u',', u'back', u'of', u'the', u'neck', u',', u'neck', u'-', u'slue', u',', u'Strong', u'shoulders', u',', u'manly', u'beard', u',', u'scapula', u',', u'hind', u'-', u'shoulders', u',', u'and', u'the', u'ample', u'side', u'-', u'round', u'of', u'the', u'chest', u',', u'Upper', u'-', u'arm', u',', u'armpit', u',', u'elbow', u'-', u'socket', u',', u'lower', u'-', u'arm', u',', u'arm', u'-', u'sinews', u',', u'arm', u'-', u'bones', u',', u'Wrist', u'and', u'wrist', u'-', u'joints', u',', u'hand', u',', u'palm', u',', u'knuckles', u',', u'thumb', u',', u'forefinger', u',', u'finger', u'-', u'joints', u',', u'finger', u'-', u'nails', u',', u'Broad', u'breast', u'-', u'front', u',', u'curling', u'hair', u'of', u'the', u'breast', u',', u'breast', u'-', u'bone', u',', u'breast', u'-', u'side', u',', u'Ribs', u',', u'belly', u',', u'backbone', u',', u'joints', u'of', u'the', u'backbone', u',', u'Hips', u',', u'hip', u'-', u'sockets', u',', u'hip', u'-', u'strength', u',', u'inward', u'and', u'outward', u'round', u',', u'man', u'-', u'balls', u',', u'man', u'-', u'root', u',', u'Strong', u'set', u'of', u'thighs', u',', u'well', u'carrying', u'the', u'trunk', u'above', u',', u'Leg', u'-', u'fibres', u',', u'knee', u',', u'knee', u'-', u'pan', u',', u'upper', u'-', u'leg', u',', u'under', u'-', u'leg', u',', u'Ankles', u',', u'instep', u',', u'foot', u'-', u'ball', u',', u'toes', u',', u'toe', u'-', u'joints', u',', u'the', u'heel', u';', u'All', u'attitudes', u',', u'all', u'the', u'shapeliness', u',', u'all', u'the', u'belongings', u'of', u'my', u'or', u'your', u'body', u'or', u'of', u'any', u'one', u"'", u's', u'body', u',', u'male', u'or', u'female', u',', u'The', u'lung', u'-', u'sponges', u',', u'the', u'stomach', u'-', u'sac', u',', u'the', u'bowels', u'sweet', u'and', u'clean', u',', u'The', u'brain', u'in', u'its', u'folds', u'inside', u'the', u'skull', u'-', u'frame', u',', u'Sympathies', u',', u'heart', u'-', u'valves', u',', u'palate', u'-', u'valves', u',', u'sexuality', u',', u'maternity', u',', u'Womanhood', u',', u'and', u'all', u'that', u'is', u'a', u'woman', u',', u'and', u'the', u'man', u'that', u'comes', u'from', u'woman', u',', u'The', u'womb', u',', u'the', u'teats', u',', u'nipples', u',', u'breast', u'-', u'milk', u',', u'tears', u',', u'laughter', u',', u'weeping', u',', u'love', u'-', u'looks', u',', u'love', u'-', u'perturbations', u'and', u'risings', u',', u'The', u'voice', u',', u'articulation', u',', u'language', u',', u'whispering', u',', u'shouting', u'aloud', u',', u'Food', u',', u'drink', u',', u'pulse', u',', u'digestion', u',', u'sweat', u',', u'sleep', u',', u'walking', u',', u'swimming', u',', u'Poise', u'on', u'the', u'hips', u',', u'leaping', u',', u'reclining', u',', u'embracing', u',', u'arm', u'-', u'curving', u'and', u'tightening', u',', u'The', u'continual', u'changes', u'of', u'the', u'flex', u'of', u'the', u'mouth', u',', u'and', u'around', u'the', u'eyes', u',', u'The', u'skin', u',', u'the', u'sunburnt', u'shade', u',', u'freckles', u',', u'hair', u',', u'The', u'curious', u'sympathy', u'one', u'feels', u'when', u'feeling', u'with', u'the', u'hand', u'the', u'naked', u'meat', u'of', u'the', u'body', u',', u'The', u'circling', u'rivers', u'the', u'breath', u',', u'and', u'breathing', u'it', u'in', u'and', u'out', u',', u'The', u'beauty', u'of', u'the', u'waist', u',', u'and', u'thence', u'of', u'the', u'hips', u',', u'and', u'thence', u'downward', u'toward', u'the', u'knees', u',', u'The', u'thin', u'red', u'jellies', u'within', u'you', u'or', u'within', u'me', u',', u'the', u'bones', u'and', u'the', u'marrow', u'in', u'the', u'bones', u',', u'The', u'exquisite', u'realization', u'of', u'health', u';', u'O', u'I', u'say', u'these', u'are', u'not', u'the', u'parts', u'and', u'poems', u'of', u'the', u'body', u'only', u',', u'but', u'of', u'the', u'soul', u',', u'O', u'I', u'say', u'now', u'these', u'are', u'the', u'soul', u'!']
# 644 [u'15', u':', u'21', u'And', u'the', u'uttermost', u'cities', u'of', u'the', u'tribe', u'of', u'the', u'children', u'of', u'Judah', u'toward', u'the', u'coast', u'of', u'Edom', u'southward', u'were', u'Kabzeel', u',', u'and', u'Eder', u',', u'and', u'Jagur', u',', u'15', u':', u'22', u'And', u'Kinah', u',', u'and', u'Dimonah', u',', u'and', u'Adadah', u',', u'15', u':', u'23', u'And', u'Kedesh', u',', u'and', u'Hazor', u',', u'and', u'Ithnan', u',', u'15', u':', u'24', u'Ziph', u',', u'and', u'Telem', u',', u'and', u'Bealoth', u',', u'15', u':', u'25', u'And', u'Hazor', u',', u'Hadattah', u',', u'and', u'Kerioth', u',', u'and', u'Hezron', u',', u'which', u'is', u'Hazor', u',', u'15', u':', u'26', u'Amam', u',', u'and', u'Shema', u',', u'and', u'Moladah', u',', u'15', u':', u'27', u'And', u'Hazargaddah', u',', u'and', u'Heshmon', u',', u'and', u'Bethpalet', u',', u'15', u':', u'28', u'And', u'Hazarshual', u',', u'and', u'Beersheba', u',', u'and', u'Bizjothjah', u',', u'15', u':', u'29', u'Baalah', u',', u'and', u'Iim', u',', u'and', u'Azem', u',', u'15', u':', u'30', u'And', u'Eltolad', u',', u'and', u'Chesil', u',', u'and', u'Hormah', u',', u'15', u':', u'31', u'And', u'Ziklag', u',', u'and', u'Madmannah', u',', u'and', u'Sansannah', u',', u'15', u':', u'32', u'And', u'Lebaoth', u',', u'and', u'Shilhim', u',', u'and', u'Ain', u',', u'and', u'Rimmon', u':', u'all', u'the', u'cities', u'are', u'twenty', u'and', u'nine', u',', u'with', u'their', u'villages', u':', u'15', u':', u'33', u'And', u'in', u'the', u'valley', u',', u'Eshtaol', u',', u'and', u'Zoreah', u',', u'and', u'Ashnah', u',', u'15', u':', u'34', u'And', u'Zanoah', u',', u'and', u'Engannim', u',', u'Tappuah', u',', u'and', u'Enam', u',', u'15', u':', u'35', u'Jarmuth', u',', u'and', u'Adullam', u',', u'Socoh', u',', u'and', u'Azekah', u',', u'15', u':', u'36', u'And', u'Sharaim', u',', u'and', u'Adithaim', u',', u'and', u'Gederah', u',', u'and', u'Gederothaim', u';', u'fourteen', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'37', u'Zenan', u',', u'and', u'Hadashah', u',', u'and', u'Migdalgad', u',', u'15', u':', u'38', u'And', u'Dilean', u',', u'and', u'Mizpeh', u',', u'and', u'Joktheel', u',', u'15', u':', u'39', u'Lachish', u',', u'and', u'Bozkath', u',', u'and', u'Eglon', u',', u'15', u':', u'40', u'And', u'Cabbon', u',', u'and', u'Lahmam', u',', u'and', u'Kithlish', u',', u'15', u':', u'41', u'And', u'Gederoth', u',', u'Bethdagon', u',', u'and', u'Naamah', u',', u'and', u'Makkedah', u';', u'sixteen', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'42', u'Libnah', u',', u'and', u'Ether', u',', u'and', u'Ashan', u',', u'15', u':', u'43', u'And', u'Jiphtah', u',', u'and', u'Ashnah', u',', u'and', u'Nezib', u',', u'15', u':', u'44', u'And', u'Keilah', u',', u'and', u'Achzib', u',', u'and', u'Mareshah', u';', u'nine', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'45', u'Ekron', u',', u'with', u'her', u'towns', u'and', u'her', u'villages', u':', u'15', u':', u'46', u'From', u'Ekron', u'even', u'unto', u'the', u'sea', u',', u'all', u'that', u'lay', u'near', u'Ashdod', u',', u'with', u'their', u'villages', u':', u'15', u':', u'47', u'Ashdod', u'with', u'her', u'towns', u'and', u'her', u'villages', u',', u'Gaza', u'with', u'her', u'towns', u'and', u'her', u'villages', u',', u'unto', u'the', u'river', u'of', u'Egypt', u',', u'and', u'the', u'great', u'sea', u',', u'and', u'the', u'border', u'thereof', u':', u'15', u':', u'48', u'And', u'in', u'the', u'mountains', u',', u'Shamir', u',', u'and', u'Jattir', u',', u'and', u'Socoh', u',', u'15', u':', u'49', u'And', u'Dannah', u',', u'and', u'Kirjathsannah', u',', u'which', u'is', u'Debir', u',', u'15', u':', u'50', u'And', u'Anab', u',', u'and', u'Eshtemoh', u',', u'and', u'Anim', u',', u'15', u':', u'51', u'And', u'Goshen', u',', u'and', u'Holon', u',', u'and', u'Giloh', u';', u'eleven', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'52', u'Arab', u',', u'and', u'Dumah', u',', u'and', u'Eshean', u',', u'15', u':', u'53', u'And', u'Janum', u',', u'and', u'Bethtappuah', u',', u'and', u'Aphekah', u',', u'15', u':', u'54', u'And', u'Humtah', u',', u'and', u'Kirjatharba', u',', u'which', u'is', u'Hebron', u',', u'and', u'Zior', u';', u'nine', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'55', u'Maon', u',', u'Carmel', u',', u'and', u'Ziph', u',', u'and', u'Juttah', u',', u'15', u':', u'56', u'And', u'Jezreel', u',', u'and', u'Jokdeam', u',', u'and', u'Zanoah', u',', u'15', u':', u'57', u'Cain', u',', u'Gibeah', u',', u'and', u'Timnah', u';', u'ten', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'58', u'Halhul', u',', u'Bethzur', u',', u'and', u'Gedor', u',', u'15', u':', u'59', u'And', u'Maarath', u',', u'and', u'Bethanoth', u',', u'and', u'Eltekon', u';', u'six', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'60', u'Kirjathbaal', u',', u'which', u'is', u'Kirjathjearim', u',', u'and', u'Rabbah', u';', u'two', u'cities', u'with', u'their', u'villages', u':', u'15', u':', u'61', u'In', u'the', u'wilderness', u',', u'Betharabah', u',', u'Middin', u',', u'and', u'Secacah', u',', u'15', u':', u'62', u'And', u'Nibshan', u',', u'and', u'the', u'city', u'of', u'Salt', u',', u'and', u'Engedi', u';', u'six', u'cities', u'with', u'their', u'villages', u'.']
# 636 [u'Of', u'them', u'standing', u'among', u'them', u',', u'one', u'lifts', u'to', u'the', u'light', u'a', u'west', u'-', u'bred', u'face', u',', u'To', u'him', u'the', u'hereditary', u'countenance', u'bequeath', u"'", u'd', u'both', u'mother', u"'", u's', u'and', u'father', u"'", u's', u',', u'His', u'first', u'parts', u'substances', u',', u'earth', u',', u'water', u',', u'animals', u',', u'trees', u',', u'Built', u'of', u'the', u'common', u'stock', u',', u'having', u'room', u'for', u'far', u'and', u'near', u',', u'Used', u'to', u'dispense', u'with', u'other', u'lands', u',', u'incarnating', u'this', u'land', u',', u'Attracting', u'it', u'body', u'and', u'soul', u'to', u'himself', u',', u'hanging', u'on', u'its', u'neck', u'with', u'incomparable', u'love', u',', u'Plunging', u'his', u'seminal', u'muscle', u'into', u'its', u'merits', u'and', u'demerits', u',', u'Making', u'its', u'cities', u',', u'beginnings', u',', u'events', u',', u'diversities', u',', u'wars', u',', u'vocal', u'in', u'him', u',', u'Making', u'its', u'rivers', u',', u'lakes', u',', u'bays', u',', u'embouchure', u'in', u'him', u',', u'Mississippi', u'with', u'yearly', u'freshets', u'and', u'changing', u'chutes', u',', u'Columbia', u',', u'Niagara', u',', u'Hudson', u',', u'spending', u'themselves', u'lovingly', u'in', u'him', u',', u'If', u'the', u'Atlantic', u'coast', u'stretch', u'or', u'the', u'Pacific', u'coast', u'stretch', u',', u'he', u'stretching', u'with', u'them', u'North', u'or', u'South', u',', u'Spanning', u'between', u'them', u'East', u'and', u'West', u',', u'and', u'touching', u'whatever', u'is', u'between', u'them', u',', u'Growths', u'growing', u'from', u'him', u'to', u'offset', u'the', u'growths', u'of', u'pine', u',', u'cedar', u',', u'hemlock', u',', u'live', u'-', u'oak', u',', u'locust', u',', u'chestnut', u',', u'hickory', u',', u'cottonwood', u',', u'orange', u',', u'magnolia', u',', u'Tangles', u'as', u'tangled', u'in', u'him', u'as', u'any', u'canebrake', u'or', u'swamp', u',', u'He', u'likening', u'sides', u'and', u'peaks', u'of', u'mountains', u',', u'forests', u'coated', u'with', u'northern', u'transparent', u'ice', u',', u'Off', u'him', u'pasturage', u'sweet', u'and', u'natural', u'as', u'savanna', u',', u'upland', u',', u'prairie', u',', u'Through', u'him', u'flights', u',', u'whirls', u',', u'screams', u',', u'answering', u'those', u'of', u'the', u'fish', u'-', u'hawk', u',', u'mocking', u'-', u'bird', u',', u'night', u'-', u'heron', u',', u'and', u'eagle', u',', u'His', u'spirit', u'surrounding', u'his', u'country', u"'", u's', u'spirit', u',', u'unclosed', u'to', u'good', u'and', u'evil', u',', u'Surrounding', u'the', u'essences', u'of', u'real', u'things', u',', u'old', u'times', u'and', u'present', u'times', u',', u'Surrounding', u'just', u'found', u'shores', u',', u'islands', u',', u'tribes', u'of', u'red', u'aborigines', u',', u'Weather', u'-', u'beaten', u'vessels', u',', u'landings', u',', u'settlements', u',', u'embryo', u'stature', u'and', u'muscle', u',', u'The', u'haughty', u'defiance', u'of', u'the', u'Year', u'One', u',', u'war', u',', u'peace', u',', u'the', u'formation', u'of', u'the', u'Constitution', u',', u'The', u'separate', u'States', u',', u'the', u'simple', u'elastic', u'scheme', u',', u'the', u'immigrants', u',', u'The', u'Union', u'always', u'swarming', u'with', u'blatherers', u'and', u'always', u'sure', u'and', u'impregnable', u',', u'The', u'unsurvey', u"'", u'd', u'interior', u',', u'log', u'-', u'houses', u',', u'clearings', u',', u'wild', u'animals', u',', u'hunters', u',', u'trappers', u',', u'Surrounding', u'the', u'multiform', u'agriculture', u',', u'mines', u',', u'temperature', u',', u'the', u'gestation', u'of', u'new', u'States', u',', u'Congress', u'convening', u'every', u'Twelfth', u'-', u'month', u',', u'the', u'members', u'duly', u'coming', u'up', u'from', u'the', u'uttermost', u'parts', u',', u'Surrounding', u'the', u'noble', u'character', u'of', u'mechanics', u'and', u'farmers', u',', u'especially', u'the', u'young', u'men', u',', u'Responding', u'their', u'manners', u',', u'speech', u',', u'dress', u',', u'friendships', u',', u'the', u'gait', u'they', u'have', u'of', u'persons', u'who', u'never', u'knew', u'how', u'it', u'felt', u'to', u'stand', u'in', u'the', u'presence', u'of', u'superiors', u',', u'The', u'freshness', u'and', u'candor', u'of', u'their', u'physiognomy', u',', u'the', u'copiousness', u'and', u'decision', u'of', u'their', u'phrenology', u',', u'The', u'picturesque', u'looseness', u'of', u'their', u'carriage', u',', u'their', u'fierceness', u'when', u'wrong', u"'", u'd', u',', u'The', u'fluency', u'of', u'their', u'speech', u',', u'their', u'delight', u'in', u'music', u',', u'their', u'curiosity', u',', u'good', u'temper', u'and', u'open', u'-', u'handedness', u',', u'the', u'whole', u'composite', u'make', u',', u'The', u'prevailing', u'ardor', u'and', u'enterprise', u',', u'the', u'large', u'amativeness', u',', u'The', u'perfect', u'equality', u'of', u'the', u'female', u'with', u'the', u'male', u',', u'the', u'fluid', u'movement', u'of', u'the', u'population', u',', u'The', u'superior', u'marine', u',', u'free', u'commerce', u',', u'fisheries', u',', u'whaling', u',', u'gold', u'-', u'digging', u',', u'Wharf', u'-', u'hemm', u"'", u'd', u'cities', u',', u'railroad', u'and', u'steamboat', u'lines', u'intersecting', u'all', u'points', u',', u'Factories', u',', u'mercantile', u'life', u',', u'labor', u'-', u'saving', u'machinery', u',', u'the', u'Northeast', u',', u'Northwest', u',', u'Southwest', u',', u'Manhattan', u'firemen', u',', u'the', u'Yankee', u'swap', u',', u'southern', u'plantation', u'life', u',', u'Slavery', u'--', u'the', u'murderous', u',', u'treacherous', u'conspiracy', u'to', u'raise', u'it', u'upon', u'the', u'ruins', u'of', u'all', u'the', u'rest', u',', u'On', u'and', u'on', u'to', u'the', u'grapple', u'with', u'it', u'--', u'Assassin', u'!']
# 596 [u'3', u':', u'23', u'And', u'Jesus', u'himself', u'began', u'to', u'be', u'about', u'thirty', u'years', u'of', u'age', u',', u'being', u'(', u'as', u'was', u'supposed', u')', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Heli', u',', u'3', u':', u'24', u'Which', u'was', u'the', u'son', u'of', u'Matthat', u',', u'which', u'was', u'the', u'son', u'of', u'Levi', u',', u'which', u'was', u'the', u'son', u'of', u'Melchi', u',', u'which', u'was', u'the', u'son', u'of', u'Janna', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'3', u':', u'25', u'Which', u'was', u'the', u'son', u'of', u'Mattathias', u',', u'which', u'was', u'the', u'son', u'of', u'Amos', u',', u'which', u'was', u'the', u'son', u'of', u'Naum', u',', u'which', u'was', u'the', u'son', u'of', u'Esli', u',', u'which', u'was', u'the', u'son', u'of', u'Nagge', u',', u'3', u':', u'26', u'Which', u'was', u'the', u'son', u'of', u'Maath', u',', u'which', u'was', u'the', u'son', u'of', u'Mattathias', u',', u'which', u'was', u'the', u'son', u'of', u'Semei', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'3', u':', u'27', u'Which', u'was', u'the', u'son', u'of', u'Joanna', u',', u'which', u'was', u'the', u'son', u'of', u'Rhesa', u',', u'which', u'was', u'the', u'son', u'of', u'Zorobabel', u',', u'which', u'was', u'the', u'son', u'of', u'Salathiel', u',', u'which', u'was', u'the', u'son', u'of', u'Neri', u',', u'3', u':', u'28', u'Which', u'was', u'the', u'son', u'of', u'Melchi', u',', u'which', u'was', u'the', u'son', u'of', u'Addi', u',', u'which', u'was', u'the', u'son', u'of', u'Cosam', u',', u'which', u'was', u'the', u'son', u'of', u'Elmodam', u',', u'which', u'was', u'the', u'son', u'of', u'Er', u',', u'3', u':', u'29', u'Which', u'was', u'the', u'son', u'of', u'Jose', u',', u'which', u'was', u'the', u'son', u'of', u'Eliezer', u',', u'which', u'was', u'the', u'son', u'of', u'Jorim', u',', u'which', u'was', u'the', u'son', u'of', u'Matthat', u',', u'which', u'was', u'the', u'son', u'of', u'Levi', u',', u'3', u':', u'30', u'Which', u'was', u'the', u'son', u'of', u'Simeon', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'which', u'was', u'the', u'son', u'of', u'Joseph', u',', u'which', u'was', u'the', u'son', u'of', u'Jonan', u',', u'which', u'was', u'the', u'son', u'of', u'Eliakim', u',', u'3', u':', u'31', u'Which', u'was', u'the', u'son', u'of', u'Melea', u',', u'which', u'was', u'the', u'son', u'of', u'Menan', u',', u'which', u'was', u'the', u'son', u'of', u'Mattatha', u',', u'which', u'was', u'the', u'son', u'of', u'Nathan', u',', u'which', u'was', u'the', u'son', u'of', u'David', u',', u'3', u':', u'32', u'Which', u'was', u'the', u'son', u'of', u'Jesse', u',', u'which', u'was', u'the', u'son', u'of', u'Obed', u',', u'which', u'was', u'the', u'son', u'of', u'Booz', u',', u'which', u'was', u'the', u'son', u'of', u'Salmon', u',', u'which', u'was', u'the', u'son', u'of', u'Naasson', u',', u'3', u':', u'33', u'Which', u'was', u'the', u'son', u'of', u'Aminadab', u',', u'which', u'was', u'the', u'son', u'of', u'Aram', u',', u'which', u'was', u'the', u'son', u'of', u'Esrom', u',', u'which', u'was', u'the', u'son', u'of', u'Phares', u',', u'which', u'was', u'the', u'son', u'of', u'Juda', u',', u'3', u':', u'34', u'Which', u'was', u'the', u'son', u'of', u'Jacob', u',', u'which', u'was', u'the', u'son', u'of', u'Isaac', u',', u'which', u'was', u'the', u'son', u'of', u'Abraham', u',', u'which', u'was', u'the', u'son', u'of', u'Thara', u',', u'which', u'was', u'the', u'son', u'of', u'Nachor', u',', u'3', u':', u'35', u'Which', u'was', u'the', u'son', u'of', u'Saruch', u',', u'which', u'was', u'the', u'son', u'of', u'Ragau', u',', u'which', u'was', u'the', u'son', u'of', u'Phalec', u',', u'which', u'was', u'the', u'son', u'of', u'Heber', u',', u'which', u'was', u'the', u'son', u'of', u'Sala', u',', u'3', u':', u'36', u'Which', u'was', u'the', u'son', u'of', u'Cainan', u',', u'which', u'was', u'the', u'son', u'of', u'Arphaxad', u',', u'which', u'was', u'the', u'son', u'of', u'Sem', u',', u'which', u'was', u'the', u'son', u'of', u'Noe', u',', u'which', u'was', u'the', u'son', u'of', u'Lamech', u',', u'3', u':', u'37', u'Which', u'was', u'the', u'son', u'of', u'Mathusala', u',', u'which', u'was', u'the', u'son', u'of', u'Enoch', u',', u'which', u'was', u'the', u'son', u'of', u'Jared', u',', u'which', u'was', u'the', u'son', u'of', u'Maleleel', u',', u'which', u'was', u'the', u'son', u'of', u'Cainan', u',', u'3', u':', u'38', u'Which', u'was', u'the', u'son', u'of', u'Enos', u',', u'which', u'was', u'the', u'son', u'of', u'Seth', u',', u'which', u'was', u'the', u'son', u'of', u'Adam', u',', u'which', u'was', u'the', u'son', u'of', u'God', u'.']

# 26 Modify the functions init_wfst() and complete_wfst() so that the contents of each cell in the WFST
# is a set of non-terminal symbols rather than a single non-terminal.

def ex26_init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[set() for i in range(numtokens+1)] for _ in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        for production in productions: 
            wfst[i][i].add(production.lhs())
    return wfst

def ex26_complete_wfst(wfst, tokens, grammar):
    import itertools
    import collections
    index=collections.defaultdict(set)
    for p in grammar.productions():
        index[p.rhs()].add(p.lhs())
    numtokens = len(tokens)
    for span in range(1,numtokens):
        for start in range(numtokens-span):
            end = start + span
            for mid in range(start, end):
                nt_s1, nt_s2 = wfst[start][mid], wfst[mid+1][end]
                for key in itertools.product(nt_s1,nt_s2):
                    if key in index:
                        for comb in index[key]:
                            wfst[start][end].add(comb)
    return wfst

def ex26_display(wfst):
    print('WFST ' + ' '.join(("%-12d" % i) for i in range(len(wfst)-1)))
    for i in range(len(wfst)-1):
        print("%-4d" % i),
        for j in range(len(wfst)-1):
            print("%-12s" % (wfst[i][j] or '.')),
        print('')

def ex26(grammar="""
                    S -> NP VP
                    PP -> P NP
                    NP -> Det N | Det N PP | 'I'
                    VP -> V NP | VP PP
                    Det -> 'an' | 'my'
                    N -> 'elephant' | 'pajamas' | 'shot'
                    V -> 'shot'
                    P -> 'in'
                    """,
                    sent="I shot an elephant in my pajamas".split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    wfst=ex26_init_wfst(sent, cfg_grammar)
    ex26_display(ex26_complete_wfst(wfst, sent, cfg_grammar))

# ex26(grammar="""
#                 S -> NP VP
#                 PP -> P NP
#                 NP -> Det N | Det N PP | 'I'
#                 VP -> V NP | VP PP
#                 Det -> 'an' | 'my'
#                 N -> 'elephant' | 'pajamas' | 'shot'
#                 V -> 'shot'
#                 P -> 'in'
#                 """,
#                 sent="I shot an elephant in my pajamas".split())
# WFST 0         1           2          3         4        5          6           
# 0    set([NP]) .           .          set([S])  .        .          set([S])     
# 1    .         set([V, N]) .          set([VP]) .        .          set([VP])    
# 2    .         .           set([Det]) set([NP]) .        .          .            
# 3    .         .           .          set([N])  .        .          .            
# 4    .         .           .          .         set([P]) .          set([PP])    
# 5    .         .           .          .         .        set([Det]) set([NP])    
# 6    .         .           .          .         .        .          set([N])  

# ex26(grammar="""
#                 S -> NP VP
#                 VP -> Verb PP | Verb NP
#                 NP -> Det Noun | NP PP | Noun Noun
#                 PP -> Prep NP
#                 Verb -> "flies" | "like" | "time"
#                 Prep -> "like"
#                 Det -> "a" | "an"
#                 Noun -> "arrow" | "flies" | "fruit" | "time" | "banana"
#                 NP -> "arrow" | "flies" | "fruit" | "time" | "banana"
#                 """,
#                 sent="time flies like an arrow".split())
# WFST 0                     1                     2                 3            4           
# 0    set([NP, Verb, Noun]) set([VP, NP])         .                 .          set([VP, NP, S]) 
# 1    .                     set([NP, Verb, Noun]) .                 .          set([NP, VP, S]) 
# 2    .                     .                     set([Verb, Prep]) .          set([VP, PP]) 
# 3    .                     .                     .                 set([Det]) set([NP])    
# 4    .                     .                     .                 .          set([NP, Noun]) 

# 27 Consider the algorithm in 4.4. Can you explain why parsing context-free grammar is proportional to n^3,
# where n is the length of the input sentence.

# For each token and each potential meaningful span length (which goes from 1 (2, technically) to the number of 
# tokens), all possible intermediate positions need be checked as valid hypothesis. This adds up to n_tokens x
# n_tokens x n_tokens

# 28 Process each tree of the Treebank corpus sample nltk.corpus.treebank and extract the productions
# with the help of Tree.productions(). Discard the productions that occur only once. Productions with the same left
# hand side, and similar right hand sides can be collapsed, resulting in an equivalent but more compact
# set of rules. Write code to output a compact grammar.

def ex28_rhs_to_string(rhs,exception_lst=['-NONE-', '-LRB-', '-RRB-'],simplify=True):
    terms=[]
    for term in rhs:
        try:
            if term.symbol() not in exception_lst and simplify:
                terms=terms+[ term.symbol().partition('-')[0] ]
            else:
                terms=terms+[ term.symbol() ]
        except AttributeError:
            terms=terms+[ '"{}"'.format(term.lower()) ]
    return ' '.join(terms)

def ex28_lhs_to_string(lhs,exception_lst=['-NONE-', '-LRB-', '-RRB-'],simplify=True):
    if lhs.symbol() not in exception_lst and simplify:
        return lhs.symbol().partition('-')[0]
    else:
        return lhs.symbol()

def ex28_grammar_to_string(grammar):
    import collections
    grammar_dict=collections.defaultdict(set)
    for prod in grammar.productions():
        grammar_dict[ex28_lhs_to_string(prod.lhs())].add(ex28_rhs_to_string(prod.rhs()))
    return [ [ '{} -> {}'.format(key,' | '.join(list(grammar_dict[key]))) ] for key in grammar_dict.keys() ]

def ex28(sents=nltk.corpus.treebank.parsed_sents(),num=1):
    prods=[]
    for sent in sents:
        prods=prods+sent.productions()
    fd=nltk.FreqDist(prods)
    prods=[rule for (rule,cnt) in fd.items() if cnt>num]
    grammar=nltk.grammar.CFG(start=nltk.grammar.Nonterminal('S'),productions=prods)
    return ex28_grammar_to_string(grammar)
    
# grammar_str=ex28()
# len(grammar_str)
# 69

# 29 One common way of defining the subject of a sentence S in English is as the noun phrase that is the child
# of S and the sibling of VP. Write a function that takes the tree for a sentence and returns the subtree
# corresponding to the subject of the sentence. What should it do if the root node of the tree passed to this
# function is not S, or it lacks a subject?

def ex29(my_tree=nltk.Tree.fromstring('(S (NP (DT The) (NP (N woman))) (VP (VP (V saw) (NP (DT a) (NP (N man)))) (NP (A last) (NP (N Thursday)))))')):
    if my_tree.label()=='S':
        NP=[]
        VP=[]
        for branch in my_tree:
            try:
                if branch.label().startswith('NP'):
                    NP=NP+[branch]
                elif branch.label().startswith('VP'):
                    VP=VP+[branch]
            except:
                pass
        if len(NP)==1 and len(VP)>0:
            return NP[0]
        elif len(VP)==0:
            print('No VP found')
        elif len(NP)==0:
            print('No NP found')
        else:
            print('Too many NPs found')
            return NP
    else:
        print('No S found')

# print(ex29())
# (NP (DT The) (NP (N woman)))

# 30 Write a function that takes a grammar (such as the one defined in 3.1) and returns a random sentence
# generated by the grammar. (Use grammar.start() to find the start symbol of the grammar; grammar.productions(lhs)
# to get the list of productions from the grammar that have the specified left-hand side; and production.rhs()
# to get the right-hand side of a production.)

def ex30_generate_random(cfg_grammar,start_node):
    import random
    sent=[]
    try:
        available_nodes=cfg_grammar.productions(start_node)
        selected_node=available_nodes[random.randint(0,len(available_nodes)-1)].rhs()
        for sub_node in selected_node:
            sent=sent + ex30_generate_random(cfg_grammar,sub_node)
        return sent
    except:
        return [ start_node ]
    
def ex30(grammar="""
                S -> NP VP
                PP -> P NP
                NP -> Det N | Det N PP | 'I'
                VP -> V NP | VP PP
                Det -> 'an' | 'my'
                N -> 'elephant' | 'pajamas' | 'shot'
                V -> 'shot'
                P -> 'in'
                """,
                set_seed=1):
    import random
    if set_seed:
        random.seed(set_seed)
    cfg_grammar=nltk.CFG.fromstring(grammar)
    return ex30_generate_random(cfg_grammar,nltk.grammar.Nonterminal('S'))

# ex30()
# [u'I', u'shot', u'my', u'shot', u'in', u'I', u'in', u'an', u'shot']

# 31 Implement a version of the shift-reduce parser using backtracking, so that it finds all possible parses
# for a sentence, what might be called a "recursive ascent parser." Consult the Wikipedia entry for backtracking
# at http://en.wikipedia.org/wiki/Backtracking

# Productions must have only two components, i.e., A -> B C is ok but A -> B C D is not. This can be always done
# writing the grammar carefully
# Productions must not mix terminal and not terminal tokens. This can always be done writing the grammar carefully

# Also, this assignment sucked balls, but there

# V1 - Easy(-ish) version
# Does not work with ambiguous grammars, i.e., those that have rules like A -> BLAH and B -> BLAH
# (e.g. 'The fish fish fish in the sea with a pole')

def ex31_pre_parse_v1(sent,cfg_grammar):
    return [ nltk.Tree(cfg_grammar.productions(rhs=wrd)[0].lhs(),[ wrd ]) for wrd in sent ]

def ex31_init_stack_and_queue_v1(sent,cfg_grammar):
    queue=ex31_pre_parse_v1(sent,cfg_grammar)
    stack=[ queue[0] ]
    queue=queue[1:]
    return stack, queue
    
def ex31_drill_for_starters_v1(cfg_grammar):
    dict_starters=dict([(prod_lhs,[]) for prod_lhs in list(set([prod.lhs() for prod in cfg_grammar.productions()]))])
    for prod_lhs in dict_starters.keys():
        starter_prods=cfg_grammar.productions(lhs=prod_lhs)
        for starter_prod in starter_prods:
            starter=starter_prod.rhs()[0]
            if not starter in dict_starters[prod_lhs]:
                dict_starters[prod_lhs]=dict_starters[prod_lhs]+[starter]
                started_prods=[prod.lhs() for prod in cfg_grammar.productions(rhs=prod_lhs) if prod.lhs()!=prod_lhs]
                for started_prod in started_prods:
                    if not starter in dict_starters[started_prod]:
                        dict_starters[started_prod]=dict_starters[started_prod]+[starter]
    return dict_starters

def ex31_dict_inv_grammar_v1(cfg_grammar):
    lst_non_terminals=[ prod for prod in cfg_grammar.productions() if nltk.grammar.is_nonterminal(prod.rhs()[0]) ]
    nt_cfg_grammar=nltk.CFG(nltk.grammar.Nonterminal('S'),lst_non_terminals)
    dict_starters=ex31_drill_for_starters_v1(nt_cfg_grammar)
    dict_inv_grammar=dict()
    for prod in lst_non_terminals:
        if prod.rhs() not in dict_inv_grammar.keys():
            dict_inv_grammar[prod.rhs()]=prod.lhs()
            if prod.rhs()[1] in dict_starters.keys():
                for starter in dict_starters[prod.rhs()[1]]:
                    if (prod.rhs()[0], starter) not in dict_inv_grammar.keys():
                        dict_inv_grammar[(prod.rhs()[0], starter)]=''
    for S_starter in dict_starters[nltk.grammar.Nonterminal('S')]:
        dict_inv_grammar[(S_starter,)]=''
    return dict_inv_grammar

def ex31_solution_v1(stack,queue):
    return len(stack)==1 and len(queue)==0

def ex31_candidate_v1(stack,dict_inv_grammar):
    return tuple([token.label() for token in stack[-2:]]) in dict_inv_grammar.keys()

def ex31_can_shift_v1(stack,queue,lst_with_rules):
    return len(queue)>0 and stack[-1].label() in lst_with_rules

def ex31_shifter_v1(stack,queue):
    return stack+[ queue[0] ], queue[1:]

def ex31_can_reduce_v1(stack,dict_inv_grammar):
    return dict_inv_grammar[tuple([token.label() for token in stack[-2:]])]!=''

def ex31_reducer_v1(stack,dict_inv_grammar):
    return stack[:-2] + [ nltk.Tree(dict_inv_grammar[tuple([token.label() for token in stack[-2:]])],stack[-2:]) ]

def ex31_backtracker_v1(stack,queue,dict_inv_grammar,lst_with_rules):
    sols=[]
    if ex31_solution_v1(stack,queue):
        return stack
    else:
        if ex31_candidate_v1(stack,dict_inv_grammar):
            if ex31_can_shift_v1(stack,queue,lst_with_rules):
                new_stack, new_queue = ex31_shifter_v1(stack,queue)
                sols = sols + ex31_backtracker_v1(new_stack,new_queue,dict_inv_grammar,lst_with_rules)
            if ex31_can_reduce_v1(stack,dict_inv_grammar):
                new_stack, new_queue = ex31_reducer_v1(stack,dict_inv_grammar), queue
                sols = sols + ex31_backtracker_v1(new_stack,new_queue,dict_inv_grammar,lst_with_rules)
    return sols

def ex31_v1(grammar="""
                       S  -> NP VP
                       VP -> V NP | VP PP
                       NP -> CD N | NP PP
                       PP -> P NP
                       V  -> "saw" | "ate" | "walked"
                       CD -> "a"   | "an"  | "the" | "my"
                       N  -> "man" | "dog" | "cat" | "telescope" | "park"
                       P  -> "in"  | "on"  | "by"  | "with"
                       """,
            sent='a cat in the park saw a dog with a man with a telescope'.split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    stack, queue=ex31_init_stack_and_queue_v1(sent,cfg_grammar)
    dict_inv_grammar=ex31_dict_inv_grammar_v1(cfg_grammar)
    lst_with_rules  =list(set([token[0] for token in dict_inv_grammar.keys()]))
    return ex31_backtracker_v1(stack,queue,dict_inv_grammar,lst_with_rules)

# for parse in ex31_v1(sent='a cat in the park saw a dog with a man with a telescope'.split()):
#     print(parse)
# (S
#   (NP (NP (CD a) (N cat)) (PP (P in) (NP (CD the) (N park))))
#   (VP
#     (V saw)
#     (NP
#       (NP (CD a) (N dog))
#       (PP
#         (P with)
#         (NP
#           (NP (CD a) (N man))
#           (PP (P with) (NP (CD a) (N telescope))))))))
# (S
#   (NP (NP (CD a) (N cat)) (PP (P in) (NP (CD the) (N park))))
#   (VP
#     (V saw)
#     (NP
#       (NP (NP (CD a) (N dog)) (PP (P with) (NP (CD a) (N man))))
#       (PP (P with) (NP (CD a) (N telescope))))))
# (S
#   (NP (NP (CD a) (N cat)) (PP (P in) (NP (CD the) (N park))))
#   (VP
#     (VP
#       (V saw)
#       (NP (NP (CD a) (N dog)) (PP (P with) (NP (CD a) (N man)))))
#     (PP (P with) (NP (CD a) (N telescope)))))
# (S
#   (NP (NP (CD a) (N cat)) (PP (P in) (NP (CD the) (N park))))
#   (VP
#     (VP (V saw) (NP (CD a) (N dog)))
#     (PP
#       (P with)
#       (NP
#         (NP (CD a) (N man))
#         (PP (P with) (NP (CD a) (N telescope)))))))
# (S
#   (NP (NP (CD a) (N cat)) (PP (P in) (NP (CD the) (N park))))
#   (VP
#     (VP
#       (VP (V saw) (NP (CD a) (N dog)))
#       (PP (P with) (NP (CD a) (N man))))
#     (PP (P with) (NP (CD a) (N telescope)))))

# V2 - Hard(-ish) version
# Works with ambiguous grammars, i.e., those that have rules like A -> BLAH and B -> BLAH
# (e.g. 'The fish fish fish in the sea with a pole')

def ex31_init_stack_and_queue_v2(sent):
    return [ sent[0] ], sent[1:]
    
def ex31_drill_for_starters_v2(cfg_grammar):
    dict_starters=dict([(prod_lhs,[]) for prod_lhs in list(set([prod.lhs() for prod in cfg_grammar.productions()]))])
    for prod_lhs in dict_starters.keys():
        starter_prods=cfg_grammar.productions(lhs=prod_lhs)
        for starter_prod in starter_prods:
            starter=starter_prod.rhs()[0]
            if not starter in dict_starters[prod_lhs]:
                dict_starters[prod_lhs]=dict_starters[prod_lhs]+[starter]
                started_prods=[prod.lhs() for prod in cfg_grammar.productions(rhs=prod_lhs) if prod.lhs()!=prod_lhs]
                for started_prod in started_prods:
                    if not starter in dict_starters[started_prod]:
                        dict_starters[started_prod]=dict_starters[started_prod]+[starter]
    return dict_starters

def ex31_dict_inv_grammar_v2(cfg_grammar):
    import collections
    dict_starters=ex31_drill_for_starters_v2(cfg_grammar)
    dict_inv_grammar=collections.defaultdict(set)
    for prod in cfg_grammar.productions():
        dict_inv_grammar[prod.rhs()].add(prod.lhs())
        if len(prod.rhs())>1:
            if prod.rhs()[1] in dict_starters.keys():
                for starter in dict_starters[prod.rhs()[1]]:
                    if (prod.rhs()[0], starter) not in dict_inv_grammar.keys():
                        dict_inv_grammar[(prod.rhs()[0], starter)].add('')
    for S_starter in dict_starters[nltk.grammar.Nonterminal('S')]:
        dict_inv_grammar[(S_starter,)]=''
    return dict_inv_grammar

def ex31_solution_v2(stack,queue):
    return len(stack)==1 and len(queue)==0

def ex31_candidate_v2(stack,dict_inv_grammar):
    try:
        key=tuple([token.label() for token in stack[-2:]])
    except AttributeError:
        key=(stack[-1],)
    return key in dict_inv_grammar.keys()

def ex31_can_shift_v2(stack,queue,lst_with_rules):
    try:
        key=stack[-1].label()
    except AttributeError:
        key=stack[-1]
    return len(queue)>0 and key in lst_with_rules

def ex31_shifter_v2(stack,queue):
    return stack+[ queue[0] ], queue[1:]

def ex31_can_reduce_v2(stack,dict_inv_grammar):
    try:
        key=tuple([token.label() for token in stack[-2:]])
    except AttributeError:
        key=(stack[-1],)
    return dict_inv_grammar[key]!=set([''])

def ex31_reducer_v2(stack,dict_inv_grammar):
    reductions=[]
    try:
        for option in dict_inv_grammar[tuple([token.label() for token in stack[-2:]])]:
            reductions=reductions + [ stack[:-2] + [ nltk.Tree(option,stack[-2:]) ] ]
    except AttributeError:
        for option in dict_inv_grammar[(stack[-1],)]:
            reductions=reductions + [ stack[:-1] + [ nltk.Tree(option,stack[-1:]) ] ]
    return reductions 

def ex31_backtracker_v2(stack,queue,dict_inv_grammar,lst_with_rules):
    sols=[]
    if ex31_solution_v2(stack,queue):
        return stack
    else:
        if ex31_candidate_v2(stack,dict_inv_grammar):
            if ex31_can_shift_v2(stack,queue,lst_with_rules):
                new_stack, new_queue = ex31_shifter_v2(stack,queue)
                sols = sols + ex31_backtracker_v2(new_stack,new_queue,dict_inv_grammar,lst_with_rules)
            if ex31_can_reduce_v2(stack,dict_inv_grammar):
                for new_stack in ex31_reducer_v2(stack,dict_inv_grammar):
                    sols = sols + ex31_backtracker_v2(new_stack,queue,dict_inv_grammar,lst_with_rules)
    return sols

def ex31_v2(grammar="""
                       S  -> NP VP
                       VP -> V NP | VP PP
                       NP -> CD N | NP PP
                       PP -> P NP
                       V  -> "fish"
                       CD -> "the"  | "my"   | "a"
                       N  -> "fish" | "pole" | "lake"
                       P  -> "with" | "in"
                       """,
            sent='the fish in the lake fish my fish with a pole'.split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    stack, queue=ex31_init_stack_and_queue_v2(sent)
    dict_inv_grammar=ex31_dict_inv_grammar_v2(cfg_grammar)
    lst_with_rules  =list(set([token[0] for token in dict_inv_grammar.keys() if nltk.grammar.is_nonterminal(token[0])]))
    return ex31_backtracker_v2(stack,queue,dict_inv_grammar,lst_with_rules)

# for parse in ex31_v2(sent='the fish in the lake fish my fish with a pole'.split()):
#     print(parse)
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (V fish)
#     (NP (NP (CD my) (N fish)) (PP (P with) (NP (CD a) (N pole))))))
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (VP (V fish) (NP (CD my) (N fish)))
#     (PP (P with) (NP (CD a) (N pole)))))

# And this is the class version

class ShiftReduceWithBacktrackingAndLeftCornerFiltering(nltk.parse.api.ParserI):
    def __init__(self, grammar):
        self._grammar = grammar
        self._dict_inv_grammar=self._dict_inv_grammar(grammar)
        self._lst_with_rules  =list(set([token[0] for token in self._dict_inv_grammar.keys() if nltk.grammar.is_nonterminal(token[0])]))
    def _drill_for_starters(self, grammar):
        dict_starters=dict([(prod_lhs,[]) for prod_lhs in list(set([prod.lhs() for prod in grammar.productions()]))])
        for prod_lhs in dict_starters.keys():
            starter_prods=grammar.productions(lhs=prod_lhs)
            for starter_prod in starter_prods:
                starter=starter_prod.rhs()[0]
                if not starter in dict_starters[prod_lhs]:
                    dict_starters[prod_lhs]=dict_starters[prod_lhs]+[starter]
                    started_prods=[prod.lhs() for prod in grammar.productions(rhs=prod_lhs) if prod.lhs()!=prod_lhs]
                    for started_prod in started_prods:
                        if not starter in dict_starters[started_prod]:
                            dict_starters[started_prod]=dict_starters[started_prod]+[starter]
        return dict_starters
    def _dict_inv_grammar(self,grammar):
        import collections
        dict_starters=self._drill_for_starters(grammar)
        dict_inv_grammar=collections.defaultdict(set)
        for prod in grammar.productions():
            dict_inv_grammar[prod.rhs()].add(prod.lhs())
            if len(prod.rhs())>1:
                if prod.rhs()[1] in dict_starters.keys():
                    for starter in dict_starters[prod.rhs()[1]]:
                        if (prod.rhs()[0], starter) not in dict_inv_grammar.keys():
                            dict_inv_grammar[(prod.rhs()[0], starter)].add('')
        for S_starter in dict_starters[nltk.grammar.Nonterminal('S')]:
            dict_inv_grammar[(S_starter,)]=''
        return dict_inv_grammar
    def _init_stack_and_queue(self,sent):
        return [ sent[0] ], sent[1:]
    def _solution(self,stack,queue):
        return len(stack)==1 and len(queue)==0
    def _candidate(self,stack):
        try:
            key=tuple([token.label() for token in stack[-2:]])
        except AttributeError:
            key=(stack[-1],)
        return key in self._dict_inv_grammar.keys()
    def _can_shift(self,stack,queue):
        try:
            key=stack[-1].label()
        except AttributeError:
            key=stack[-1]
        return len(queue)>0 and key in self._lst_with_rules
    def _shifter(self,stack,queue):
        return stack+[ queue[0] ], queue[1:]
    def _can_reduce(self,stack):
        try:
            key=tuple([token.label() for token in stack[-2:]])
        except AttributeError:
            key=(stack[-1],)
        return self._dict_inv_grammar[key]!=set([''])
    def _reducer(self,stack):
        reductions=[]
        try:
            for option in self._dict_inv_grammar[tuple([token.label() for token in stack[-2:]])]:
                reductions=reductions + [ stack[:-2] + [ nltk.Tree(option,stack[-2:]) ] ]
        except AttributeError:
            for option in self._dict_inv_grammar[(stack[-1],)]:
                reductions=reductions + [ stack[:-1] + [ nltk.Tree(option,stack[-1:]) ] ]
        return reductions 
    def _backtracker(self,stack,queue):
        if self._solution(stack,queue):
            yield stack[0]
        else:
            if self._candidate(stack):
                if self._can_shift(stack,queue):
                    new_stack, new_queue = self._shifter(stack,queue)
                    for sol in self._backtracker(new_stack,new_queue):
                        yield sol
                if self._can_reduce(stack):
                    for new_stack in self._reducer(stack):
                        for sol in self._backtracker(new_stack,queue):
                            yield sol
    def parse(self,sent):
        stack, queue=self._init_stack_and_queue(sent)
        return self._backtracker(stack,queue)

def ex31_v3(grammar="""
                       S  -> NP VP
                       VP -> V NP | VP PP
                       NP -> CD N | NP PP
                       PP -> P NP
                       V  -> "fish"
                       CD -> "the"  | "my"   | "a"
                       N  -> "fish" | "pole" | "lake"
                       P  -> "with" | "in"
                       """,
            sent='the fish in the lake fish my fish with a pole'.split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    parser=ShiftReduceWithBacktrackingAndLeftCornerFiltering(cfg_grammar)
    for p in parser.parse(sent):
        print p

# ex31_v3()
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (V fish)
#     (NP (NP (CD my) (N fish)) (PP (P with) (NP (CD a) (N pole))))))
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (VP (V fish) (NP (CD my) (N fish)))
#     (PP (P with) (NP (CD a) (N pole)))))

# 32 As we saw in 7., it is possible to collapse chunks down to their chunk label. When we do this for sentences
# involving the word gave, we find patterns such as the following:
# - gave NP
# - gave up NP in NP
# - gave NP up
# - gave NP NP
# - gave NP to NP
# - Use this method to study the complementation patterns of a verb of interest, and write suitable grammar
# productions. (This task is sometimes called lexical acquisition.)
# - Identify some English verbs that are near-synonyms, such as the dumped/filled/loaded example from earlier
# in this chapter. Use the chunking method to study the complementation patterns of these verbs. Create a grammar
# to cover these cases. Can the verbs be freely substituted for each other, or are their constraints? Discuss your
# findings.

def ex32_collapse_tree(tree, keep_preps=True, shorten_codes=True, keep_target=False):
    aux_out=[ tree[0][0] ] if keep_target else []
    for t in tree[1:]:
        if keep_preps and t.label().startswith('PP'):
            aux_out=aux_out+[ t[0][0], t[1][0].label()[:2] if shorten_codes else t[1][0].label() ]
        else:
            aux_out=aux_out+[ t.label()[:2] if shorten_codes else t.label() ]
    return ' '.join(aux_out)

def ex32_jaccard(set_a,set_b):
    return 1.0 * len(set_a.union(set_b)-set_a.intersection(set_b)) / len(set_a.union(set_b))

def ex32(target='gave',sents=nltk.corpus.treebank.parsed_sents(),
         keep_preps=True,shorten_codes=True):
    aux_out=set()
    for sent in sents:
        located = [ ex32_collapse_tree(tree,keep_preps,shorten_codes) for tree in sent.subtrees(lambda t: t.label()=='VP' and t[0][0]==target) ]
        for loc in located:
            aux_out.add(loc)
    return aux_out

# sets=map(ex32,['gave','dumped','filled','loaded'])
# 
# 'gave'
#
# for clause in list(sets[0]):
#     print clause 
# NP
# NP NP AD
# NP NP
# NP to NP
# PR NP
# NP to NN
# NP PR
# PR S
# 
# 'dumped'
#
# for clause in list(sets[1]):
#     print clause 
# NP
# NP on DT
# NP into NP in DT
# NP into DT
# 
# 'filled'
#
# for clause in list(sets[2]):
#     print clause 
# NP with NP
# 
# 'loaded'
#
# for clause in list(sets[3]):
#     print clause 
# NP

# ex32_jaccard(sets[0],sets[1])
# 0.9090909090909091
# ex32_jaccard(sets[0],sets[2])
# 1.0
# ex32_jaccard(sets[0],sets[3])
# 0.875
# 
# ex32_jaccard(sets[1],sets[2])
# 1.0
# ex32_jaccard(sets[1],sets[3])
# 0.75
# ex32_jaccard(sets[2],sets[3])
# 1.0

# Improving the clustering of meaning by using the Jaccard distance would require more processing of the labels
# and probably more data so that examples of all usages are available. Another option would be to return a 
# FreqDist instead of a set, but that would require a different distance function

# 33 Develop a left-corner parser based on the recursive descent parser, and inheriting from ParseI.

# Left-corner parsing, despite what the book says, does NOT on its own (as described in the book) avoid
# the left hand recursion trap - and neither does my implementation.

class LeftCornerParser(nltk.parse.api.ParserI):
    """
    A simple top-down CFG parser that parses texts by recursively
    expanding the fringe of a Tree, and matching it against a
    text.
    
    Left-Corner checking added by yours truly.

    ``LeftCornerParser`` uses a list of tree locations called a
    "frontier" to remember which subtrees have not yet been expanded
    and which leaves have not yet been matched against the text.  Each
    tree location consists of a list of child indices specifying the
    path from the root of the tree to a subtree or a leaf; see the
    reference documentation for Tree for more information
    about tree locations.
    
    Only subtrees deemed Left-Corner Worthy will be added to the frontier.

    When the parser begins parsing a text, it constructs a tree
    containing only the start symbol, and a frontier containing the
    location of the tree's root node.  It then extends the tree to
    cover the text, using the following recursive procedure:

      - If the frontier is empty, and the text is covered by the tree,
        then return the tree as a possible parse.
      - If the frontier is empty, and the text is not covered by the
        tree, then return no parses.
      - If the first element of the frontier is a subtree, then
        use CFG productions to "expand" it.  For each applicable
        production, add the expanded subtree's children to the
        frontier, and recursively find all parses that can be
        generated by the new tree and frontier.
      - If the first element of the frontier is a token, then "match"
        it against the next token from the text.  Remove the token
        from the frontier, and recursively find all parses that can be
        generated by the new tree and frontier.

    :see: ``nltk.grammar``
    """
    def __init__(self, grammar):
        """
        Create a new ``RecursiveDescentParser``, that uses ``grammar``
        to parse texts.

        :type grammar: CFG
        :param grammar: The grammar used to parse texts.
        """
        self._grammar = grammar
        self._left_corner_table=self._drill_for_starters(grammar)
    def _drill_for_starters(self, grammar):
        dict_starters=dict([(prod_lhs,[]) for prod_lhs in list(set([prod.lhs() for prod in grammar.productions()]))])
        for prod_lhs in dict_starters.keys():
            starter_prods=grammar.productions(lhs=prod_lhs)
            for starter_prod in starter_prods:
                starter=starter_prod.rhs()[0]
                if not starter in dict_starters[prod_lhs]:
                    dict_starters[prod_lhs]=dict_starters[prod_lhs]+[starter]
                    started_prods=[prod.lhs() for prod in grammar.productions(rhs=prod_lhs) if prod.lhs()!=prod_lhs]
                    for started_prod in started_prods:
                        if not starter in dict_starters[started_prod]:
                            dict_starters[started_prod]=dict_starters[started_prod]+[starter]
        for prod in grammar.productions():
            for term in prod.rhs():
                if not term in dict_starters.keys():
                    dict_starters[term]=[ term ]
        return dict_starters
    def grammar(self):
        return self._grammar
    def parse(self, tokens):
        # Inherit docs from ParserI
        tokens = list(tokens)
        self._grammar.check_coverage(tokens)
        # Start a recursive descent parse, with an initial tree
        # containing just the start symbol.
        start = self._grammar.start().symbol()
        initial_tree = nltk.Tree(start, [])
        frontier = [()]
        return self._parse(tokens, initial_tree, frontier)
    def _parse(self, remaining_text, tree, frontier):
        """
        Recursively expand and match each elements of ``tree``
        specified by ``frontier``, to cover ``remaining_text``.  Return
        a list of all parses found.

        :return: An iterator of all parses that can be generated by
            matching and expanding the elements of ``tree``
            specified by ``frontier``.
        :rtype: iter(Tree)
        :type tree: Tree
        :param tree: A partial structure for the text that is
            currently being parsed.  The elements of ``tree``
            that are specified by ``frontier`` have not yet been
            expanded or matched.
        :type remaining_text: list(str)
        :param remaining_text: The portion of the text that is not yet
            covered by ``tree``.
        :type frontier: list(tuple(int))
        :param frontier: A list of the locations within ``tree`` of
            all subtrees that have not yet been expanded, and all
            leaves that have not yet been matched.  This list sorted
            in left-to-right order of location within the tree.
        """
        # If the tree covers the text, and there's nothing left to
        # expand, then we've found a complete parse; return it.
        if len(remaining_text) == 0 and len(frontier) == 0:
            # DEBUG print "Found a candidate tree:"
            yield tree
        # If there's still text, but nothing left to expand, we failed.
        elif len(frontier) == 0:
            # DEBUG print "Nothing to expand but not yet done - backtracking"
            pass
        # If the next element on the frontier is a tree, expand it.
        elif isinstance(tree[frontier[0]], nltk.Tree):
            for result in self._expand(remaining_text, tree, frontier):
                yield result
        # If the next element on the frontier is a token, match it.
        else:
            for result in self._match(remaining_text, tree, frontier):
                yield result
    def _match(self, rtext, tree, frontier):
        """
        :rtype: iter(Tree)
        :return: an iterator of all parses that can be generated by
            matching the first element of ``frontier`` against the
            first token in ``rtext``.  In particular, if the first
            element of ``frontier`` has the same type as the first
            token in ``rtext``, then substitute the token into
            ``tree``; and return all parses that can be generated by
            matching and expanding the remaining elements of
            ``frontier``.  If the first element of ``frontier`` does not
            have the same type as the first token in ``rtext``, then
            return empty list.

        :type tree: Tree
        :param tree: A partial structure for the text that is
            currently being parsed.  The elements of ``tree``
            that are specified by ``frontier`` have not yet been
            expanded or matched.
        :type rtext: list(str)
        :param rtext: The portion of the text that is not yet
            covered by ``tree``.
        :type frontier: list of tuple of int
        :param frontier: A list of the locations within ``tree`` of
            all subtrees that have not yet been expanded, and all
            leaves that have not yet been matched.
        """
        # DEBUG print rtext
        # DEBUG print tree
        # DEBUG print frontier
        # DEBUG print "Matching node:"
        # DEBUG print tree[frontier[0]]
        tree_leaf = tree[frontier[0]]
        if (len(rtext) > 0 and tree_leaf == rtext[0]):
            # If it's a terminal that matches rtext[0], then substitute
            # in the token, and continue parsing.
            # DEBUG print "Matched {}".format(tree_leaf)
            # DEBUG raw_input("(Enter to continue)")
            newtree = tree.copy(deep=True)
            newtree[frontier[0]] = rtext[0]
            for result in self._parse(rtext[1:], newtree, frontier[1:]):
                yield result
        # DEBUG else:
            # DEBUG print "{} (expected in the tree) did not match against {} (next token)".format(tree_leaf, rtext[0])
            # DEBUG raw_input("(Enter to continue)")
    def _expand(self, remaining_text, tree, frontier, production=None):
        """
        :rtype: iter(Tree)
        :return: An iterator of all parses that can be generated by
            expanding the first element of ``frontier`` with
            ``production``.  In particular, if the first element of
            ``frontier`` is a subtree whose node type is equal to
            ``production``'s left hand side, then add a child to that
            subtree for each element of ``production``'s right hand
            side; and return all parses that can be generated by
            matching and expanding the remaining elements of
            ``frontier``.  If the first element of ``frontier`` is not a
            subtree whose node type is equal to ``production``'s left
            hand side, then return an empty list.  If ``production`` is
            not specified, then return a list of all parses that can
            be generated by expanding the first element of ``frontier``
            with *any* CFG production.

        :type tree: Tree
        :param tree: A partial structure for the text that is
            currently being parsed.  The elements of ``tree``
            that are specified by ``frontier`` have not yet been
            expanded or matched.
        :type remaining_text: list(str)
        :param remaining_text: The portion of the text that is not yet
            covered by ``tree``.
        :type frontier: list(tuple(int))
        :param frontier: A list of the locations within ``tree`` of
            all subtrees that have not yet been expanded, and all
            leaves that have not yet been matched.
        """
        # DEBUG print remaining_text
        # DEBUG print tree
        # DEBUG print frontier
        # DEBUG print "Expanding node:"
        # DEBUG print tree[frontier[0]]
        if production is None: productions = self._grammar.productions()
        else: productions = [production]
        for production in productions:
            lhs = production.lhs().symbol()
            # These are the lines changed to implement Left-Corner Parsing
            if lhs == tree[frontier[0]].label():
                if len(remaining_text)>0:
                    # DEBUG print "Trying to expand production {}".format(production)
                    if remaining_text[0] in self._left_corner_table[production.rhs()[0]]:
                        # DEBUG print "Production opener {}, with starters {}, matched against {}".format(production.rhs()[0], self._left_corner_table[production.rhs()[0]], remaining_text[0])
                        # That is it
                        subtree = self._production_to_tree(production)
                        if frontier[0] == ():
                            newtree = subtree
                        else:
                            newtree = tree.copy(deep=True)
                            newtree[frontier[0]] = subtree
                        new_frontier = [frontier[0]+(i,) for i in
                                        range(len(production.rhs()))]
                        # DEBUG raw_input("(Enter to continue)")
                        for result in self._parse(remaining_text, newtree,
                                                  new_frontier + frontier[1:]):
                            yield result
                    # DEBUG else:
                        # DEBUG print "Production opener {}, with starters {}, did not match against {}".format(production.rhs()[0], self._left_corner_table[production.rhs()[0]], remaining_text[0])
                        # DEBUG raw_input("(Enter to continue)")
    def _production_to_tree(self, production):
        """
        :rtype: Tree
        :return: The Tree that is licensed by ``production``.
            In particular, given the production ``[lhs -> elt[1] ... elt[n]]``
            return a tree that has a node ``lhs.symbol``, and
            ``n`` children.  For each nonterminal element
            ``elt[i]`` in the production, the tree token has a
            childless subtree with node value ``elt[i].symbol``; and
            for each terminal element ``elt[j]``, the tree token has
            a leaf token with type ``elt[j]``.

        :param production: The CFG production that licenses the tree
            token that should be returned.
        :type production: Production
        """
        children = []
        for elt in production.rhs():
            if isinstance(elt, nltk.Nonterminal):
                children.append(nltk.Tree(elt.symbol(), []))
            else:
                # This will be matched.
                children.append(elt)
        return nltk.Tree(production.lhs().symbol(), children)

def ex33(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> NPP | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    NPP -> "John" | "Mary" | "Bob"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
                sent="John saw a man with a telescope".split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    parser=LeftCornerParser(cfg_grammar)
    return parser.parse(sent)

# num_trees=0
# for tree in ex33(grammar="""
#                     S -> NP VP
#                     VP -> V NP | V NP PP
#                     PP -> P NP
#                     V -> "saw" | "ate" | "walked"
#                     NP -> NPP | Det N | Det N PP
#                     Det -> "a" | "an" | "the" | "my"
#                     NPP -> "John" | "Mary" | "Bob"
#                     N -> "man" | "dog" | "cat" | "telescope" | "park"
#                     P -> "in" | "on" | "by" | "with"
#                     """,
#                 sent="John saw a man with a telescope".split()):
#     num_trees=num_trees+1
#     print tree
# print num_trees
# (S
#   (NP (NPP John))
#   (VP
#     (V saw)
#     (NP (Det a) (N man) (PP (P with) (NP (Det a) (N telescope))))))
# (S
#   (NP (NPP John))
#   (VP
#     (V saw)
#     (NP (Det a) (N man))
#     (PP (P with) (NP (Det a) (N telescope)))))
# 2

# Inheriting from nltk.RecursiveDescentParser

class LeftCornerParserRD(nltk.RecursiveDescentParser):
    def __init__(self, grammar, trace=0):
        self._grammar = grammar
        self._trace = trace
        self._left_corner_table=self._drill_for_starters(grammar)
    def _drill_for_starters(self, grammar):
        dict_starters=dict([(prod_lhs,[]) for prod_lhs in list(set([prod.lhs() for prod in grammar.productions()]))])
        for prod_lhs in dict_starters.keys():
            starter_prods=grammar.productions(lhs=prod_lhs)
            for starter_prod in starter_prods:
                starter=starter_prod.rhs()[0]
                if not starter in dict_starters[prod_lhs]:
                    dict_starters[prod_lhs]=dict_starters[prod_lhs]+[starter]
                    started_prods=[prod.lhs() for prod in grammar.productions(rhs=prod_lhs) if prod.lhs()!=prod_lhs]
                    for started_prod in started_prods:
                        if not starter in dict_starters[started_prod]:
                            dict_starters[started_prod]=dict_starters[started_prod]+[starter]
        for prod in grammar.productions():
            for term in prod.rhs():
                if not term in dict_starters.keys():
                    dict_starters[term]=[ term ]
        return dict_starters
    def _expand(self, remaining_text, tree, frontier, production=None):
        if production is None: productions = self._grammar.productions()
        else: productions = [production]
        for production in productions:
            lhs = production.lhs().symbol()
            # These are the lines changed to implement Left-Corner Parsing
            if lhs == tree[frontier[0]].label():
                if len(remaining_text)>0:
                    if remaining_text[0] in self._left_corner_table[production.rhs()[0]]:
                        # That is it
                        subtree = self._production_to_tree(production)
                        if frontier[0] == ():
                            newtree = subtree
                        else:
                            newtree = tree.copy(deep=True)
                            newtree[frontier[0]] = subtree
                        new_frontier = [frontier[0]+(i,) for i in
                                        range(len(production.rhs()))]
                        if self._trace:
                            self._trace_expand(newtree, new_frontier, production)
                        for result in self._parse(remaining_text, newtree,
                                                  new_frontier + frontier[1:]):
                            yield result

def ex33_v2(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> NPP | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    NPP -> "John" | "Mary" | "Bob"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
                sent="John saw a man with a telescope".split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    parser=LeftCornerParserRD(cfg_grammar)
    return parser.parse(sent)

# num_trees=0
# for tree in ex33_v2(grammar="""
#                     S -> NP VP
#                     VP -> V NP | V NP PP
#                     PP -> P NP
#                     V -> "saw" | "ate" | "walked"
#                     NP -> NPP | Det N | Det N PP
#                     Det -> "a" | "an" | "the" | "my"
#                     NPP -> "John" | "Mary" | "Bob"
#                     N -> "man" | "dog" | "cat" | "telescope" | "park"
#                     P -> "in" | "on" | "by" | "with"
#                     """,
#                 sent="John saw a man with a telescope".split()):
#     num_trees=num_trees+1
#     print tree
# print num_trees
# (S
#   (NP (NPP John))
#   (VP
#     (V saw)
#     (NP (Det a) (N man) (PP (P with) (NP (Det a) (N telescope))))))
# (S
#   (NP (NPP John))
#   (VP
#     (V saw)
#     (NP (Det a) (N man))
#     (PP (P with) (NP (Det a) (N telescope)))))
# 2

def ex33_timer(grammar="""
                    S -> NP VP
                    VP -> V NP | V NP PP
                    PP -> P NP
                    V -> "saw" | "ate" | "walked"
                    NP -> NPP | Det N | Det N PP
                    Det -> "a" | "an" | "the" | "my"
                    NPP -> "John" | "Mary" | "Bob"
                    N -> "man" | "dog" | "cat" | "telescope" | "park"
                    P -> "in" | "on" | "by" | "with"
                    """,
                sent='a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a cat on a dog with a man in a park with a telescope'.split(),
                parsers=[ nltk.RecursiveDescentParser, LeftCornerParser, LeftCornerParserRD ],
                loops=1000000):
    import timeit
    cfg_grammar = nltk.CFG.fromstring(grammar)
    aux_out=[]
    for parser in parsers:
        t_pars=parser(cfg_grammar)
        tim_out=timeit.Timer(lambda: t_pars.parse(sent)).timeit(number=loops)
        num_trees=sum([1 for _ in t_pars.parse(sent)])
        aux_out=aux_out+[[num_trees,tim_out]]
    return aux_out

# ex33_timer(grammar="""
#                     S -> NP VP
#                     VP -> V NP | V NP PP
#                     PP -> P NP
#                     V -> "saw" | "ate" | "walked"
#                     NP -> NPP | Det N | Det N PP
#                     Det -> "a" | "an" | "the" | "my"
#                     N -> "man" | "dog" | "cat" | "telescope" | "park"
#                     P -> "in" | "on" | "by" | "with"
#                     NPP -> "John" | "Mary" | "Bob"
#                     """,
#                 sent='a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a cat on a dog with a man in a park with a telescope'.split())
# [[9, 13.242717027664185], [9, 13.447087049484253], [9, 13.534765005111694]]
# 
# ex33_timer(grammar="""
#                     S -> NP VP
#                     VP -> V NP | V NP PP
#                     PP -> P NP
#                     V -> "saw" | "ate" | "walked"
#                     NP -> NPP | Det N | Det N PP
#                     Det -> "a" | "an" | "the" | "my"
#                     N -> "man" | "dog" | "cat" | "telescope" | "park"
#                     P -> "in" | "on" | "by" | "with"
#                     NPP -> NP01 | NP02 | NP03
#                     NP01 -> NP11 | NP12 | NP13
#                     NP02 -> NP11 | NP12 | NP13
#                     NP03 -> NP11 | NP12 | NP13
#                     NP11 -> "John" | "Bob" | "Jeremy" | "Charlie" | "Lucy" | "Mary" | "Betty" | "Bo" | "LucasKlander" | "Batman" | "TheBigMonster"
#                     NP12 -> "John" | "Bob" | "Jeremy" | "Charlie" | "Lucy" | "Mary" | "Betty" | "Bo" | "LucasKlander" | "Batman" | "TheBigMonster"
#                     NP13 -> "John" | "Bob" | "Jeremy" | "Charlie" | "Lucy" | "Mary" | "Betty" | "Bo" | "LucasKlander" | "Batman" | "TheBigMonster"
#                     """,
#                 sent='a cat on a dog with a man in a park saw a cat on a dog with a man in a park on a cat on a dog with a man in a park with a telescope'.split())
# [[9, 13.816289186477661], [9, 13.424597024917603], [9, 13.421097993850708]]

# I guess the grammar must be made much more complex for the efficiency gains to become more visible

# 34 Extend NLTK's shift-reduce parser to incorporate backtracking, so that it is guaranteed to find all parses
# that exist (i.e. it is complete).

class ShiftReduceWithBacktracking(nltk.ShiftReduceParser):
    def _parse(self, stack, remaining_text):
        # DEBUG print stack
        # DEBUG remaining_text
        if len(remaining_text)==0 and len(stack)==1:
            yield stack[0]
        else:
            if len(remaining_text)>0:
                for p in self._parse(stack+[remaining_text[0]],remaining_text[1:]):
                    yield p
            if len(stack)>0:
                # Try each production, in order.
                for production in self._grammar.productions():
                    rhslen = len(production.rhs())
                    # check if the RHS of a production matches the top of the stack
                    if self._match_rhs(production.rhs(), stack[-rhslen:]):
                        # combine the tree to reflect the reduction
                        tree = nltk.Tree(production.lhs().symbol(), stack[-rhslen:])
                        for p in self._parse(stack[:-rhslen]+[tree],remaining_text):
                            yield p
                        # We reduced something
                        if self._trace:
                            self._trace_reduce(stack[:-rhslen]+[tree], production, remaining_text)
    def parse(self, tokens):
        tokens = list(tokens)
        self._grammar.check_coverage(tokens)
        # initialize the stack.
        stack = []
        remaining_text = tokens
        # Trace output.
        if self._trace:
            print('Parsing %r' % " ".join(tokens))
            self._trace_stack(stack, remaining_text)
        return self._parse(stack, remaining_text)
    def _check_grammar(self):
        pass

def ex34(grammar="""
                       S  -> NP VP
                       VP -> V NP | VP PP
                       NP -> CD N | NP PP
                       PP -> P NP
                       V  -> "fish"
                       CD -> "the"  | "my"   | "a"
                       N  -> "fish" | "pole" | "lake"
                       P  -> "with" | "in"
                       """,
            sent='the fish in the lake fish my fish with a pole'.split()):
    cfg_grammar = nltk.CFG.fromstring(grammar)
    parser=ShiftReduceWithBacktracking(cfg_grammar)
    for p in parser.parse(sent):
        print p

# ex34()
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (V fish)
#     (NP (NP (CD my) (N fish)) (PP (P with) (NP (CD a) (N pole))))))
# (S
#   (NP (NP (CD the) (N fish)) (PP (P in) (NP (CD the) (N lake))))
#   (VP
#     (VP (V fish) (NP (CD my) (N fish)))
#     (PP (P with) (NP (CD a) (N pole)))))

# ShiftReduceWithBacktracking against ShiftReduceWithBacktrackingAndLeftCornerFiltering

def ex34_timer(grammar="""
                       S  -> NP VP
                       VP -> V NP | VP PP
                       NP -> CD N | NP PP
                       PP -> P NP
                       V  -> "fish"
                       CD -> "the"  | "my"   | "a"
                       N  -> "fish" | "pole" | "lake"
                       P  -> "with" | "in"
                       """,
            sent='the fish in the lake fish my fish with a pole'.split(),
                parsers=[ ShiftReduceWithBacktracking, ShiftReduceWithBacktrackingAndLeftCornerFiltering ],
                loops=1000000):
    import timeit
    cfg_grammar = nltk.CFG.fromstring(grammar)
    aux_out=[]
    for parser in parsers:
        t_pars=parser(cfg_grammar)
        tim_out=timeit.Timer(lambda: t_pars.parse(sent)).timeit(number=loops)
        num_trees=sum([1 for _ in t_pars.parse(sent)])
        aux_out=aux_out+[[num_trees,tim_out]]
    return aux_out

# ex34_timer()
# [[2, 4.968210935592651], [2, 0.9873178005218506]]

# Hooray!!!

# 35 Modify the functions init_wfst() and complete_wfst() so that when a non-terminal symbol is added to a cell
# in the WFST, it includes a record of the cells from which it was derived. Implement a function that will convert
# a WFST in this form to a parse tree.

def ex35_init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[(None,) for i in range(numtokens+1)] for _ in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        for production in productions: 
            wfst[i][i]=(production.lhs(),[tokens[i]])
    return wfst

def ex35_complete_wfst(wfst, tokens, grammar):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(1,numtokens):
        for start in range(numtokens-span):
            end = start + span
            for mid in range(start, end):
                nt_s1, nt_s2 = wfst[start][mid][0], wfst[mid+1][end][0]
                if (nt_s1,nt_s2) in index:
                    wfst[start][end]=(index[(nt_s1,nt_s2)],[(start,mid),(mid+1,end)])
    return wfst

def ex35_display(wfst):
    print('WFST ' + ' '.join(("%-12d" % i) for i in range(len(wfst)-1)))
    for i in range(len(wfst)-1):
        print("%-4d" % i),
        for j in range(len(wfst)-1):
            print("%-12s" % (wfst[i][j][0] or '.')),
        print('')

def ex35_wfst_to_tree(wfst,start_node=None):
    if not start_node:
        start_node=(0,len(wfst)-2)
    tree=nltk.Tree(wfst[start_node[0]][start_node[1]][0].symbol(),[])
    if len(wfst[start_node[0]][start_node[1]][1])==1:
        tree.append(wfst[start_node[0]][start_node[1]][1][0])
        return tree
    else:
        for leave in wfst[start_node[0]][start_node[1]][1]:
            tree.append(ex35_wfst_to_tree(wfst,leave))
        return tree

def ex35(grammar="""
                    S -> NP VP
                    PP -> P NP
                    NP -> Det N | Det N PP | 'I'
                    VP -> V NP | VP PP
                    Det -> 'an' | 'my'
                    N -> 'elephant' | 'pajamas' | 'shot'
                    V -> 'shot'
                    P -> 'in'
                    """,
                    sent="I shot an elephant in my pajamas".split()):
    cfg_grammar=nltk.CFG.fromstring(grammar)
    wfst=ex35_init_wfst(sent, cfg_grammar)
    return ex35_complete_wfst(wfst, sent, cfg_grammar)

# ex35_display(ex35())
# WFST 0            1            2            3            4            5            6           
# 0    NP           .            .            S            .            .            S            
# 1    .            V            .            VP           .            .            VP           
# 2    .            .            Det          NP           .            .            .            
# 3    .            .            .            N            .            .            .            
# 4    .            .            .            .            P            .            PP           
# 5    .            .            .            .            .            Det          NP           
# 6    .            .            .            .            .            .            N 

# print(ex35_wfst_to_tree(ex35()))
# (S
#   (NP I)
#   (VP
#     (VP (V shot) (NP (Det an) (N elephant)))
#     (PP (P in) (NP (Det my) (N pajamas)))))