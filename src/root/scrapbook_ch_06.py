'''
Created on Sep 8, 2015

@author: ggomarr
'''

import nltk

# 1 Read up on one of the language technologies mentioned in this section, such as word sense disambiguation, semantic role labeling, question answering, machine translation, named entity detection. Find out what type and quantity of annotated data is required for developing such systems. Why do you think a large amount of data is required?

# NA

# 2 Using any of the three classifiers described in this chapter, and any features you can think of,
# build the best name gender classifier you can. Begin by splitting the Names Corpus into three subsets:
# 500 words for the test set, 500 words for the dev-test set, and the remaining 6900 words for the training set.
# Then, starting with the example name gender classifier, make incremental improvements.
# Use the dev-test set to check your progress. Once you are satisfied with your classifier,
# check its final performance on the test set. How does the performance on the test set compare
# to the performance on the dev-test set? Is this what you'd expect?

def ex02_fe_01(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos-1"] = nom[-1:]
    return my_features

def ex02_fe_02(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    return my_features

def ex02_fe_02_l(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    my_features["length"] = len(nom)
    return my_features

def ex02_fe_03(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos+1"] = nom[:0]
    my_features["pos+2"] = nom[:1]
    my_features["pos+3"] = nom[:2]
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    return my_features

def ex02_fe_03_l(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos+1"] = nom[:0]
    my_features["pos+2"] = nom[:1]
    my_features["pos+3"] = nom[:2]
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    my_features["length"] = len(nom)
    return my_features

def ex02_fe_04(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos+1"] = nom[:0]
    my_features["pos+2"] = nom[:1]
    my_features["pos+3"] = nom[:2]
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    my_features["length"] = len(nom)
    vowels=['a','e','i','o','u']
    my_features["num_vowels"] = sum( [ nom.count(vowel) for vowel in vowels ] )
    return my_features

def ex02_fe_05(nom):
    nom = nom.lower()
    my_features = {}
    my_features["pos+1"] = nom[:0]
    my_features["pos+2"] = nom[:1]
    my_features["pos+3"] = nom[:2]
    my_features["pos-1"] = nom[-1:]
    my_features["pos-2"] = nom[-2:]
    my_features["pos-3"] = nom[-3:]
    my_features["length"] = len(nom)
    vowels=['a','e','i','o','u']
    my_features["num_vowels"] = sum( [ nom.count(vowel) for vowel in vowels ] )
    my_features["starts_with_vowel"] = nom[0] in vowels
    return my_features

def ex02_construct_data():
    return [(name, 'male') for name in nltk.corpus.names.words('male.txt')] + [(name, 'female') for name in nltk.corpus.names.words('female.txt')]
   
def ex02_extract_features(data_set,extractor=ex02_fe_01):
    return [ (extractor(nom),gender) for (nom,gender) in data_set ]

def ex02_split_data(feature_set, fracs=[0.98,0.01,0.01], rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    random.shuffle(feature_set)
    num_inst=[ int(len(feature_set)*frac) for frac in fracs ]
    return feature_set[:num_inst[0]], feature_set[num_inst[0]:num_inst[0]+num_inst[1]], feature_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]

def ex02_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex02_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex02(train_classifiers=[True,True,True], feature_extractor=ex02_fe_03_l, final=False):
    my_data=ex02_construct_data()
    my_f_set=ex02_extract_features(my_data, feature_extractor)
    my_dev, my_dev_test, my_test=ex02_split_data(my_f_set, fracs=[0.5,0.25,0.25], rnd_seed=1)
    my_classifiers=ex02_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex02_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex02_perfs(my_classifiers,my_dev_test)
    return my_perfs

# ex02(feature_extractor=ex02_fe_01)
# [0.7613293051359517, 0.7608257804632427, 0.7613293051359517]
# ex02(feature_extractor=ex02_fe_02)
# [0.7598187311178247, 0.8001007049345418, 0.7995971802618328]
# ex02(feature_extractor=ex02_fe_02_l)
# [0.7381671701913394, 0.797583081570997, 0.8006042296072508]
# ex02(feature_extractor=ex02_fe_03)
# [0.7220543806646526, 0.8207452165156093, 0.8141993957703928]
# ex02(feature_extractor=ex02_fe_03_l)
# [0.7225579053373615, 0.823766364551863, 0.8141993957703928]
# ex02(feature_extractor=ex02_fe_04)
# [0.7215508559919436, 0.8101711983887211, 0.8136958710976838]
# ex02(feature_extractor=ex02_fe_05)
# [0.7215508559919436, 0.81067472306143, 0.8136958710976838]

# ex02(feature_extractor=ex02_fe_03_l, final=True)
# [0.7185297079556898, 0.8026183282980867, 0.8061430010070494]

# 3 The Senseval 2 Corpus contains data intended to train word-sense disambiguation classifiers.
# It contains data for four words: hard, interest, line, and serve. Choose one of these four words,
# and load the corresponding data: 
# >>> from nltk.corpus import senseval
# >>> instances = senseval.instances('hard.pos')
# >>> size = int(len(instances) * 0.1)
# >>> train_set, test_set = instances[size:], instances[:size]
# Using this dataset, build a classifier that predicts the correct sense tag for a given instance.
# See the corpus HOWTO at http://nltk.org/howto for information on using the instance objects
# returned by the Senseval 2 Corpus.

def ex03_fe_01(context,position):
    my_features = {}
    my_features["POS_0"] = context[position][1]
    return my_features

def ex03_fe_02_prev(context,position):
    my_features = {}
    my_features["POS_00"] = context[position][1]
    if position>0:
        my_features["WRD_-1"] = context[position-1][1]
        my_features["POS_-1"] = context[position-1][1]
    else:
        my_features["WRD_-1"] = "<START>"
        my_features["POS_-1"] = "<START>"
    return my_features

def ex03_fe_02_next(context,position):
    my_features = {}
    my_features["POS_00"] = context[position][1]
    if position<len(context):
        my_features["WRD_+1"] = context[position+1][1]
        my_features["POS_+1"] = context[position+1][1]
    else:
        my_features["WRD_+1"] = "<END>"
        my_features["POS_+1"] = "<END>"
    return my_features

def ex03_fe_03(context,position):
    my_features = {}
    my_features["POS_00"] = context[position][1]
    if position>0:
        my_features["WRD_-1"] = context[position-1][1]
        my_features["POS_-1"] = context[position-1][1]
    else:
        my_features["WRD_-1"] = "<START>"
        my_features["POS_-1"] = "<START>"
    if position<len(context):
        my_features["WRD_+1"] = context[position+1][1]
        my_features["POS_+1"] = context[position+1][1]
    else:
        my_features["WRD_+1"] = "<END>"
        my_features["POS_+1"] = "<END>"
    return my_features

def ex03_fe_03_pos(context,position):
    my_features = {}
    my_features["POS_00"] = context[position][1]
    if position>0:
        my_features["POS_-1"] = context[position-1][1]
    else:
        my_features["POS_-1"] = "<START>"
    if position<len(context):
        my_features["POS_+1"] = context[position+1][1]
    else:
        my_features["POS_+1"] = "<END>"
    return my_features

def ex03_fe_03_pos_pimped(context,position,pos_lst=[-3,-2,-1,0,1,2,3]):
    my_features = {}
    for i in pos_lst:
        if position+i>=0 and position+i<len(context):
            my_features["POS_{}".format(i)] = context[position+i][1]
        else:
            my_features["POS_{}".format(i)] = "<NA>"
    return my_features

def ex03_construct_data(wrd='hard.pos'):
    return [(instance.context, instance.position, instance.senses[0]) for instance in nltk.corpus.senseval.instances(wrd)]
   
def ex03_extract_features(data_set,extractor=ex03_fe_01):
    return [ (extractor(context,position),sense) for (context,position,sense) in data_set ]

def ex03_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex03_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex03_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex03(word='hard.pos', train_classifiers=[True,True,True], feature_extractor=ex03_fe_01, equilibrated_split=True, final=False):
    my_data=ex03_construct_data(word)
    my_f_set=ex03_extract_features(my_data, feature_extractor)
    my_dev, my_dev_test, my_test=ex03_split_data(my_f_set, fracs=[0.5,0.25,0.25], equilibrate=equilibrated_split, rnd_seed=1)
    my_classifiers=ex03_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex03_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex03_perfs(my_classifiers,my_dev_test)
    return my_perfs
 
# ex03(feature_extractor=ex03_fe_01)
# [0.7975970425138632, 0.7975970425138632, 0.7975970425138632]
# ex03(feature_extractor=ex03_fe_02_prev)
# [0.7985212569316081, 0.7717190388170055, 0.7975970425138632]
# ex03(feature_extractor=ex03_fe_02_next)
# [0.8012939001848429, 0.7347504621072088, 0.8012939001848429]
# ex03(feature_extractor=ex03_fe_03)
# [0.8179297597042514, 0.7393715341959335, 0.8179297597042514]
# ex03(feature_extractor=ex03_fe_03_pos)
# [0.8179297597042514, 0.7532347504621072, 0.8207024029574861]
# ex03(feature_extractor=ex03_fe_03_pos, final=True) 
# [0.8419593345656192, 0.7523105360443623, 0.8317929759704251] 

# ex03(feature_extractor=ex03_fe_03_pos_pimped)
# [0.7504621072088724, 0.788354898336414, 0.8391866913123844]
# ex03(feature_extractor=ex03_fe_03_pos_pimped, final=True) 
# [0.7809611829944547, 0.7985212569316081, 0.8317929759704251]

# Trying the classifiers on other words gives 0 accuracy

# 4 Using the movie review document classifier discussed in this chapter, generate a list of the 30 features
# that the classifier finds to be most informative. Can you explain why these particular features are informative?
# Do you find any of them surprising?

def ex04_fe_01(vocabulary,description):
    my_features = {}
    description=set(description)
    for vocab in vocabulary:
        my_features['contains({})'.format(vocab)] = (vocab in description)
    return my_features

def ex04_construct_data(): 
    return [ (list(nltk.corpus.movie_reviews.words(fileid)), evaluation)
             for evaluation in nltk.corpus.movie_reviews.categories()
             for fileid in nltk.corpus.movie_reviews.fileids(evaluation) ]

def ex04_construct_vocabulary(num=2000):
    vocab=[ wrd for (wrd,_) in nltk.FreqDist([ word.lower() for word in nltk.corpus.movie_reviews.words() ]).most_common(num) ]
    return vocab
   
def ex04_extract_features(data_set,vocabulary,extractor=ex04_fe_01):
    return [ (extractor(vocabulary,description), evaluation) for (description, evaluation) in data_set ]

def ex04_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex04_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex04_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex04(train_classifiers=[False,True,False], feature_extractor=ex04_fe_01, equilibrated_split=True, final=False):
    my_data=ex04_construct_data()
    my_vocabulary=ex04_construct_vocabulary()
    my_f_set=ex04_extract_features(my_data,my_vocabulary,feature_extractor)
    my_dev, my_dev_test, my_test=ex04_split_data(my_f_set,fracs=[0.5,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex04_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex04_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex04_perfs(my_classifiers,my_dev_test)
    return my_perfs, my_classifiers

# (perfs4,my_classifiers4)=ex04()
# perfs4
# [0.858] 
# my_classifiers4[0].show_most_informative_features(30)
# Most Informative Features
#    contains(outstanding) = True              pos : neg    =     12.2 : 1.0
#           contains(lame) = True              neg : pos    =      7.7 : 1.0
#      contains(portrayed) = True              pos : neg    =      7.2 : 1.0
#      contains(fantastic) = True              pos : neg    =      6.8 : 1.0
#         contains(social) = True              pos : neg    =      5.7 : 1.0
#          contains(awful) = True              neg : pos    =      4.8 : 1.0
#         contains(poorly) = True              neg : pos    =      4.8 : 1.0
#    contains(wonderfully) = True              pos : neg    =      4.7 : 1.0
#          contains(damon) = True              pos : neg    =      4.6 : 1.0
#      contains(laughable) = True              neg : pos    =      4.5 : 1.0
#       contains(terrible) = True              neg : pos    =      4.5 : 1.0
#          contains(waste) = True              neg : pos    =      4.5 : 1.0
#           contains(pulp) = True              pos : neg    =      4.5 : 1.0
#            contains(era) = True              pos : neg    =      4.2 : 1.0
#          contains(blame) = True              neg : pos    =      4.2 : 1.0
#         contains(boring) = True              neg : pos    =      4.2 : 1.0
#         contains(superb) = True              pos : neg    =      4.2 : 1.0
#          contains(hanks) = True              pos : neg    =      4.2 : 1.0
#         contains(stupid) = True              neg : pos    =      4.2 : 1.0
#    contains(masterpiece) = True              pos : neg    =      3.8 : 1.0
#         contains(wasted) = True              neg : pos    =      3.7 : 1.0
#          contains(flynt) = True              pos : neg    =      3.7 : 1.0
#       contains(emotions) = True              pos : neg    =      3.7 : 1.0
#          contains(mulan) = True              pos : neg    =      3.7 : 1.0
#         contains(allows) = True              pos : neg    =      3.6 : 1.0
#        contains(unfunny) = True              neg : pos    =      3.6 : 1.0
#          contains(naked) = True              neg : pos    =      3.6 : 1.0
#          contains(badly) = True              neg : pos    =      3.5 : 1.0
#        contains(complex) = True              pos : neg    =      3.5 : 1.0
#      contains(memorable) = True              pos : neg    =      3.5 : 1.0
 
# 5 Select one of the classification tasks described in this chapter, such as name gender detection,
# document classification, part-of-speech tagging, or dialog act classification. Using the same training
# and test data, and the same feature extractor, build three classifiers for the task: a decision tree,
# a naive Bayes classifier, and a Maximum Entropy classifier. Compare the performance of the three classifiers
# on your selected task. How do you think that your results might be different if you used a different
# feature extractor?

# Done
 
# 6 The synonyms strong and powerful pattern differently (try combining them with chip and sales).
# What features are relevant in this distinction? Build a classifier that predicts when each word should be used.

def ex06_fe_01_pos(sent,position,pos_lst=[-3,-2,-1,1,2,3]):
    my_features = {}
    for i in pos_lst:
        if position+i>=0 and position+i<len(sent):
            my_features["POS_{}".format(i)] = sent[position+i][1]
        else:
            my_features["POS_{}".format(i)] = "<NA>"
    return my_features

def ex06_find_all(target,wrds):
    return [ pos for (pos,wrd) in enumerate(wrds) if wrd==target ]

def ex06_construct_data(sents=nltk.corpus.brown.tagged_sents(),targets=['powerful','strong']):
    data=[]
    for sent in sents:
        wrds=[ wrd for (wrd,_) in sent ]
        for target in targets:
            target_pos_lst=ex06_find_all(target,wrds)
            if target_pos_lst:
                data=data+[ (sent, target_pos, target) for target_pos in target_pos_lst ]
    return data
   
def ex06_extract_features(data_set,extractor=ex06_fe_01_pos):
    return [ (extractor(sent,word_pos),word) for (sent,word_pos,word) in data_set ]

def ex06_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex06_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex06_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex06(synonyms=['powerful','strong'], train_classifiers=[True,True,True], feature_extractor=ex06_fe_01_pos, equilibrated_split=True, final=False):
    my_data=ex06_construct_data(targets=synonyms)
    my_f_set=ex06_extract_features(my_data,feature_extractor)
    my_dev, my_dev_test, my_test=ex06_split_data(my_f_set,fracs=[0.50,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex06_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex06_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex06_perfs(my_classifiers,my_dev_test)
    return my_perfs

# ex06()
# [0.5555555555555556, 0.6349206349206349, 0.6825396825396826]
# ex06(final=True)
# [0.5873015873015873, 0.6825396825396826, 0.6825396825396826]

# 7 The dialog act classifier assigns labels to individual posts, without considering the context
# in which the post is found. However, dialog acts are highly dependent on context,
# and some sequences of dialog act are much more likely than others.
# For example, a ynQuestion dialog act is much more likely to be answered by a yanswer than by a greeting.
# Make use of this fact to build a consecutive classifier for labeling dialog acts.
# Be sure to consider what features might be useful. See the code for the consecutive classifier
# for part-of-speech tags in 1.7 to get some ideas.

def ex07_fe_01_pos(posts,position,pos_lst=[-3,-2,-1]):
    my_features = {}
    for i in pos_lst:
        if position+i>=0 and position+i<len(posts):
            my_features["POS_{}".format(i)] = posts[position+i]
        else:
            my_features["POS_{}".format(i)] = "<NA>"
    return my_features

def ex07_construct_data():
    return [ post.get('class') for post in nltk.corpus.nps_chat.xml_posts() ]
   
def ex07_extract_features(data_set,extractor=ex07_fe_01_pos):
    return [ (extractor(data_set,post_pos),data_set[post_pos]) for post_pos in range(len(data_set)) ]

def ex07_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex07_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex07_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex07(train_classifiers=[True,True,True], feature_extractor=ex07_fe_01_pos, equilibrated_split=True, final=False):
    my_data=ex07_construct_data()
    my_f_set=ex07_extract_features(my_data,feature_extractor)
    my_dev, my_dev_test, my_test=ex07_split_data(my_f_set,fracs=[0.50,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex07_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex07_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex07_perfs(my_classifiers,my_dev_test)
    return my_perfs

# ex07() 
# [0.28148710166919577, 0.3319423368740516, 0.3334597875569044]
# ex07(final=True)
# [0.2071320182094082, 0.3216995447647951, 0.3311836115326252] 
 
# 8 Word features can be very useful for performing document classification,
# since the words that appear in a document give a strong indication about what its semantic content is.
# However, many words occur very infrequently, and some of the most informative words in a document
# may never have occurred in our training data. One solution is to make use of a lexicon,
# which describes how different words relate to one another.
# Using WordNet lexicon, augment the movie review document classifier presented in this chapter
# to use features that generalize the words that appear in a document, making it more likely
# that they will match words found in the training data.

def ex08_fe_01(vocabulary,description):
    my_features = {}
    synset_list=[]
    for word in description:
        synset_list=synset_list + nltk.corpus.wordnet.synsets(word.lower())
    description=set(synset_list)
    for vocab in vocabulary:
        my_features['contains({})'.format(vocab)] = (vocab in description)
    return my_features

def ex08_construct_data(): 
    return [ (list(nltk.corpus.movie_reviews.words(fileid)), evaluation)
             for evaluation in nltk.corpus.movie_reviews.categories()
             for fileid in nltk.corpus.movie_reviews.fileids(evaluation) ]

def ex08_construct_syn_vocabulary(num=2000):
    vocab=[ wrd for (wrd,_) in nltk.FreqDist([ word.lower() for word in nltk.corpus.movie_reviews.words() ]).most_common(num) ]
    synset_list=[]
    for word in vocab:
        synset_list=synset_list + nltk.corpus.wordnet.synsets(word.lower())
    return list(set(synset_list))
   
def ex08_extract_features(data_set,vocabulary,extractor=ex08_fe_01):
    return [ (extractor(vocabulary,description), evaluation) for (description, evaluation) in data_set ]

def ex08_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex08_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex08_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex08(train_classifiers=[False,True,False], feature_extractor=ex08_fe_01, equilibrated_split=True, final=False):
    my_data=ex08_construct_data()
    my_syn_vocabulary=ex08_construct_syn_vocabulary()
    my_f_set=ex08_extract_features(my_data,my_syn_vocabulary,feature_extractor)
    my_dev, my_dev_test, my_test=ex08_split_data(my_f_set,fracs=[0.5,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex08_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex08_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex08_perfs(my_classifiers,my_dev_test)
    return my_perfs, my_classifiers

# (perfs8,my_classifiers8)=ex08()
# perfs8
# [0.802]
 
# 9 The PP Attachment Corpus is a corpus describing prepositional phrase attachment decisions.
# Each instance in the corpus is encoded as a PPAttachment object:
#      
# >>> from nltk.corpus import ppattach
# >>> ppattach.attachments('training')
# [PPAttachment(sent='0', verb='join', noun1='board',
#               prep='as', noun2='director', attachment='V'),
#  PPAttachment(sent='1', verb='is', noun1='chairman',
#               prep='of', noun2='N.V.', attachment='N'),
#  ...]
# >>> inst = ppattach.attachments('training')[1]
# >>> (inst.noun1, inst.prep, inst.noun2)
# ('chairman', 'of', 'N.V.')
# Select only the instances where inst.attachment is N:
#      
# >>> nattach = [inst for inst in ppattach.attachments('training')
# ...            if inst.attachment == 'N']
# Using this sub-corpus, build a classifier that attempts to predict which preposition is used
# to connect a given pair of nouns. For example, given the pair of nouns "team" and "researchers,"
# the classifier should predict the preposition "of".
# See the corpus HOWTO at http://nltk.org/howto for more information on using the PP attachment corpus.

def ex09_fe_01_verb(inst):
    my_features = {}
    my_features['verb'] = inst[0]
    return my_features

def ex09_fe_01_noun1(inst):
    my_features = {}
    my_features['noun1'] = inst[1]
    return my_features

def ex09_fe_01_noun2(inst):
    my_features = {}
    my_features['noun2'] = inst[2]
    return my_features

def ex09_fe_02_nouns(inst):
    my_features = {}
    my_features['noun1'] = inst[1]
    my_features['noun2'] = inst[2]
    return my_features

def ex09_fe_03_all(inst):
    my_features = {}
    my_features['verb'] = inst[0]
    my_features['noun1'] = inst[1]
    my_features['noun2'] = inst[2]
    return my_features

def ex09_construct_data(): 
    return [ inst
             for inst in nltk.corpus.ppattach.attachments('training')
             if inst.attachment == 'N']

def ex09_extract_features(data_set,extractor=ex09_fe_01_verb):
    return [ (extractor([ inst.verb, inst.noun1, inst.noun2 ]), inst.prep) for inst in data_set ]

def ex09_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex09_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex09_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex09(train_classifiers=[True,True,True], feature_extractor=ex09_fe_01_verb, equilibrated_split=True, final=False):
    my_data=ex09_construct_data()
    my_f_set=ex09_extract_features(my_data,feature_extractor)
    my_dev, my_dev_test, my_test=ex09_split_data(my_f_set,fracs=[0.5,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex09_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex09_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex09_perfs(my_classifiers,my_dev_test)
    return my_perfs, my_classifiers

# (perfs,_)=ex09(feature_extractor=ex09_fe_01_verb)
# perfs
# [0.3854437430375046, 0.5016709988860008, 0.38024507983661343]

# (perfs,_)=ex09(feature_extractor=ex09_fe_01_noun1)
# perfs
# [0.506869662086892, 0.5989602673598218, 0.5087263275157816]

# (perfs,_)=ex09(feature_extractor=ex09_fe_01_noun2)
# perfs
# [0.35536576308949125, 0.5224656516895655, 0.35425176383215745]

# (perfs,_)=ex09(feature_extractor=ex09_fe_02_nouns)
# perfs
# [0.46193835870776084, 0.5785369476420349, 0.5384329743780171]

# (perfs,_)=ex09(feature_extractor=ex09_fe_03_all)
# perfs
# [0.47307835128109915, 0.558113627924248, 0.5692536204975863]

# (perfs, _)=ex09(feature_extractor=ex09_fe_01_noun1,final=True)
# perfs
# [0.49832900111399925, 0.590790939472707, 0.4994430003713331]

# 10 Suppose you wanted to automatically generate a prose description of a scene,
# and already had a word to uniquely describe each entity, such as the jar,
# and simply wanted to decide whether to use in or on in relating various items,
# e.g. the book is in the cupboard vs the book is on the shelf.
# Explore this issue by looking at corpus data; writing programs as needed.
# 
# a.        in the car versus on the train
# b.        in town versus on campus
# c.        in the picture versus on the screen
# d.        in Macbeth versus on Letterman

def ex10_fe_01_word(sent,pos_prep,pos_noun,pos_lst=[-1]):
    my_features = {}
    my_features['WORD_noun']=sent[pos_noun][0]
    return my_features

def ex10_fe_01_word_and_pos(sent,pos_prep,pos_noun,pos_lst=[-1]):
    my_features = {}
    my_features['WORD_noun']=sent[pos_noun][0]
    my_features['POS_noun']=sent[pos_noun][1]
    return my_features

def ex10_fe_02_pos(sent,pos_prep,pos_noun,pos_lst=[-1]):
    my_features = {}
    for i in pos_lst:
        if pos_prep+i>=0 and pos_prep+i<len(sent):
            my_features["POS_{}".format(i)] = sent[pos_prep+i][1]
        else:
            my_features["POS_{}".format(i)] = "<NA>"
    my_features['WORD_noun']=sent[pos_noun][0]
    my_features['POS_noun']=sent[pos_noun][1]
    return my_features

def ex10_fe_02_word(sent,pos_prep,pos_noun,pos_lst=[-1]):
    my_features = {}
    for i in pos_lst:
        if pos_prep+i>=0 and pos_prep+i<len(sent):
            my_features["WORD_{}".format(i)] = sent[pos_prep+i][0]
        else:
            my_features["WORD_{}".format(i)] = "<NA>"
    my_features['WORD_noun']=sent[pos_noun][0]
    my_features['POS_noun']=sent[pos_noun][1]
    return my_features

def ex10_find_noun(sent,target_pos,valid_pos_lst=['NN','NP'],splitters='(),.-:?!',search_range=5):
    pos_noun=None
    if target_pos+1<len(sent):
        for i in range(target_pos+1,min(target_pos+1+search_range,len(sent))):
            if sum([ valid_pos in sent[i][1] for valid_pos in valid_pos_lst ]):
                pos_noun=i
                break
            if sent[i][1] in splitters:
                break
    return pos_noun

def ex10_find_all(target,sent):
    wrds=[ wrd for (wrd,_) in sent ]
    candidate_pos_list=[ [pos,ex10_find_noun(sent,pos)] for (pos,wrd) in enumerate(wrds) if wrd==target ]
    return [ inst for inst in candidate_pos_list if inst[1] ]

def ex10_construct_data(sents=nltk.corpus.brown.tagged_sents(),targets=['on','in']):
    data=[]
    for sent in sents:
        for target in targets:
            target_pos_lst=ex10_find_all(target,sent)
            if target_pos_lst:
                data=data+[ (sent, target_pos[0], target_pos[1], target) for target_pos in target_pos_lst ]
    return data
   
def ex10_extract_features(data_set,extractor=ex10_fe_01_word):
    return [ (extractor(sent,prep_pos,noun_pos),prep) for (sent,prep_pos,noun_pos,prep) in data_set ]

def ex10_split_data(feature_set, fracs=[0.98,0.01,0.01], equilibrate=True, rnd_seed=False):
    import random
    if rnd_seed:
        random.seed(rnd_seed)
    dev_set, dev_test_set, test_set = [], [], []
    if equilibrate:
        label_set=set([ instance[1] for instance in feature_set ])
        feature_set=[ [ instance for instance in feature_set if instance[1]==label ] for label in label_set ]
    else:
        feature_set=[ feature_set ]
    for this_set in feature_set:
        random.shuffle(this_set)
        num_inst=[ int(len(this_set)*frac) for frac in fracs ]
        dev_set=dev_set+this_set[:num_inst[0]]
        dev_test_set=dev_test_set+this_set[num_inst[0]:num_inst[0]+num_inst[1]]
        test_set=test_set+this_set[num_inst[0]+num_inst[1]:num_inst[0]+num_inst[1]+num_inst[2]]
    return dev_set, dev_test_set, test_set

def ex10_train_classifiers(dev,train_classifiers=[True,True,True]):
    classifiers=[]
    if train_classifiers[0]:
        classifiers=classifiers+[ nltk.DecisionTreeClassifier.train(dev) ]
    if train_classifiers[1]:
        classifiers=classifiers+[ nltk.NaiveBayesClassifier.train(dev) ]
    if train_classifiers[2]:
        classifiers=classifiers+[ nltk.MaxentClassifier.train(dev,max_iter=10) ]
    return classifiers

def ex10_perfs(classifiers,test_set):
    return [ nltk.classify.accuracy(classifier,test_set) for classifier in classifiers ]

def ex10(preps=['on','in'], train_classifiers=[True,True,True], feature_extractor=ex10_fe_01_word, equilibrated_split=True, final=False):
    my_data=ex10_construct_data(targets=preps)
    my_f_set=ex10_extract_features(my_data,feature_extractor)
    my_dev, my_dev_test, my_test=ex10_split_data(my_f_set,fracs=[0.50,0.25,0.25],equilibrate=equilibrated_split,rnd_seed=1)
    my_classifiers=ex10_train_classifiers(my_dev,train_classifiers)
    if final:
        my_perfs=ex10_perfs(my_classifiers,my_test)
    else:
        my_perfs=ex10_perfs(my_classifiers,my_dev_test)
    return my_perfs, my_classifiers

# (perfs,_)=ex10(feature_extractor=ex10_fe_01_word)
# perfs
# [0.7873387644263408, 0.7954854039375424, 0.6961982348947726]

# (perfs,_)=ex10(feature_extractor=ex10_fe_01_word_and_pos)
# perfs
# [0.7871690427698574, 0.7953156822810591, 0.7951459606245757]

# (perfs,_)=ex10(feature_extractor=ex10_fe_02_pos)
# perfs
# [0.7922606924643585, 0.787847929395791, 0.7927698574338086]

# (perfs,_)=ex10(feature_extractor=ex10_fe_02_word)
# perfs
# [0.7854718262050238, 0.7829260013577732, 0.8185675492192804]

# (perfs,_)=ex10(feature_extractor=ex10_fe_02_word, final=True)
# perfs
# [0.7881873727087576, 0.7875084860828242, 0.814663951120163]

# This is cheating, I know, I know...
# (perfs,_)=ex10(feature_extractor=ex10_fe_01_word, final=True)
# perfs
# [0.7898845892735913, 0.7970128988458928, 0.6887304820095044]