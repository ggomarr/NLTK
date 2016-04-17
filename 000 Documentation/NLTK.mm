<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1450102818310" ID="ID_0" MODIFIED="1455031877622" TEXT="NLTK">
<node CREATED="1450102818310" FOLDED="true" ID="ID_1" MODIFIED="1450102818310" POSITION="right" TEXT="1. Language Processing and Python">
<node CREATED="1450102818310" FOLDED="true" ID="ID_2" MODIFIED="1450102818310" TEXT="Examples of basic manipulation">
<node CREATED="1450102818310" FOLDED="true" ID="ID_3" MODIFIED="1450102818310" TEXT="Python calculator">
<node CREATED="1450102818310" FOLDED="true" ID="ID_4" MODIFIED="1450102818310" TEXT="3+2"/>
<node CREATED="1450102818310" FOLDED="true" ID="ID_5" MODIFIED="1450102818310" TEXT="1.0/3"/>
</node>
<node CREATED="1450102818311" FOLDED="true" ID="ID_6" MODIFIED="1450102818311" TEXT="[text].count([str])">
<node CREATED="1450102818311" FOLDED="true" ID="ID_7" MODIFIED="1450102818311" TEXT="Counts the number of appearances of [str] in [text]"/>
</node>
<node CREATED="1450102818311" FOLDED="true" ID="ID_8" MODIFIED="1450102818311" TEXT="[text].concordance([str])">
<node CREATED="1450102818311" FOLDED="true" ID="ID_9" MODIFIED="1450102818311" TEXT="Looks up [str] in [text]"/>
<node CREATED="1450102818311" FOLDED="true" ID="ID_10" MODIFIED="1450102818311" TEXT="Returns all occurences with some context"/>
</node>
<node CREATED="1450102818311" FOLDED="true" ID="ID_11" MODIFIED="1450102818311" TEXT="[text].similar([str])">
<node CREATED="1450102818311" FOLDED="true" ID="ID_12" MODIFIED="1450102818311" TEXT="Looks for words used in a similar context as [str] in [text]"/>
</node>
<node CREATED="1450102818311" FOLDED="true" ID="ID_13" MODIFIED="1450102818311" TEXT="[text].common_contexts([str1],[str2])">
<node CREATED="1450102818311" FOLDED="true" ID="ID_14" MODIFIED="1450102818311" TEXT="Looks for contexts where the two words are used similarlly"/>
</node>
<node CREATED="1450102818312" FOLDED="true" ID="ID_15" MODIFIED="1450102818312" TEXT="[text].dispersion_plot([[str1],[str2],...])">
<node CREATED="1450102818312" FOLDED="true" ID="ID_16" MODIFIED="1450102818312" TEXT="Produces a graph showing the position of the [str*] in [text]"/>
</node>
<node CREATED="1450102818312" FOLDED="true" ID="ID_17" MODIFIED="1450102818312" TEXT="[text].generate()">
<node CREATED="1450102818312" FOLDED="true" ID="ID_18" MODIFIED="1450102818312" TEXT="Generate a random text using similar constructions to those found in [text]"/>
<node CREATED="1450102818312" FOLDED="true" ID="ID_19" MODIFIED="1450102818312" TEXT="Has been removed from the latest nltk"/>
</node>
<node CREATED="1450102818312" FOLDED="true" ID="ID_20" MODIFIED="1450102818312" TEXT="len([text])">
<node CREATED="1450102818312" FOLDED="true" ID="ID_21" MODIFIED="1450102818312" TEXT="Returns number of tokens in [text]"/>
</node>
<node CREATED="1450102818312" FOLDED="true" ID="ID_22" MODIFIED="1450102818312" TEXT="set([text])">
<node CREATED="1450102818313" FOLDED="true" ID="ID_23" MODIFIED="1450102818313" TEXT="Returns a list of unique tokens in [text]"/>
</node>
<node CREATED="1450102818313" FOLDED="true" ID="ID_24" MODIFIED="1450102818313" TEXT="sorted(set([text]))">
<node CREATED="1450102818313" FOLDED="true" ID="ID_25" MODIFIED="1450102818313" TEXT="Returns the sorted list of unique tokens in [text]"/>
</node>
<node CREATED="1450102818313" FOLDED="true" ID="ID_26" MODIFIED="1450102818313" TEXT="len(set([text]))">
<node CREATED="1450102818313" FOLDED="true" ID="ID_27" MODIFIED="1450102818313" TEXT="Returns the number of unique tokens in [text]"/>
</node>
<node CREATED="1450102818313" FOLDED="true" ID="ID_28" MODIFIED="1450102818313" TEXT="len(set([word.lower() for word in [text]]))">
<node CREATED="1450102818313" FOLDED="true" ID="ID_29" MODIFIED="1450102818313" TEXT="Returns the number of unique tokens in [text], ignoring case"/>
</node>
<node CREATED="1450102818313" FOLDED="true" ID="ID_30" MODIFIED="1450102818313" TEXT="len(set([word.lower() for word in [text] if word.isalpha()]))">
<node CREATED="1450102818314" FOLDED="true" ID="ID_31" MODIFIED="1450102818314" TEXT="Returns the number of unique alphanumeric tokens in [text], ignoring case"/>
</node>
<node CREATED="1450102818314" FOLDED="true" ID="ID_32" MODIFIED="1450102818314" TEXT="fdist=FreqDist([text])">
<node CREATED="1450102818314" FOLDED="true" ID="ID_33" MODIFIED="1450102818314" TEXT="Returns a distribution of counts of words in [text]"/>
<node CREATED="1450102818314" FOLDED="true" ID="ID_34" MODIFIED="1450102818314" TEXT="fdist.keys()">
<node CREATED="1450102818314" FOLDED="true" ID="ID_35" MODIFIED="1450102818314" TEXT="Returns a list containing the tokens, most popular first"/>
</node>
<node CREATED="1450102818314" FOLDED="true" ID="ID_36" MODIFIED="1450102818314" TEXT="fdist([key])">
<node CREATED="1450102818314" FOLDED="true" ID="ID_37" MODIFIED="1450102818314" TEXT="Number of times that [key] appeared in the [text] that was used to generate [fdist]"/>
</node>
<node CREATED="1450102818315" FOLDED="true" ID="ID_38" MODIFIED="1450102818315" TEXT="fdist.plot([num], ...)">
<node CREATED="1450102818315" FOLDED="true" ID="ID_39" MODIFIED="1450102818315" TEXT="Plots the distribution of the most popular [num] tokens"/>
</node>
<node CREATED="1450102818315" FOLDED="true" ID="ID_40" MODIFIED="1450102818315" TEXT="fdist.hapaxes()">
<node CREATED="1450102818315" FOLDED="true" ID="ID_41" MODIFIED="1450102818315" TEXT="Returns a list of words that appear rarely"/>
</node>
</node>
<node CREATED="1450102818315" FOLDED="true" ID="ID_42" MODIFIED="1450102818315" TEXT="bigrams([text])">
<node CREATED="1450102818315" FOLDED="true" ID="ID_43" MODIFIED="1450102818315" TEXT="Returns an iterator over the pairs of words in [text]"/>
</node>
<node CREATED="1450102818315" FOLDED="true" ID="ID_44" MODIFIED="1450102818315" TEXT="[text].collocations()">
<node CREATED="1450102818316" FOLDED="true" ID="ID_45" MODIFIED="1450102818316" TEXT="Returns a list of bigrams that">
<node CREATED="1450102818316" FOLDED="true" ID="ID_46" MODIFIED="1450102818316" TEXT="Occur more often that expected given the frequency of the individual words"/>
</node>
</node>
<node CREATED="1450102818316" FOLDED="true" ID="ID_47" MODIFIED="1450102818316" TEXT="lexical diversity">
<node CREATED="1450102818316" FOLDED="true" ID="ID_48" MODIFIED="1450102818316" TEXT="def lexical_diversity(text): return len(text) / len(set(text))"/>
<node CREATED="1450102818316" FOLDED="true" ID="ID_49" MODIFIED="1450102818316" TEXT="Returns the average number of times a word is used in a text"/>
</node>
<node CREATED="1450102818316" FOLDED="true" ID="ID_50" MODIFIED="1450102818316" TEXT="[word for word in [vocab] if [cond]]">
<node CREATED="1450102818316" FOLDED="true" ID="ID_51" MODIFIED="1450102818316" TEXT="Returns the list of words in [vocab] that match [cond]"/>
</node>
<node CREATED="1450102818317" FOLDED="true" ID="ID_52" MODIFIED="1450102818317" TEXT="sorted([word for word in set([text]) if len(word) &gt; [min_len] and fdist5[word] &gt; [min_cnt]])">
<node CREATED="1450102818317" FOLDED="true" ID="ID_53" MODIFIED="1450102818317" TEXT="Returns the sorted list of words in [text] that">
<node CREATED="1450102818317" FOLDED="true" ID="ID_54" MODIFIED="1450102818317" TEXT="Are longer than [min_len]"/>
<node CREATED="1450102818317" FOLDED="true" ID="ID_55" MODIFIED="1450102818317" TEXT="Appear more than [min_cnt] times"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818317" FOLDED="true" ID="ID_56" MODIFIED="1453699410595" POSITION="right" TEXT="2. Accessing Text Corpora and Lexical Resources">
<node CREATED="1450102818317" ID="ID_57" MODIFIED="1450367374082" TEXT="Corpus">
<node CREATED="1450102818317" FOLDED="true" ID="ID_58" MODIFIED="1450102818317" TEXT="A collection of texts with additional metadata">
<node CREATED="1450102818317" FOLDED="true" ID="ID_59" MODIFIED="1450102818317" TEXT="Can be also individual words"/>
</node>
<node CREATED="1450102818318" FOLDED="true" ID="ID_60" MODIFIED="1450102818318" TEXT="Corpus readers">
<node CREATED="1450102818318" FOLDED="true" ID="ID_61" MODIFIED="1450102818318" TEXT="[corpus_raw_reader]=[corpus].raw([text_id])"/>
<node CREATED="1450102818318" FOLDED="true" ID="ID_62" MODIFIED="1450102818318" TEXT="[corpus_sentence_reader]=[corpus].sents([text_id])"/>
<node CREATED="1450102818318" FOLDED="true" ID="ID_63" MODIFIED="1450102818318" TEXT="[corpus_word_reader]=[corpus].words([text_id])"/>
<node CREATED="1450102818318" FOLDED="true" ID="ID_64" MODIFIED="1450102818318" TEXT="[text]=ntlk.Text([corpus_word_reader])">
<node CREATED="1450102818318" FOLDED="true" ID="ID_65" MODIFIED="1450102818318" TEXT="Returns a text from a corpus word reader"/>
</node>
</node>
<node CREATED="1450102818319" ID="ID_66" MODIFIED="1450367376175" TEXT="Available corpus">
<node CREATED="1450102818319" FOLDED="true" ID="ID_67" MODIFIED="1450102818319" TEXT="Texts">
<node CREATED="1450102818319" FOLDED="true" ID="ID_68" MODIFIED="1450102818319" TEXT="gutemberg"/>
<node CREATED="1450102818319" FOLDED="true" ID="ID_69" MODIFIED="1450102818319" TEXT="brown">
<node CREATED="1450102818319" FOLDED="true" ID="ID_70" MODIFIED="1450102818319" TEXT="Categorized">
<node CREATED="1450102818319" FOLDED="true" ID="ID_71" MODIFIED="1450102818319" TEXT="nltk.corpus.brown.categories()"/>
</node>
</node>
<node CREATED="1450102818319" FOLDED="true" ID="ID_72" MODIFIED="1450102818319" TEXT="reuters">
<node CREATED="1450102818319" FOLDED="true" ID="ID_73" MODIFIED="1450102818319" TEXT="Also categorized"/>
</node>
<node CREATED="1450102818320" FOLDED="true" ID="ID_74" MODIFIED="1450102818320" TEXT="inaugural"/>
<node CREATED="1450102818320" FOLDED="true" ID="ID_75" MODIFIED="1450102818320" TEXT="webtext"/>
<node CREATED="1450102818320" FOLDED="true" ID="ID_76" MODIFIED="1450102818320" TEXT="nps_chat"/>
<node CREATED="1450102818320" FOLDED="true" ID="ID_77" MODIFIED="1450102818320" TEXT="abc"/>
<node CREATED="1450102818320" FOLDED="true" ID="ID_78" MODIFIED="1450102818320" TEXT="genesis"/>
</node>
<node CREATED="1450102818320" ID="ID_79" MODIFIED="1450367377683" TEXT="Lexical resources">
<node CREATED="1450102818320" FOLDED="true" ID="ID_80" MODIFIED="1450102818320" TEXT="Word lists">
<node CREATED="1450102818320" FOLDED="true" ID="ID_81" MODIFIED="1450102818320" TEXT="words">
<node CREATED="1450102818321" FOLDED="true" ID="ID_82" MODIFIED="1450102818321" TEXT="words.words(&apos;en&apos;)"/>
<node CREATED="1450102818321" FOLDED="true" ID="ID_83" MODIFIED="1450102818321" TEXT="..."/>
</node>
<node CREATED="1450102818321" FOLDED="true" ID="ID_84" MODIFIED="1450102818321" TEXT="stopwords"/>
<node CREATED="1450102818321" FOLDED="true" ID="ID_85" MODIFIED="1450102818321" TEXT="names"/>
</node>
<node CREATED="1450102818321" FOLDED="true" ID="ID_86" MODIFIED="1450102818321" TEXT="Pronouncing dictionaries">
<node CREATED="1450102818321" FOLDED="true" ID="ID_87" MODIFIED="1450102818321" TEXT="cmudict"/>
</node>
<node CREATED="1450102818321" FOLDED="true" ID="ID_88" MODIFIED="1450102818321" TEXT="Comparative wordlists">
<node CREATED="1450102818322" FOLDED="true" ID="ID_89" MODIFIED="1450102818322" TEXT="swadesh"/>
<node CREATED="1450102818322" FOLDED="true" ID="ID_90" MODIFIED="1450102818322" TEXT="List of common words in different languages"/>
</node>
<node CREATED="1450102818322" ID="ID_91" MODIFIED="1450367407057" TEXT="Toolbox files">
<node CREATED="1450102818322" FOLDED="true" ID="ID_92" MODIFIED="1450102818322" TEXT="toolbox"/>
<node CREATED="1450102818322" FOLDED="true" ID="ID_93" MODIFIED="1450102818322" TEXT="Word list with adhoc internal structure"/>
<node CREATED="1450102818322" FOLDED="true" ID="ID_94" MODIFIED="1450102818322" TEXT="Very powerful but difficult to use"/>
</node>
<node CREATED="1450102818323" ID="ID_95" MODIFIED="1450367383131" TEXT="WordNet">
<node CREATED="1450102818323" FOLDED="true" ID="ID_96" MODIFIED="1450102818323" TEXT="Toolbox on steroids"/>
<node CREATED="1450102818323" FOLDED="true" ID="ID_97" MODIFIED="1450102818323" TEXT="Semantical English dictionary"/>
<node CREATED="1450102818323" ID="ID_98" MODIFIED="1450367391559" TEXT="Lemma">
<node CREATED="1450102818323" ID="ID_99" MODIFIED="1450367413705" TEXT="Pair of word and meaning it refers to">
<node CREATED="1450102818323" ID="ID_100" MODIFIED="1450367414582" TEXT="Dish">
<node CREATED="1450102818323" ID="ID_101" MODIFIED="1450367416698" TEXT="Dish as in &apos;Carbonara is a dish.&apos;">
<node CREATED="1450102818323" FOLDED="true" ID="ID_102" MODIFIED="1450102818323" TEXT="Lemma 1"/>
</node>
<node CREATED="1450102818323" ID="ID_103" MODIFIED="1450367415142" TEXT="Dish as in &apos;Satellite dish.&apos;">
<node CREATED="1450102818323" FOLDED="true" ID="ID_104" MODIFIED="1450102818323" TEXT="Lemma 2"/>
</node>
<node CREATED="1450102818324" ID="ID_105" MODIFIED="1450367418986" TEXT="Dish as in &apos;Do the dishes.&apos;">
<node CREATED="1450102818324" FOLDED="true" ID="ID_106" MODIFIED="1450102818324" TEXT="Lemma 3"/>
</node>
</node>
<node CREATED="1450102818324" FOLDED="true" ID="ID_107" MODIFIED="1450102818324" TEXT="The &apos;meaning it refers to&apos; is known as a &apos;synset&apos;"/>
</node>
<node CREATED="1450102818324" ID="ID_108" MODIFIED="1450367400154" TEXT="lemmas([word])">
<node CREATED="1450102818324" FOLDED="true" ID="ID_109" MODIFIED="1450102818324" TEXT="Returns a list with the lemmas of [word]"/>
</node>
<node CREATED="1450102818324" FOLDED="true" ID="ID_110" MODIFIED="1450102818324" TEXT="lemma([lemma_id])">
<node CREATED="1450102818324" FOLDED="true" ID="ID_111" MODIFIED="1450102818324" TEXT="[lemma_id]=&apos;car.n.01.automobile&apos;">
<node CREATED="1450102818324" FOLDED="true" ID="ID_112" MODIFIED="1450102818324" TEXT="~&quot;Word &apos;automobile&apos; when it refers to the synset &apos;car.n.01&apos;&quot;"/>
</node>
<node CREATED="1450102818324" FOLDED="true" ID="ID_113" MODIFIED="1450102818324" TEXT="synset()"/>
<node CREATED="1450102818325" FOLDED="true" ID="ID_114" MODIFIED="1450102818325" TEXT="name()"/>
</node>
</node>
<node CREATED="1450102818325" ID="ID_115" MODIFIED="1450367431347" TEXT="Synset">
<node CREATED="1450102818325" FOLDED="true" ID="ID_116" MODIFIED="1450102818325" TEXT="Set of lemmas with a common meaning"/>
<node CREATED="1450102818325" ID="ID_117" MODIFIED="1450367433062" TEXT="synsets([word])">
<node CREATED="1450102818325" FOLDED="true" ID="ID_118" MODIFIED="1450102818325" TEXT="Returns a list with the synsets that [word] belongs to"/>
</node>
<node CREATED="1450102818325" ID="ID_119" MODIFIED="1450367434962" TEXT="synset([synset_id])">
<node CREATED="1450102818325" ID="ID_120" MODIFIED="1450367437026" TEXT="[synset_id]=&apos;car.n.01&apos;">
<node CREATED="1450102818325" FOLDED="true" ID="ID_121" MODIFIED="1450102818325" TEXT="~&quot;Meaning 01 of the noun &apos;car&apos;&quot;"/>
</node>
<node CREATED="1450102818325" ID="ID_122" MODIFIED="1450367436529" TEXT="lemmas()">
<node CREATED="1450102818326" FOLDED="true" ID="ID_123" MODIFIED="1450102818326" TEXT="Returns the lemmas that belong to [synset_id]"/>
</node>
<node CREATED="1450102818326" ID="ID_124" MODIFIED="1450367435889" TEXT="lemma_names()">
<node CREATED="1450102818326" FOLDED="true" ID="ID_125" MODIFIED="1450102818326" TEXT="Returns a list of the names of the lemmas that belong to [synset_id]"/>
</node>
<node CREATED="1450102818326" FOLDED="true" ID="ID_126" MODIFIED="1450102818326" TEXT="definition()"/>
<node CREATED="1450102818326" FOLDED="true" ID="ID_127" MODIFIED="1450102818326" TEXT="examples()"/>
</node>
</node>
<node CREATED="1450102818326" ID="ID_128" MODIFIED="1450367445732" TEXT="Lexical relations">
<node CREATED="1450102818326" FOLDED="true" ID="ID_129" MODIFIED="1450102818326" TEXT="There are hierarchies of synsets and lemmas"/>
<node CREATED="1450102818326" ID="ID_130" MODIFIED="1450367448066" TEXT="synset([synset_id])">
<node CREATED="1450102818327" ID="ID_131" MODIFIED="1450367488030" TEXT="Root nodes called &apos;unique beginners&apos;">
<node CREATED="1450102818327" FOLDED="true" ID="ID_132" MODIFIED="1450102818327" TEXT="Entity"/>
<node CREATED="1450102818327" FOLDED="true" ID="ID_133" MODIFIED="1450102818327" TEXT="State"/>
<node CREATED="1450102818327" FOLDED="true" ID="ID_134" MODIFIED="1450102818327" TEXT="Event"/>
<node CREATED="1450102818327" FOLDED="true" ID="ID_135" MODIFIED="1450102818327" TEXT="..."/>
</node>
<node CREATED="1450102818327" ID="ID_136" MODIFIED="1450367464943" TEXT="hyponyms()">
<node CREATED="1450102818327" ID="ID_137" MODIFIED="1450367499928" TEXT="Child categories of a synset"/>
</node>
<node CREATED="1450102818327" ID="ID_138" MODIFIED="1450367464445" TEXT="hypernyms()">
<node CREATED="1450102818327" FOLDED="true" ID="ID_139" MODIFIED="1450102818327" TEXT="Parent categories of a synset"/>
</node>
<node CREATED="1450102818328" ID="ID_140" MODIFIED="1450367463962" TEXT="hypernym_paths()">
<node CREATED="1450102818328" FOLDED="true" ID="ID_141" MODIFIED="1450102818328" TEXT="List of all paths from root nodes to [synset_id]"/>
</node>
<node CREATED="1450102818328" ID="ID_142" MODIFIED="1450367463279" TEXT="root_hypernyms()">
<node CREATED="1450102818328" FOLDED="true" ID="ID_143" MODIFIED="1450102818328" TEXT="List of all root nodes that can derive into [synset_id]"/>
</node>
<node CREATED="1450102818328" ID="ID_144" MODIFIED="1450367466263" TEXT="part_meronyms()">
<node CREATED="1450102818328" FOLDED="true" ID="ID_145" MODIFIED="1450102818328" TEXT="List of the parts that compose the [synset_id]">
<node CREATED="1450102818328" FOLDED="true" ID="ID_146" MODIFIED="1450102818328" TEXT="&apos;tree&apos; to &apos;trunk&apos;"/>
</node>
</node>
<node CREATED="1450102818328" ID="ID_147" MODIFIED="1450367466708" TEXT="part_holonyms()">
<node CREATED="1450102818328" FOLDED="true" ID="ID_148" MODIFIED="1450102818328" TEXT="List of the wholes that contain the part [synset_id]">
<node CREATED="1450102818329" FOLDED="true" ID="ID_149" MODIFIED="1450102818329" TEXT="&apos;trunk&apos; to &apos;tree&apos;"/>
</node>
</node>
<node CREATED="1450102818329" ID="ID_150" MODIFIED="1450367467163" TEXT="substance_meronyms()">
<node CREATED="1450102818329" FOLDED="true" ID="ID_151" MODIFIED="1450102818329" TEXT="List of the substances that compose the [synset_id]">
<node CREATED="1450102818329" FOLDED="true" ID="ID_152" MODIFIED="1450102818329" TEXT="&apos;tree&apos; to &apos;wood&apos;"/>
</node>
</node>
<node CREATED="1450102818329" ID="ID_153" MODIFIED="1450367467626" TEXT="substance_holonyms()">
<node CREATED="1450102818329" FOLDED="true" ID="ID_154" MODIFIED="1450102818329" TEXT="List of the wholes that are composed of the substance [synset_id]">
<node CREATED="1450102818329" FOLDED="true" ID="ID_155" MODIFIED="1450102818329" TEXT="&apos;wood&apos; to &apos;tree&apos;"/>
</node>
</node>
<node CREATED="1450102818329" ID="ID_156" MODIFIED="1450367468100" TEXT="member_meronyms()">
<node CREATED="1450102818329" FOLDED="true" ID="ID_157" MODIFIED="1450102818329" TEXT="List of the items that compose the group [synset_id]">
<node CREATED="1450102818330" FOLDED="true" ID="ID_158" MODIFIED="1450102818330" TEXT="&apos;forest&apos; to &apos;tree&apos;"/>
</node>
</node>
<node CREATED="1450102818330" ID="ID_159" MODIFIED="1450367468583" TEXT="member_holonyms()">
<node CREATED="1450102818330" FOLDED="true" ID="ID_160" MODIFIED="1450102818330" TEXT="List of the groups that have [synset_id] as members">
<node CREATED="1450102818330" FOLDED="true" ID="ID_161" MODIFIED="1450102818330" TEXT="&apos;tree&apos; to &apos;forest&apos;"/>
</node>
</node>
<node CREATED="1450102818330" ID="ID_162" MODIFIED="1450367469117" TEXT="entailments()">
<node CREATED="1450102818330" ID="ID_163" MODIFIED="1450367469616" TEXT="List of actions that are most likely taking place if [synset_id] is taking place">
<node CREATED="1450102818330" FOLDED="true" ID="ID_164" MODIFIED="1450102818330" TEXT="&apos;Eat&apos; entails &apos;chew&apos; and &apos;swallow&apos;"/>
</node>
</node>
</node>
<node CREATED="1450102818331" ID="ID_165" MODIFIED="1450367451297" TEXT="lemma([lemma_id])">
<node CREATED="1450102818331" ID="ID_166" MODIFIED="1450367452245" TEXT="antonyms()">
<node CREATED="1450102818331" FOLDED="true" ID="ID_167" MODIFIED="1450102818331" TEXT="List of lemmas with opposite meaning"/>
</node>
</node>
<node CREATED="1450102818331" ID="ID_168" MODIFIED="1450367453747" TEXT="dir() helps find the relations defined on an object">
<node CREATED="1450102818331" FOLDED="true" ID="ID_169" MODIFIED="1450102818331" TEXT="dir(nltk.corpus.wordnet.synset(&apos;harmony.n.02&apos;))"/>
</node>
</node>
<node CREATED="1450102818331" FOLDED="true" ID="ID_170" MODIFIED="1450102818331" TEXT="Similarity">
<node CREATED="1450102818331" FOLDED="true" ID="ID_171" MODIFIED="1450102818331" TEXT="Lexical relation can be used to induce semantical relation">
<node CREATED="1450102818331" FOLDED="true" ID="ID_172" MODIFIED="1450102818331" TEXT="Lowest possible common hypernym">
<node CREATED="1450102818331" FOLDED="true" ID="ID_173" MODIFIED="1450102818331" TEXT="synset([synset_id_1]).lowest_common_hypernym([synset_id_2])"/>
</node>
<node CREATED="1450102818331" FOLDED="true" ID="ID_174" MODIFIED="1450102818331" TEXT="Depth of the lowest possible common hypernym">
<node CREATED="1450102818332" FOLDED="true" ID="ID_175" MODIFIED="1450102818332" TEXT="synset([synset_id]).min_depth()"/>
</node>
<node CREATED="1450102818332" FOLDED="true" ID="ID_176" MODIFIED="1450102818332" TEXT="Graph distance functions">
<node CREATED="1450102818332" FOLDED="true" ID="ID_177" MODIFIED="1450102818332" TEXT="synset([synset_id_1]).path_similarity([synset_id_2])"/>
</node>
<node CREATED="1450102818332" FOLDED="true" ID="ID_178" MODIFIED="1450102818332" TEXT="...">
<node CREATED="1450102818332" FOLDED="true" ID="ID_179" MODIFIED="1450102818332" TEXT="(there are other distances defined in ntlk.corpus.wordnet)"/>
</node>
</node>
</node>
<node CREATED="1450102818332" FOLDED="true" ID="ID_180" MODIFIED="1450102818332" TEXT="Others also exist">
<node CREATED="1450102818332" FOLDED="true" ID="ID_181" MODIFIED="1450102818332" TEXT="nltk.corpus.verbnet"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818332" FOLDED="true" ID="ID_182" MODIFIED="1450102818332" TEXT="Custom corpus handling">
<node CREATED="1450102818332" FOLDED="true" ID="ID_183" MODIFIED="1450102818332">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>corpus_root = '/usr/share/dict'</p>
                                    <p>my_corpus = nltk.corpus.PlaintextCorpusReader(corpus_root, '.*')</p>
                                </body>
                            </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818333" FOLDED="true" ID="ID_184" MODIFIED="1450102818333" TEXT="cfd=CondFreqDist([list_of_pairs])">
<node CREATED="1450102818333" FOLDED="true" ID="ID_185" MODIFIED="1450102818333" TEXT="In general, CondFreqDist requires a list of pairs">
<node CREATED="1450102818333" FOLDED="true" ID="ID_186" MODIFIED="1450102818333">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>genre_word =</p>
                                    <p>[ (genre, word)</p>
                                    <p>for genre in ['news', 'romance']</p>
                                    <p>for word in brown.words(categories=genre) ]</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818333" FOLDED="true" ID="ID_187" MODIFIED="1450102818333" TEXT="But it can be called on the list generator too">
<node CREATED="1450102818334" FOLDED="true" ID="ID_188" MODIFIED="1450102818334">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>( (genre, word)</p>
                                    <p>for genre in brown.categories()</p>
                                    <p>for word in brown.words(categories=genre) )</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818334" FOLDED="true" ID="ID_189" MODIFIED="1450102818334" TEXT="(...and even on other similar objects, like a list of strings of length 2)"/>
<node CREATED="1450102818334" FOLDED="true" ID="ID_190" MODIFIED="1450102818334" TEXT="Examples">
<node CREATED="1450102818334" FOLDED="true" ID="ID_191" MODIFIED="1450102818334">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>( (lang, len(word))</p>
                                    <p>for lang in languages</p>
                                    <p>for word in udhr.words(lang + '-Latin1') )</p>
                                </body>
                            </html></richcontent>
</node>
<node CREATED="1450102818334" FOLDED="true" ID="ID_192" MODIFIED="1450102818334">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>( (target, fileid[:4])</p>
                                    <p>for fileid in inaugural.fileids()</p>
                                    <p>for target in ['america', 'citizen'] for w in inaugural.words(fileid) if w.lower().startswith(target) )</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818335" FOLDED="true" ID="ID_193" MODIFIED="1450102818335">
<richcontent TYPE="NODE"><html>
                            <head/>
                            <body>
                                <p>cfd.plot(</p>
                                <p>conditions=[ [cnd1], [cond2], ... ],</p>
                                <p>samples=[ [samp1], [samp2], ... ],</p>
                                <p>cumulative=[True|False] )</p>
                            </body>
                        </html></richcontent>
<node CREATED="1450102818335" FOLDED="true" ID="ID_194" MODIFIED="1450102818335" TEXT="All arguments are optional"/>
</node>
<node CREATED="1450102818335" FOLDED="true" ID="ID_195" MODIFIED="1450102818335" TEXT="cfd.tabulate()">
<node CREATED="1450102818335" FOLDED="true" ID="ID_196" MODIFIED="1450102818335" TEXT="Works just as cfd.plot()"/>
</node>
</node>
</node>
<node CREATED="1450102818335" FOLDED="true" ID="ID_197" MODIFIED="1450102818335" POSITION="right" TEXT="3. Processing Raw Text">
<node CREATED="1450102818335" ID="ID_198" MODIFIED="1450102818335" TEXT="Text processing workflow">
<node CREATED="1450102818335" FOLDED="true" ID="ID_199" MODIFIED="1450102818335" TEXT="Grabbing">
<node CREATED="1450102818336" FOLDED="true" ID="ID_200" MODIFIED="1450102818336" TEXT="Local file">
<node CREATED="1450102818336" FOLDED="true" ID="ID_201" MODIFIED="1450102818336">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>file = open('document.txt')</p>
                                        <p>raw = f.read()</p>
                                        <p>#raw = open('document.txt').read() does the same thing</p>
                                    </body>
                                </html></richcontent>
<node CREATED="1450102818336" FOLDED="true" ID="ID_202" MODIFIED="1450102818336" TEXT="If the file is text, raw will contain a string of text"/>
<node CREATED="1450102818336" FOLDED="true" ID="ID_203" MODIFIED="1450102818336" TEXT="If the file is html, raw will contain a string of html"/>
</node>
</node>
<node CREATED="1450102818336" FOLDED="true" ID="ID_204" MODIFIED="1450102818336" TEXT="File from the internet (text or html)">
<node CREATED="1450102818336" FOLDED="true" ID="ID_205" MODIFIED="1450102818336">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>url = "http://www.gutenberg.org/files/2554/2554.txt"</p>
                                        <p>response = urllib.request.urlopen(url)</p>
                                        <p>raw = response.read()</p>
                                        <p>#raw = urllib.request.urlopen(url).read() does the same thing</p>
                                    </body>
                                </html></richcontent>
<node CREATED="1450102818337" FOLDED="true" ID="ID_206" MODIFIED="1450102818337" TEXT="If the file is text, raw will contain a string of text"/>
<node CREATED="1450102818337" FOLDED="true" ID="ID_207" MODIFIED="1450102818337" TEXT="If the file is html, raw will contain a string of html"/>
</node>
</node>
<node CREATED="1450102818337" FOLDED="true" ID="ID_208" MODIFIED="1450102818337" TEXT="RSS feed">
<node CREATED="1450102818337" FOLDED="true" ID="ID_209" MODIFIED="1450102818337" TEXT="Using feedparser">
<node CREATED="1450102818337" FOLDED="true" ID="ID_210" MODIFIED="1450102818337">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>RSSfeed = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")</p>
                                            <p>post = RSSfeed.entries[2]</p>
                                            <p>raw = post.content[0].value</p>
                                        </body>
                                    </html></richcontent>
<node CREATED="1450102818337" FOLDED="true" ID="ID_211" MODIFIED="1450102818337" TEXT="raw will contain html"/>
</node>
</node>
</node>
<node CREATED="1450102818337" FOLDED="true" ID="ID_212" MODIFIED="1450102818337" TEXT="Handling encoding">
<node CREATED="1450102818337" FOLDED="true" ID="ID_213" MODIFIED="1450102818337" TEXT="Encoding is to be taken into account when the file is opened/read">
<node CREATED="1450102818338" FOLDED="true" ID="ID_214" MODIFIED="1450102818338" TEXT="open(path, encoding=&apos;latin2&apos;)"/>
<node CREATED="1450102818338" FOLDED="true" ID="ID_215" MODIFIED="1450102818338" TEXT="read().decode(&apos;utf8&apos;)"/>
</node>
<node CREATED="1450102818338" FOLDED="true" ID="ID_216" MODIFIED="1450102818338" TEXT="Internal recoding options">
<node CREATED="1450102818338" FOLDED="true" ID="ID_217" MODIFIED="1450102818338" TEXT="[text].encode(&apos;unicode_escape&apos;)">
<node CREATED="1450102818338" FOLDED="true" ID="ID_218" MODIFIED="1450102818338" TEXT="Returns [text] with the &apos;extended&apos; charachters replaced by by their equivalent &apos;\uXXXX&apos;"/>
</node>
<node CREATED="1450102818338" FOLDED="true" ID="ID_219" MODIFIED="1450102818338" TEXT="hex(ord([char]))">
<node CREATED="1450102818338" FOLDED="true" ID="ID_220" MODIFIED="1450102818338" TEXT="Returns the XXXX hex integer ordinal of [char]"/>
<node CREATED="1450102818338" FOLDED="true" ID="ID_221" MODIFIED="1450102818338" TEXT="[char] would be &apos;\uXXXX&apos;"/>
</node>
<node CREATED="1450102818339" FOLDED="true" ID="ID_222" MODIFIED="1450102818339" TEXT="[char].encode(&apos;utf8&apos;)">
<node CREATED="1450102818339" FOLDED="true" ID="ID_223" MODIFIED="1450102818339" TEXT="Returns [char]&apos;s utf8 byte sequence"/>
</node>
<node CREATED="1450102818339" FOLDED="true" ID="ID_224" MODIFIED="1450102818339" TEXT="unicodedata.name([char])">
<node CREATED="1450102818339" FOLDED="true" ID="ID_225" MODIFIED="1450102818339" TEXT="Returns the unicode name of [char]">
<node CREATED="1450102818339" FOLDED="true" ID="ID_226" MODIFIED="1450102818339" TEXT="LATIN SMALL LETTER O WITH ACUTE"/>
<node CREATED="1450102818339" FOLDED="true" ID="ID_227" MODIFIED="1450102818339" TEXT="..."/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1450102818339" FOLDED="true" ID="ID_228" MODIFIED="1450102818339" TEXT="Preprocessing">
<node CREATED="1450102818340" FOLDED="true" ID="ID_229" MODIFIED="1450102818340" TEXT="HTML">
<node CREATED="1450102818340" FOLDED="true" ID="ID_230" MODIFIED="1450102818340" TEXT="Using BeautifulSoup">
<node CREATED="1450102818340" FOLDED="true" ID="ID_231" MODIFIED="1450102818340" TEXT="raw = bs4.BeautifulSoup(raw).get_text()"/>
</node>
<node CREATED="1450102818340" FOLDED="true" ID="ID_232" MODIFIED="1450102818340" TEXT="Using NLTK">
<node CREATED="1450102818340" FOLDED="true" ID="ID_233" MODIFIED="1450102818340" TEXT="raw = nltk.clean_html(raw)"/>
</node>
</node>
<node CREATED="1450102818340" FOLDED="true" ID="ID_234" MODIFIED="1450102818340" TEXT="Text string with [BEGIN] and [END] flags">
<node CREATED="1450102818340" FOLDED="true" ID="ID_235" MODIFIED="1450102818340">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>begin_pos = raw.find('[BEGIN]')</p>
                                        <p>end_pos = raw.rfind('[END]')</p>
                                        <p>raw = raw[begin_pos:end_pos]</p>
                                    </body>
                                </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818340" FOLDED="true" ID="ID_236" MODIFIED="1450102818340" TEXT="Tokenizing">
<node CREATED="1450102818341" ID="ID_237" MODIFIED="1450102818341" TEXT="Text string">
<node CREATED="1450102818341" FOLDED="true" ID="ID_238" MODIFIED="1450102818341" TEXT="tokens = nltk.word_tokenize(raw)"/>
<node CREATED="1450102818341" FOLDED="true" ID="ID_239" MODIFIED="1450102818341" TEXT="sents = nltk.sent_tokenize(raw)">
<node CREATED="1450102818341" FOLDED="true" ID="ID_240" MODIFIED="1450102818341" TEXT="Splits into sentences - useful in some cases"/>
</node>
<node CREATED="1450102818341" FOLDED="true" ID="ID_241" MODIFIED="1450102818341" TEXT="Can also be done using regex (see below)">
<node CREATED="1450102818341" FOLDED="true" ID="ID_242" MODIFIED="1450102818341" TEXT="re.split(r&apos;\W+&apos;, raw)"/>
<node CREATED="1450102818341" FOLDED="true" ID="ID_243" MODIFIED="1450102818341" TEXT="re.findall(r&quot;\w+(?:[-&apos;]\w+)*|&apos;|[-.(]+|\S\w*&quot;, raw)"/>
</node>
<node CREATED="1450102818341" FOLDED="true" ID="ID_244" MODIFIED="1450102818341" TEXT="Can also be done using the ntlk regex tokenizer">
<node CREATED="1450102818341" FOLDED="true" ID="ID_245" MODIFIED="1450102818341" TEXT="nltk.regexp_tokenize([raw],[pattern])"/>
<node CREATED="1450102818341" FOLDED="true" ID="ID_246" MODIFIED="1450102818341">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>[pattern] =</p>
                                            <p>r'''(?x) # set flag to allow verbose regexps</p>
                                            <p>([A-Z]\.)+ # abbreviations, e.g. U.S.A.</p>
                                            <p>| \w+(-\w+)* # words with optional internal hyphens</p>
                                            <p>| \$?\d+(\.\d+)?%? # currency and percentages, e.g. $12.40, 82%</p>
                                            <p>| \.\.\. # ellipsis</p>
                                            <p>| [][.,;"'?():-_`] # these are separate tokens; includes ], [</p>
                                            <p>'''</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
<node CREATED="1450102818342" FOLDED="true" ID="ID_247" MODIFIED="1450102818342" TEXT="Quality can be evaluated using a hand tokenized text">
<node CREATED="1450102818342" FOLDED="true" ID="ID_248" MODIFIED="1450102818342" TEXT="nltk.corpus.treebank_raw.raw()">
<node CREATED="1450102818342" FOLDED="true" ID="ID_249" MODIFIED="1450102818342" TEXT="Raw version"/>
</node>
<node CREATED="1450102818342" FOLDED="true" ID="ID_250" MODIFIED="1450102818342" TEXT="nltk.corpus.treebank.words()">
<node CREATED="1450102818342" FOLDED="true" ID="ID_251" MODIFIED="1450102818342" TEXT="Tokenized version"/>
</node>
</node>
<node CREATED="1450102818342" FOLDED="true" ID="ID_252" MODIFIED="1450102818342" TEXT="Tokenizing is a type of segmentation">
<node CREATED="1450102818342" FOLDED="true" ID="ID_253" MODIFIED="1450102818342" TEXT="Separating streams into chunks"/>
<node CREATED="1450102818343" FOLDED="true" ID="ID_254" MODIFIED="1450102818343" TEXT="Specially tricky when we do not know the units to begin with">
<node CREATED="1450102818343" FOLDED="true" ID="ID_255" MODIFIED="1450102818343" TEXT="Completely new language"/>
<node CREATED="1450102818343" FOLDED="true" ID="ID_256" MODIFIED="1450102818343" TEXT="Chinese written language"/>
</node>
<node CREATED="1450102818343" FOLDED="true" ID="ID_257" MODIFIED="1450102818343" TEXT="This is a search problem">
<node CREATED="1450102818343" FOLDED="true" ID="ID_258" MODIFIED="1450102818343" TEXT="Define a vocabulary that minimizes the representation cost of the coplete text"/>
</node>
<node CREATED="1450102818343" FOLDED="true" ID="ID_259" MODIFIED="1450102818343" TEXT="The possibilities are endless">
<node CREATED="1450102818343" FOLDED="true" ID="ID_260" MODIFIED="1450102818343" TEXT="Simulated annealing"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818343" FOLDED="true" ID="ID_261" MODIFIED="1450102818343" TEXT="Normalization">
<node CREATED="1450102818343" FOLDED="true" ID="ID_262" MODIFIED="1450102818343" TEXT="Make lowercase">
<node CREATED="1450102818343" FOLDED="true" ID="ID_263" MODIFIED="1450102818343" TEXT="tokens = [ wd.lower for wd in tokens ]"/>
</node>
<node CREATED="1450102818344" FOLDED="true" ID="ID_264" MODIFIED="1450102818344" TEXT="Remove non-alpha tokens">
<node CREATED="1450102818344" FOLDED="true" ID="ID_265" MODIFIED="1450102818344" TEXT="tokens = [ wd for wd in tokens if wd.alpha()==True ]"/>
</node>
<node CREATED="1450102818344" FOLDED="true" ID="ID_266" MODIFIED="1450102818344" TEXT="Stemming">
<node CREATED="1450102818344" FOLDED="true" ID="ID_267" MODIFIED="1450102818344" TEXT="Tries to remove affixes"/>
<node CREATED="1450102818344" FOLDED="true" ID="ID_268" MODIFIED="1450102818344" TEXT="Porter">
<node CREATED="1450102818344" FOLDED="true" ID="ID_269" MODIFIED="1450102818344" TEXT="tokens = [ nltk.PorterStemmer().stem(t) for t in tokens ]"/>
</node>
<node CREATED="1450102818344" FOLDED="true" ID="ID_270" MODIFIED="1450102818344" TEXT="Lancaster">
<node CREATED="1450102818344" FOLDED="true" ID="ID_271" MODIFIED="1450102818344" TEXT="tokens = [ nltk.LancasterStemmer().stem(t) for t in tokens ]"/>
</node>
</node>
<node CREATED="1450102818344" FOLDED="true" ID="ID_272" MODIFIED="1450102818344" TEXT="Lemmatization">
<node CREATED="1450102818345" FOLDED="true" ID="ID_273" MODIFIED="1450102818345" TEXT="Tries to map to a lemma">
<node CREATED="1450102818345" FOLDED="true" ID="ID_274" MODIFIED="1450102818345" TEXT="Closely related to stemming, but not quite the same"/>
</node>
<node CREATED="1450102818345" FOLDED="true" ID="ID_275" MODIFIED="1450102818345" TEXT="WordNet">
<node CREATED="1450102818345" FOLDED="true" ID="ID_276" MODIFIED="1450102818345" TEXT="tokens = [ nltk.WordNetLemmatizer().lemmatize(t) for t in tokens ]"/>
</node>
</node>
<node CREATED="1450102818345" FOLDED="true" ID="ID_277" MODIFIED="1450102818345" TEXT="Removal of non standard words">
<node CREATED="1450102818345" FOLDED="true" ID="ID_278" MODIFIED="1450102818345" TEXT="Numbers"/>
<node CREATED="1450102818345" FOLDED="true" ID="ID_279" MODIFIED="1450102818345" TEXT="Abbreviations"/>
<node CREATED="1450102818345" FOLDED="true" ID="ID_280" MODIFIED="1450102818345" TEXT="Dates"/>
<node CREATED="1450102818345" FOLDED="true" ID="ID_281" MODIFIED="1450102818345" TEXT="..."/>
<node CREATED="1450102818345" FOLDED="true" ID="ID_282" MODIFIED="1450102818345" TEXT="Can be mapped to specific keys to keep the dictionary small"/>
</node>
</node>
<node CREATED="1450102818345" FOLDED="true" ID="ID_283" MODIFIED="1450102818345" TEXT="Create a vocabulary">
<node CREATED="1450102818346" FOLDED="true" ID="ID_284" MODIFIED="1450102818346" TEXT="vocabulary = sorted(set(tokens))"/>
</node>
<node CREATED="1450102818346" FOLDED="true" ID="ID_285" MODIFIED="1450102818346" TEXT="NLTK-texting">
<node CREATED="1450102818346" FOLDED="true" ID="ID_286" MODIFIED="1450102818346" TEXT="Tokens">
<node CREATED="1450102818346" FOLDED="true" ID="ID_287" MODIFIED="1450102818346" TEXT="text = nltk.Text(tokens)"/>
</node>
</node>
</node>
<node CREATED="1450102818346" FOLDED="true" ID="ID_288" MODIFIED="1450102818346" TEXT="Regex">
<node CREATED="1450102818346" FOLDED="true" ID="ID_289" MODIFIED="1450102818346" TEXT="Module re"/>
<node CREATED="1450102818346" FOLDED="true" ID="ID_290" MODIFIED="1450102818346" TEXT="re.search([pattern], [string])">
<node CREATED="1450102818346" FOLDED="true" ID="ID_291" MODIFIED="1450102818346" TEXT="Returns whether [pattern] is found in [string] or not"/>
</node>
<node CREATED="1450102818346" FOLDED="true" ID="ID_292" MODIFIED="1450102818346" TEXT="re.findall([pattern], [string])">
<node CREATED="1450102818346" FOLDED="true" ID="ID_293" MODIFIED="1450102818346" TEXT="Returns a list with all non overlapping occurence of [pattern] in [string]"/>
</node>
<node CREATED="1450102818346" FOLDED="true" ID="ID_294" MODIFIED="1450102818346" TEXT="re.split([pattern], [string])">
<node CREATED="1450102818347" FOLDED="true" ID="ID_295" MODIFIED="1450102818347" TEXT="Splits [string] on [pattern]">
<node CREATED="1450102818347" FOLDED="true" ID="ID_296" MODIFIED="1450102818347" TEXT="Naive tokenizer">
<node CREATED="1450102818347" FOLDED="true" ID="ID_297" MODIFIED="1450102818347" TEXT="re.split(r&apos;[ \t\n]+&apos;, raw)"/>
<node CREATED="1450102818347" FOLDED="true" ID="ID_298" MODIFIED="1450102818347" TEXT="re.split(r&apos;\s+&apos;, raw)">
<node CREATED="1450102818347" FOLDED="true" ID="ID_299" MODIFIED="1450102818347" TEXT="Same output: \s means &apos;any whitespace character&apos;"/>
</node>
<node CREATED="1450102818347" FOLDED="true" ID="ID_300" MODIFIED="1450102818347" TEXT="re.split(r&apos;\W+&apos;, raw)">
<node CREATED="1450102818347" FOLDED="true" ID="ID_301" MODIFIED="1450102818347" TEXT="Split on anything other than a character"/>
<node CREATED="1450102818347" FOLDED="true" ID="ID_302" MODIFIED="1450102818347" TEXT="\w means [a-zA-Z0-9_]">
<node CREATED="1450102818347" FOLDED="true" ID="ID_303" MODIFIED="1450102818347" TEXT="\W is the opposite"/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1450102818347" FOLDED="true" ID="ID_304" MODIFIED="1450102818347" TEXT="nltk.re_show([pattern], [string])">
<node CREATED="1450102818347" FOLDED="true" ID="ID_305" MODIFIED="1450102818347" TEXT="Returns an annotated string that highlights where [pattern] was found"/>
</node>
<node CREATED="1450102818347" FOLDED="true" ID="ID_306" MODIFIED="1450102818347" TEXT="[pattern]">
<node CREATED="1450102818347" FOLDED="true" ID="ID_307" MODIFIED="1450102818347" TEXT="\">
<node CREATED="1450102818347" FOLDED="true" ID="ID_308" MODIFIED="1450102818347" TEXT="The following character (expected to be special) is escaped"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_309" MODIFIED="1450102818348" TEXT=".">
<node CREATED="1450102818348" FOLDED="true" ID="ID_310" MODIFIED="1450102818348" TEXT="Any character"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_311" MODIFIED="1450102818348" TEXT="[abc]">
<node CREATED="1450102818348" FOLDED="true" ID="ID_312" MODIFIED="1450102818348" TEXT="One of the characters &apos;a&apos;, &apos;b&apos; or &apos;c&apos;"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_313" MODIFIED="1450102818348" TEXT="[a-c]">
<node CREATED="1450102818348" FOLDED="true" ID="ID_314" MODIFIED="1450102818348" TEXT="One of the characters between &apos;a&apos; and &apos;c&apos;"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_315" MODIFIED="1450102818348" TEXT="[^unit]">
<node CREATED="1450102818348" FOLDED="true" ID="ID_316" MODIFIED="1450102818348" TEXT="Complementary set to [unit]"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_317" MODIFIED="1450102818348" TEXT="[str]$">
<node CREATED="1450102818348" FOLDED="true" ID="ID_318" MODIFIED="1450102818348" TEXT="[str] at the end of the string"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_319" MODIFIED="1450102818348" TEXT="^[str]">
<node CREATED="1450102818348" FOLDED="true" ID="ID_320" MODIFIED="1450102818348" TEXT="[str] at the beginning of the string"/>
</node>
<node CREATED="1450102818348" FOLDED="true" ID="ID_321" MODIFIED="1450102818348" TEXT="?">
<node CREATED="1450102818349" FOLDED="true" ID="ID_322" MODIFIED="1450102818349" TEXT="The previous unit is optional"/>
</node>
<node CREATED="1450102818349" FOLDED="true" ID="ID_323" MODIFIED="1450102818349" TEXT="+">
<node CREATED="1450102818349" FOLDED="true" ID="ID_324" MODIFIED="1450102818349" TEXT="The previous unit can appear once or more"/>
</node>
<node CREATED="1450102818349" FOLDED="true" ID="ID_325" MODIFIED="1450102818349" TEXT="*">
<node CREATED="1450102818349" FOLDED="true" ID="ID_326" MODIFIED="1450102818349" TEXT="The previous unit can appear zero, one, or multiple times"/>
<node CREATED="1450102818349" FOLDED="true" ID="ID_327" MODIFIED="1450102818349" TEXT="* is greedy (it will try to maximize what it is matching)"/>
<node CREATED="1450102818349" FOLDED="true" ID="ID_328" MODIFIED="1450102818349" TEXT="The non-greedy version would be *?"/>
</node>
<node CREATED="1450102818349" FOLDED="true" ID="ID_329" MODIFIED="1450102818349" TEXT="{n,m}">
<node CREATED="1450102818349" FOLDED="true" ID="ID_330" MODIFIED="1450102818349" TEXT="The previous unit must appear between n and m times"/>
<node CREATED="1450102818349" FOLDED="true" ID="ID_331" MODIFIED="1450102818349" TEXT="Other options">
<node CREATED="1450102818349" FOLDED="true" ID="ID_332" MODIFIED="1450102818349" TEXT="{n}">
<node CREATED="1450102818349" FOLDED="true" ID="ID_333" MODIFIED="1450102818349" TEXT="Exactly n times"/>
</node>
<node CREATED="1450102818349" FOLDED="true" ID="ID_334" MODIFIED="1450102818349" TEXT="{n,}">
<node CREATED="1450102818350" FOLDED="true" ID="ID_335" MODIFIED="1450102818350" TEXT="n or more times"/>
</node>
<node CREATED="1450102818350" FOLDED="true" ID="ID_336" MODIFIED="1450102818350" TEXT="{,m}">
<node CREATED="1450102818350" FOLDED="true" ID="ID_337" MODIFIED="1450102818350" TEXT="m or less times"/>
</node>
</node>
</node>
<node CREATED="1450102818350" FOLDED="true" ID="ID_338" MODIFIED="1450102818350" TEXT="|">
<node CREATED="1450102818350" FOLDED="true" ID="ID_339" MODIFIED="1450102818350" TEXT="Either unit">
<node CREATED="1450102818350" FOLDED="true" ID="ID_340" MODIFIED="1450102818350" TEXT="The usage of &apos;scoping&apos; (see below) with | is almost mandatory"/>
</node>
</node>
<node CREATED="1450102818350" FOLDED="true" ID="ID_341" MODIFIED="1450102818350" TEXT="()">
<node CREATED="1450102818350" FOLDED="true" ID="ID_342" MODIFIED="1450102818350" TEXT="Scope of the operators">
<node CREATED="1450102818350" FOLDED="true" ID="ID_343" MODIFIED="1450102818350" TEXT="Mainly applicable to |"/>
</node>
<node CREATED="1450102818350" FOLDED="true" ID="ID_344" MODIFIED="1450102818350" TEXT="Secondary behaviour">
<node CREATED="1450102818350" FOLDED="true" ID="ID_345" MODIFIED="1450102818350" TEXT="Determines what will be returned by re.findall()"/>
<node CREATED="1450102818351" FOLDED="true" ID="ID_346" MODIFIED="1450102818351" TEXT="To avoid this secondary behaviour, the form (?:a|b|c) must be used"/>
<node CREATED="1450102818351" FOLDED="true" ID="ID_347" MODIFIED="1450102818351" TEXT="Example">
<node CREATED="1450102818351" FOLDED="true" ID="ID_348" MODIFIED="1450102818351" TEXT="re.findall(r&apos;^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$&apos;, &apos;processes&apos;)">
<node CREATED="1450102818351" FOLDED="true" ID="ID_349" MODIFIED="1450102818351" TEXT="[&apos;s&apos;]"/>
<node CREATED="1450102818351" FOLDED="true" ID="ID_350" MODIFIED="1450102818351" TEXT="Returns only what is between the parenthesys"/>
</node>
<node CREATED="1450102818351" FOLDED="true" ID="ID_351" MODIFIED="1450102818351" TEXT="re.findall(r&apos;^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$&apos;, &apos;processes&apos;)">
<node CREATED="1450102818351" FOLDED="true" ID="ID_352" MODIFIED="1450102818351" TEXT="[&apos;processes&apos;]"/>
<node CREATED="1450102818351" FOLDED="true" ID="ID_353" MODIFIED="1450102818351" TEXT="Returns the whole word"/>
</node>
<node CREATED="1450102818351" FOLDED="true" ID="ID_354" MODIFIED="1450102818351" TEXT="re.findall(r&apos;^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$&apos;, &apos;processes&apos;)">
<node CREATED="1450102818351" FOLDED="true" ID="ID_355" MODIFIED="1450102818351" TEXT="[&apos;processe&apos;, &apos;s&apos;]"/>
<node CREATED="1450102818351" FOLDED="true" ID="ID_356" MODIFIED="1450102818351" TEXT="Returns both parts, but * is greedy"/>
</node>
<node CREATED="1450102818351" FOLDED="true" ID="ID_357" MODIFIED="1450102818351" TEXT="re.findall(r&apos;^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$&apos;, &apos;processes&apos;)">
<node CREATED="1450102818352" FOLDED="true" ID="ID_358" MODIFIED="1450102818352" TEXT="[&apos;process&apos;, &apos;es&apos;]"/>
<node CREATED="1450102818352" FOLDED="true" ID="ID_359" MODIFIED="1450102818352" TEXT="Works as expected"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818352" FOLDED="true" ID="ID_360" MODIFIED="1450102818352" TEXT="Special characters">
<node CREATED="1450102818352" FOLDED="true" ID="ID_361" MODIFIED="1450102818352">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>\b	Word boundary (zero width)</p>
                                        <p>\d	Any decimal digit (equivalent to [0-9])</p>
                                        <p>\D	Any non-digit character (equivalent to [^0-9])</p>
                                        <p>\s	Any whitespace character (equivalent to [ \t\n\r\f\v])</p>
                                        <p>\S	Any non-whitespace character (equivalent to [^ \t\n\r\f\v])</p>
                                        <p>\w	Any alphanumeric character (equivalent to [a-zA-Z0-9_])</p>
                                        <p>\W	Any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])</p>
                                        <p>\t	The tab character</p>
                                        <p>\n	The newline character</p>
                                    </body>
                                </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818352" FOLDED="true" ID="ID_362" MODIFIED="1450102818352" TEXT="Patterns can be applied to complete tokens and applied to texts">
<node CREATED="1450102818352" FOLDED="true" ID="ID_363" MODIFIED="1450102818352" TEXT="Just wrap them in &lt;[pattern]&gt;">
<node CREATED="1450102818353" FOLDED="true" ID="ID_364" MODIFIED="1450102818353" TEXT="Spaces between &lt;[pattern]&gt; units are ignored"/>
</node>
<node CREATED="1450102818353" FOLDED="true" ID="ID_365" MODIFIED="1450102818353" TEXT="&apos;&lt;a&gt;(&lt;.*&gt;)&lt;man&gt;&apos; will match &apos;a&apos;, followed by one token, followed by &apos;man&apos;">
<node CREATED="1450102818353" FOLDED="true" ID="ID_366" MODIFIED="1450102818353" TEXT="findall() will return only the token in between &apos;a&apos; and &apos;man&apos;"/>
</node>
</node>
</node>
<node CREATED="1450102818353" FOLDED="true" ID="ID_367" MODIFIED="1450102818353" TEXT="nltk.Index([list_of_pairs])">
<node CREATED="1450102818353" FOLDED="true" ID="ID_368" MODIFIED="1450102818353" TEXT="Creates an indexed structure out of a list of pairs">
<node CREATED="1450102818353" FOLDED="true" ID="ID_369" MODIFIED="1450102818353" TEXT="(k,v) -&gt; key:value1 associated with key"/>
</node>
<node CREATED="1450102818353" FOLDED="true" ID="ID_370" MODIFIED="1450102818353" TEXT="Works similarly to a dictionary">
<node CREATED="1450102818353" FOLDED="true" ID="ID_371" MODIFIED="1450102818353" TEXT="There can be several values for the same key"/>
</node>
</node>
<node CREATED="1450102818353" FOLDED="true" ID="ID_372" MODIFIED="1450102818353" TEXT="Formatting output strings">
<node CREATED="1450102818353" FOLDED="true" ID="ID_373" MODIFIED="1450102818353" TEXT="Joining">
<node CREATED="1450102818353" FOLDED="true" ID="ID_374" MODIFIED="1450102818353" TEXT="&apos; &apos;.join([list])"/>
</node>
<node CREATED="1450102818353" FOLDED="true" ID="ID_375" MODIFIED="1450102818353" TEXT="Substitution">
<node CREATED="1450102818354" FOLDED="true" ID="ID_376" MODIFIED="1450102818354" TEXT="&apos;{}-&gt;{};&apos;.format(&apos;cat&apos;, 3)">
<node CREATED="1450102818354" FOLDED="true" ID="ID_377" MODIFIED="1450102818354" TEXT="&apos;cat-&gt;3&apos;"/>
</node>
<node CREATED="1450102818354" FOLDED="true" ID="ID_378" MODIFIED="1450102818354" TEXT="&apos;from {1} to {0}&apos;.format(&apos;A&apos;, &apos;B&apos;)">
<node CREATED="1450102818354" FOLDED="true" ID="ID_379" MODIFIED="1450102818354" TEXT="&apos;from B to A&apos;"/>
</node>
<node CREATED="1450102818354" FOLDED="true" ID="ID_380" MODIFIED="1450102818354" TEXT="&apos;Here be {tag}&apos;.format(tag=&apos;dragons&apos;)">
<node CREATED="1450102818354" FOLDED="true" ID="ID_381" MODIFIED="1450102818354" TEXT="&apos;Here be dragons&apos;"/>
</node>
<node CREATED="1450102818354" FOLDED="true" ID="ID_382" MODIFIED="1450102818354" TEXT="Another approach">
<node CREATED="1450102818354" FOLDED="true" ID="ID_383" MODIFIED="1450102818354" TEXT="&apos;Here be %s&apos; % &apos;dragons&apos;"/>
</node>
</node>
<node CREATED="1450102818354" FOLDED="true" ID="ID_384" MODIFIED="1450102818354" TEXT="Printing without newline">
<node CREATED="1450102818354" FOLDED="true" ID="ID_385" MODIFIED="1450102818354">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>for word in sorted(fdist):</p>
                                    <p>print('{}-&gt;{};'.format(word, fdist[word]), end=' ')</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818355" FOLDED="true" ID="ID_386" MODIFIED="1450102818355" TEXT="Padding">
<node CREATED="1450102818355" FOLDED="true" ID="ID_387" MODIFIED="1450102818355" TEXT="Numbers">
<node CREATED="1450102818355" FOLDED="true" ID="ID_388" MODIFIED="1450102818355" TEXT="Numbers align to the right by default"/>
<node CREATED="1450102818355" FOLDED="true" ID="ID_389" MODIFIED="1450102818355" TEXT="&apos;{:6}&apos;.format(41)">
<node CREATED="1450102818355" FOLDED="true" ID="ID_390" MODIFIED="1450102818355" TEXT="41, right aligned, filled up to 6 spaces"/>
</node>
<node CREATED="1450102818355" FOLDED="true" ID="ID_391" MODIFIED="1450102818355" TEXT="&apos;{:&lt;6}&apos; .format(41)">
<node CREATED="1450102818355" FOLDED="true" ID="ID_392" MODIFIED="1450102818355" TEXT="41, left aligned, filled up to 6 spaces"/>
</node>
</node>
<node CREATED="1450102818355" FOLDED="true" ID="ID_393" MODIFIED="1450102818355" TEXT="Strings">
<node CREATED="1450102818355" FOLDED="true" ID="ID_394" MODIFIED="1450102818355" TEXT="Strings align to the left by default"/>
<node CREATED="1450102818355" FOLDED="true" ID="ID_395" MODIFIED="1450102818355" TEXT="&apos;{:6}&apos;.format(&apos;dog&apos;)">
<node CREATED="1450102818355" FOLDED="true" ID="ID_396" MODIFIED="1450102818355" TEXT="dog, left aligned, filled up to 6 spaces"/>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_397" MODIFIED="1450102818356" TEXT="&apos;{:&gt;6}&apos;.format(&apos;dog&apos;)">
<node CREATED="1450102818356" FOLDED="true" ID="ID_398" MODIFIED="1450102818356" TEXT="dog, right aligned, filled up to 6 spaces"/>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_399" MODIFIED="1450102818356" TEXT="This would also work">
<node CREATED="1450102818356" FOLDED="true" ID="ID_400" MODIFIED="1450102818356" TEXT=" &apos;{:{width}}&apos; % (&quot;Monty Python&quot;, width=15)"/>
</node>
</node>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_401" MODIFIED="1450102818356" TEXT="Decimal places">
<node CREATED="1450102818356" FOLDED="true" ID="ID_402" MODIFIED="1450102818356" TEXT="&apos;{:.4f}&apos;.format(math.pi)">
<node CREATED="1450102818356" FOLDED="true" ID="ID_403" MODIFIED="1450102818356" TEXT="3.1416"/>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_404" MODIFIED="1450102818356" TEXT="&apos;{:.4%}&apos;.format(0.3418666)">
<node CREATED="1450102818356" FOLDED="true" ID="ID_405" MODIFIED="1450102818356" TEXT="34.1867%"/>
</node>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_406" MODIFIED="1450102818356" TEXT="Text wrapping">
<node CREATED="1450102818356" FOLDED="true" ID="ID_407" MODIFIED="1450102818356" TEXT="textwrap.fill([raw])"/>
</node>
</node>
</node>
<node CREATED="1450102818356" FOLDED="true" ID="ID_408" MODIFIED="1450102818356" POSITION="right" TEXT="4. Writing Structured Programs">
<node CREATED="1450102818356" FOLDED="true" ID="ID_409" MODIFIED="1450102818356" TEXT="Mostly on Python programming"/>
<node CREATED="1450102818356" FOLDED="true" ID="ID_410" MODIFIED="1450102818356" TEXT="docstring">
<node CREATED="1450102818356" FOLDED="true" ID="ID_411" MODIFIED="1450102818356" TEXT="The first string inside a function">
<node CREATED="1450102818357" FOLDED="true" ID="ID_412" MODIFIED="1450102818357" TEXT="Documents the purpose of the function"/>
<node CREATED="1450102818357" FOLDED="true" ID="ID_413" MODIFIED="1450102818357" TEXT="Is accessible through help([function])"/>
<node CREATED="1450102818357" FOLDED="true" ID="ID_414" MODIFIED="1450102818357" TEXT="Example">
<node CREATED="1450102818357" FOLDED="true" ID="ID_415" MODIFIED="1450102818357">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>def get_text(file):</p>
                                        <p>"""Read text from a file, normalizing whitespace and stripping HTML markup."""</p>
                                        <p>text = open(file).read()</p>
                                        <p>text = re.sub(r'&lt;.*?&gt;', ' ', text)</p>
                                        <p>text = re.sub('\s+', ' ', text)</p>
                                        <p>return text</p>
                                    </body>
                                </html></richcontent>
</node>
</node>
</node>
</node>
<node CREATED="1450102818357" FOLDED="true" ID="ID_416" MODIFIED="1450102818357" TEXT="assert">
<node CREATED="1450102818357" FOLDED="true" ID="ID_417" MODIFIED="1450102818357" TEXT="Check inputs to a function">
<node CREATED="1450102818357" FOLDED="true" ID="ID_418" MODIFIED="1450102818357">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>def tag(word):</p>
                                    <p>assert isinstance(word, basestring), "argument to tag() must be a string"</p>
                                    <p>if word in ['a', 'the', 'all']:</p>
                                    <p>return 'det'</p>
                                    <p>else:</p>
                                    <p>return 'noun'</p>
                                </body>
                            </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818358" FOLDED="true" ID="ID_419" MODIFIED="1450102818358" TEXT="lambda expressions">
<node CREATED="1450102818358" FOLDED="true" ID="ID_420" MODIFIED="1450102818358" TEXT="Mini functions ususally used within another function call"/>
<node CREATED="1450102818358" FOLDED="true" ID="ID_421" MODIFIED="1450102818358" TEXT="With normal function">
<node CREATED="1450102818358" FOLDED="true" ID="ID_422" MODIFIED="1450102818358">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>aux_sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',</p>
                                    <p>'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']</p>
                                    <p>def extract_property(prop, sent):</p>
                                    <p>return [prop(word) for word in sent]</p>
                                    <p>def last_letter(word):</p>
                                    <p>return word[-1]</p>
                                    <p>extract_property(last_letter, aux_sent)</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818358" FOLDED="true" ID="ID_423" MODIFIED="1450102818358" TEXT="[&apos;e&apos;, &apos;e&apos;, &apos;f&apos;, &apos;e&apos;, &apos;e&apos;, &apos;,&apos;, &apos;d&apos;, &apos;e&apos;, &apos;s&apos;, &apos;l&apos;, &apos;e&apos;, &apos;e&apos;, &apos;f&apos;, &apos;s&apos;, &apos;.&apos;]"/>
</node>
</node>
<node CREATED="1450102818358" FOLDED="true" ID="ID_424" MODIFIED="1450102818358" TEXT="With lambda expression">
<node CREATED="1450102818358" FOLDED="true" ID="ID_425" MODIFIED="1450102818358">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>aux_sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',</p>
                                    <p>'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']</p>
                                    <p>def extract_property(prop, sent):</p>
                                    <p>return [prop(word) for word in sent]</p>
                                    <p>extract_property(lambda w: w[-1], aux_sent)</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818358" FOLDED="true" ID="ID_426" MODIFIED="1450102818358" TEXT="[&apos;e&apos;, &apos;e&apos;, &apos;f&apos;, &apos;e&apos;, &apos;e&apos;, &apos;,&apos;, &apos;d&apos;, &apos;e&apos;, &apos;s&apos;, &apos;l&apos;, &apos;e&apos;, &apos;e&apos;, &apos;f&apos;, &apos;s&apos;, &apos;.&apos;]"/>
</node>
</node>
</node>
<node CREATED="1450102818359" FOLDED="true" ID="ID_427" MODIFIED="1450102818359" TEXT="yield">
<node CREATED="1450102818359" FOLDED="true" ID="ID_428" MODIFIED="1450102818359" TEXT="Yield functions operate as generators">
<node CREATED="1450102818359" FOLDED="true" ID="ID_429" MODIFIED="1450102818359" TEXT="The first time this function is called, it gets as far as the yield statement and pauses"/>
</node>
<node CREATED="1450102818359" FOLDED="true" ID="ID_430" MODIFIED="1450102818359" TEXT="Example">
<node CREATED="1450102818359" FOLDED="true" ID="ID_431" MODIFIED="1450102818359" TEXT="Both do the same thing"/>
<node CREATED="1450102818359" FOLDED="true" ID="ID_432" MODIFIED="1450102818359" TEXT="Without yield">
<node CREATED="1450102818359" FOLDED="true" ID="ID_433" MODIFIED="1450102818359">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>def search1(substring, words):</p>
                                        <p>result = []</p>
                                        <p>for word in words:</p>
                                        <p>if substring in word:</p>
                                        <p>result.append(word)</p>
                                        <p>return result</p>
                                    </body>
                                </html></richcontent>
<node CREATED="1450102818359" FOLDED="true" ID="ID_434" MODIFIED="1450102818359">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>for item in search1('zz', nltk.corpus.brown.words()):</p>
                                            <p>print(item, end=" ")</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818360" FOLDED="true" ID="ID_435" MODIFIED="1450102818360" TEXT="With yield">
<node CREATED="1450102818360" FOLDED="true" ID="ID_436" MODIFIED="1450102818360">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>def search2(substring, words):</p>
                                        <p>for word in words:</p>
                                        <p>if substring in word:</p>
                                        <p>yield word</p>
                                    </body>
                                </html></richcontent>
<node CREATED="1450102818360" FOLDED="true" ID="ID_437" MODIFIED="1450102818360">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>for item in search2('zz', nltk.corpus.brown.words()):</p>
                                            <p>print(item, end=" ")</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1450102818360" FOLDED="true" ID="ID_438" MODIFIED="1450102818360" TEXT="filter">
<node CREATED="1450102818360" FOLDED="true" ID="ID_439" MODIFIED="1450102818360" TEXT="Aplies the first parameter (function) to each item in the sequence contained in its second parameter, and retains the items for which the function returns True"/>
</node>
<node CREATED="1450102818360" ID="ID_440" MODIFIED="1450102818360" TEXT="map">
<node CREATED="1450102818360" FOLDED="true" ID="ID_441" MODIFIED="1450102818360" TEXT="Applies a function to every item in a sequence"/>
</node>
<node CREATED="1450102818360" ID="ID_442" MODIFIED="1450102818360" TEXT="def generic(*args, **kwargs):">
<node CREATED="1450102818360" ID="ID_443" MODIFIED="1450102818360" TEXT="args">
<node CREATED="1450102818360" FOLDED="true" ID="ID_444" MODIFIED="1450102818360" TEXT="Unnamed parameters"/>
</node>
<node CREATED="1450102818360" ID="ID_445" MODIFIED="1450102818360" TEXT="kwargs">
<node CREATED="1450102818360" FOLDED="true" ID="ID_446" MODIFIED="1450102818360" TEXT="Named parameters"/>
</node>
<node CREATED="1450102818360" ID="ID_447" MODIFIED="1450102818360" TEXT="*args">
<node CREATED="1450102818360" ID="ID_448" MODIFIED="1450102818360" TEXT="All/Each of the values of &apos;args&apos;">
<node CREATED="1450102818361" FOLDED="true" ID="ID_449" MODIFIED="1450102818361">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>song =</p>
                                        <p>[['four', 'calling', 'birds'],</p>
                                        <p>['three', 'French', 'hens'],</p>
                                        <p>['two', 'turtle', 'doves']]</p>
                                    </body>
                                </html></richcontent>
</node>
<node CREATED="1450102818361" ID="ID_450" MODIFIED="1450102818361" TEXT="*song==[song[0],sing[1].song[2]]">
<node CREATED="1450102818361" FOLDED="true" ID="ID_451" MODIFIED="1450102818361" TEXT="Almost"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818361" ID="ID_452" MODIFIED="1450102818361" TEXT="with open([file]) as f:">
<node CREATED="1450102818361" FOLDED="true" ID="ID_453" MODIFIED="1450102818361" TEXT="Will close the file automatically when the &apos;with&apos; is done"/>
</node>
<node CREATED="1450102818361" FOLDED="true" ID="ID_454" MODIFIED="1450102818361" TEXT="memoization">
<node CREATED="1450102818361" FOLDED="true" ID="ID_455" MODIFIED="1450102818361" TEXT="Related to caching"/>
<node CREATED="1450102818361" FOLDED="true" ID="ID_456" MODIFIED="1450102818361" TEXT="WORTH LOOKING MORE INTO"/>
</node>
</node>
<node CREATED="1450102818361" FOLDED="true" ID="ID_457" MODIFIED="1450102818361" POSITION="right" TEXT="5. Categorizing and Tagging Words">
<node CREATED="1450102818361" ID="ID_458" MODIFIED="1450102818361" TEXT="Tagging">
<node CREATED="1450102818361" FOLDED="true" ID="ID_459" MODIFIED="1450102818361" TEXT="A.k.a. &apos;Parts-of-speech tagging&apos; or &apos;POS-tagging&apos;"/>
<node CREATED="1450102818361" FOLDED="true" ID="ID_468" MODIFIED="1450102818361" TEXT="Usually done after tokenization"/>
<node CREATED="1450102818361" FOLDED="true" ID="ID_629" MODIFIED="1450102818361" TEXT="How is it done to begin with">
<node CREATED="1450102818361" ID="ID_630" MODIFIED="1450102818361" TEXT="Morphological cues">
<node CREATED="1450102818361" ID="ID_633" MODIFIED="1450102818361" TEXT="-ness is associated with nouns">
<node CREATED="1450102818361" ID="ID_634" MODIFIED="1450102818361" TEXT="happiness"/>
</node>
<node CREATED="1450102818361" ID="ID_635" MODIFIED="1450102818361" TEXT="-ment is associated with nouns">
<node CREATED="1450102818362" ID="ID_636" MODIFIED="1450102818362" TEXT="government"/>
</node>
</node>
<node CREATED="1450102818362" ID="ID_631" MODIFIED="1450102818362" TEXT="Syntactic cues">
<node CREATED="1450102818362" ID="ID_637" MODIFIED="1450102818362" TEXT="In &apos;det + ? + noun&apos;, ? is likely to be and adjective"/>
<node CREATED="1450102818362" ID="ID_638" MODIFIED="1450102818362" TEXT="In &apos;det + noun + BE + ?&apos;, ? is likely to be and adjective"/>
</node>
<node CREATED="1450102818362" ID="ID_632" MODIFIED="1450102818362" TEXT="Semantic cues">
<node CREATED="1450102818362" ID="ID_639" MODIFIED="1450102818362" TEXT="Most human"/>
<node CREATED="1450102818362" FOLDED="true" ID="ID_640" MODIFIED="1450102818362" TEXT="Very hard to formalize"/>
</node>
<node CREATED="1450102818362" ID="ID_641" MODIFIED="1450102818362" TEXT="New words">
<node CREATED="1450102818362" ID="ID_642" MODIFIED="1450102818362" TEXT="Languages grow over time, but most (if not all) new words are nouns">
<node CREATED="1450102818362" ID="ID_643" MODIFIED="1450102818362" TEXT="It is very unlikely that new prepositions will be added to any language"/>
<node CREATED="1450102818362" ID="ID_644" MODIFIED="1450102818362" TEXT="Verbs and adjectives, maybe"/>
</node>
</node>
</node>
<node CREATED="1450102818362" FOLDED="true" ID="ID_469" MODIFIED="1450102818362" TEXT="Parts of speech">
<node CREATED="1450102818362" FOLDED="true" ID="ID_470" MODIFIED="1450102818362" TEXT="Word classes"/>
<node CREATED="1450102818362" FOLDED="true" ID="ID_471" MODIFIED="1450102818362" TEXT="Lexical categories"/>
</node>
<node CREATED="1450102818362" ID="ID_472" MODIFIED="1450102818362" TEXT="Set of tags">
<node CREATED="1450102818362" FOLDED="true" ID="ID_473" MODIFIED="1450102818362" TEXT="tagset">
<node CREATED="1450102818362" ID="ID_474" MODIFIED="1450102818362" TEXT="CC">
<node CREATED="1450102818362" FOLDED="true" ID="ID_475" MODIFIED="1450102818362" TEXT="Coordinating conjunction"/>
</node>
<node CREATED="1450102818362" FOLDED="true" ID="ID_476" MODIFIED="1450102818362" TEXT="RB">
<node CREATED="1450102818362" FOLDED="true" ID="ID_477" MODIFIED="1450102818362" TEXT="Adverb"/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_478" MODIFIED="1450102818363" TEXT="IN">
<node CREATED="1450102818363" FOLDED="true" ID="ID_479" MODIFIED="1450102818363" TEXT="Preposition"/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_480" MODIFIED="1450102818363" TEXT="NN">
<node CREATED="1450102818363" FOLDED="true" ID="ID_481" MODIFIED="1450102818363" TEXT="Noun"/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_482" MODIFIED="1450102818363" TEXT="JJ">
<node CREATED="1450102818363" FOLDED="true" ID="ID_483" MODIFIED="1450102818363" TEXT="Adjective"/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_484" MODIFIED="1450102818363" TEXT="..."/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_485" MODIFIED="1450102818363" TEXT="Help on tags">
<node CREATED="1450102818363" FOLDED="true" ID="ID_486" MODIFIED="1450102818363" TEXT="nltk.help.upenn_tagset(&apos;RB&apos;)"/>
<node CREATED="1450102818363" FOLDED="true" ID="ID_487" MODIFIED="1450102818363" TEXT="nltk.help.upenn_tagset(&apos;NN.*&apos;)">
<node CREATED="1450102818363" FOLDED="true" ID="ID_488" MODIFIED="1450102818363" TEXT="Regex"/>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_489" MODIFIED="1450102818363" TEXT="nltk.corpus.[corpus].readme()">
<node CREATED="1450102818363" FOLDED="true" ID="ID_490" MODIFIED="1450102818363" TEXT="Info on how [corpus] is constructed, including tagging convention if applicable"/>
</node>
</node>
<node CREATED="1450102818363" ID="ID_645" MODIFIED="1450102818363" TEXT="The choice of tags is a very important one">
<node CREATED="1450102818363" ID="ID_646" MODIFIED="1450102818363" TEXT="How finely to classify tokens is a choice"/>
<node CREATED="1450102818363" ID="ID_647" MODIFIED="1450102818363" TEXT="There is no &apos;best tagset&apos;">
<node CREATED="1450102818363" ID="ID_648" MODIFIED="1450102818363" TEXT="It depends on the objective"/>
</node>
</node>
</node>
<node CREATED="1450102818363" FOLDED="true" ID="ID_491" MODIFIED="1450102818363" TEXT="Representation of tagged words">
<node CREATED="1450102818363" FOLDED="true" ID="ID_492" MODIFIED="1450102818363" TEXT="&apos;Standard&apos;">
<node CREATED="1450102818363" FOLDED="true" ID="ID_493" MODIFIED="1450102818363" TEXT="String &apos;[word]/[tag]&apos;"/>
</node>
<node CREATED="1450102818364" FOLDED="true" ID="ID_494" MODIFIED="1450102818364" TEXT="NLTK">
<node CREATED="1450102818364" FOLDED="true" ID="ID_495" MODIFIED="1450102818364" TEXT="Tuple (&apos;[word]&apos;, &apos;[tag]&apos;)"/>
</node>
<node CREATED="1450102818364" FOLDED="true" ID="ID_496" MODIFIED="1450102818364" TEXT="(&apos;[word]&apos;, &apos;[tag]&apos;) = nltk.tag.str2tuple(&apos;[word]/[tag]&apos;)"/>
</node>
<node CREATED="1450102818364" ID="ID_497" MODIFIED="1450102818364" TEXT="Retrieval of tags from corpus">
<node CREATED="1450102818364" FOLDED="true" ID="ID_498" MODIFIED="1450102818364" TEXT="nltk.corpus.[corpus].tagged_words()"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_499" MODIFIED="1450102818364" TEXT="nltk.corpus.[corpus].tagged_words(tagset=&apos;universal&apos;)"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_500" MODIFIED="1450102818364" TEXT="nltk.corpus.[corpus].tagged_sents()"/>
</node>
<node CREATED="1450102818364" ID="ID_460" MODIFIED="1450102818364" TEXT="Techniques">
<node CREATED="1450102818364" FOLDED="true" ID="ID_461" MODIFIED="1450102818364" TEXT="Sequence labeling"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_462" MODIFIED="1450102818364" TEXT="n-gram models"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_463" MODIFIED="1450102818364" TEXT="Backoff"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_464" MODIFIED="1450102818364" TEXT="Evaluation"/>
<node CREATED="1450102818364" FOLDED="true" ID="ID_465" MODIFIED="1450102818364" TEXT="..."/>
<node CREATED="1450102818364" ID="ID_466" MODIFIED="1450102818364" TEXT="Simplest tagger">
<node CREATED="1450102818364" FOLDED="true" ID="ID_467" MODIFIED="1450102818364" TEXT="nltk.pos_tag([tokenized_text])"/>
</node>
</node>
<node CREATED="1450102818364" ID="ID_546" MODIFIED="1450102818364" TEXT="Automatic tagging">
<node CREATED="1450102818364" ID="ID_579" MODIFIED="1450102818364" TEXT="Evaluating taggers">
<node CREATED="1450102818364" ID="ID_580" MODIFIED="1450102818364" TEXT="Cross check a tagger&apos;s performance against a manually tagged text body">
<node CREATED="1450102818364" ID="ID_581" MODIFIED="1450102818364" TEXT="Note manual tagging is not error proof"/>
</node>
<node CREATED="1450102818364" ID="ID_582" MODIFIED="1450102818364" TEXT="[tagger].evaluate([tagged_tokens])">
<node CREATED="1450102818364" ID="ID_584" MODIFIED="1450102818364" TEXT="% of correctly tagged tokens"/>
</node>
<node CREATED="1450102818365" ID="ID_583" MODIFIED="1450102818365" TEXT="nltk.ConfusionMatrix([set_1_tags], [set_2_tags])">
<node CREATED="1450102818365" ID="ID_585" MODIFIED="1450102818365" TEXT="Matrix of set_1 against set_2 number of tags"/>
<node CREATED="1450102818365" ID="ID_586" MODIFIED="1450102818365" TEXT="Usually &apos;set_1&apos; and &apos;set_2&apos; are &apos;correct&apos; and &apos;computed&apos;"/>
</node>
</node>
<node CREATED="1450102818365" ID="ID_547" MODIFIED="1450102818365" TEXT="Default taggers">
<node CREATED="1450102818365" FOLDED="true" ID="ID_548" MODIFIED="1450102818365" TEXT="Tags every word with the same tag"/>
<node CREATED="1450102818365" ID="ID_549" MODIFIED="1450102818365" TEXT="Weak overall performance">
<node CREATED="1450102818365" ID="ID_552" MODIFIED="1450102818365" TEXT="10-15%"/>
</node>
<node CREATED="1450102818365" ID="ID_550" MODIFIED="1450102818365" TEXT="Interesting as an addition to mature taggers for words that have never been encountered">
<node CREATED="1450102818365" ID="ID_565" MODIFIED="1450102818365" TEXT="Technique known as &apos;backoff&apos;"/>
<node CREATED="1450102818365" ID="ID_551" MODIFIED="1450102818365" TEXT="These tend to be nouns"/>
</node>
<node CREATED="1450102818365" ID="ID_553" MODIFIED="1450102818365" TEXT="default_tagger = nltk.DefaultTagger(&apos;NN&apos;)">
<node CREATED="1450102818365" ID="ID_554" MODIFIED="1450102818365" TEXT="default_tagger.tag([tokens])">
<node CREATED="1450102818365" ID="ID_555" MODIFIED="1450102818365" TEXT="List of tagged words in [tokens]"/>
</node>
<node CREATED="1450102818365" ID="ID_556" MODIFIED="1450102818365" TEXT="default_tagger.evaluate([tagged_tokens])">
<node CREATED="1450102818365" ID="ID_557" MODIFIED="1450102818365" TEXT="Performance of the tagger"/>
</node>
</node>
</node>
<node CREATED="1450102818365" ID="ID_558" MODIFIED="1450102818365" TEXT="Regexp taggers">
<node CREATED="1450102818365" ID="ID_559" MODIFIED="1450102818365" TEXT="Tags using a list of tuples, each containing a regex and a tag"/>
<node CREATED="1450102818365" ID="ID_561" MODIFIED="1450102818365" TEXT="Still weak performance">
<node CREATED="1450102818365" ID="ID_562" MODIFIED="1450102818365" TEXT="20-25%"/>
</node>
<node CREATED="1450102818365" ID="ID_560" MODIFIED="1450102818365">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>patterns = [</p>
                                        <p>(r'.*ing$', 'VBG'),               # gerunds</p>
                                        <p>(r'.*ed$', 'VBD'),                # simple past</p>
                                        <p>(r'.*es$', 'VBZ'),                # 3rd singular present</p>
                                        <p>(r'.*ould$', 'MD'),               # modals</p>
                                        <p>(r'.*\'s$', 'NN$'),               # possessive nouns</p>
                                        <p>(r'.*s$', 'NNS'),                 # plural nouns</p>
                                        <p>(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers</p>
                                        <p>(r'.*', 'NN')                     # nouns (default)</p>
                                        <p>]</p>
                                        <p>regexp_tagger = nltk.RegexpTagger(patterns)</p>
                                    </body>
                                </html></richcontent>
</node>
</node>
<node CREATED="1450102818366" ID="ID_566" MODIFIED="1450102818366" TEXT="Lookup taggers/Unigram taggers">
<node CREATED="1450102818366" ID="ID_567" MODIFIED="1450102818366" TEXT="Tag tokens using a dictionary of tokens and their associated tag">
<node CREATED="1450102818366" ID="ID_568" MODIFIED="1450102818366" TEXT="Should be the most frequent tokens and their most likely tag"/>
</node>
<node CREATED="1450102818366" ID="ID_569" MODIFIED="1450102818366" TEXT="Performance depends on model size">
<node CREATED="1450102818366" ID="ID_570" MODIFIED="1450102818366" TEXT="From 50% to 90% for models containing from 100 to 10k words"/>
</node>
<node CREATED="1450102818366" ID="ID_649" MODIFIED="1450102818366" TEXT="Training">
<node CREATED="1450102818366" ID="ID_651" MODIFIED="1450102818366" TEXT="baseline_tagger = nltk.UnigramTagger([list_of_tagged_sentences])"/>
<node CREATED="1450102818366" ID="ID_571" MODIFIED="1450102818366" TEXT="baseline_tagger = nltk.UnigramTagger(model=[dict_of_words_and_tags])"/>
</node>
<node CREATED="1450102818366" ID="ID_573" MODIFIED="1450102818366" TEXT="Accepts the definition of a backoff">
<node CREATED="1450102818366" ID="ID_572" MODIFIED="1450102818366" TEXT="baseline_tagger = nltk.UnigramTagger(model=[dict_of_words_and_tags], backoff=nltk.DefaultTagger(&apos;NN&apos;))"/>
</node>
</node>
<node CREATED="1450102818366" ID="ID_574" MODIFIED="1450102818366" TEXT="N-gram taggers">
<node CREATED="1450102818366" ID="ID_575" MODIFIED="1450102818366" TEXT="Tag N-grams using a dictionary of N-grams and their associated tags">
<node CREATED="1450102818366" ID="ID_576" MODIFIED="1450102818366" TEXT="Should be the most frequent N-grams and their most likely tags"/>
</node>
<node CREATED="1450102818367" ID="ID_577" MODIFIED="1450102818367" TEXT="Actually, N-grams are not really used">
<node CREATED="1450102818367" ID="ID_578" MODIFIED="1450102818367" TEXT="The keys are composed by the token being tagged and the POSs of the n-1 tokens before it"/>
<node CREATED="1450102818367" ID="ID_587" MODIFIED="1450102818367" TEXT="Only backward looking">
<node CREATED="1450102818367" ID="ID_594" MODIFIED="1450102818367" TEXT="Sentence boundaries should not be crossed"/>
</node>
<node CREATED="1450102818367" ID="ID_588" MODIFIED="1450102818367" TEXT="No weighting of different potential solutions"/>
</node>
<node CREATED="1450102818367" ID="ID_589" MODIFIED="1450102818367" TEXT="The higher the N, the higher the probability of a certain key not having been found in the training set">
<node CREATED="1450102818367" ID="ID_590" MODIFIED="1450102818367" TEXT="As soon as an unknown word is found (for example), the tagger fails"/>
<node CREATED="1450102818367" ID="ID_591" MODIFIED="1450102818367" TEXT="This is the sparse data problem"/>
<node CREATED="1450102818367" ID="ID_592" MODIFIED="1450102818367" TEXT="There is a tradeoff between accuracy and coverage">
<node CREATED="1450102818367" ID="ID_593" MODIFIED="1450102818367" TEXT="A version of the precission/recall tradeoff"/>
</node>
</node>
</node>
<node CREATED="1450102818367" ID="ID_595" MODIFIED="1450102818367" TEXT="Combined taggers">
<node CREATED="1450102818367" ID="ID_596" MODIFIED="1450102818367" TEXT="Begin with N-gram">
<node CREATED="1450102818367" ID="ID_597" MODIFIED="1450102818367" TEXT="If N-gram fails, backoff to N-1-gram">
<node CREATED="1450102818367" ID="ID_598" MODIFIED="1450102818367" TEXT="If N-1-gram fails, backoff to N-2-gram">
<node CREATED="1450102818367" ID="ID_599" MODIFIED="1450102818367" TEXT="...etc"/>
</node>
</node>
</node>
<node CREATED="1450102818367" ID="ID_601" MODIFIED="1450102818367" TEXT="Backoff taggers can be nested"/>
<node CREATED="1450102818367" ID="ID_600" MODIFIED="1450102818367">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>t0 = nltk.DefaultTagger('NN')</p>
                                        <p>t1 = nltk.UnigramTagger(train_sents, backoff=t0)</p>
                                        <p>t2 = nltk.BigramTagger(train_sents, backoff=t1)</p>
                                        <p>t2.evaluate(test_sents)</p>
                                    </body>
                                </html></richcontent>
<node CREATED="1450102818368" ID="ID_602" MODIFIED="1450102818368" TEXT="t0 could be improved">
<node CREATED="1450102818368" ID="ID_603" MODIFIED="1450102818368" TEXT="Selecting a finite vocabulary and substituting all other tokens by an unknown flag">
<node CREATED="1450102818368" ID="ID_604" MODIFIED="1450102818368" TEXT="E.g., &apos;UNK&apos;"/>
</node>
<node CREATED="1450102818368" ID="ID_605" MODIFIED="1450102818368" TEXT="This allows the N-grams to be trained on the infrequent tokens"/>
<node CREATED="1450102818368" ID="ID_606" MODIFIED="1450102818368" TEXT="When an unknown word (i.e., not in the vocabulary) is found, it is searched using the flag instead"/>
</node>
</node>
</node>
<node CREATED="1450102818368" ID="ID_614" MODIFIED="1450102818368" TEXT="Transformation taggers">
<node CREATED="1450102818368" ID="ID_615" MODIFIED="1450102818368" TEXT="N-gram systems have issues">
<node CREATED="1450102818368" ID="ID_620" MODIFIED="1450102818368" TEXT="Size">
<node CREATED="1450102818368" ID="ID_616" MODIFIED="1450102818368" TEXT="They require humongous lookup tables"/>
</node>
<node CREATED="1450102818368" ID="ID_621" MODIFIED="1450102818368" TEXT="Context">
<node CREATED="1450102818368" ID="ID_622" MODIFIED="1450102818368" TEXT="They look only leftwards"/>
<node CREATED="1450102818368" ID="ID_623" MODIFIED="1450102818368" TEXT="They need to have seen the context before"/>
</node>
<node CREATED="1450102818369" ID="ID_625" MODIFIED="1450102818369" TEXT="Basically, they are &apos;bottom up&apos;"/>
</node>
<node CREATED="1450102818369" ID="ID_617" MODIFIED="1450102818369" TEXT="Different approach">
<node CREATED="1450102818369" ID="ID_624" MODIFIED="1450102818369" TEXT="Top down">
<node CREATED="1450102818369" ID="ID_627" MODIFIED="1450102818369" TEXT="Start broad and refine using learned rules"/>
</node>
<node CREATED="1450102818369" ID="ID_626" MODIFIED="1450102818369" TEXT="Learn rules from data so that applying the rules results in the highest increase in accuracy">
<node CREATED="1450102818369" ID="ID_628" MODIFIED="1450102818369" TEXT="Build a decision tree"/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1450102818369" FOLDED="true" ID="ID_501" MODIFIED="1450102818369" TEXT="Dictionaries">
<node CREATED="1450102818369" FOLDED="true" ID="ID_502" MODIFIED="1450102818369" TEXT="Also called hash arrays or associative arrays"/>
<node CREATED="1450102818369" ID="ID_503" MODIFIED="1450102818369" TEXT="Can be created in many ways">
<node CREATED="1450102818369" FOLDED="true" ID="ID_504" MODIFIED="1450102818369" TEXT="my_dict = {&apos;colorless&apos;: &apos;ADJ&apos;, &apos;ideas&apos;: &apos;N&apos;, &apos;sleep&apos;: &apos;V&apos;, &apos;furiously&apos;: &apos;ADV&apos;}"/>
<node CREATED="1450102818369" FOLDED="true" ID="ID_505" MODIFIED="1450102818369" TEXT="my_dict = dict(colorless=&apos;ADJ&apos;, ideas=&apos;N&apos;, sleep=&apos;V&apos;, furiously=&apos;ADV&apos;)"/>
<node CREATED="1450102818369" FOLDED="true" ID="ID_506" MODIFIED="1450102818369" TEXT="my_dict = collections.defaultdict(str, colorless=&apos;ADJ&apos;, ideas=&apos;N&apos;, sleep=&apos;V&apos;, furiously=&apos;ADV&apos;)">
<node CREATED="1450102818370" FOLDED="true" ID="ID_507" MODIFIED="1450102818370" TEXT="If an unknown entry is requested, a new one will be created using the output of &apos;str&apos;"/>
<node CREATED="1450102818370" FOLDED="true" ID="ID_508" MODIFIED="1450102818370" TEXT="In this case, the default value is an empty string"/>
</node>
<node CREATED="1450102818370" FOLDED="true" ID="ID_509" MODIFIED="1450102818370" TEXT="my_dict = collections.defaultdict(lambda: &apos;NOUN&apos;)">
<node CREATED="1450102818370" FOLDED="true" ID="ID_510" MODIFIED="1450102818370" TEXT="In this case, the default value is the output of the lambda function, i.e. &apos;NOUN&apos;"/>
</node>
<node CREATED="1450102818370" FOLDED="true" ID="ID_511" MODIFIED="1450102818370" TEXT="nltk.Index([list of tuples])">
<node CREATED="1450102818370" FOLDED="true" ID="ID_512" MODIFIED="1450102818370" TEXT="Creates a dictionary-like object"/>
<node CREATED="1450102818370" FOLDED="true" ID="ID_513" MODIFIED="1450102818370" TEXT="The keys are the firs element of the tuples"/>
<node CREATED="1450102818370" FOLDED="true" ID="ID_514" MODIFIED="1450102818370" TEXT="The values are lists aggregating all the second elements of the tuples by key"/>
</node>
<node CREATED="1450102818370" FOLDED="true" ID="ID_515" MODIFIED="1450102818370" TEXT="nltk.FreqDist([list of words])">
<node CREATED="1450102818370" FOLDED="true" ID="ID_516" MODIFIED="1450102818370" TEXT="Creates a dictionary-like object"/>
<node CREATED="1450102818370" FOLDED="true" ID="ID_517" MODIFIED="1450102818370" TEXT="The keys are the words"/>
<node CREATED="1450102818370" FOLDED="true" ID="ID_518" MODIFIED="1450102818370" TEXT="The values are the number of times each word is encountered"/>
</node>
</node>
<node CREATED="1450102818371" ID="ID_519" MODIFIED="1450102818371" TEXT="Keys can be fairly complex">
<node CREATED="1450102818371" ID="ID_520" MODIFIED="1450102818371">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>my_dict = collections.defaultdict(lambda: collections.defaultdict(int))</p>
                                    <p>brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')</p>
                                    <p>for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):</p>
                                    <p>my_dict[(t1, w2)][t2] += 1</p>
                                    <p>my_dict[('DET', 'right')]</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818371" ID="ID_521" MODIFIED="1450102818371" TEXT="defaultdict(&lt;class &apos;int&apos;&gt;, {&apos;ADJ&apos;: 11, &apos;NOUN&apos;: 5})"/>
<node CREATED="1450102818371" ID="ID_525" MODIFIED="1450102818371" TEXT="The keys of the outer dictionary are tuples ([POS_of_word_i-1], [word_i] )"/>
<node CREATED="1450102818371" ID="ID_524" MODIFIED="1450102818371" TEXT="The values of the outer dictionary are dictionaries with default value an integer"/>
<node CREATED="1450102818371" ID="ID_526" MODIFIED="1450102818371" TEXT="The keys of the inner dictionary are [POS_of_word]"/>
<node CREATED="1450102818371" ID="ID_527" MODIFIED="1450102818371" TEXT="The values of the inner dictionary are counts"/>
</node>
</node>
<node CREATED="1450102818371" ID="ID_532" MODIFIED="1450102818371" TEXT="Inversion">
<node CREATED="1450102818372" ID="ID_533" MODIFIED="1450102818372" TEXT="Very few times: just look them up">
<node CREATED="1450102818372" ID="ID_534" MODIFIED="1450102818372" TEXT="[ key for (key, value) in my_dict.items() if value == my_val ]"/>
</node>
<node CREATED="1450102818372" ID="ID_536" MODIFIED="1450102818372" TEXT="Often: construct an inverse dictionary">
<node CREATED="1450102818372" ID="ID_538" MODIFIED="1450102818372" TEXT="Values are not repeated">
<node CREATED="1450102818372" ID="ID_541" MODIFIED="1450102818372" TEXT="inv_my_dict = dict( (value, key) for (key, value) in my_dict.items() )"/>
</node>
<node CREATED="1450102818372" ID="ID_542" MODIFIED="1450102818372" TEXT="Values are repeated">
<node CREATED="1450102818372" ID="ID_543" MODIFIED="1450102818372">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>inv_my_dict = collections.defaultdict(list)</p>
                                            <p>for key, value in my_dict.items():</p>
                                            <p>inv_my_dict[value].append(key)</p>
                                        </body>
                                    </html></richcontent>
</node>
<node CREATED="1450102818372" ID="ID_544" MODIFIED="1450102818372" TEXT="NLTK to the rescue!">
<node CREATED="1450102818372" ID="ID_545" MODIFIED="1450102818372" TEXT="inv_my_dict = nltk.Index( (value, key) for (key, value) in my_dict.items() )"/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1450102818372" FOLDED="true" ID="ID_607" MODIFIED="1450102818372" TEXT="Saving and retrieving data structures, e.g., trained taggers">
<node CREATED="1450102818373" ID="ID_608" MODIFIED="1450102818373" TEXT="Save">
<node CREATED="1450102818373" ID="ID_610" MODIFIED="1450102818373">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>import pickle</p>
                                    <p>output = open('tagger.pkl', 'wb')</p>
                                    <p>pickle.dump([tagger], output, -1)</p>
                                    <p>output.close()</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818373" ID="ID_609" MODIFIED="1450102818373" TEXT="Retrieve">
<node CREATED="1450102818373" ID="ID_613" MODIFIED="1450102818373">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>import pickle</p>
                                    <p>input = open('tagger.pkl', 'rb')</p>
                                    <p>pickle.load(input)</p>
                                    <p>input.close()</p>
                                </body>
                            </html></richcontent>
</node>
</node>
</node>
</node>
<node CREATED="1450102818373" FOLDED="true" ID="ID_652" MODIFIED="1453699454021" POSITION="right" TEXT="6. Learning to Classify Text">
<node CREATED="1450102818374" FOLDED="true" ID="ID_653" MODIFIED="1453699451235" TEXT="Classification">
<node CREATED="1450102818374" ID="ID_654" MODIFIED="1450102818374" TEXT="Choosing the right class label for an input"/>
<node CREATED="1450102818374" ID="ID_657" MODIFIED="1450102818374" TEXT="Basic classification">
<node CREATED="1450102818374" FOLDED="true" ID="ID_655" MODIFIED="1450102818374" TEXT="Inputs are independent"/>
<node CREATED="1450102818374" ID="ID_656" MODIFIED="1450102818374" TEXT="The set of labels is known a priori"/>
</node>
<node CREATED="1450102818374" ID="ID_658" MODIFIED="1450102818374" TEXT="There are many other types">
<node CREATED="1450102818374" ID="ID_659" MODIFIED="1450102818374" TEXT="Multi-label classification">
<node CREATED="1450102818374" ID="ID_664" MODIFIED="1450102818374" TEXT="Inputs may be assigned multiple labels"/>
</node>
<node CREATED="1450102818374" ID="ID_660" MODIFIED="1450102818374" TEXT="Open-class classification">
<node CREATED="1450102818374" ID="ID_663" MODIFIED="1450102818374" TEXT="The set of labels is not known a priori"/>
</node>
<node CREATED="1450102818374" ID="ID_661" MODIFIED="1450102818374" TEXT="Sequence classification">
<node CREATED="1450102818374" ID="ID_662" MODIFIED="1450102818374" TEXT="Group of inputs are classified jointly"/>
</node>
</node>
<node CREATED="1450102818374" FOLDED="true" ID="ID_665" MODIFIED="1450104257373" TEXT="Supervised/Unsupervised">
<node CREATED="1450102818374" ID="ID_666" MODIFIED="1450102818374" TEXT="Supervised">
<node CREATED="1450102818374" ID="ID_667" MODIFIED="1450102818374" TEXT="A training corpora is available with correct labels"/>
<node CREATED="1450102818374" ID="ID_670" MODIFIED="1450102818374" TEXT="[Known input] + [Correct labels]">
<node CREATED="1450102818374" ID="ID_673" MODIFIED="1450102818374" TEXT="Pass [Known input] through a Feature_Extractor()">
<node CREATED="1450102818375" ID="ID_671" MODIFIED="1450102818375" TEXT="[Input features] + [Correct labels]">
<node CREATED="1450102818375" ID="ID_672" MODIFIED="1450102818375" TEXT="Pass through Machine_Learning_Algoryithm()">
<node CREATED="1450102818375" ID="ID_674" MODIFIED="1450102818375" TEXT="Classifier_Model()"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818375" ID="ID_675" MODIFIED="1450102818375" TEXT="[Unknown input]">
<node CREATED="1450102818375" ID="ID_676" MODIFIED="1450102818375" TEXT="Pass [Unknown input] through the Feature_Extractor()">
<node CREATED="1450102818375" ID="ID_677" MODIFIED="1450102818375" TEXT="[Input features]">
<node CREATED="1450102818375" ID="ID_678" MODIFIED="1450102818375" TEXT="Pass through Classifier_Model()">
<node CREATED="1450102818375" ID="ID_679" MODIFIED="1450102818375" TEXT="[Estimated labels]"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818375" ID="ID_680" MODIFIED="1450102818375" TEXT="Feature extractors are usually coded as functions">
<node CREATED="1450102818375" ID="ID_681" MODIFIED="1450102818375" TEXT="They usually return dictionaries of features with their values for the specific input"/>
</node>
<node CREATED="1450102818375" ID="ID_742" MODIFIED="1450102818375" TEXT="Examples">
<node CREATED="1450102818375" ID="ID_743" MODIFIED="1450102818375" TEXT="Classify names as male or female">
<node CREATED="1450102818375" ID="ID_744" MODIFIED="1450102818375" TEXT="Corpus of previously classified names"/>
<node CREATED="1450102818375" ID="ID_745" MODIFIED="1450102818375" TEXT="Features extracted from the names"/>
</node>
<node CREATED="1450102818376" ID="ID_747" MODIFIED="1450102818376" TEXT="Assign words to their POS independently">
<node CREATED="1450102818376" ID="ID_748" MODIFIED="1450102818376" TEXT="Corpus of tagged words"/>
<node CREATED="1450102818376" ID="ID_749" MODIFIED="1450102818376" TEXT="Features extracted from the words"/>
<node CREATED="1450102818376" ID="ID_751" MODIFIED="1450102818376" TEXT="Similar to a regexp tagger that learns the best rules on its own"/>
</node>
<node CREATED="1450102818376" ID="ID_752" MODIFIED="1450102818376" TEXT="Assign words to their POS in context">
<node CREATED="1450102818376" ID="ID_755" MODIFIED="1450102818376" TEXT="Corpus of tagged sentences"/>
<node CREATED="1450102818376" ID="ID_757" MODIFIED="1450102818376" TEXT="Features extracted from the words and the surrounding words">
<node CREATED="1450102818376" ID="ID_760" MODIFIED="1450102818376" TEXT="Can include the POS of the surrounding words, if known"/>
</node>
</node>
<node CREATED="1450103592189" ID="ID_1369343308" MODIFIED="1450104001008" TEXT="Segmenting text into sentences">
<node CREATED="1450103698608" ID="ID_279493514" MODIFIED="1450103708967" TEXT="Corpus of text segmented into sentences"/>
<node CREATED="1450103709486" ID="ID_257433435" MODIFIED="1450103770131" TEXT="Features including segmentor symbols and properties of the surrounding words">
<node CREATED="1450103771394" ID="ID_652931212" MODIFIED="1450103780067" TEXT="Word length"/>
<node CREATED="1450103780589" ID="ID_616574307" MODIFIED="1450103785541" TEXT="Capitalized or not"/>
</node>
</node>
<node CREATED="1450103796936" ID="ID_812857037" MODIFIED="1450103965695" TEXT="Identify dialog act types">
<node CREATED="1450103874085" ID="ID_1956869713" MODIFIED="1450103888131" TEXT="Corpus of pretagged chat sentences">
<node CREATED="1450103917635" ID="ID_1663261082" MODIFIED="1450103919064" TEXT="nltk.corpus.nps_chat.xml_posts()"/>
</node>
<node CREATED="1450103967356" ID="ID_506271974" MODIFIED="1450103989177" TEXT="Features can be the words in the chat sentence"/>
</node>
<node CREATED="1450104002799" ID="ID_647725177" MODIFIED="1450104019160" TEXT="Recognizing textual entailment">
<node CREATED="1450104032238" ID="ID_1564590402" MODIFIED="1450104055744" TEXT="Determining whether a given piece of text T entails another text H (called the &quot;hypothesis&quot;)"/>
<node CREATED="1450104078638" ID="ID_1168703016" MODIFIED="1450104197416" TEXT="Corpus of pairs of T, H and whether T entails H or not"/>
<node CREATED="1450104204608" ID="ID_993516900" MODIFIED="1450104227930" TEXT="Quite difficult problem - some feature extractors exist but do not perform that well">
<node CREATED="1450104243471" ID="ID_1175805511" MODIFIED="1450104248208" TEXT="nltk.RTEFeatureExtractor([rtepair])"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818376" ID="ID_668" MODIFIED="1450102818376" TEXT="Unsupervised">
<node CREATED="1450102818376" ID="ID_669" MODIFIED="1450102818376" TEXT="Such corpora is not available"/>
</node>
</node>
</node>
<node CREATED="1450102818376" FOLDED="true" ID="ID_682" MODIFIED="1453699448574" TEXT="Techniques">
<node CREATED="1450102818378" ID="ID_726" MODIFIED="1450195299666" TEXT="Decision Tree">
<node CREATED="1450102818378" ID="ID_727" MODIFIED="1450102818378">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>def POS_features(word):</p>
                                    <p>features = {}</p>
                                    <p>for suffix in common_suffixes:</p>
                                    <p>features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)</p>
                                    <p>return features</p>
                                    <p>suffix_fdist = nltk.FreqDist()</p>
                                    <p>for word in nltk.corpus.brown.words():</p>
                                    <p>word = word.lower()</p>
                                    <p>suffix_fdist[word[-1:]] += 1</p>
                                    <p>suffix_fdist[word[-2:]] += 1</p>
                                    <p>suffix_fdist[word[-3:]] += 1</p>
                                    <p>common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]</p>
                                    <p>tagged_words = nltk.corpus.brown.tagged_words(categories='news')</p>
                                    <p>featuresets = [(POS_features(n), g) for (n,g) in tagged_words]</p>
                                    <p>size = int(len(featuresets) * 0.1)</p>
                                    <p>train_set, test_set = featuresets[size:], featuresets[:size]</p>
                                    <p>classifier = nltk.DecisionTreeClassifier.train(train_set)</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818379" ID="ID_728" MODIFIED="1450102818379" TEXT="nltk.classify.accuracy(classifier, test_set)">
<node CREATED="1450102818379" ID="ID_729" MODIFIED="1450102818379" TEXT="0.63"/>
</node>
<node CREATED="1450102818379" ID="ID_730" MODIFIED="1450102818379" TEXT="classifier.classify(POS_features(&apos;cats&apos;))">
<node CREATED="1450102818379" ID="ID_731" MODIFIED="1450102818379" TEXT="&apos;NNS&apos;"/>
</node>
<node CREATED="1450102818379" ID="ID_732" MODIFIED="1450102818379" TEXT="classifier.pseudocode(depth=3)">
<node CREATED="1450102818379" ID="ID_737" MODIFIED="1450102818379">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>if endswith(the) == True: return 'AT'</p>
                                            <p>if endswith(the) == False:</p>
                                            <p>if endswith(,) == True: return ','</p>
                                            <p>if endswith(,) == False:</p>
                                            <p>if endswith(s) == False: return '.'</p>
                                            <p>if endswith(s) == True: return 'PP$'</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
<node CREATED="1450102818380" ID="ID_739" MODIFIED="1450102818380" TEXT="To add context to this classifier, a different feature constructor could be used">
<node CREATED="1450102818380" ID="ID_740" MODIFIED="1450102818380">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>def POS_features(sentence, i):</p>
                                            <p>features = {"suffix(1)": sentence[i][-1:],</p>
                                            <p>"suffix(2)": sentence[i][-2:],</p>
                                            <p>"suffix(3)": sentence[i][-3:]}</p>
                                            <p>if i == 0:</p>
                                            <p>features["prev-word"] = "&lt;START&gt;"</p>
                                            <p>else:</p>
                                            <p>features["prev-word"] = sentence[i-1]</p>
                                            <p>return features</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450105746938" ID="ID_184025150" MODIFIED="1450107141389" TEXT="Some theory">
<node CREATED="1450105753147" ID="ID_125337870" MODIFIED="1450105761344" TEXT="Naive top down approach">
<node CREATED="1450106036662" ID="ID_824693389" MODIFIED="1450106214993" TEXT="For any given set, choose as stump the feature that when used to classify most increases accuracy"/>
<node CREATED="1450106138978" ID="ID_591071870" MODIFIED="1450106161954" TEXT="Repeat until desired accuracy has been reached"/>
<node CREATED="1450106146223" ID="ID_1181395824" MODIFIED="1450106151156" TEXT="Prune as needed"/>
</node>
<node CREATED="1450106192897" ID="ID_133635716" MODIFIED="1450106201043" TEXT="Stump selection">
<node CREATED="1450106232147" ID="ID_1541228906" MODIFIED="1450106236657" TEXT="Information gain">
<node CREATED="1450106253501" ID="ID_127931011" MODIFIED="1450106293948" TEXT="Entropy reduction">
<node CREATED="1450106650073" ID="ID_1007388277" MODIFIED="1450106665579" TEXT="Entropy before applying the stump and after">
<node CREATED="1450106669922" ID="ID_92993485" MODIFIED="1450106729166" TEXT="The &apos;after&apos; requires averaging leaf entropy values weighted by the number of samples in each leaf"/>
</node>
</node>
<node CREATED="1450106456976" ID="ID_686435982" MODIFIED="1450106458353" TEXT="Entropy">
<node CREATED="1450106497531" ID="ID_380983416" MODIFIED="1450106514180" TEXT="Measure of how variable a feature is in a given set of subjects"/>
<node CREATED="1450106473813" ID="ID_1169034905" MODIFIED="1450106489165" TEXT="Measure of how much information can be extracted from a feature">
<node CREATED="1450106519936" ID="ID_1911532222" MODIFIED="1450106583527" TEXT="If everyone is labeled as A on feature F...">
<node CREATED="1450106604401" ID="ID_227228137" MODIFIED="1450106607416" TEXT="Feature F is useless for classification purposes"/>
<node CREATED="1450106584878" ID="ID_1228836341" MODIFIED="1450106604094" TEXT="The entropy of feature F is 0"/>
</node>
</node>
<node CREATED="1450106294976" ID="ID_597916162" MODIFIED="1450106471867" TEXT="Sum of the probability of each label times the log probability of that same label"/>
<node CREATED="1450106356569" ID="ID_696243335" MODIFIED="1450106446088" TEXT="def entropy(labels):&#xa;&#x9;import math&#xa;&#x9;freqdist = nltk.FreqDist(labels)&#xa;&#x9;probs = [ freqdist.freq(l) for l in freqdist ]&#xa;&#x9;return -sum( [ p * math.log(p,2) for p in probs ] )"/>
</node>
</node>
</node>
<node CREATED="1450106782356" ID="ID_1489612507" MODIFIED="1450106788619" TEXT="Benefits">
<node CREATED="1450106789901" ID="ID_1849967911" MODIFIED="1450106796604" TEXT="Easy to interpret"/>
</node>
<node CREATED="1450106799846" ID="ID_643710762" MODIFIED="1450106802579" TEXT="Drawbacks">
<node CREATED="1450106804472" ID="ID_1756228455" MODIFIED="1450106829961" TEXT="As the training set gets segmented, its size is reduced">
<node CREATED="1450106831162" ID="ID_1685949905" MODIFIED="1450106851819" TEXT="Will eventually lead to overfitting"/>
</node>
<node CREATED="1450106915386" ID="ID_1855220390" MODIFIED="1450106943438" TEXT="They force features to be checked in a specific order">
<node CREATED="1450106945468" ID="ID_1184071827" MODIFIED="1450106954501" TEXT="This is not always the best strategy">
<node CREATED="1450106956356" ID="ID_586644986" MODIFIED="1450107016621" TEXT="When classifying documents into topics, the presence of &apos;football&apos; may be a strong indicator of the document being sports"/>
<node CREATED="1450107017377" ID="ID_1258870663" MODIFIED="1450107028715" TEXT="However, there is very little space at the top of the tree"/>
<node CREATED="1450107031188" ID="ID_832483935" MODIFIED="1450107052140" TEXT="This leads to duplicaton of strong features in sevral branches of the tree"/>
</node>
</node>
<node CREATED="1450107066939" ID="ID_1957587336" MODIFIED="1450107085896" TEXT="Weak predictors which would make sense at a global level never make it into the decision tree">
<node CREATED="1450107086914" ID="ID_771327545" MODIFIED="1450107117228" TEXT="By the time they grab some attention, the size of the segments is too small"/>
</node>
</node>
</node>
</node>
<node CREATED="1450102818376" ID="ID_683" MODIFIED="1450109035574" TEXT="Naive Bayes">
<node CREATED="1450102818377" ID="ID_684" MODIFIED="1450102818377">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>import random</p>
                                    <p>def gender_features(word):</p>
                                    <p>return {'last_letter': word[-1]}</p>
                                    <p>labeled_names = ([(name, 'male') for name in nltk.corpus.names.words('male.txt')] +</p>
                                    <p>[(name, 'female') for name in nltk.corpus.names.words('female.txt')])</p>
                                    <p>random.shuffle(labeled_names)</p>
                                    <p>featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]</p>
                                    <p>train_set, test_set = featuresets[500:], featuresets[:500]</p>
                                    <p>classifier = nltk.NaiveBayesClassifier.train(train_set)</p>
                                    <p>classifier.classify(gender_features('Neo'))</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818377" ID="ID_685" MODIFIED="1450102818377" TEXT="classifier.classify(gender_features(&apos;Neo&apos;))">
<node CREATED="1450102818377" ID="ID_686" MODIFIED="1450102818377" TEXT="male"/>
</node>
<node CREATED="1450102818377" ID="ID_687" MODIFIED="1450102818377" TEXT="classifier.classify(gender_features(&apos;Trinity&apos;))">
<node CREATED="1450102818377" ID="ID_688" MODIFIED="1450102818377" TEXT="female"/>
</node>
<node CREATED="1450102818377" ID="ID_689" MODIFIED="1450102818377" TEXT="nltk.classify.accuracy(classifier, test_set)">
<node CREATED="1450102818378" ID="ID_690" MODIFIED="1450102818378" TEXT="0.74"/>
</node>
<node CREATED="1450102818378" ID="ID_691" MODIFIED="1450102818378" TEXT="classifier.show_most_informative_features(5)">
<node CREATED="1450102818378" ID="ID_692" MODIFIED="1450102818378">
<richcontent TYPE="NODE"><html>
                                        <head/>
                                        <body>
                                            <p>Most Informative Features</p>
                                            <p>last_letter = 'a'            female : male   =     33.2 : 1.0</p>
                                            <p>last_letter = 'k'              male : female =     32.6 : 1.0</p>
                                            <p>last_letter = 'p'              male : female =     19.7 : 1.0</p>
                                            <p>last_letter = 'v'              male : female =     18.6 : 1.0</p>
                                            <p>last_letter = 'f'              male : female =     17.3 : 1.0</p>
                                        </body>
                                    </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450107148043" ID="ID_1171272720" MODIFIED="1450107150401" TEXT="Some theory">
<node CREATED="1450107151937" ID="ID_660462599" MODIFIED="1450107166278" TEXT="Evaluates all features &apos;in parallel&apos;"/>
<node CREATED="1450107475897" ID="ID_1021549974" MODIFIED="1450107498351" TEXT="Caculates prior probabilities of the labels in the training set"/>
<node CREATED="1450107499572" ID="ID_564898745" MODIFIED="1450107532763" TEXT="Calculates how related any given feature is to a lable"/>
<node CREATED="1450107533351" ID="ID_71899521" MODIFIED="1450107571134" TEXT="Convolutes the prior probabilities and the feature contributions into a label likelihood"/>
<node CREATED="1450107582281" ID="ID_1873142709" MODIFIED="1450107684611" TEXT="Prior_P([Labels]) x Contribution(Feature_1 | [Labels]) x ... x Contribution(Feature_i | [Labels]) = Likelihood([Labels])">
<node CREATED="1450108000141" ID="ID_1840552753" MODIFIED="1450108131540" TEXT="We want to estimate P(label | features)"/>
<node CREATED="1450107987524" ID="ID_1879327457" MODIFIED="1450108128247" TEXT="P(label | features) = P(features, label)/P(features)">
<node CREATED="1450108020211" ID="ID_1475898973" MODIFIED="1450108059311" TEXT="If we only need the maximizing label, we can forget about P(features), which is a constant across labels"/>
</node>
<node CREATED="1450108060381" ID="ID_188939492" MODIFIED="1450108135256" TEXT="P(features, label) = P(label) &#xd7; P(features | label)">
<node CREATED="1450108147701" ID="ID_762964385" MODIFIED="1450108152845" TEXT="And assuming independence"/>
</node>
<node CREATED="1450108091817" ID="ID_206671696" MODIFIED="1450108116797" TEXT="P(features, label) = P(label) &#xd7; Prod[f in features] P(f | label)">
<node CREATED="1450108622144" ID="ID_1904389231" MODIFIED="1450108633989" TEXT="count(f,label)/count(label) is a good estimate for P(f | label)"/>
</node>
</node>
<node CREATED="1450107714583" ID="ID_1985658940" MODIFIED="1450108179370" TEXT="This assumes the features are independent">
<node CREATED="1450107726270" ID="ID_1490457109" MODIFIED="1450107737389" TEXT="Most likely not the case"/>
<node CREATED="1450108861119" ID="ID_8425356" MODIFIED="1450108872567" TEXT="Leads to some degree of double counting"/>
<node CREATED="1450108916661" ID="ID_704756747" MODIFIED="1450108941883" TEXT="The methodology can be modified to take this into account">
<node CREATED="1450108943414" ID="ID_992194391" MODIFIED="1450108972460" TEXT="If this is needed, it is likely that Maximum Entropy Classifiers should be used"/>
</node>
</node>
<node CREATED="1450108180297" ID="ID_746523889" MODIFIED="1450108188257" TEXT="Also, zero counts are problematic">
<node CREATED="1450108194926" ID="ID_1614080886" MODIFIED="1450108229304" TEXT="The fact that a feature was never seen in a label does not mean that it automatcally drops the probability of the label to zero"/>
<node CREATED="1450108189330" ID="ID_148370738" MODIFIED="1450108194312" TEXT="Some smoothing is necessary">
<node CREATED="1450108653454" ID="ID_1339956606" MODIFIED="1450108665821" TEXT="nltk.probability provides several smoothing techniques"/>
</node>
</node>
<node CREATED="1450108690587" ID="ID_257436165" MODIFIED="1450108703032" TEXT="Features have been assumed to be binary">
<node CREATED="1450108704157" ID="ID_1207724112" MODIFIED="1450108719408" TEXT="They can always be made binary through binning"/>
<node CREATED="1450108741157" ID="ID_1936009126" MODIFIED="1450108802599" TEXT="Also, regression models can be used on continuous features"/>
</node>
</node>
</node>
<node CREATED="1450109023238" ID="ID_216689113" MODIFIED="1450109027541" TEXT="Maximum Entropy">
<node CREATED="1450109037764" ID="ID_945391331" MODIFIED="1450109040578" TEXT="Some theory">
<node CREATED="1450109044550" ID="ID_806118176" MODIFIED="1450109069638" TEXT="Similar model to Naive Bayes...">
<node CREATED="1450109071530" ID="ID_814129962" MODIFIED="1450109124033" TEXT="...but instead of computing the probabilities independently, it searches through the whole space for the set that maximizes the performance of the classifier"/>
</node>
<node CREATED="1450109149865" ID="ID_588675205" MODIFIED="1450109168342" TEXT="Cannot be computed - must use iterative optimization"/>
<node CREATED="1450109193599" ID="ID_967448320" MODIFIED="1450109201867" TEXT="Can be very slow">
<node CREATED="1450109211860" ID="ID_854532600" MODIFIED="1450109230144" TEXT="Avoid the use of Generalized Iterative Scaling (GIS) or Improved Iterative Scaling (IIS)"/>
<node CREATED="1450109211860" ID="ID_67790912" MODIFIED="1450109244164" TEXT="Use instead the Conjugate Gradient (CG) and the BFGS optimization methods"/>
</node>
<node CREATED="1450109354435" ID="ID_1610555969" MODIFIED="1450109380037" TEXT="The user can specify which feature and label pairs are relevant">
<node CREATED="1450109421874" ID="ID_1437869090" MODIFIED="1450109454891" TEXT="Each relevant pair is called a joint-feature"/>
<node CREATED="1450109503538" ID="ID_199660899" MODIFIED="1450109534336" TEXT="In practice, most often the set of joint-features is exhaustive and maps to that used by Naive Bayes"/>
</node>
<node CREATED="1450109663681" ID="ID_617005613" MODIFIED="1450109694380" TEXT="The method searches, from all probability distributions that match the evidence, the one that maximizes entropy"/>
</node>
</node>
<node CREATED="1450109808992" ID="ID_1941099799" MODIFIED="1450109821317" TEXT="Generative vs. conditional classifiers">
<node CREATED="1450109835879" ID="ID_1229203332" MODIFIED="1450109838408" TEXT="Conditional">
<node CREATED="1450109830947" ID="ID_1684003080" MODIFIED="1450109835201" TEXT="Maximum Entropy"/>
<node CREATED="1450109900610" ID="ID_628723341" MODIFIED="1450109915219" TEXT="Computes P(label|input)"/>
<node CREATED="1450109960980" ID="ID_403386821" MODIFIED="1450109962933" TEXT="Answers">
<node CREATED="1450109966902" ID="ID_456768546" MODIFIED="1450109974070" TEXT="What is the most likely label?"/>
<node CREATED="1450109974877" ID="ID_1756473994" MODIFIED="1450109978703" TEXT="How likely is it?"/>
</node>
</node>
<node CREATED="1450109827093" ID="ID_1524742982" MODIFIED="1450109830191" TEXT="Generative">
<node CREATED="1450109860723" ID="ID_1548087218" MODIFIED="1450109935467" TEXT="Computes P(input, label)">
<node CREATED="1450109938948" ID="ID_1718619570" MODIFIED="1450109954128" TEXT="Which can be used to campute P(label|input)"/>
</node>
<node CREATED="1450109841040" ID="ID_1841718394" MODIFIED="1450109851597" TEXT="Can answer more types of questions">
<node CREATED="1450109990120" ID="ID_1215753812" MODIFIED="1450109999285" TEXT="What is the most likely input?"/>
<node CREATED="1450109999795" ID="ID_334319759" MODIFIED="1450110000941" TEXT="..."/>
</node>
<node CREATED="1450109822453" ID="ID_34115510" MODIFIED="1450109826188" TEXT="Naive Bayes"/>
</node>
<node CREATED="1450110008212" ID="ID_1887777561" MODIFIED="1450110057255" TEXT="Given that the size of the training set is fixed and the generative classifiers need to estimate more parameters, they may perform worse on the basic questions than the conditional classifiers"/>
</node>
</node>
<node CREATED="1450102818381" FOLDED="true" ID="ID_693" MODIFIED="1450107144159" TEXT="Tips&apos;n tricks">
<node CREATED="1450102818381" ID="ID_694" MODIFIED="1450102818381" TEXT="Efficient feature construction">
<node CREATED="1450102818381" ID="ID_716" MODIFIED="1450102818381" TEXT="Large datasets or number of features">
<node CREATED="1450102818381" ID="ID_695" MODIFIED="1450102818381" TEXT="train_set = nltk.classify.apply_features([feature_extractor], [labeled_input_data])"/>
</node>
<node CREATED="1450102818381" ID="ID_717" MODIFIED="1450104494716" TEXT="[word] in [set] is a much faster lookup than [word] in [list]">
<node CREATED="1450102818381" ID="ID_718" MODIFIED="1450102818381">
<richcontent TYPE="NODE"><html>
                                    <head/>
                                    <body>
                                        <p>def document_features(document):</p>
                                        <p>document_words = set(document)</p>
                                        <p>features = {}</p>
                                        <p>for word in [word_vocabulary]:</p>
                                        <p>features['contains({})'.format(word)] = (word in document_words)</p>
                                        <p>return features</p>
                                    </body>
                                </html></richcontent>
</node>
</node>
</node>
<node CREATED="1450102818381" ID="ID_700" MODIFIED="1450102818381" TEXT="Avoiding overfitting">
<node CREATED="1450104506800" ID="ID_658096358" MODIFIED="1450104519701" TEXT="def gender_features(word):&#xa;&#x9;return {&apos;last_letter&apos;: word[-1]}">
<node CREATED="1450102818382" ID="ID_705" MODIFIED="1450102818382" TEXT="Works well"/>
</node>
<node CREATED="1450102818382" ID="ID_704" MODIFIED="1450102818382">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>def gender_features2(word):</p>
                                    <p>return {'suffix1': word[-1:], 'suffix2': word[-2:]}</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818382" ID="ID_706" MODIFIED="1450102818382" TEXT="Works better"/>
</node>
<node CREATED="1450102818382" ID="ID_702" MODIFIED="1450102818382">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>def gender_features3(name):</p>
                                    <p>features = {}</p>
                                    <p>features["first_letter"] = name[0].lower()</p>
                                    <p>features["last_letter"] = name[-1].lower()</p>
                                    <p>for letter in 'abcdefghijklmnopqrstuvwxyz':</p>
                                    <p>features["count({})".format(letter)] = name.lower().count(letter)</p>
                                    <p>features["has({})".format(letter)] = (letter in name.lower())</p>
                                    <p>return features</p>
                                </body>
                            </html></richcontent>
<node CREATED="1450102818383" ID="ID_703" MODIFIED="1450102818383" TEXT="Leads to overfitting"/>
</node>
</node>
<node CREATED="1450104540490" FOLDED="true" ID="ID_84746276" MODIFIED="1450105739840" TEXT="Evaluation">
<node CREATED="1450102818383" ID="ID_707" MODIFIED="1450102818383" TEXT="Dataset division">
<node CREATED="1450102818383" ID="ID_708" MODIFIED="1450102818383" TEXT="Training set">
<node CREATED="1450102818383" ID="ID_709" MODIFIED="1450102818383" TEXT="Train set"/>
<node CREATED="1450102818383" ID="ID_710" MODIFIED="1450102818383" TEXT="Dev-test set">
<node CREATED="1450102818383" ID="ID_712" MODIFIED="1450102818383" TEXT="For fine tuning as many times as needed"/>
</node>
</node>
<node CREATED="1450102818383" ID="ID_711" MODIFIED="1450102818383" TEXT="Test set">
<node CREATED="1450102818383" ID="ID_713" MODIFIED="1450102818383" TEXT="For final evaluation only"/>
<node CREATED="1450104560320" ID="ID_31783189" MODIFIED="1450104588637" TEXT="Optimally, each label should be represented by at least 50 instances">
<node CREATED="1450104589232" ID="ID_551415873" MODIFIED="1450104625110" TEXT="If the test set is well balanced and the labels equally distributed, as little as 100 instances can be enough"/>
</node>
<node CREATED="1450104730890" ID="ID_216582715" MODIFIED="1450104771617" TEXT="It is better if it is extracted from a different source than the training set">
<node CREATED="1450104772761" ID="ID_1191732962" MODIFIED="1450104821919" TEXT="E.g., train with nltk.corpus.brown.tagged_sents(categories=&apos;news&apos;) and test with nltk.corpus.brown.tagged_sents(categories=&apos;fiction&apos;)"/>
</node>
<node CREATED="1450105400591" ID="ID_1613643103" MODIFIED="1450105456941" TEXT="If there is just not enough data, n-fold cross validation can be used"/>
</node>
</node>
<node CREATED="1450104702760" ID="ID_1538903526" MODIFIED="1450104857345" TEXT="Accuracy">
<node CREATED="1450104904974" ID="ID_679162540" MODIFIED="1450104920415" TEXT="Percentage of inputs that were labeled correctly"/>
<node CREATED="1450104921685" ID="ID_726210047" MODIFIED="1450104955605" TEXT="Can be misleading if labels are not uniformly distributed">
<node CREATED="1450104957005" ID="ID_886689717" MODIFIED="1450104993848" TEXT="If 95% of all instances are Label_A and 5% Label_B, a 95% accuracy is not very impressive"/>
</node>
</node>
<node CREATED="1450105250967" ID="ID_1039098716" MODIFIED="1450105329762" TEXT="Beyond accuracy">
<node CREATED="1450105256707" ID="ID_1705592403" MODIFIED="1450105261050" TEXT="True positives">
<node CREATED="1450105287718" ID="ID_1500237220" MODIFIED="1450105295150" TEXT="Are A and were labeled A"/>
</node>
<node CREATED="1450105261733" ID="ID_1407069634" MODIFIED="1450105266199" TEXT="True negatives">
<node CREATED="1450105296791" ID="ID_566362363" MODIFIED="1450105302865" TEXT="Are not A and were not labeled A"/>
</node>
<node CREATED="1450105266779" ID="ID_1764802386" MODIFIED="1450105269877" TEXT="False positives">
<node CREATED="1450105273009" ID="ID_610676756" MODIFIED="1450105276651" TEXT="Type I errors"/>
<node CREATED="1450105304840" ID="ID_1160789593" MODIFIED="1450105313197" TEXT="Are not A but were labeled A"/>
</node>
<node CREATED="1450105277394" ID="ID_747939370" MODIFIED="1450105281285" TEXT="False negatives">
<node CREATED="1450105282301" ID="ID_318189510" MODIFIED="1450105285776" TEXT="Type II errors"/>
<node CREATED="1450105315060" ID="ID_181400194" MODIFIED="1450105322379" TEXT="Are A but were not labeled A"/>
</node>
</node>
<node CREATED="1450104995751" ID="ID_1028110330" MODIFIED="1450105043272" TEXT="Precision">
<node CREATED="1450105044482" ID="ID_110888408" MODIFIED="1450105072611" TEXT="True positives / ( True positives + False positives )">
<node CREATED="1450105113996" ID="ID_1254490092" MODIFIED="1450105128370" TEXT="From those labeled as A, how many were A"/>
</node>
</node>
<node CREATED="1450105075082" ID="ID_261080382" MODIFIED="1450105189447" TEXT="Recall">
<node CREATED="1450105091391" ID="ID_1738399086" MODIFIED="1450105107884" TEXT="True positives / ( True positives + False negatives )">
<node CREATED="1450105130708" ID="ID_1026145470" MODIFIED="1450105149905" TEXT="From those that were A, how many were labeled as A"/>
</node>
</node>
<node CREATED="1450105190444" ID="ID_1475482597" MODIFIED="1450105192730" TEXT="F-score">
<node CREATED="1450105199997" ID="ID_1598717033" MODIFIED="1450105231850" TEXT="( 2 x Precision x Recall ) / ( Precision + Recall )">
<node CREATED="1450105235762" ID="ID_1687058633" MODIFIED="1450105239668" TEXT="Harmonic mean"/>
</node>
</node>
<node CREATED="1450105349793" ID="ID_1876369704" MODIFIED="1450105358829" TEXT="Confusion matrix">
<node CREATED="1450105359863" ID="ID_1637099394" MODIFIED="1450105372275" TEXT="When there is more than one label"/>
</node>
</node>
<node CREATED="1450102818383" ID="ID_714" MODIFIED="1450105410386" TEXT="Error inspection">
<node CREATED="1450102818383" ID="ID_715" MODIFIED="1450102818383">
<richcontent TYPE="NODE"><html>
                                <head/>
                                <body>
                                    <p>errors = []</p>
                                    <p>for (name, tag) in devtest_names:</p>
                                    <p>guess = classifier.classify(gender_features(name))</p>
                                    <p>if guess != tag:</p>
                                    <p>errors.append( (tag, guess, name) )</p>
                                </body>
                            </html></richcontent>
</node>
</node>
<node CREATED="1450102818384" ID="ID_719" MODIFIED="1450102818384" TEXT="Classifier inspection">
<node CREATED="1450102818384" ID="ID_722" MODIFIED="1450102818384" TEXT="NaiveBayes">
<node CREATED="1450102818384" ID="ID_725" MODIFIED="1450102818384" TEXT="[classifier].show_most_informative_features(5)"/>
</node>
<node CREATED="1450102818384" ID="ID_723" MODIFIED="1450102818384" TEXT="Decision Tree">
<node CREATED="1450102818384" ID="ID_724" MODIFIED="1450102818384" TEXT="[classifier].pseudocode(depth=4)"/>
</node>
</node>
<node CREATED="1450102818384" FOLDED="true" ID="ID_734" MODIFIED="1450104708669" TEXT="Sequence classification">
<node CREATED="1450102818384" ID="ID_735" MODIFIED="1450102818384" TEXT="E.g., POS label assignment of [word_i] using as a feature the POS label of [word_i-1]"/>
<node CREATED="1450102818384" ID="ID_736" MODIFIED="1450102900072" TEXT="Can be implemented using [history variables]">
<node CREATED="1450102924812" ID="ID_821072228" MODIFIED="1450103005040" TEXT="Feature extraction">
<node CREATED="1450103440667" ID="ID_838888716" MODIFIED="1450103529017" TEXT="def POS_features(sentence, i, history):&#xa;&#x9;features = {&quot;suffix(1)&quot;: sentence[i][-1:],&#xa;&#x9;&#x9;&quot;suffix(2)&quot;: sentence[i][-2:],&#xa;&#x9;&#x9;&quot;suffix(3)&quot;: sentence[i][-3:]}&#x9;&#xa;&#x9;if i == 0:&#xa;&#x9;&#x9;features[&quot;prev-word&quot;] = &quot;&lt;START&gt;&quot;&#xa;&#x9;&#x9;features[&quot;prev-tag&quot;] = &quot;&lt;START&gt;&quot;&#xa;&#x9;else:&#xa;&#x9;&#x9;features[&quot;prev-word&quot;] = sentence[i-1]&#xa;&#x9;&#x9;features[&quot;prev-tag&quot;] = history[i-1]&#xa;&#x9;return features"/>
</node>
<node CREATED="1450103005962" ID="ID_1885285456" MODIFIED="1450103008099" TEXT="Training">
<node CREATED="1450103015195" ID="ID_1055480140" MODIFIED="1450103430694" TEXT="train_set = []&#xa;for tagged_sent in train_sents:&#xa;&#x9;untagged_sent = [ wrd for (wrd, _) in tagged_sent ]&#xa;&#x9;tags = [ tag for (_, tag) in tagged_sent ]&#xa;&#x9;train_set = train_set + [ (POS_features(untagged_sent, i, tags), tags[i]) for i in range(len(tags)) ]&#xa;classifier = nltk.NaiveBayesClassifier.train(train_set)"/>
</node>
<node CREATED="1450102929463" ID="ID_1900243642" MODIFIED="1450102932968" TEXT="Tagging">
<node CREATED="1450103258579" ID="ID_663033205" MODIFIED="1450103545889" TEXT="history = []&#xa;for i in range(len(sentence)):&#xa;&#x9;tag = classifier.classify(POS_features(sentence, i, history))&#xa;&#x9;history = history + [ tag ]&#xa;zip(sentence, history)"/>
</node>
</node>
<node CREATED="1450103605912" ID="ID_187029393" MODIFIED="1450103610651" TEXT="Other methods exist">
<node CREATED="1450103612210" ID="ID_1950531772" MODIFIED="1450103616962" TEXT="Hidden Markov Models"/>
<node CREATED="1450103619664" ID="ID_843639184" MODIFIED="1450103646740" TEXT="Maximum Entropy Models"/>
<node CREATED="1450103640228" ID="ID_483808848" MODIFIED="1450103643509" TEXT="Linear-Chain Conditional Random Field Models"/>
</node>
</node>
<node CREATED="1450104263325" ID="ID_86017589" MODIFIED="1450104269572" TEXT="Scaling up to large datasets">
<node CREATED="1450104270696" ID="ID_998999832" MODIFIED="1450104300035" TEXT="NLTK allows to call machine learning C libraries with minimal code modification"/>
</node>
</node>
</node>
<node CREATED="1453699413581" FOLDED="true" ID="ID_23322773" MODIFIED="1453977430293" POSITION="right" TEXT="7. Extracting Information from Text">
<node CREATED="1453699455885" ID="ID_989366980" MODIFIED="1453699625358" TEXT="Information Extraction">
<node CREATED="1453699464508" ID="ID_1177327712" MODIFIED="1453699478231" TEXT="Turn unstructured text into structured data that cna be queried"/>
<node CREATED="1453699516413" ID="ID_23570281" MODIFIED="1453699537651" TEXT="&apos;Structured data&apos; means list of tuples with reoationships">
<node CREATED="1453699551991" ID="ID_498692839" MODIFIED="1453699581476" TEXT="(&apos;New York City&apos;, &apos;IS&apos;, &apos;City&apos;)"/>
<node CREATED="1453699551991" ID="ID_1437622935" MODIFIED="1453699595735" TEXT="(&apos;New York City&apos;, &apos;IN&apos;, &apos;USA&apos;)"/>
<node CREATED="1453699598743" ID="ID_434922531" MODIFIED="1453699600204" TEXT="..."/>
</node>
<node CREATED="1453704100601" ID="ID_726572241" MODIFIED="1453704103731" TEXT="Steps">
<node CREATED="1453699626645" ID="ID_1094647634" MODIFIED="1453704154245" TEXT="Input: raw text"/>
<node CREATED="1453699639593" ID="ID_1058541181" MODIFIED="1453699645710" TEXT="Sentence segmentation"/>
<node CREATED="1453699646540" ID="ID_150696550" MODIFIED="1453699655135" TEXT="Tokenization"/>
<node CREATED="1453704113310" ID="ID_1120787145" MODIFIED="1453704116525" TEXT="POS tagging"/>
<node CREATED="1453704116774" ID="ID_707971461" MODIFIED="1453704124463" TEXT="Entity detection">
<node CREATED="1453704271290" ID="ID_956539778" MODIFIED="1453704274941" TEXT="Chunking"/>
</node>
<node CREATED="1453704137521" ID="ID_1729285799" MODIFIED="1453704140953" TEXT="Relation detection"/>
<node CREATED="1453704155981" ID="ID_1326304796" MODIFIED="1453704161425" TEXT="Output: relations"/>
</node>
</node>
<node CREATED="1453704276675" ID="ID_91986945" MODIFIED="1453717501429" TEXT="Chunking">
<node CREATED="1453705584268" ID="ID_1240338005" MODIFIED="1453705587601" TEXT="Representing chunks">
<node CREATED="1453705602300" ID="ID_1987789334" MODIFIED="1453705604502" TEXT="Tags">
<node CREATED="1453705605537" ID="ID_1041275144" MODIFIED="1453705608282" TEXT="Most common">
<node CREATED="1453705883507" ID="ID_1592303663" MODIFIED="1453705890574" TEXT="Easy to implement and store"/>
</node>
<node CREATED="1453705608617" ID="ID_7863978" MODIFIED="1453705611587" TEXT="IOB tags">
<node CREATED="1453705615129" ID="ID_1295173305" MODIFIED="1453705635399" TEXT="Inside a chunk"/>
<node CREATED="1453705615129" ID="ID_1936373390" MODIFIED="1453705639743" TEXT="Outside a chunk"/>
<node CREATED="1453705640177" ID="ID_136955397" MODIFIED="1453705665629" TEXT="Beginning of a chunk"/>
</node>
<node CREATED="1453705671307" ID="ID_113345594" MODIFIED="1453705854470" TEXT="Each token is tagged with an IOB tag">
<node CREATED="1453705692052" ID="ID_1464130097" MODIFIED="1453705707155" TEXT="The first one in a chunk, with a B followed by the type of chunk">
<node CREATED="1453705763508" ID="ID_1552273515" MODIFIED="1453705796814" TEXT="Example: B-NP"/>
</node>
<node CREATED="1453705707694" ID="ID_1084307534" MODIFIED="1453705744113" TEXT="All remaining tokens of the chunk, with an I followed by the type of chunk">
<node CREATED="1453705763508" ID="ID_1588737482" MODIFIED="1453705801952" TEXT="Example: I-NP"/>
</node>
<node CREATED="1453705728238" ID="ID_1983942882" MODIFIED="1453705738156" TEXT="All those not in a chunk, with an O">
<node CREATED="1453705804939" ID="ID_1109212730" MODIFIED="1453705807714" TEXT="Example: O"/>
</node>
</node>
</node>
<node CREATED="1453705865622" ID="ID_139756844" MODIFIED="1453705867502" TEXT="Trees">
<node CREATED="1453705869295" ID="ID_422254859" MODIFIED="1453717980618" TEXT="Allows direct access to the complete chunk and chunk recursion"/>
<node CREATED="1453717982206" ID="ID_1923509545" MODIFIED="1453717996896" TEXT="Used internally by NLTK"/>
<node CREATED="1453717991602" ID="ID_249132573" MODIFIED="1453718035494" TEXT="NLTK utils to handle trees">
<node CREATED="1453718048508" ID="ID_1926021801" MODIFIED="1453718083065" TEXT="tree1 = nltk.Tree(&apos;NP&apos;, [&apos;Alice&apos;])&#xa;tree2 = nltk.Tree(&apos;NP&apos;, [&apos;the&apos;, &apos;rabbit&apos;])&#xa;tree3 = nltk.Tree(&apos;VP&apos;, [&apos;chased&apos;, tree2])&#xa;tree4 = nltk.Tree(&apos;S&apos;, [tree1, tree3])">
<node CREATED="1453718086932" ID="ID_880789327" MODIFIED="1453718103175" TEXT="print(tree4)">
<node CREATED="1453718118919" ID="ID_1541276887" MODIFIED="1453718120175" TEXT="(S (NP Alice) (VP chased (NP the rabbit)))"/>
</node>
<node CREATED="1453718088692" ID="ID_1654475233" MODIFIED="1453718203336" TEXT="print(tree4).label()">
<node CREATED="1453718188467" ID="ID_616130789" MODIFIED="1453718211293" TEXT="&apos;S&apos;"/>
</node>
<node CREATED="1453718218552" ID="ID_1641684050" MODIFIED="1453718222222" TEXT="tree4.leaves()">
<node CREATED="1453718230659" ID="ID_851216929" MODIFIED="1453718231780" TEXT="[&apos;Alice&apos;, &apos;chased&apos;, &apos;the&apos;, &apos;rabbit&apos;]"/>
</node>
<node CREATED="1453718236370" ID="ID_1583306672" MODIFIED="1453718239652" TEXT="tree4.draw()">
<node CREATED="1453718241698" ID="ID_930448137" MODIFIED="1453718249157" TEXT="[visual representation of the tree]"/>
</node>
</node>
</node>
<node CREATED="1453718312137" ID="ID_1552406612" MODIFIED="1453718354976" TEXT="Often used recursive technique to traverse a complete tree">
<node CREATED="1453718356021" ID="ID_1223271525" MODIFIED="1453718677714" TEXT="def traverse(t):&#xa;&#x9;try:&#xa;&#x9;&#x9;t.label()&#xa;&#x9;except AttributeError:&#xa;&#x9;&#x9;print(t, end=&quot; &quot;)&#xa;&#x9;else:         # Now we know that t.node is defined&#xa;&#x9;&#x9;print(&apos;(&apos;, t.label(), end=&quot; &quot;)&#xa;&#x9;&#x9;for child in t:&#xa;&#x9;&#x9;traverse(child)&#xa;&#x9;&#x9;print(&apos;)&apos;, end=&quot; &quot;)">
<node CREATED="1453718686357" ID="ID_911053048" MODIFIED="1453718711469" TEXT="The &apos;try&apos; makes sure the current node is a node and not a terminal leave"/>
</node>
</node>
</node>
<node CREATED="1453713586827" ID="ID_1951654096" MODIFIED="1453713594326" TEXT="Convert tags to trees">
<node CREATED="1453713595374" ID="ID_204727365" MODIFIED="1453713604695" TEXT="nltk.chunk.conllstr2tree([text], chunk_types=[&apos;NP&apos;]).draw()">
<node CREATED="1453713605780" ID="ID_1992477327" MODIFIED="1453713623096" TEXT="[test] is an IOB tagged chunked text"/>
</node>
<node CREATED="1453713648378" ID="ID_556030495" MODIFIED="1453713665722" TEXT="Allows to select which chunk_types to represent"/>
</node>
<node CREATED="1453714298015" ID="ID_1183726011" MODIFIED="1453714303084" TEXT="Convert trees to tags">
<node CREATED="1453714304192" ID="ID_438761048" MODIFIED="1453714312999" TEXT="nltk.chunk.tree2conlltags([sent])"/>
</node>
</node>
<node CREATED="1453704747589" ID="ID_1714138524" MODIFIED="1453715231261" TEXT="Regexp chunker">
<node CREATED="1453704414777" ID="ID_177953716" MODIFIED="1453704479083" TEXT="Regexp grammar">
<node CREATED="1453704440918" ID="ID_338254718" MODIFIED="1453704450628" TEXT="Rules indicating how a sentence should be chunked">
<node CREATED="1453704524209" ID="ID_937628199" MODIFIED="1453704532583" TEXT="Very often use POS tag patterns"/>
</node>
<node CREATED="1453704297155" ID="ID_614950920" MODIFIED="1453704302535" TEXT="Noun Phrase chunking">
<node CREATED="1453704491208" ID="ID_1525637567" MODIFIED="1453704492320" TEXT="grammar = &quot;NP: {&lt;DT&gt;?&lt;JJ&gt;*&lt;NN&gt;}&quot;"/>
<node CREATED="1453704860243" ID="ID_1233501809" MODIFIED="1453704983294" TEXT="grammar = r&quot;&quot;&quot;NP:&#xa;&#x9;{&lt;DT|PP\$&gt;?&lt;JJ&gt;*&lt;NN&gt;} # chunk determiner/possessive, adjectives and noun&#xa;&#x9;{&lt;NNP&gt;+} # chunk sequences of proper nouns&#xa;&#x9;&quot;&quot;&quot;">
<node CREATED="1453704915207" ID="ID_154784961" MODIFIED="1453704937409" TEXT="If comments exist, they are appended as part of the verbose output"/>
</node>
</node>
<node CREATED="1453705046441" ID="ID_581293460" MODIFIED="1453705065344" TEXT="Parsers allow to find any sequence of POS tags">
<node CREATED="1453705066775" ID="ID_326652131" MODIFIED="1453705109201" TEXT="The chunks do not need to be &apos;semantic entity&apos; related"/>
<node CREATED="1453705139160" ID="ID_107475334" MODIFIED="1453705146119" TEXT="Example: &quot;NOUNS: {&lt;N.*&gt;{4,}}&quot;">
<node CREATED="1453705148257" ID="ID_1330754308" MODIFIED="1453705160623" TEXT="Would find 4 or more nouns together"/>
</node>
</node>
</node>
<node CREATED="1453704779546" ID="ID_516239667" MODIFIED="1453704788284" TEXT="Rules are applied sequentially">
<node CREATED="1453704789058" ID="ID_98287003" MODIFIED="1453704821426" TEXT="Chunks are allocated on a first found first served left to right fashion"/>
</node>
<node CREATED="1453705286007" ID="ID_1225022390" MODIFIED="1453705490089" TEXT="Allows &apos;Chinking&apos;">
<node CREATED="1453705295873" ID="ID_945753119" MODIFIED="1453705307387" TEXT="&apos;Opposite approach&apos; to chunking">
<node CREATED="1453705308405" ID="ID_1962746451" MODIFIED="1453705350150" TEXT="Take the complete sentence, find the most likely chunk limits, and split"/>
</node>
<node CREATED="1453705356010" ID="ID_912556607" MODIFIED="1453705365548" TEXT="Sample grammar">
<node CREATED="1453705376445" ID="ID_1164272192" MODIFIED="1453705409957" TEXT="grammar = r&quot;&quot;&quot;NP:&#xa;&#x9;{&lt;.*&gt;+} # Chunk everything&#xa;&#x9;}&lt;VBD|IN&gt;+{ # Chink sequences of VBD and IN&#xa;&#x9;&quot;&quot;&quot;">
<node CREATED="1453705419474" ID="ID_219765664" MODIFIED="1453705471790" TEXT="Splits sentences in all the &apos;verb + preposition&apos; occurences"/>
</node>
</node>
</node>
</node>
<node CREATED="1453705929160" ID="ID_521943590" MODIFIED="1453705935747" TEXT="Chunk corpus">
<node CREATED="1453705961016" ID="ID_1051951164" MODIFIED="1453705961763" TEXT="CoNLL 2000">
<node CREATED="1453713692975" ID="ID_1377277352" MODIFIED="1453713707078" TEXT="nltk.corpus.conll2000.chunked_sents(&apos;train.txt&apos;, chunk_types=[&apos;NP&apos;])"/>
<node CREATED="1453713714794" ID="ID_314988580" MODIFIED="1453713728230" TEXT="The corpus is divided into train and test sets"/>
<node CREATED="1453713728512" ID="ID_953032794" MODIFIED="1453713742326" TEXT="Different types of chunk_types can also be extracted">
<node CREATED="1453713748028" ID="ID_1456032643" MODIFIED="1453713753474" TEXT="NP: noun phrases"/>
<node CREATED="1453713753738" ID="ID_1444552894" MODIFIED="1453713759675" TEXT="VP: verb phrases">
<node CREATED="1453713780905" ID="ID_1490050820" MODIFIED="1453713785605" TEXT="&apos;has already delivered&apos;"/>
</node>
<node CREATED="1453713760164" ID="ID_239709290" MODIFIED="1453713768739" TEXT="PP: prepositional phrases">
<node CREATED="1453713769897" ID="ID_1480987029" MODIFIED="1453713773761" TEXT="&apos;because of&apos;"/>
</node>
</node>
<node CREATED="1453713842971" ID="ID_810009347" MODIFIED="1453713858445" TEXT="Allows to easily evaluate chunkers">
<node CREATED="1453713871033" ID="ID_786516993" MODIFIED="1453713876161" TEXT="Empty chunker">
<node CREATED="1453713877578" ID="ID_103882457" MODIFIED="1453723590809" TEXT="grammar = r&quot;&quot;&#xa;cp = nltk.RegexpParser(grammar)&#xa;test_sents = nltk.corpus.conll2000.chunked_sents(&apos;test.txt&apos;, chunk_types=[&apos;NP&apos;])&#xa;cp.evaluate(test_sents)">
<node CREATED="1453713940319" ID="ID_1979816153" MODIFIED="1453713963329" TEXT="ChunkParse score:&#xa;&#x9;IOB Accuracy:  43.4%&#xa;&#x9;Precision:      0.0%&#xa;&#x9;Recall:         0.0%&#xa;&#x9;F-Measure:      0.0%"/>
</node>
</node>
<node CREATED="1453713969374" ID="ID_1263255321" MODIFIED="1453713972997" TEXT="Naive NP chunker">
<node CREATED="1453713877578" ID="ID_1857145712" MODIFIED="1453714054275" TEXT="grammar = r&quot;NP: {&lt;[CDJNP].*&gt;+}&quot;&#xa;cp = nltk.RegexpParser(grammar)&#xa;test_sents = nltk.corpus.conll2000.chunked_sents(&apos;test.txt&apos;, chunk_types=[&apos;NP&apos;])&#xa;cp.evaluate(test_sents)">
<node CREATED="1453713940319" ID="ID_133513725" MODIFIED="1453714081145" TEXT="ChunkParse score:&#xa;&#x9;IOB Accuracy:  87.7%&#xa;&#x9;Precision:      70.6%&#xa;&#x9;Recall:         67.8%&#xa;&#x9;F-Measure:      69.2%"/>
</node>
</node>
</node>
<node CREATED="1453714565694" ID="ID_665641807" MODIFIED="1453714577168" TEXT="Allows to train new chunkers">
<node CREATED="1453715243914" ID="ID_471185413" MODIFIED="1453715267028" TEXT="See sections on N-Gram tagger chunkers and Classifier chunkers"/>
</node>
</node>
</node>
<node CREATED="1453714988404" ID="ID_1411776136" MODIFIED="1453715273761" TEXT="N-Gram tagger chunkers">
<node CREATED="1453714651372" ID="ID_94184942" MODIFIED="1453714749911" TEXT="class UnigramChunker(nltk.ChunkParserI):&#xa; &#x9;def __init__(self, train_sents):&#xa; &#x9;&#x9;train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]&#xa; &#x9;&#x9;&#x9;for sent in train_sents]&#xa; &#x9;&#x9;self.tagger = nltk.UnigramTagger(train_data)&#xa;  &#x9;def parse(self, sentence):&#xa; &#x9;&#x9;pos_tags = [pos for (word,pos) in sentence]&#xa; &#x9;&#x9;tagged_pos_tags = self.tagger.tag(pos_tags)&#xa; &#x9;&#x9;chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]&#xa; &#x9;&#x9;conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)&#xa; &#x9;&#x9;&#x9;in zip(sentence, chunktags)]&#xa; &#x9;&#x9;return nltk.chunk.conlltags2tree(conlltags)">
<node CREATED="1453714808106" ID="ID_1834423547" MODIFIED="1453714820417" TEXT="Class defined over the base ChunkParserI class"/>
<node CREATED="1453714869577" ID="ID_1329784663" MODIFIED="1453714882787" TEXT="A lot of effort goes into switching from trees to tags"/>
<node CREATED="1453714752472" ID="ID_32074426" MODIFIED="1453714899796" TEXT="Uses the same UnigramTagger we saw at POS tagging to associate POSs to their most likely IOB tag"/>
<node CREATED="1453714799558" ID="ID_252866955" MODIFIED="1453714806279" TEXT="Performs surprisingly well">
<node CREATED="1453714913934" ID="ID_874093782" MODIFIED="1453714937029" TEXT="ChunkParse score:&#xa;&#x9;IOB Accuracy:  92.9%&#xa;&#x9;Precision:     79.9%&#xa;&#x9;Recall:        86.8%&#xa;&#x9;F-Measure:     83.2%"/>
</node>
</node>
<node CREATED="1453714942186" ID="ID_1482432963" MODIFIED="1453714966441" TEXT="Same thing but using &apos;self.tagger = nltk.BigramTagger(train_data)&apos;">
<node CREATED="1453714967937" ID="ID_131695784" MODIFIED="1453714977604" TEXT="Performs slightly better"/>
</node>
</node>
<node CREATED="1453715004703" ID="ID_1770881421" MODIFIED="1453715272204" TEXT="Classifier chunkers">
<node CREATED="1453715282013" ID="ID_262689810" MODIFIED="1453715302775" TEXT="Replace N-Gram chunkers when more features are needed">
<node CREATED="1453715304297" ID="ID_1220567513" MODIFIED="1453715320348" TEXT="The words themselves, and not only the POSs"/>
<node CREATED="1453715320815" ID="ID_362513328" MODIFIED="1453715332161" TEXT="Forward looking features"/>
<node CREATED="1453715333007" ID="ID_417893585" MODIFIED="1453715339683" TEXT="Complex context features">
<node CREATED="1453715341297" ID="ID_1863272186" MODIFIED="1453716941886" TEXT="&apos;All tags since the last determinant&apos;"/>
<node CREATED="1453716942235" ID="ID_983429256" MODIFIED="1453716943455" TEXT="..."/>
</node>
</node>
<node CREATED="1453715762703" ID="ID_1891080614" MODIFIED="1453716063575" TEXT="class ConsecutiveNPChunkTagger(nltk.TaggerI):&#xa; &#x9;def __init__(self, train_sents):&#xa; &#x9;&#x9;train_set = []&#xa; &#x9;&#x9;for tagged_sent in train_sents:&#xa; &#x9;&#x9;&#x9;untagged_sent = nltk.tag.untag(tagged_sent)&#xa; &#x9;&#x9;&#x9;history = []&#xa; &#x9;&#x9;&#x9;for i, (word, tag) in enumerate(tagged_sent):&#xa; &#x9;&#x9;&#x9;&#x9;featureset = npchunk_features(untagged_sent, i, history)&#xa; &#x9;&#x9;&#x9;&#x9;train_set.append( (featureset, tag) )&#xa; &#x9;&#x9;&#x9;&#x9;history.append(tag)&#xa; &#x9;&#x9;self.classifier = nltk.MaxentClassifier.train(train_set, algorithm=&apos;megam&apos;, trace=0)&#xa; &#x9;def tag(self, sentence):&#xa; &#x9;&#x9;history = []&#xa; &#x9;&#x9;for i, word in enumerate(sentence):&#xa; &#x9;&#x9;&#x9;featureset = npchunk_features(sentence, i, history)&#xa; &#x9;&#x9;&#x9;tag = self.classifier.classify(featureset)&#xa; &#x9;&#x9;&#x9;history.append(tag)&#xa; &#x9;&#x9;return zip(sentence, history)&#xa;class ConsecutiveNPChunker(nltk.ChunkParserI):&#xa; &#x9;def __init__(self, train_sents):&#xa; &#x9;&#x9;tagged_sents = [[((w,t),c) for (w,t,c) in nltk.chunk.tree2conlltags(sent)]&#xa;&#x9;&#x9;&#x9;for sent in train_sents]&#xa; &#x9;&#x9;self.tagger = ConsecutiveNPChunkTagger(tagged_sents)&#xa; &#x9;def parse(self, sentence):&#xa; &#x9;&#x9;tagged_sents = self.tagger.tag(sentence)&#xa; &#x9;&#x9;conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]&#xa; &#x9;&#x9;return nltk.chunk.conlltags2tree(conlltags)">
<node CREATED="1453716002150" ID="ID_488957807" MODIFIED="1453716008747" TEXT="Define two classes">
<node CREATED="1453716009894" ID="ID_163409313" MODIFIED="1453716114509" TEXT="One for the classifier tagger">
<node CREATED="1453716115201" ID="ID_737253404" MODIFIED="1453716127081" TEXT="In this case, a MaxentClassifier"/>
<node CREATED="1453716256971" ID="ID_699247408" MODIFIED="1453716329388" TEXT="&apos;untagged&apos; in &apos;untagged_sent&apos; refers to &apos;without the IOB tag&apos; (as opposed to &apos;without the POS tag&apos;; POS tags are still found in &apos;untagged sent&apos;)"/>
</node>
<node CREATED="1453716014173" ID="ID_1405005776" MODIFIED="1453716018590" TEXT="One for the chunker"/>
</node>
<node CREATED="1453716026453" ID="ID_1539997723" MODIFIED="1453716436384" TEXT="The feature extractor &apos;npchunk_features()&apos; is left undefined until runtime">
<node CREATED="1453716437673" ID="ID_1834098733" MODIFIED="1453716512946" TEXT="def npchunk_features(sentence, i, history):&#xa; &#x9;word, pos = sentence[i]&#xa; &#x9;return {&quot;pos&quot;: pos}">
<node CREATED="1453716523852" ID="ID_1045152691" MODIFIED="1453716720808" TEXT="Features are the POS of the word">
<node CREATED="1453716534306" ID="ID_342940441" MODIFIED="1453716573479" TEXT="Performs like the UnigrammChunker above"/>
</node>
<node CREATED="1453717142000" ID="ID_1491754289" MODIFIED="1453717318643" TEXT="IOB Accuracy:  92.9%     &#xa;Precision:     79.9%     &#xa;Recall:        86.7%     &#xa;F-Measure:     83.2%"/>
</node>
<node CREATED="1453716664981" ID="ID_1411555797" MODIFIED="1453716689628" TEXT="def npchunk_features(sentence, i, history):&#xa; &#x9;word, pos = sentence[i]&#xa; &#x9;if i == 0:&#xa; &#x9;&#x9;prevword, prevpos = &quot;&lt;START&gt;&quot;, &quot;&lt;START&gt;&quot;&#xa; &#x9;else:&#xa; &#x9;&#x9;prevword, prevpos = sentence[i-1]&#xa; &#x9;return {&quot;pos&quot;: pos, &quot;prevpos&quot;: prevpos}">
<node CREATED="1453716692515" ID="ID_618381409" MODIFIED="1453716706602" TEXT="Features are the POS of the word and the POS of the previous word">
<node CREATED="1453716534306" ID="ID_436248041" MODIFIED="1453716716336" TEXT="Performs like the BigrammChunker above"/>
</node>
<node CREATED="1453717331006" ID="ID_236793711" MODIFIED="1453717347371" TEXT="IOB Accuracy:  93.6%     &#xa;Precision:     81.9%     &#xa;Recall:        87.2%     &#xa;F-Measure:     84.5%"/>
</node>
<node CREATED="1453716437673" ID="ID_1133068588" MODIFIED="1453716522031" TEXT="def npchunk_features(sentence, i, history):&#xa; &#x9;word, pos = sentence[i]&#xa; &#x9;if i == 0:&#xa; &#x9;&#x9;prevword, prevpos = &quot;&lt;START&gt;&quot;, &quot;&lt;START&gt;&quot;&#xa; &#x9;else:&#xa; &#x9;&#x9;prevword, prevpos = sentence[i-1]&#xa; &#x9;return {&quot;pos&quot;: pos, &quot;word&quot;: word, &quot;prevpos&quot;: prevpos}">
<node CREATED="1453716576197" ID="ID_1209467320" MODIFIED="1453716735502" TEXT="Features are the word itself, the POS of the word, and the POS of the previous word"/>
<node CREATED="1453717358111" ID="ID_891447067" MODIFIED="1453717378599" TEXT="IOB Accuracy:  94.5%     &#xa;Precision:     84.2%     &#xa;Recall:        89.4%     &#xa;F-Measure:     86.7%"/>
</node>
<node CREATED="1453716828729" ID="ID_1959240449" MODIFIED="1453717012815" TEXT="def npchunk_features(sentence, i, history):&#xa; &#x9;word, pos = sentence[i]&#xa; &#x9;if i == 0:&#xa; &#x9;&#x9;prevword, prevpos = &quot;&lt;START&gt;&quot;, &quot;&lt;START&gt;&quot;&#xa; &#x9;else:&#xa; &#x9;&#x9;prevword, prevpos = sentence[i-1]&#xa; &#x9;if i == len(sentence)-1:&#xa; &#x9;&#x9;nextword, nextpos = &quot;&lt;END&gt;&quot;, &quot;&lt;END&gt;&quot;&#xa; &#x9;else:&#xa; &#x9;&#x9;nextword, nextpos = sentence[i+1]&#xa; &#x9;return {&quot;pos&quot;: pos,&#xa; &#x9;&#x9;&quot;word&quot;: word,&#xa; &#x9;&#x9;&quot;prevpos&quot;: prevpos,&#xa; &#x9;&#x9;&quot;nextpos&quot;: nextpos,&#xa; &#x9;&#x9;&quot;prevpos+pos&quot;: &quot;%s+%s&quot; % (prevpos, pos),&#xa; &#x9;&#x9;&quot;pos+nextpos&quot;: &quot;%s+%s&quot; % (pos, nextpos),&#xa; &#x9;&#x9;&quot;tags-since-dt&quot;: tags_since_dt(sentence, i)}&#xa;def tags_since_dt(sentence, i):&#xa; &#x9;tags = set()&#xa; &#x9;for word, pos in sentence[:i]:&#xa; &#x9;&#x9;if pos == &apos;DT&apos;:&#xa; &#x9;&#x9;&#x9;tags = set()&#xa; &#x9;&#x9;else:&#xa; &#x9;&#x9;&#x9;tags.add(pos)&#xa; &#x9;return &apos;+&apos;.join(sorted(tags))">
<node CREATED="1453717038479" ID="ID_177292277" MODIFIED="1453717043500" TEXT="Features are">
<node CREATED="1453716576197" ID="ID_191618672" MODIFIED="1453717064719" TEXT="The word itself, the POS of the word, and the POS of the previous word"/>
<node CREATED="1453717065346" ID="ID_807211955" MODIFIED="1453717072471" TEXT="The pos of the next word"/>
<node CREATED="1453717072938" ID="ID_447193165" MODIFIED="1453717129898" TEXT="The pairs &apos;POS of the word, POS of the previous word&apos; and &apos;POS of the word, POS of the next word&apos;"/>
<node CREATED="1453717097894" ID="ID_445426403" MODIFIED="1453717117789" TEXT="The POS of all previous words until the previous determinant (or the beginning of the sentence)"/>
</node>
<node CREATED="1453717387994" ID="ID_1680543228" MODIFIED="1453717400947" TEXT="IOB Accuracy:  96.0%     &#xa;Precision:     88.6%     &#xa;Recall:        91.0%     &#xa;F-Measure:     89.8%"/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1453717591921" ID="ID_1569673808" MODIFIED="1453717599432" TEXT="Recursive chunking">
<node CREATED="1453717614513" ID="ID_1733786565" MODIFIED="1453717628478" TEXT="Allows to find phrases nested within phrases">
<node CREATED="1453717633287" ID="ID_1398082795" MODIFIED="1453717643510" TEXT="True structure of natural language"/>
</node>
<node CREATED="1453717668287" ID="ID_1308664453" MODIFIED="1453717683513" TEXT="Regexp chunker">
<node CREATED="1453717684726" ID="ID_290171516" MODIFIED="1453717819647" TEXT="grammar = r&quot;&quot;&quot;NP:&#xa;&#x9;{&lt;DT|JJ|NN.*&gt;+} # Chunk sequences of DT, JJ, NN&#xa;&#x9;PP: {&lt;IN&gt;&lt;NP&gt;} # Chunk prepositions followed by NP&#xa;&#x9;VP: {&lt;VB.*&gt;&lt;NP|PP|CLAUSE&gt;+$} # Chunk verbs and their arguments&#xa;&#x9;CLAUSE: {&lt;NP&gt;&lt;VP&gt;} # Chunk NP, VP&#xa;&#x9;&quot;&quot;&quot;&#xa;cp = nltk.RegexpParser(grammar)"/>
<node CREATED="1453717747189" ID="ID_1817340553" MODIFIED="1453717767139" TEXT="Misses sentences with more than four levels">
<node CREATED="1453717770659" ID="ID_1642650558" MODIFIED="1453717783883" TEXT="Can chunk recursively by using loops"/>
<node CREATED="1453717807337" ID="ID_329670474" MODIFIED="1453717808318" TEXT="cp = nltk.RegexpParser(grammar, loop=2)">
<node CREATED="1453717823984" ID="ID_1941261964" MODIFIED="1453717836816" TEXT="Still, there is a hard depth limit"/>
<node CREATED="1453717837353" ID="ID_458517052" MODIFIED="1453717859932" TEXT="After a certain depth it is better to do full parsing instead"/>
</node>
</node>
</node>
</node>
<node CREATED="1453720050960" ID="ID_443352099" MODIFIED="1453720058434" TEXT="Named Entity Recognition">
<node CREATED="1453720079766" ID="ID_1805597369" MODIFIED="1453720087501" TEXT="Of special significance">
<node CREATED="1453720089555" ID="ID_232114106" MODIFIED="1453720125743" TEXT="Identifying Named Entities early is crucial to properly extract information from text"/>
</node>
<node CREATED="1453720060277" ID="ID_861802021" MODIFIED="1453720076764" TEXT="Very similar problem to chunking">
<node CREATED="1453720177287" ID="ID_920768546" MODIFIED="1453720201296" TEXT="A classifier chunker can be trained on a pre-tagged corpus"/>
</node>
<node CREATED="1453720203042" ID="ID_1697472121" MODIFIED="1453720221344" TEXT="A trained Named Entity classifier comes with NLTK">
<node CREATED="1453720236391" ID="ID_213308909" MODIFIED="1453720237214" TEXT="nltk.ne_chunk()">
<node CREATED="1453720267824" ID="ID_1021802545" MODIFIED="1453720282559" TEXT="Parameter binary=True">
<node CREATED="1453720283984" ID="ID_305653487" MODIFIED="1453720313382" TEXT="Named Entities are tagged as NE"/>
</node>
<node CREATED="1453720276932" ID="ID_1903091113" MODIFIED="1453720279453" TEXT="Otherwise">
<node CREATED="1453720324327" ID="ID_1927987168" MODIFIED="1453720360515" TEXT="Named Entities are classified further">
<node CREATED="1453720342838" ID="ID_1044303908" MODIFIED="1453720347244" TEXT="ORGANIZATION"/>
<node CREATED="1453720347555" ID="ID_1838733908" MODIFIED="1453720349280" TEXT="PERSON"/>
<node CREATED="1453720349579" ID="ID_1858723229" MODIFIED="1453720350773" TEXT="GPE"/>
<node CREATED="1453720351034" ID="ID_493767615" MODIFIED="1453720352918" TEXT="LOCATION"/>
<node CREATED="1453720353263" ID="ID_580734870" MODIFIED="1453720354281" TEXT="..."/>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1453720830672" ID="ID_817071684" MODIFIED="1453720834724" TEXT="Relation Extraction">
<node CREATED="1453720851741" ID="ID_747054377" MODIFIED="1453720872731" TEXT="Once a text has been chunked, relationships can be extracted using regexp"/>
<node CREATED="1453720881638" ID="ID_1628655412" MODIFIED="1453721390003" TEXT="IN = re.compile(r&apos;.*\bin\b(?!\b.+ing)&apos;)&#xa;for doc in nltk.corpus.ieer.parsed_docs(&apos;NYT_19980315&apos;):&#xa;&#x9;for rel in nltk.sem.extract_rels(&apos;ORG&apos;, &apos;LOC&apos;, doc, corpus=&apos;ieer&apos;, pattern = IN):&#xa;&#x9;&#x9;print(nltk.sem.rtuple(rel))">
<node CREATED="1453721035016" ID="ID_253846758" MODIFIED="1453721055047" TEXT="Trying to identify what ORGs are located in which LOCs"/>
<node CREATED="1453720933232" ID="ID_967123589" MODIFIED="1453721028070" TEXT="Regexp pattern">
<node CREATED="1453721029619" ID="ID_920447379" MODIFIED="1453721034175" TEXT="Any of the tags followed by any of the tags, given that it is not a gerung"/>
</node>
<node CREATED="1453721152234" ID="ID_1703468539" MODIFIED="1453721168114" TEXT="print(nltk.sem.rtuple(rel))">
<node CREATED="1453721193923" ID="ID_1801553131" MODIFIED="1453721195286" TEXT="[ORG: &apos;Bastille Opera&apos;] &apos;in&apos; [LOC: &apos;Paris&apos;]"/>
</node>
<node CREATED="1453721132724" FOLDED="true" ID="ID_1126102313" MODIFIED="1453721454800" TEXT="print(nltk.sem.clause(rel, relsym=&quot;IN&quot;))">
<node CREATED="1453721197938" ID="ID_356246267" MODIFIED="1453721250046" TEXT="IN(&apos;bastille_opera&apos;, &apos;paris&apos;)"/>
</node>
</node>
</node>
</node>
<node CREATED="1453977431555" FOLDED="true" ID="ID_264317425" MODIFIED="1453996166074" POSITION="right" TEXT="8. Analyzing Sentence Structure">
<node CREATED="1453983301970" ID="ID_1745393902" MODIFIED="1453983306290" TEXT="Caveats">
<node CREATED="1453982835558" ID="ID_1464289129" MODIFIED="1453982853814" TEXT="Sentences can have arbitrary length">
<node CREATED="1453982860136" ID="ID_1641495169" MODIFIED="1453982879360" TEXT="Sentence parse trees can have arbitrary depth">
<node CREATED="1453982880951" ID="ID_733804933" MODIFIED="1453982892325" TEXT="Chunking methods cannot be used"/>
<node CREATED="1453983229144" ID="ID_608403594" MODIFIED="1453983234788" TEXT="Grammars need be used instead"/>
</node>
</node>
<node CREATED="1453977447412" ID="ID_1934291955" MODIFIED="1453983244391" TEXT="Sentences are structurally ambiguous">
<node CREATED="1453983003075" ID="ID_587320096" MODIFIED="1453983277399" TEXT="Example: prepositional phrase attachment ambiguity">
<node CREATED="1453977456647" ID="ID_447158450" MODIFIED="1453977797476" TEXT="groucho_grammar = nltk.CFG.fromstring(&quot;&quot;&quot;&#xa;&#x9;S -&gt; NP VP&#xa;&#x9;PP -&gt; P NP&#xa;&#x9;NP -&gt; Det N | Det N PP | &apos;I&apos;&#xa;&#x9;VP -&gt; V NP | VP PP&#xa;&#x9;Det -&gt; &apos;an&apos; | &apos;my&apos;&#xa;&#x9;N -&gt; &apos;elephant&apos; | &apos;pajamas&apos;&#xa;&#x9;V -&gt; &apos;shot&apos;&#xa;&#x9;P -&gt; &apos;in&apos;&#xa;&#x9;&quot;&quot;&quot;)&#xa;sent = [&apos;I&apos;, &apos;shot&apos;, &apos;an&apos;, &apos;elephant&apos;, &apos;in&apos;, &apos;my&apos;, &apos;pajamas&apos;]&#xa;parser = nltk.ChartParser(groucho_grammar)&#xa;for tree in parser.parse(sent):&#xa;&#x9;print(tree)">
<node CREATED="1453977591152" ID="ID_1084330686" MODIFIED="1453977755923" TEXT="(S&#xa;&#x9;(NP I)&#xa;&#x9;(VP&#xa;&#x9;&#x9;(VP (V shot) (NP (Det an) (N elephant)))&#xa;&#x9;&#x9;(PP (P in) (NP (Det my) (N pajamas)))))&#xa;(S&#xa;&#x9;(NP I)&#xa;&#x9;(VP&#xa;&#x9;(V shot)&#xa;&#x9;&#x9;(NP (Det an) (N elephant) (PP (P in) (NP (Det my) (N pajamas))))))"/>
</node>
</node>
</node>
</node>
<node CREATED="1453983293077" ID="ID_1425608867" MODIFIED="1453983296453" TEXT="Grammars">
<node CREATED="1453983071286" ID="ID_1181392121" MODIFIED="1453983081817" TEXT="Saving grammars to file">
<node CREATED="1453983083398" ID="ID_1092908498" MODIFIED="1453983092222" TEXT="grammar = nltk.data.load(&apos;file:mygrammar.cfg&apos;)"/>
<node CREATED="1453983105681" ID="ID_1022114487" MODIFIED="1453983116697" TEXT="To confirm things are going as expected, turn trace on">
<node CREATED="1453983117754" ID="ID_1079183859" MODIFIED="1453983663165" TEXT="parser = nltk.ChartParser(grammar, trace=2)"/>
</node>
<node CREATED="1453983133493" ID="ID_605392485" MODIFIED="1453983141840" TEXT="To take a look nto the grammar">
<node CREATED="1453983149320" ID="ID_1799773124" MODIFIED="1453983150105" TEXT="for p in grammar1.productions(): print(p)"/>
</node>
</node>
<node CREATED="1453983314168" ID="ID_811744215" MODIFIED="1453983318366" TEXT="Recursive grammars">
<node CREATED="1453983363698" ID="ID_284369453" MODIFIED="1453983366678" TEXT="Direct recursion">
<node CREATED="1453983356034" ID="ID_290249643" MODIFIED="1453983361338" TEXT="Nom -&gt; Adj Nom | N"/>
</node>
<node CREATED="1453983370438" ID="ID_348868347" MODIFIED="1453983374016" TEXT="Indirect recursion">
<node CREATED="1453983380204" ID="ID_1028075568" MODIFIED="1453983393103" TEXT="S -&gt; NP VP&#xa;VP -&gt; V S"/>
</node>
<node CREATED="1453983665386" ID="ID_1770275087" MODIFIED="1453983685953" TEXT="recursive_parser=nltk.RecursiveDescentParser(grammar)"/>
</node>
</node>
<node CREATED="1453985163067" ID="ID_377008893" MODIFIED="1453991662618" TEXT="Context Free Grammars">
<node CREATED="1453991713073" ID="ID_1176536229" MODIFIED="1453991750772" TEXT="How word-types and sequences of words combine to form other sequences, and eventually sentences"/>
<node CREATED="1453985166836" ID="ID_1292143050" MODIFIED="1453985167935" TEXT="Recursive Descent Parsing">
<node CREATED="1453985168768" ID="ID_1479058580" MODIFIED="1453985170845" TEXT="Top down">
<node CREATED="1453985543178" ID="ID_1245132011" MODIFIED="1453985551795" TEXT="The grammar predicts how the parsing will take place"/>
</node>
<node CREATED="1453985789880" ID="ID_729500951" MODIFIED="1453985831099" TEXT="nltk.RecursiveDescentParser(grammar)"/>
<node CREATED="1453985171335" ID="ID_1516646511" MODIFIED="1453985238007" TEXT="The parser begins with a tree consisting of the root node S&#xa;At each stage it consults the grammar to find a production that can be used to enlarge the tree&#xa;When a lexical production is encountered, its word is compared against the input&#xa;After a complete parse has been found, the parser backtracks to look for more parses"/>
<node CREATED="1453985323133" ID="ID_51082543" MODIFIED="1453985324962" TEXT="Caveats">
<node CREATED="1453985326153" ID="ID_1138777125" MODIFIED="1453985353712" TEXT="Cannot handle left-recursive productions like NP -&gt; NP PP">
<node CREATED="1453985355357" ID="ID_1809229213" MODIFIED="1453985359870" TEXT="Infinite loop"/>
</node>
<node CREATED="1453985360838" ID="ID_1166814339" MODIFIED="1453985408369" TEXT="A lot of time is wasted considering structures that do not correspond to the input sentence">
<node CREATED="1453985411305" ID="ID_138799883" MODIFIED="1453985425416" TEXT="It search is grammar-complete"/>
</node>
<node CREATED="1453985439260" ID="ID_819305615" MODIFIED="1453985447622" TEXT="Backtracking process may discard parsed constituents that will need to be rebuilt again later">
<node CREATED="1453985484323" ID="ID_59578790" MODIFIED="1453985532524" TEXT="Backtracking from VP -&gt; V NP will discard the NP subtree. If VP -&gt; V NP PP is then explored, the subtree will be computed again"/>
</node>
</node>
</node>
<node CREATED="1453985572036" ID="ID_1752285071" MODIFIED="1453985573201" TEXT="Shift-Reduce Parsing">
<node CREATED="1453985575011" ID="ID_1520346874" MODIFIED="1453987755307" TEXT="Bottom up">
<node CREATED="1453985603095" ID="ID_291454933" MODIFIED="1453985628830" TEXT="Find sequences of words that correspond to the right hand side of a grammar production, and replace them with the left-hand side, until the whole sentence is reduced to the root S"/>
</node>
<node CREATED="1453985833550" ID="ID_513008528" MODIFIED="1453985845728" TEXT="nltk.ShiftReduceParser(grammar)"/>
<node CREATED="1453985848427" ID="ID_1899132144" MODIFIED="1453985957801" TEXT="The parser begins with the first word in the stack and tries to find a higher level entity that matches with it&#xa;If none is found, the next word is added to the stack, and the complete stack is treated as another sentence to be parsed"/>
<node CREATED="1453986021415" ID="ID_544812742" MODIFIED="1453986023562" TEXT="Caveats">
<node CREATED="1453986047060" ID="ID_957341374" MODIFIED="1453986058688" TEXT="Backtracking is very difficult to implement">
<node CREATED="1453986060412" ID="ID_1964053018" MODIFIED="1453986070827" TEXT="The parser may fail to find a parse, even if one exists"/>
<node CREATED="1453986071153" ID="ID_288542670" MODIFIED="1453986082037" TEXT="The parser will only find one parse, even if many exist"/>
</node>
</node>
</node>
<node CREATED="1453986149879" ID="ID_230953403" MODIFIED="1453986157514" TEXT="Left-Corner Parsing">
<node CREATED="1453986159032" ID="ID_139674516" MODIFIED="1453986161281" TEXT="Hybrid">
<node CREATED="1453986237301" ID="ID_1839710318" MODIFIED="1453986269713" TEXT="Filters top-down grammar rules and selects those that can result in the actual input"/>
<node CREATED="1453986294598" ID="ID_457512148" MODIFIED="1453986306409" TEXT="Does not get trapped in left-recursive productions"/>
</node>
<node CREATED="1453986795336" ID="ID_957994314" MODIFIED="1453986935603" TEXT="An allowed production starters table is created for each non terminal production&#xa;For a production to be considered by the parser, the next input word must be compatible with at least one of the allowed production starters"/>
</node>
<node CREATED="1453987738277" ID="ID_1239553959" MODIFIED="1453987741719" TEXT="Chart Parsing">
<node CREATED="1453987743146" ID="ID_421916723" MODIFIED="1453987794091" TEXT="Technique that stores intermediate groups so that they do not need to be computed again"/>
<node CREATED="1453987794679" ID="ID_1734183882" MODIFIED="1453987814702" TEXT="Depending on the implementation, it behaves like a bottom up parser"/>
<node CREATED="1453988212029" FOLDED="true" ID="ID_1639502592" MODIFIED="1453989317360" TEXT="Example">
<node CREATED="1453977456647" ID="ID_1800154332" MODIFIED="1453988587285" TEXT="groucho_grammar = nltk.CFG.fromstring(&quot;&quot;&quot;&#xa;&#x9;S -&gt; NP VP&#xa;&#x9;PP -&gt; P NP&#xa;&#x9;NP -&gt; Det N | Det N PP | &apos;I&apos;&#xa;&#x9;VP -&gt; V NP | VP PP&#xa;&#x9;Det -&gt; &apos;an&apos; | &apos;my&apos;&#xa;&#x9;N -&gt; &apos;elephant&apos; | &apos;pajamas&apos;&#xa;&#x9;V -&gt; &apos;shot&apos;&#xa;&#x9;P -&gt; &apos;in&apos;&#xa;&#x9;&quot;&quot;&quot;)&#xa;sent = [&apos;I&apos;, &apos;shot&apos;, &apos;an&apos;, &apos;elephant&apos;, &apos;in&apos;, &apos;my&apos;, &apos;pajamas&apos;]"/>
<node CREATED="1453988220902" ID="ID_1790222004" MODIFIED="1453988381379" TEXT="Construct a table (a triangular matrix, really), with the production of each word in the diagonal">
<node CREATED="1453988286310" ID="ID_164844921" MODIFIED="1453988376361" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    .    .    .    .&#xa;1    .    V    .    .    .    .    .&#xa;2    .    .    Det  .    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    .&#xa;5    .    .    .    .    .    Det  .&#xa;6    .    .    .    .    .    .    N"/>
<node CREATED="1453988384245" ID="ID_1189629934" MODIFIED="1453988403172" TEXT="The lines are where the chunk starts, the columns where it ends">
<node CREATED="1453988404522" ID="ID_667226090" MODIFIED="1453988460562" TEXT="(0,1) -&gt; &apos;I&apos;"/>
<node CREATED="1453988417671" ID="ID_776639546" MODIFIED="1453988456188" TEXT="(3,7) -&gt; &apos;elephant in my pajamas&apos;"/>
</node>
</node>
<node CREATED="1453988469211" ID="ID_912603831" MODIFIED="1453989265515" TEXT="For each pair of lines, search for rules that map to &apos;any group of line i&apos; + &apos;the last group of line i+1&apos;">
<node CREATED="1453988646630" ID="ID_1708923127" MODIFIED="1453988662518" TEXT="Line 0 -&gt; NP + V (no rule)"/>
<node CREATED="1453988663097" ID="ID_569177090" MODIFIED="1453988753382" TEXT="Line 2 -&gt; Det (2,3) + N (3,4) =&gt; NP to be populated in (2,4)">
<node CREATED="1453988286310" ID="ID_1715349726" MODIFIED="1453988984433" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    .    .    .    .&#xa;1    .    V    .    .    .    .    .&#xa;2    .    .    Det  NP    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    .&#xa;5    .    .    .    .    .    Det  .&#xa;6    .    .    .    .    .    .    N"/>
</node>
<node CREATED="1453989036070" ID="ID_1190502848" MODIFIED="1453989082462" TEXT="[end of pass 1]">
<node CREATED="1453988286310" ID="ID_642037068" MODIFIED="1453989066940" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    .    .    .    .&#xa;1    .    V    .    .    .    .    .&#xa;2    .    .    Det  NP    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    .&#xa;5    .    .    .    .    .    Det  NP&#xa;6    .    .    .    .    .    .    N"/>
</node>
</node>
<node CREATED="1453989046046" ID="ID_1045252042" MODIFIED="1453989050246" TEXT="Repeat">
<node CREATED="1453989071221" ID="ID_1947575032" MODIFIED="1453989076423" TEXT="[end of pass 2]">
<node CREATED="1453988286310" ID="ID_1851597367" MODIFIED="1453989112495" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    .    .    .    .&#xa;1    .    V    .    VP    .    .    .&#xa;2    .    .    Det  NP    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    PP&#xa;5    .    .    .    .    .    Det  NP&#xa;6    .    .    .    .    .    .    N"/>
</node>
<node CREATED="1453989071221" ID="ID_341751217" MODIFIED="1453989124917" TEXT="[end of pass 3]">
<node CREATED="1453988286310" ID="ID_1883969249" MODIFIED="1453989164996" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    S    .    .    .&#xa;1    .    V    .    VP    .    .    VP&#xa;2    .    .    Det  NP    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    PP&#xa;5    .    .    .    .    .    Det  NP&#xa;6    .    .    .    .    .    .    N"/>
</node>
<node CREATED="1453989071221" ID="ID_1023358378" MODIFIED="1453989275733" TEXT="[end of pass 4]">
<node CREATED="1453988286310" ID="ID_1236809839" MODIFIED="1453989284435" TEXT="     1    2    3    4    5    6    7&#xa;0    NP   .    .    S    .    .    S&#xa;1    .    V    .    VP    .    .    VP&#xa;2    .    .    Det  NP    .    .    .&#xa;3    .    .    .    N    .    .    .&#xa;4    .    .    .    .    P    .    PP&#xa;5    .    .    .    .    .    Det  NP&#xa;6    .    .    .    .    .    .    N"/>
</node>
<node CREATED="1453989308160" ID="ID_944442112" MODIFIED="1453989311814" TEXT="Done!"/>
</node>
</node>
<node CREATED="1453988187317" ID="ID_141194393" MODIFIED="1453988189321" TEXT="Caveats">
<node CREATED="1453989322368" ID="ID_224900152" MODIFIED="1453989354039" TEXT="It is not a parser - it only recognizes that a sentence is admitted by a grammar"/>
<node CREATED="1453989366661" ID="ID_1092640767" MODIFIED="1453989375979" TEXT="Non-lexical productions have to be binary"/>
<node CREATED="1453989383195" ID="ID_1918799302" MODIFIED="1453989403813" TEXT="Does not handle ambiguity"/>
</node>
<node CREATED="1453989415917" ID="ID_1512380822" MODIFIED="1453989449454" TEXT="Chart parsing is a family of methods, some of which can tackle these caveats"/>
</node>
</node>
<node CREATED="1453991681527" ID="ID_1802950060" MODIFIED="1453991687146" TEXT="Dependency Grammars">
<node CREATED="1453991754966" ID="ID_1674592344" MODIFIED="1453991768225" TEXT="How words relate to other words">
<node CREATED="1453991781397" ID="ID_219074504" MODIFIED="1453991883941" TEXT="Dependency is a binary asymmetric relation that holds between a &apos;Head&apos; and its &apos;Dependents&apos;"/>
<node CREATED="1453991795421" ID="ID_728769796" MODIFIED="1453991818892" TEXT="Dependency representation -&gt; Labeled directed graph"/>
<node CREATED="1453991857045" ID="ID_462798692" MODIFIED="1453991873829" TEXT="How to determine the &apos;Head&apos;">
<node CREATED="1453991892814" ID="ID_1364475222" MODIFIED="1453991905207" TEXT="Determines the class of the construction"/>
<node CREATED="1453991908729" ID="ID_1049703242" MODIFIED="1453991919985" TEXT="Determines the semantic type of the dependent"/>
<node CREATED="1453991928443" ID="ID_1548592562" MODIFIED="1453991942520" TEXT="Is obligatory, as opposed to the dependent"/>
<node CREATED="1453991943060" ID="ID_436482246" MODIFIED="1453991963499" TEXT="Selects the dependent and determines whether it is obligatory or not"/>
<node CREATED="1453991967712" ID="ID_1094000970" MODIFIED="1453991976625" TEXT="Determines the morphological form of the dependent">
<node CREATED="1453991981811" ID="ID_1449179306" MODIFIED="1453991983943" TEXT="Agreement"/>
</node>
</node>
<node CREATED="1453991988553" ID="ID_1100066085" MODIFIED="1453991998395" TEXT="In English, sentence heads are usually verbs"/>
</node>
<node CREATED="1453992006391" ID="ID_1238427246" MODIFIED="1453992011441" TEXT="Example">
<node CREATED="1453992025438" ID="ID_501678696" MODIFIED="1453992327164" TEXT="I shot an elephant in my pajamas">
<node CREATED="1453992042948" ID="ID_382866486" MODIFIED="1453992050186" TEXT="Head: shot">
<node CREATED="1453992058588" ID="ID_1550717544" MODIFIED="1453992065811" TEXT="-&gt; Subject: I"/>
<node CREATED="1453992212715" ID="ID_742257687" MODIFIED="1453992225880" TEXT="-&gt; Object: an elephant in my pajamas">
<node CREATED="1453992066246" ID="ID_1662299923" MODIFIED="1453992235285" TEXT="Head: elephant">
<node CREATED="1453992130499" ID="ID_207286156" MODIFIED="1453992147282" TEXT="-&gt; Determinant modifier: an"/>
<node CREATED="1453992148122" ID="ID_266565095" MODIFIED="1453992260419" TEXT="-&gt; Noun modifier: in my pajamas">
<node CREATED="1453992263695" ID="ID_1529465604" MODIFIED="1453992268803" TEXT="Head: in">
<node CREATED="1453992274505" ID="ID_305409468" MODIFIED="1453992289334" TEXT="-&gt; Prepositional modifier: my pajamas">
<node CREATED="1453992292513" ID="ID_634258258" MODIFIED="1453992297290" TEXT="Head: pajamas">
<node CREATED="1453992298588" ID="ID_1325945544" MODIFIED="1453992315547" TEXT="-&gt; Determinant modifier: my"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1453992442359" ID="ID_1733356967" MODIFIED="1453992509973" TEXT="groucho_dep_grammar = nltk.DependencyGrammar.fromstring(&quot;&quot;&quot;&#xa;&#x9;&apos;shot&apos; -&gt; &apos;I&apos; | &apos;elephant&apos; | &apos;in&apos;&#xa;&#x9;&apos;elephant&apos; -&gt; &apos;an&apos; | &apos;in&apos;&#xa;&#x9;&apos;in&apos; -&gt; &apos;pajamas&apos;&#xa;&#x9;&apos;pajamas&apos; -&gt; &apos;my&apos;&#xa;&#x9;&quot;&quot;&quot;)&#xa;pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)&#xa;sent = &apos;I shot an elephant in my pajamas&apos;.split()&#xa;trees = pdp.parse(sent)&#xa;for tree in trees:&#xa;&#x9;print(tree)">
<node CREATED="1453992511720" ID="ID_1453987097" MODIFIED="1453992521087" TEXT="(shot I (elephant an (in (pajamas my))))&#xa;(shot I (elephant an) (in (pajamas my)))"/>
</node>
</node>
<node CREATED="1453992357884" ID="ID_363071515" MODIFIED="1453992392057" TEXT="A dependency graph is projective if, when all the words are written in linear order, the edges can be drawn above the words without crossing">
<node CREATED="1453992410688" ID="ID_1099509658" MODIFIED="1453992417562" TEXT="A word and all its descendents (dependents and dependents of its dependents, etc.) form a contiguous sequence of words within the sentence"/>
</node>
<node CREATED="1453992533550" ID="ID_1002773150" MODIFIED="1453992556910" TEXT="This approach seems unnatural, but it is very close to context free grammars">
<node CREATED="1453992559221" ID="ID_1641406260" MODIFIED="1453992625067" TEXT="Saying PP -&gt; P NP implicitly assigns head and dependent relationships"/>
</node>
<node CREATED="1453992723526" ID="ID_249736978" MODIFIED="1453992726558" TEXT="Valencies">
<node CREATED="1453992735512" ID="ID_1466445774" MODIFIED="1453992748888" TEXT="Complements that the different heads actually accept">
<node CREATED="1453992759210" ID="ID_1074268076" MODIFIED="1453992788552" TEXT="&apos;was&apos; accepts [Adjectives] but not [Sentences]">
<node CREATED="1453992814114" ID="ID_818305989" MODIFIED="1453992839413" TEXT="The squirrell was frightened"/>
<node CREATED="1453992840483" ID="ID_831498143" MODIFIED="1453992849255" TEXT="The squirrell was Buster was angry">
<node CREATED="1453992851209" ID="ID_1858077042" MODIFIED="1453992853287" TEXT="Invalid"/>
</node>
</node>
<node CREATED="1453992792478" ID="ID_173165135" MODIFIED="1453992809117" TEXT="&apos;thought&apos; accepts [Sentences] but not [Adjectives]">
<node CREATED="1453992829443" ID="ID_1735976456" MODIFIED="1453992830821" TEXT="&#x9;Chatterer thought Buster was angry"/>
<node CREATED="1453992854432" ID="ID_109713301" MODIFIED="1453992864600" TEXT="Chatterer thought frightened">
<node CREATED="1453992865456" ID="ID_232529868" MODIFIED="1453992867354" TEXT="Invalid"/>
</node>
</node>
</node>
<node CREATED="1453992869334" ID="ID_545884455" MODIFIED="1453992891979" TEXT="The set of valencies of a dependency grammar is actually fairly restrictive"/>
<node CREATED="1453992966264" ID="ID_1505657198" MODIFIED="1453992998219" TEXT="New classes can be defined to group heads with the same valencies">
<node CREATED="1453993008395" ID="ID_520819314" MODIFIED="1453993012834" TEXT="Intransitive verbs"/>
<node CREATED="1453993000727" ID="ID_1286417667" MODIFIED="1453993004883" TEXT="Transitive verbs">
<node CREATED="1453993038559" ID="ID_1662303604" MODIFIED="1453993052157" TEXT="TVP -&gt; TV NP"/>
<node CREATED="1453993056907" ID="ID_323683416" MODIFIED="1453993074001" TEXT="TV -&gt; &apos;saw&apos; | &apos;chased&apos;"/>
<node CREATED="1453993076774" ID="ID_692610099" MODIFIED="1453993104274" TEXT="&apos;saw the dog&apos; and &apos;chased the dog&apos; are valid Transitive VPs"/>
</node>
<node CREATED="1453993014471" ID="ID_812262422" MODIFIED="1453993016970" TEXT="Dative verbs"/>
<node CREATED="1453993020091" ID="ID_1867907525" MODIFIED="1453993022718" TEXT="Sentential verbs"/>
</node>
</node>
<node CREATED="1453994023328" ID="ID_799339105" MODIFIED="1453994029251" TEXT="Modifiers/adjuncts">
<node CREATED="1453994033294" ID="ID_1168932994" MODIFIED="1453994058152" TEXT="A different kind of dependent than complements">
<node CREATED="1453994068013" ID="ID_1723606857" MODIFIED="1453994074883" TEXT="Prepositional phrases"/>
<node CREATED="1453994077195" ID="ID_787036466" MODIFIED="1453994079510" TEXT="Adjectives"/>
<node CREATED="1453994079846" ID="ID_1427391327" MODIFIED="1453994081937" TEXT="Adverbs"/>
</node>
<node CREATED="1453994087212" ID="ID_1715261316" MODIFIED="1453994094307" TEXT="They are always optional"/>
<node CREATED="1453994098187" ID="ID_639080881" MODIFIED="1453994101604" TEXT="Can be iterated"/>
<node CREATED="1453994107536" ID="ID_1899365260" MODIFIED="1453994116781" TEXT="Their relationship with the head is &apos;looser&apos;"/>
</node>
</node>
<node CREATED="1453994135691" ID="ID_1139474777" MODIFIED="1453994140444" TEXT="Scaling grammars up">
<node CREATED="1453994372518" ID="ID_389008222" MODIFIED="1453994428178" TEXT="Fully annotated corpuses can be used to develop a grammar">
<node CREATED="1453994429692" ID="ID_1223650950" MODIFIED="1453994463823" TEXT="nltk.corpus.treebank.parsed_sents(&apos;wsj_0001.mrg&apos;)[0]">
<node CREATED="1453994555700" ID="ID_1954402667" MODIFIED="1453994592142" TEXT="Can be used to construct context free grammar rules or to find which verbs usually follow which rule"/>
<node CREATED="1453994465099" ID="ID_1951214545" MODIFIED="1453994515439" TEXT="(S&#xa;&#x9;(NP-SBJ&#xa;&#x9;&#x9;(NP (NNP Pierre) (NNP Vinken))&#xa;&#x9;&#x9;(, ,)&#xa;&#x9;&#x9;(ADJP (NP (CD 61) (NNS years)) (JJ old))&#xa;&#x9;&#x9;(, ,))&#xa;&#x9;(VP&#xa;&#x9;&#x9;(MD will)&#xa;&#x9;&#x9;(VP&#xa;      &#x9;&#x9;&#x9;(VB join)&#xa;&#x9;&#x9;&#x9;(NP (DT the) (NN board))&#xa;&#x9;&#x9;&#x9;(PP-CLR&#xa;&#x9;&#x9;&#x9;&#x9;(IN as)&#xa;&#x9;&#x9;&#x9;&#x9;(NP (DT a) (JJ nonexecutive) (NN director)))&#xa;&#x9;&#x9;(NP-TMP (NNP Nov.) (CD 29))))&#xa;&#x9;(. .))"/>
</node>
<node CREATED="1453994547014" ID="ID_1267423389" MODIFIED="1453994548290" TEXT="nltk.corpus.ppattach.attachments(&apos;training&apos;)">
<node CREATED="1453994598844" ID="ID_1690478766" MODIFIED="1453994616791" TEXT="Can be used to determine the valency of a verb"/>
<node CREATED="1453994811982" ID="ID_1196667566" MODIFIED="1453994981389" TEXT="PPAttachment(sent=&apos;0&apos;, verb=&apos;rejected&apos;, noun1=&apos;offer&apos;, prep=&apos;from&apos;, noun2=&apos;group&apos;, attachment=&apos;N&apos;),&#xa;PPAttachment(sent=&apos;1&apos;, verb=&apos;received&apos;, noun1=&apos;offer&apos;, prep=&apos;from&apos;, noun2=&apos;group&apos;, attachment=&apos;V&apos;),">
<node CREATED="1453994955338" ID="ID_110221112" MODIFIED="1453995016157" TEXT="&apos;received&apos; expects a clarification to the &apos;offer from group&apos; (hence the &apos;V&apos;)"/>
<node CREATED="1453995005706" ID="ID_361391159" MODIFIED="1453995033488" TEXT="&apos;rejected&apos; does not; in this case &apos;offer from group&apos; is a complete NP"/>
</node>
</node>
<node CREATED="1453995075975" ID="ID_1102619865" MODIFIED="1453995099150" TEXT="large_grammars package">
<node CREATED="1453995087401" ID="ID_980882852" MODIFIED="1453995095485" TEXT="Much larger grammars to compare parsers"/>
<node CREATED="1453995100025" ID="ID_1270759091" MODIFIED="1453995107142" TEXT="Needs to be downloaded separately"/>
</node>
<node CREATED="1453995122300" ID="ID_1154098443" MODIFIED="1453995123502" TEXT="nltk.corpus.sinica_treebank.parsed_sents()">
<node CREATED="1453995126223" ID="ID_720339651" MODIFIED="1453995133031" TEXT="Fully annotated corpus in Chinese"/>
</node>
</node>
<node CREATED="1453995525249" ID="ID_145161641" MODIFIED="1453995532668" TEXT="The challenges, however, are humongous">
<node CREATED="1453994142846" ID="ID_569672666" MODIFIED="1453994154820" TEXT="Constructing a real grammar is a very hard problem">
<node CREATED="1453994189717" ID="ID_1274574583" MODIFIED="1453994197565" TEXT="It is hard to modularize"/>
<node CREATED="1453994198009" ID="ID_1553879651" MODIFIED="1453995296703" TEXT="Ambiguity increases exponentially with coverage">
<node CREATED="1453995300612" ID="ID_1184664877" MODIFIED="1453995306234" TEXT="And with it the number of rules"/>
</node>
</node>
<node CREATED="1453995259356" ID="ID_347128699" MODIFIED="1453995269040" TEXT="Applying a real grammar is also a very hard problem">
<node CREATED="1453995270119" ID="ID_680601088" MODIFIED="1453995290687" TEXT="Ambiguity increases exponentially with length">
<node CREATED="1453995307650" ID="ID_1515267206" MODIFIED="1453995317106" TEXT="And with it the number of potential parses"/>
</node>
</node>
<node CREATED="1453995395419" ID="ID_796831594" MODIFIED="1453995411103" TEXT="Semantic ambiguity is to be added on top of it all">
<node CREATED="1453995417913" ID="ID_1825178212" MODIFIED="1453995444178" TEXT="The word representing a verb is also the word representing the word representing a verb">
<node CREATED="1453995445366" ID="ID_1607801884" MODIFIED="1453995498529" TEXT="All verbs could be nouns"/>
</node>
<node CREATED="1453995480058" ID="ID_1342440618" MODIFIED="1453995492982" TEXT="Similarly, it is possible to verbalize many nouns"/>
</node>
</node>
<node CREATED="1453995541088" ID="ID_55211149" MODIFIED="1453995552826" TEXT="Probabilistic grammars have been developed to tackle the ambiguity"/>
</node>
<node CREATED="1453995589569" ID="ID_1103722693" MODIFIED="1453995593923" TEXT="Probabilistic grammars">
<node CREATED="1453995740826" ID="ID_1379163550" MODIFIED="1453995755349" TEXT="Probabilistic context free grammar">
<node CREATED="1453995758756" ID="ID_884123399" MODIFIED="1453995771630" TEXT="Assigns a probability to each of the productions"/>
</node>
<node CREATED="1453995872377" ID="ID_59211530" MODIFIED="1453995881017" TEXT="These probabilities do exist">
<node CREATED="1453995882278" ID="ID_1980306952" MODIFIED="1453995901402" TEXT="&apos;give&apos; tends to be followed by the shorter object first">
<node CREATED="1453995902676" ID="ID_700232402" MODIFIED="1453995907602" TEXT="Give me the cookie">
<node CREATED="1453995923417" ID="ID_677477308" MODIFIED="1453995931720" TEXT="Specially when one of the objects is a pronoun"/>
</node>
<node CREATED="1453995911111" ID="ID_1383959466" MODIFIED="1453995922316" TEXT="Give the cookie to the children"/>
</node>
<node CREATED="1453995934126" ID="ID_203810504" MODIFIED="1453995947466" TEXT="However, not always - other factors also play a role">
<node CREATED="1453995948572" ID="ID_833499021" MODIFIED="1453995975346" TEXT="Give the Government officials a raise">
<node CREATED="1453995978789" ID="ID_1801139473" MODIFIED="1453995997419" TEXT="Animosity seems to play a very important role"/>
</node>
</node>
<node CREATED="1453996001568" ID="ID_1102419440" MODIFIED="1453996007486" TEXT="They can also be extracted from corpora"/>
</node>
<node CREATED="1453995772482" ID="ID_555407561" MODIFIED="1453996082019" TEXT="grammar = nltk.PCFG.fromstring(&quot;&quot;&quot;&#xa;&#x9;S    -&gt; NP VP              [1.0]&#xa;&#x9;VP   -&gt; TV NP              [0.4]&#xa;&#x9;VP   -&gt; IV                 [0.3]&#xa;&#x9;VP   -&gt; DatV NP NP         [0.3]&#xa;&#x9;TV   -&gt; &apos;saw&apos;              [1.0]&#xa;&#x9;IV   -&gt; &apos;ate&apos;              [1.0]&#xa;&#x9;DatV -&gt; &apos;gave&apos;             [1.0]&#xa;&#x9;NP   -&gt; &apos;telescopes&apos;       [0.8]&#xa;&#x9;NP   -&gt; &apos;Jack&apos;             [0.2]&#xa;&#x9;&quot;&quot;&quot;)&#xa;viterbi_parser = nltk.ViterbiParser(grammar)&#xa;for tree in viterbi_parser.parse([&apos;Jack&apos;, &apos;saw&apos;, &apos;telescopes&apos;]):&#xa;&#x9;print(tree)">
<node CREATED="1453996094782" ID="ID_267638219" MODIFIED="1453996096219" TEXT="(S (NP Jack) (VP (TV saw) (NP telescopes))) (p=0.064)"/>
<node CREATED="1453995826662" ID="ID_827580493" MODIFIED="1453995840469" TEXT="Please note all &apos;VP&apos; should add to 1">
<node CREATED="1453995849039" ID="ID_840043891" MODIFIED="1453995849990" TEXT="VP -&gt; TV NP [0.4] | IV [0.3] | DatV NP NP [0.3]"/>
</node>
</node>
</node>
</node>
<node CREATED="1455031881049" FOLDED="true" ID="ID_1764620401" MODIFIED="1456727127271" POSITION="right" TEXT="9. Building Feature Based Grammars">
<node CREATED="1455034050238" ID="ID_56365819" MODIFIED="1455034060977" TEXT="Reading grammars from files">
<node CREATED="1455034103289" ID="ID_1658904718" MODIFIED="1455034110769" TEXT="nltk.data.load([path_to_grammar])"/>
<node CREATED="1455034112242" ID="ID_844236618" MODIFIED="1455034137992" TEXT="It should start with &apos;% start S&apos;">
<node CREATED="1455034140130" ID="ID_655806991" MODIFIED="1455034149054" TEXT="Means the root node is &apos;S&apos;"/>
</node>
</node>
<node CREATED="1455032585380" ID="ID_237359359" MODIFIED="1455032612431" TEXT="Grammars must multiply in size to accomodate certain basic linguistic principles">
<node CREATED="1455032613701" ID="ID_614172493" MODIFIED="1455032616916" TEXT="Agreement">
<node CREATED="1455032618301" ID="ID_1955482731" MODIFIED="1455032663730" TEXT="This dog runs">
<node CREATED="1455032624490" ID="ID_1918807402" MODIFIED="1455032626588" TEXT="Correct"/>
</node>
<node CREATED="1455032627365" ID="ID_259721423" MODIFIED="1455032674451" TEXT="This dogs runs">
<node CREATED="1455032633071" ID="ID_5565816" MODIFIED="1455032635319" TEXT="Incorrect"/>
</node>
<node CREATED="1455032641601" ID="ID_1916548213" MODIFIED="1455034088552" TEXT="Normal grammar including agreement">
<node CREATED="1455032709413" ID="ID_485311494" MODIFIED="1455032717081" TEXT="S -&gt; NP_SG VP_SG&#xa;S -&gt; NP_PL VP_PL&#xa;NP_SG -&gt; Det_SG N_SG&#xa;NP_PL -&gt; Det_PL N_PL&#xa;VP_SG -&gt; V_SG&#xa;VP_PL -&gt; V_PL&#xa;&#xa;Det_SG -&gt; &apos;this&apos;&#xa;Det_PL -&gt; &apos;these&apos;&#xa;N_SG -&gt; &apos;dog&apos;&#xa;N_PL -&gt; &apos;dogs&apos;&#xa;V_SG -&gt; &apos;runs&apos;&#xa;V_PL -&gt; &apos;run&apos;">
<node CREATED="1455032728458" ID="ID_873055413" MODIFIED="1455032734595" TEXT="The grammar doubled in size"/>
</node>
</node>
</node>
<node CREATED="1455032735931" ID="ID_56846386" MODIFIED="1455034046045" TEXT="This can be avoided if tokens are allowed to have properties">
<node CREATED="1455032783877" ID="ID_52731999" MODIFIED="1455033569789" TEXT="Tokens (or categories) become &apos;dictionaries&apos;">
<node CREATED="1455033519274" ID="ID_1950723575" MODIFIED="1455033520732" TEXT="kim = {&apos;CAT&apos;: &apos;NP&apos;, &apos;ORTH&apos;: &apos;Kim&apos;, &apos;REF&apos;: &apos;k&apos;}">
<node CREATED="1455033735243" ID="ID_402224287" MODIFIED="1455033757537" TEXT="This is more descriptive and provides interesting options"/>
</node>
</node>
<node CREATED="1455033528068" ID="ID_1892848590" MODIFIED="1455033533998" TEXT="Expanded grammar">
<node CREATED="1455033585447" ID="ID_129088151" MODIFIED="1455033638981" TEXT="S -&gt; NP[NUM=?n] VP[NUM=?n]&#xa;NP[NUM=?n] -&gt; Det[NUM=?n] N[NUM=?n]&#xa;VP[NUM=?n] -&gt; V[NUM=?n]&#xa;&#xa;Det[NUM=sg] -&gt; &apos;this&apos;&#xa;Det[NUM=pl] -&gt; &apos;these&apos;&#xa;N[NUM=sg] -&gt; &apos;dog&apos;&#xa;N[NUM=pl] -&gt; &apos;dogs&apos;&#xa;V[NUM=sg] -&gt; &apos;runs&apos;&#xa;V[NUM=pl] -&gt; &apos;run&apos;">
<node CREATED="1455033649148" ID="ID_1756922879" MODIFIED="1455033658876" TEXT="At least the non-terminal grammar stays the same"/>
<node CREATED="1455033769454" ID="ID_1479798140" MODIFIED="1455033804952" TEXT="The items from the terminal grammar that do not need to change also stay the same">
<node CREATED="1455033815417" ID="ID_721507502" MODIFIED="1455033816889" TEXT="Det[NUM=?n] -&gt; &apos;the&apos; | &apos;some&apos; | &apos;any&apos;"/>
</node>
</node>
</node>
<node CREATED="1455033870436" ID="ID_345698544" MODIFIED="1455033972739" TEXT="More features (such as verb tense) can be added">
<node CREATED="1455033952176" ID="ID_721490635" MODIFIED="1455033958027" TEXT="# ###################&#xa;# Grammar Productions&#xa;# ###################&#xa;# S expansion productions&#xa;S -&gt; NP[NUM=?n] VP[NUM=?n]&#xa;# NP expansion productions&#xa;NP[NUM=?n] -&gt; N[NUM=?n]&#xa;NP[NUM=?n] -&gt; PropN[NUM=?n]&#xa;NP[NUM=?n] -&gt; Det[NUM=?n] N[NUM=?n]&#xa;NP[NUM=pl] -&gt; N[NUM=pl]&#xa;# VP expansion productions&#xa;VP[TENSE=?t, NUM=?n] -&gt; IV[TENSE=?t, NUM=?n]&#xa;VP[TENSE=?t, NUM=?n] -&gt; TV[TENSE=?t, NUM=?n] NP&#xa;# ###################&#xa;# Lexical Productions&#xa;# ###################&#xa;Det[NUM=sg] -&gt; &apos;this&apos; | &apos;every&apos;&#xa;Det[NUM=pl] -&gt; &apos;these&apos; | &apos;all&apos;&#xa;Det -&gt; &apos;the&apos; | &apos;some&apos; | &apos;several&apos;&#xa;PropN[NUM=sg]-&gt; &apos;Kim&apos; | &apos;Jody&apos;&#xa;N[NUM=sg] -&gt; &apos;dog&apos; | &apos;girl&apos; | &apos;car&apos; | &apos;child&apos;&#xa;N[NUM=pl] -&gt; &apos;dogs&apos; | &apos;girls&apos; | &apos;cars&apos; | &apos;children&apos;&#xa;IV[TENSE=pres,  NUM=sg] -&gt; &apos;disappears&apos; | &apos;walks&apos;&#xa;TV[TENSE=pres, NUM=sg] -&gt; &apos;sees&apos; | &apos;likes&apos;&#xa;IV[TENSE=pres,  NUM=pl] -&gt; &apos;disappear&apos; | &apos;walk&apos;&#xa;TV[TENSE=pres, NUM=pl] -&gt; &apos;see&apos; | &apos;like&apos;&#xa;IV[TENSE=past] -&gt; &apos;disappeared&apos; | &apos;walked&apos;&#xa;TV[TENSE=past] -&gt; &apos;saw&apos; | &apos;liked&apos;"/>
</node>
<node CREATED="1455033973377" ID="ID_1563440335" MODIFIED="1455033989273" TEXT="The number of categories is arbitrary"/>
</node>
</node>
<node CREATED="1455034462876" ID="ID_203667544" MODIFIED="1455034470292" TEXT="Feature based grammars">
<node CREATED="1455035370898" ID="ID_1424927967" MODIFIED="1455035377132" TEXT="Feature Structures">
<node CREATED="1455035344261" ID="ID_123880976" MODIFIED="1455035352135" TEXT="Very similar to dictionaries"/>
<node CREATED="1455035380750" ID="ID_306272730" MODIFIED="1455035412889" TEXT="Can be used to describe entities other than linguistic objects"/>
</node>
<node CREATED="1455034471373" ID="ID_822913725" MODIFIED="1455034477670" TEXT="Additional notation">
<node CREATED="1455034482359" ID="ID_445422995" MODIFIED="1455034487287" TEXT="Boolean features">
<node CREATED="1455034543825" ID="ID_621942895" MODIFIED="1455034551937" TEXT="&apos;Can&apos; is an &apos;auxiliary&apos;">
<node CREATED="1455034488456" ID="ID_121665421" MODIFIED="1455034526677" TEXT="V[TENSE=pres, AUX=true] -&gt; &apos;can&apos;"/>
<node CREATED="1455034488456" ID="ID_522507424" MODIFIED="1455034568841" TEXT="V[TENSE=pres, AUX=+] -&gt; &apos;can&apos;"/>
<node CREATED="1455034488456" ID="ID_1971187562" MODIFIED="1455034574461" TEXT="V[TENSE=pres, +AUX] -&gt; &apos;can&apos;">
<node CREATED="1455034575479" ID="ID_1322389987" MODIFIED="1455034583435" TEXT="In practice this one is used"/>
</node>
</node>
</node>
<node CREATED="1455035064659" ID="ID_311543399" MODIFIED="1455035068269" TEXT="Bundled features">
<node CREATED="1455035069502" ID="ID_1823897131" MODIFIED="1455035126533" TEXT="N[NUM=sg] is equivalent to [POS=N, NUM=sg]"/>
</node>
<node CREATED="1455034858843" ID="ID_36152500" MODIFIED="1455034863089" TEXT="Complex features">
<node CREATED="1455034864399" ID="ID_1848524345" MODIFIED="1455034966606" TEXT="The &apos;agreement&apos; (&apos;number&apos; + &apos;person&apos; + &apos;gender&apos;) of &apos;Kim&apos; is &apos;singular, third, femenine&apos;">
<node CREATED="1455034899245" ID="ID_761657598" MODIFIED="1455035000524" TEXT="PropN[AGR=[NUM=sg, PER=3, GND=fem]] -&gt; &apos;Kim&apos;"/>
</node>
</node>
</node>
<node CREATED="1455035170823" ID="ID_1490093861" MODIFIED="1455035177872" TEXT="Handling Feature Structures">
<node CREATED="1455035205976" ID="ID_1789111205" MODIFIED="1455035217416" TEXT="fs1 = nltk.FeatStruct(TENSE=&apos;past&apos;, NUM=&apos;sg&apos;)">
<node CREATED="1455035244732" ID="ID_1369280659" MODIFIED="1455035255966" TEXT="print(fs1)">
<node CREATED="1455035257238" ID="ID_1791877600" MODIFIED="1455035266541" TEXT="[ NUM   = &apos;sg&apos;   ]&#xa;[ TENSE = &apos;past&apos; ]"/>
</node>
</node>
<node CREATED="1455035235017" ID="ID_1617896329" MODIFIED="1455035236112" TEXT="fs2 = nltk.FeatStruct(POS=&apos;N&apos;, AGR=fs1)">
<node CREATED="1455035269308" ID="ID_1900918575" MODIFIED="1455035277477" TEXT="print(fs2)">
<node CREATED="1455035285184" ID="ID_794163662" MODIFIED="1455035290973" TEXT="[       [ CASE = &apos;acc&apos; ] ]&#xa;[ AGR = [ GND  = &apos;fem&apos; ] ]&#xa;[       [ NUM  = &apos;pl&apos;  ] ]&#xa;[       [ PER  = 3     ] ]&#xa;[                        ]&#xa;[ POS = &apos;N&apos;              ]"/>
</node>
</node>
<node CREATED="1455035312134" ID="ID_1074781887" MODIFIED="1455035329020" TEXT="fs2_alt = nltk.FeatStruct(&quot;[POS=&apos;N&apos;, AGR=[PER=3, NUM=&apos;pl&apos;, GND=&apos;fem&apos;]]&quot;)"/>
</node>
<node CREATED="1455035534841" ID="ID_958362533" MODIFIED="1455035544855" TEXT="Feature Structures can be looked at as graphs">
<node CREATED="1455035545626" ID="ID_1505657042" MODIFIED="1455035561185" TEXT="Complex features are subtrees of the graph">
<node CREATED="1455035573553" ID="ID_481131830" MODIFIED="1455036051290" TEXT="fs1 = [root] -&gt;&#xa;&#x9;Name = Lee&#xa;&#x9;Age = 33&#xa;&#x9;Address -&gt;&#xa;&#x9;&#x9;Street = rue St. Dominique&#xa;&#x9;&#x9;City = Paris"/>
</node>
<node CREATED="1455035650662" ID="ID_1339040459" MODIFIED="1455035657220" TEXT="Graphs can be linked">
<node CREATED="1455035573553" ID="ID_1034166416" MODIFIED="1455036064839" TEXT="fs2 = [root] -&gt;&#xa;&#x9;Name = Lee&#xa;&#x9;Age = 33&#xa;&#x9;Address -&gt;&#xa;&#x9;&#x9;Street = rue St. Dominique&#xa;&#x9;&#x9;City = Paris&#xa;&#x9;Spouse -&gt;&#xa;&#x9;&#x9;Name = Angela&#xa;&#x9;&#x9;Age = 35&#xa;&#x9;&#x9;Address -&gt;&#xa;&#x9;&#x9;&#x9;Street = rue St. Dominique&#xa;&#x9;&#x9;&#x9;City = Paris"/>
<node CREATED="1455035708075" ID="ID_728007266" MODIFIED="1455035754302" TEXT="Redundancies can be eliminated using &apos;tags&apos; or &apos;coindexes&apos;">
<node CREATED="1455035768371" ID="ID_570593203" MODIFIED="1455036319758" TEXT="fs2=nltk.FeatStruct(&quot;&quot;&quot;[&#xa;&#x9;NAME=&apos;Lee&apos;,&#xa;&#x9;AGE=33&#xa;&#x9;ADDRESS=(1)[&#xa;&#x9;&#x9;CITY=&apos;Paris&apos;,&#xa;&#x9;&#x9;STREET=&apos;rue St. Dominique&apos;],&#xa;&#x9;SPOUSE=[&#xa;&#x9;&#x9;NAME=&apos;Angela&apos;,&#xa;&#x9;&#x9;AGE=35,&#xa;&#x9;&#x9;ADDRESS-&gt;(1)]]&quot;&quot;&quot;)"/>
</node>
</node>
<node CREATED="1455036001185" ID="ID_1189078536" MODIFIED="1455036004398" TEXT="Subsumption">
<node CREATED="1455036007118" ID="ID_1724364796" MODIFIED="1455036034082" TEXT="fs1 subsumes fs2 if all information in fs1 is present in fs2">
<node CREATED="1455036069427" ID="ID_848216054" MODIFIED="1455036076280" TEXT="In our case, true"/>
</node>
</node>
<node CREATED="1455036109400" ID="ID_1396789139" MODIFIED="1455036111959" TEXT="Unification">
<node CREATED="1455036115018" ID="ID_766916280" MODIFIED="1455036208792" TEXT="Merging of two Feature Structures">
<node CREATED="1455036145278" ID="ID_1759760249" MODIFIED="1455036147034" TEXT="fs1 = nltk.FeatStruct(NUMBER=74, STREET=&apos;rue Pascal&apos;)"/>
<node CREATED="1455036148864" ID="ID_323444500" MODIFIED="1455036156638" TEXT="fs2 = nltk.FeatStruct(CITY=&apos;Paris&apos;)"/>
<node CREATED="1455036157372" ID="ID_121955851" MODIFIED="1455036170681" TEXT="print(fs1.unify(fs2))">
<node CREATED="1455036178635" ID="ID_857611811" MODIFIED="1455036182057" TEXT="[ CITY   = &apos;Paris&apos;      ]&#xa;[ NUMBER = 74           ]&#xa;[ STREET = &apos;rue Pascal&apos; ]"/>
</node>
</node>
<node CREATED="1455036234169" ID="ID_1247797565" MODIFIED="1455036246091" TEXT="fs1.unify(fs2)==fs2.unify(fs1)"/>
<node CREATED="1455036209275" ID="ID_1783326294" MODIFIED="1455036227115" TEXT="If fs1 subsumes fs2, fs1.unify(fs2)==fs2"/>
<node CREATED="1455036273486" ID="ID_77552888" MODIFIED="1455036300290" TEXT="Unification will fail if both Feature Structures share the same path, but it is linked to different values">
<node CREATED="1455036302778" ID="ID_1815404672" MODIFIED="1455036342580" TEXT="fs1=nltk.FeatStruct(NAME=&apos;Lee&apos;)"/>
<node CREATED="1455036302778" ID="ID_1844407237" MODIFIED="1455036357757" TEXT="fs2=nltk.FeatStruct(NAME=&apos;Leonardo&apos;)"/>
<node CREATED="1455036358198" ID="ID_1883458512" MODIFIED="1455036365425" TEXT="fs1.unify(fs2)">
<node CREATED="1455036367124" ID="ID_342420712" MODIFIED="1455036368473" TEXT="None"/>
</node>
</node>
<node CREATED="1455036486821" ID="ID_865113586" MODIFIED="1455036524614" TEXT="Unifying Feature Structures with shared features populated by variables will generate &apos;tags&apos;">
<node CREATED="1455036527475" ID="ID_1269890321" MODIFIED="1455036544271" TEXT="fs1 = nltk.FeatStruct(&quot;[HOME_ADDRESS=[NUMBER=74, STREET=&apos;rue Pascal&apos;]]&quot;)"/>
<node CREATED="1455036553306" ID="ID_1603513122" MODIFIED="1455036565381" TEXT="fs2 = nltk.FeatStruct(&quot;[HOME_ADDRESS1=?x, WORK_ADDRESS2=?x]&quot;)"/>
<node CREATED="1455036566812" ID="ID_62810525" MODIFIED="1455036596420" TEXT="print(fs2.unify(fs1))">
<node CREATED="1455036600528" ID="ID_1646685775" MODIFIED="1455036627912" TEXT="[ HOME_ADDRESS1 = (1) [ NUMBER = 74           ] ]&#xa;[                [ STREET = &apos;rue Pascal&apos; ] ]&#xa;[                                          ]&#xa;[ WORK_ADDRESS2 -&gt; (1)                          ]&#xa;"/>
</node>
</node>
</node>
</node>
<node CREATED="1455082648844" ID="ID_130598765" MODIFIED="1455082658884" TEXT="Subcategorization">
<node CREATED="1455082672536" ID="ID_1994221498" MODIFIED="1455082782625" TEXT="Features that provide information about lexical categories">
<node CREATED="1455082784707" ID="ID_1597695870" MODIFIED="1455082797996" TEXT="Very similar to &apos;agreement&apos; or &apos;tense&apos;, really"/>
</node>
<node CREATED="1455082922863" ID="ID_1878799278" MODIFIED="1455087966883" TEXT="Generalized Phrase Structure Grammar (GPSG)">
<node CREATED="1455082865484" ID="ID_359945314" MODIFIED="1455082877849" TEXT="Using &apos;subcategories&apos;"/>
<node CREATED="1455082833230" ID="ID_621652761" MODIFIED="1455082855046" TEXT="Transitive/intransitive/enunciative VPs">
<node CREATED="1455082820688" ID="ID_644054110" MODIFIED="1455082825431" TEXT="VP[TENSE=?t, NUM=?n] -&gt; V[SUBCAT=intrans, TENSE=?t, NUM=?n]&#xa;VP[TENSE=?t, NUM=?n] -&gt; V[SUBCAT=trans, TENSE=?t, NUM=?n] NP&#xa;VP[TENSE=?t, NUM=?n] -&gt; V[SUBCAT=clause, TENSE=?t, NUM=?n] SBar"/>
</node>
</node>
<node CREATED="1455083804377" ID="ID_516351948" MODIFIED="1455083821628" TEXT="PATR or Head-driven Phrase Structure Grammar">
<node CREATED="1455083826333" ID="ID_1578469453" MODIFIED="1455083854195" TEXT="Using a feature that directly encodes the valency of a head">
<node CREATED="1455083946014" ID="ID_1239238276" MODIFIED="1455084011617" TEXT="V[SUBCAT=&lt;NP, NP, PP&gt;] -&gt; &apos;put&apos;"/>
<node CREATED="1455083968874" ID="ID_1342228916" MODIFIED="1455084050062" TEXT="&apos;put&apos; requires two NPs (the subject and the object) and a PP around it"/>
<node CREATED="1455083995698" ID="ID_1641746306" MODIFIED="1455084084163" TEXT="As the required elements are added, they are dropped from the SUBCAT feature"/>
<node CREATED="1455084120080" ID="ID_1481296290" MODIFIED="1455084142764" TEXT="The complete VP would have a SUBCAT=&lt;NP&gt;"/>
<node CREATED="1455084084902" ID="ID_521828598" MODIFIED="1455084103639" TEXT="The sentence S has an empty SUBCAT"/>
</node>
</node>
</node>
<node CREATED="1455087975283" ID="ID_307530220" MODIFIED="1455087987393" TEXT="A differnet view on heads">
<node CREATED="1455088020513" ID="ID_313595519" MODIFIED="1455088022085" TEXT="X-bar Syntax">
<node CREATED="1455088028145" ID="ID_1755607040" MODIFIED="1455088042164" TEXT="Introduces phrasal level">
<node CREATED="1455088046227" ID="ID_304428227" MODIFIED="1455088097262" TEXT="N (noun) -&gt; N&apos; (noun + PP) -&gt; N&quot; (det + noun + PP, or full NP)"/>
<node CREATED="1455088123687" ID="ID_568690747" MODIFIED="1455088138912" TEXT="N is the &apos;zero projection&apos;"/>
<node CREATED="1455088098985" ID="ID_868725361" MODIFIED="1455088143441" TEXT="N&apos; and N&quot; are &apos;phrasal projections&apos; of N"/>
</node>
<node CREATED="1455088623997" ID="ID_1530833489" MODIFIED="1455088627315" TEXT="Complements">
<node CREATED="1455088660177" ID="ID_259792764" MODIFIED="1455088674963" TEXT="Directly modify the meaning of the head"/>
<node CREATED="1455088675509" ID="ID_882988221" MODIFIED="1455088678746" TEXT="Limited number"/>
<node CREATED="1455088679092" ID="ID_604606071" MODIFIED="1455088687100" TEXT="Cannot be removed"/>
<node CREATED="1455088688060" ID="ID_806280648" MODIFIED="1455088699910" TEXT="Usually cannot be moved around in the sentence"/>
<node CREATED="1455088702875" ID="ID_1007080445" MODIFIED="1455088779645" TEXT="The student &apos;of French&apos;"/>
<node CREATED="1455088791698" ID="ID_297790080" MODIFIED="1455088802413" TEXT="In X-bar, they are at the same level as the head"/>
</node>
<node CREATED="1455088627633" ID="ID_1972450144" MODIFIED="1455088630410" TEXT="Adjuncts">
<node CREATED="1455088723283" ID="ID_1387928140" MODIFIED="1455088729310" TEXT="Provide additional information"/>
<node CREATED="1455088729544" ID="ID_190909559" MODIFIED="1455088737270" TEXT="Unlimited number"/>
<node CREATED="1455088737800" ID="ID_794401645" MODIFIED="1455088740733" TEXT="Can be removed"/>
<node CREATED="1455088741149" ID="ID_1789202762" MODIFIED="1455088745010" TEXT="Can be moved around"/>
<node CREATED="1455088745568" ID="ID_327447613" MODIFIED="1455088788158" TEXT="The student &apos;from France&apos; &apos;with good grades&apos;"/>
<node CREATED="1455088804300" ID="ID_978400821" MODIFIED="1455088816370" TEXT="In X-bar, they end up associated with intermediate levels"/>
</node>
<node CREATED="1455088914767" ID="ID_139712741" MODIFIED="1455088919775" TEXT="Example">
<node CREATED="1455088921688" ID="ID_472246471" MODIFIED="1455088966031" TEXT="S -&gt; N[BAR=2] V[BAR=2]&#xa;N[BAR=2] -&gt; Det N[BAR=1]&#xa;N[BAR=1] -&gt; N[BAR=1] P[BAR=2] (adjunct P&quot;s)&#xa;N[BAR=1] -&gt; N[BAR=0] P[BAR=2] (complement P&quot;)&#xa;N[BAR=1] -&gt; N[BAR=0]"/>
</node>
</node>
</node>
<node CREATED="1455089447264" ID="ID_769962850" MODIFIED="1455089454342" TEXT="Auxiliary verbs and inversion">
<node CREATED="1455089462805" ID="ID_1251907995" MODIFIED="1455089503287" TEXT="Inverted clauses (of the form Verb Subject)">
<node CREATED="1455089504300" ID="ID_470145535" MODIFIED="1455089510355" TEXT="Interrogatives">
<node CREATED="1455089525160" ID="ID_1643569548" MODIFIED="1455089532406" TEXT="Do you like apples?"/>
</node>
<node CREATED="1455089510675" ID="ID_1751032306" MODIFIED="1455089524151" TEXT="&apos;Negative&apos; adverbs">
<node CREATED="1455089534107" ID="ID_1265246708" MODIFIED="1455089613982" TEXT="Never have I seen anything like that"/>
</node>
</node>
<node CREATED="1455089548314" ID="ID_307264654" MODIFIED="1455089556067" TEXT="Not with just any verb">
<node CREATED="1455089588278" ID="ID_1126728622" MODIFIED="1455089592744" TEXT="Like you apples?"/>
<node CREATED="1455089593221" ID="ID_943218124" MODIFIED="1455089603797" TEXT="Never see I anything like that"/>
</node>
<node CREATED="1455089617621" ID="ID_1213243477" MODIFIED="1455089628212" TEXT="Only with &apos;auxiliary&apos; verbs"/>
<node CREATED="1455089628705" ID="ID_1613644655" MODIFIED="1455089632720" TEXT="Sample productions">
<node CREATED="1455089643243" ID="ID_512143959" MODIFIED="1455089644573" TEXT="S[+INV] -&gt; V[+AUX] NP VP"/>
</node>
</node>
<node CREATED="1455089971365" ID="ID_32198696" MODIFIED="1455089979612" TEXT="Unbounded dependency constructions">
<node CREATED="1455089987015" ID="ID_1305214083" MODIFIED="1455089998328" TEXT="There are verbs that require certain complements">
<node CREATED="1455090000141" ID="ID_452263618" MODIFIED="1455090035762" TEXT="&apos;You like Judy&apos; (grammatical) vs &apos;You like&apos; (ungrammatical)"/>
</node>
<node CREATED="1455090045649" ID="ID_322047741" MODIFIED="1455090104789" TEXT="These can (and must!) be ommited if a filler is present">
<node CREATED="1455090057295" ID="ID_615318049" MODIFIED="1455090089846" TEXT="&apos;Who do you like?&apos; (grammatical) vs. &apos;Who do you like Judy?&apos; (ungrammatical)"/>
</node>
<node CREATED="1455090125432" ID="ID_967265193" MODIFIED="1455090142391" TEXT="&apos;Fillers&apos; can occur if lincensed by a &apos;gap&apos;">
<node CREATED="1455090147617" ID="ID_1398286941" MODIFIED="1455090167968" TEXT="&apos;Filler&apos; and &apos;gap&apos; are said to have a &apos;dependency&apos;"/>
</node>
<node CREATED="1455090169635" ID="ID_1255317798" MODIFIED="1455090192175" TEXT="The distance between &apos;filler&apos; and &apos;gap&apos; does not have an upper bound though">
<node CREATED="1455090193459" ID="ID_1215923154" MODIFIED="1455090212804" TEXT="&apos;Who do you claim that Jody says that you like?&apos;"/>
</node>
<node CREATED="1455090228381" ID="ID_587112497" MODIFIED="1455090252908" TEXT="In order to parse this, GPSG uses SLASH categories">
<node CREATED="1455090260422" ID="ID_1245255677" MODIFIED="1455090282691" TEXT="[category]/[sub_category]">
<node CREATED="1455090288608" ID="ID_295913293" MODIFIED="1455090303862" TEXT="[category] which is missing the subcategory [sub_category]"/>
<node CREATED="1455090308058" ID="ID_806448584" MODIFIED="1455090319123" TEXT="S/NP -&gt; A sentence missing the subject"/>
</node>
</node>
<node CREATED="1455090346817" ID="ID_1854169226" MODIFIED="1455090349441" TEXT="Example">
<node CREATED="1455090350525" ID="ID_183329871" MODIFIED="1455090354304" TEXT="Who do you like">
<node CREATED="1455090355130" ID="ID_910975958" MODIFIED="1455090685749" TEXT="(S&#xa;&#x9;(NP[+WH] Who)&#xa;&#x9;(S[+INV]/NP&#xa;&#x9;&#x9;(V[+AUX] do)&#xa;&#x9;&#x9;(NP[-WH] you)&#xa;&#x9;&#x9;(VP/NP&#xa;&#x9;&#x9;&#x9;(V[-AUX, SUBCAT=&apos;trans&apos;] like)&#xa;&#x9;&#x9;&#x9;NP/NP)))"/>
<node CREATED="1455090708114" ID="ID_430987268" MODIFIED="1455090724027" TEXT="WH are &apos;Wh-&apos; particles">
<node CREATED="1455090725137" ID="ID_1191890768" MODIFIED="1455090730038" TEXT="Who, what, ..."/>
</node>
</node>
<node CREATED="1455090765424" ID="ID_1650035762" MODIFIED="1455090777605" TEXT="Grammar">
<node CREATED="1455090779010" ID="ID_1189015869" MODIFIED="1455091026556" TEXT="% start S&#xa;# ###################&#xa;# Grammar Productions&#xa;# ###################&#xa;S[-INV] -&gt; NP VP&#xa;S[-INV]/?x -&gt; NP VP/?x&#xa;S[-INV] -&gt; NP S/NP&#xa;S[-INV] -&gt; Adv[+NEG] S[+INV]&#xa;S[+INV] -&gt; V[+AUX] NP VP&#xa;S[+INV]/?x -&gt; V[+AUX] NP VP/?x&#xa;SBar -&gt; Comp S[-INV]&#xa;SBar/?x -&gt; Comp S[-INV]/?x&#xa;VP -&gt; V[SUBCAT=intrans, -AUX]&#xa;VP -&gt; V[SUBCAT=trans, -AUX] NP&#xa;VP/?x -&gt; V[SUBCAT=trans, -AUX] NP/?x&#xa;VP -&gt; V[SUBCAT=clause, -AUX] SBar&#xa;VP/?x -&gt; V[SUBCAT=clause, -AUX] SBar/?x&#xa;VP -&gt; V[+AUX] VP&#xa;VP/?x -&gt; V[+AUX] VP/?x&#xa;# ###################&#xa;# Lexical Productions&#xa;# ###################&#xa;V[SUBCAT=intrans, -AUX] -&gt; &apos;walk&apos; | &apos;sing&apos;&#xa;V[SUBCAT=trans, -AUX] -&gt; &apos;see&apos; | &apos;like&apos;&#xa;V[SUBCAT=clause, -AUX] -&gt; &apos;say&apos; | &apos;claim&apos;&#xa;V[+AUX] -&gt; &apos;do&apos; | &apos;can&apos;&#xa;NP[-WH] -&gt; &apos;you&apos; | &apos;cats&apos;&#xa;NP[+WH] -&gt; &apos;who&apos;&#xa;Adv[+NEG] -&gt; &apos;rarely&apos; | &apos;never&apos;&#xa;NP/NP -&gt;&#xa;Comp -&gt; &apos;that&apos;">
<node CREATED="1455090879625" ID="ID_1265271215" MODIFIED="1455090885140" TEXT="Gap introduction">
<node CREATED="1455090886396" ID="ID_1953758730" MODIFIED="1455091069422" TEXT="S[-INV] -&gt; NP S/NP (at the top, closing the gap)&#xa;...&#xa;VP/?x -&gt; V[+AUX] VP/?x (in between, shifting it up or down)&#xa;...&#xa;NP/NP -&gt; (at the bottom, starting it)"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node CREATED="1456726565372" ID="ID_802121873" MODIFIED="1456726592502" POSITION="right" TEXT="10. Analyzing the Meaning of Sentences">
<node CREATED="1456727128532" ID="ID_504258475" MODIFIED="1456727151671" TEXT="Grammars can be built to translate natural language to (e.g.) SQL">
<node CREATED="1456727486903" ID="ID_203528259" MODIFIED="1456727495749" TEXT="% start S&#xa;S[SEM=(?np + WHERE + ?vp)] -&gt; NP[SEM=?np] VP[SEM=?vp]&#xa;VP[SEM=(?v + ?pp)] -&gt; IV[SEM=?v] PP[SEM=?pp]&#xa;VP[SEM=(?v + ?ap)] -&gt; IV[SEM=?v] AP[SEM=?ap]&#xa;NP[SEM=(?det + ?n)] -&gt; Det[SEM=?det] N[SEM=?n]&#xa;PP[SEM=(?p + ?np)] -&gt; P[SEM=?p] NP[SEM=?np]&#xa;AP[SEM=?pp] -&gt; A[SEM=?a] PP[SEM=?pp]&#xa;NP[SEM=&apos;Country=&quot;greece&quot;&apos;] -&gt; &apos;Greece&apos;&#xa;NP[SEM=&apos;Country=&quot;china&quot;&apos;] -&gt; &apos;China&apos;&#xa;Det[SEM=&apos;SELECT&apos;] -&gt; &apos;Which&apos; | &apos;What&apos;&#xa;N[SEM=&apos;City FROM city_table&apos;] -&gt; &apos;cities&apos;&#xa;IV[SEM=&apos;&apos;] -&gt; &apos;are&apos;&#xa;A[SEM=&apos;&apos;] -&gt; &apos;located&apos;&#xa;P[SEM=&apos;&apos;] -&gt; &apos;in&apos;"/>
<node CREATED="1456727624990" ID="ID_193664744" MODIFIED="1456727643561" TEXT="After a successul parse, SEM will contain the SQL query">
<node CREATED="1456727548095" ID="ID_1776984727" MODIFIED="1456727690697" TEXT="parse(&apos;What cities are located in China&apos;)">
<node CREATED="1456727595359" ID="ID_1933680118" MODIFIED="1456727610199" TEXT="SELECT City FROM city_table WHERE Country=&quot;china&quot;"/>
</node>
<node CREATED="1456727582794" ID="ID_1818186913" MODIFIED="1456727593931" TEXT="parse(&apos;Which cities are located in Greece&apos;">
<node CREATED="1456727613647" ID="ID_1182353237" MODIFIED="1456727620934" TEXT="SELECT City FROM city_table WHERE Country=&quot;greece&quot;"/>
</node>
</node>
<node CREATED="1456727156314" ID="ID_907660930" MODIFIED="1456727168478" TEXT="The problem is not different from translating from one language to another"/>
<node CREATED="1456727169031" ID="ID_1102173878" MODIFIED="1456727191132" TEXT="They tend to have drawbacks">
<node CREATED="1456727435916" ID="ID_461083538" MODIFIED="1456727442338" TEXT="Very detailed"/>
<node CREATED="1456727442716" ID="ID_1176784985" MODIFIED="1456727457521" TEXT="Hard coded knowledge about the languages"/>
<node CREATED="1456727659947" ID="ID_711523532" MODIFIED="1456727669688" TEXT="Translation does not imply understanding"/>
</node>
</node>
<node CREATED="1456727698601" ID="ID_929565021" MODIFIED="1456727712369" TEXT="A better solution is to translate into a meta language first">
<node CREATED="1456727717526" ID="ID_1116137195" MODIFIED="1456728888242" TEXT="Powerful option: logic">
<node CREATED="1456728271570" ID="ID_582606050" MODIFIED="1456728296227" TEXT="NLTK has integrated logic modules"/>
<node CREATED="1456728888775" ID="ID_1352887311" MODIFIED="1456728914395" TEXT="Prepositional logic">
<node CREATED="1456728462442" ID="ID_83704417" MODIFIED="1456728468671" TEXT="Boolean expressions">
<node CREATED="1456728332875" ID="ID_1074073514" MODIFIED="1456728356387" TEXT="read_expr = nltk.sem.Expression.fromstring&#xa;read_expr(&apos;-(P &amp; Q)&apos;)&#xa;&#x9;&lt;NegatedExpression -(P &amp; Q)&gt;&#xa;read_expr(&apos;P &amp; Q&apos;)&#xa;&#x9;&lt;AndExpression (P &amp; Q)&gt;&#xa;read_expr(&apos;P | (R -&gt; Q)&apos;)&#xa;&#x9;&lt;OrExpression (P | (R -&gt; Q))&gt;&#xa;read_expr(&apos;P &lt;-&gt; -- P&apos;)&#xa;&#x9;&lt;IffExpression (P &lt;-&gt; --P)&gt;&#xa;"/>
</node>
<node CREATED="1456728428904" ID="ID_932792261" MODIFIED="1456728455178" TEXT="Theorem prover">
<node CREATED="1456728365986" ID="ID_323814823" MODIFIED="1456728423132" TEXT="read_expr = nltk.sem.Expression.fromstring&#xa;SnF = read_expr(&apos;SnF&apos;)&#xa;NotFnS = read_expr(&apos;-FnS&apos;)&#xa;R = read_expr(&apos;SnF -&gt; -FnS&apos;)&#xa;prover = nltk.Prover9()&#xa;prover.prove(NotFnS, [SnF, R])&#xa;&#x9;True"/>
</node>
<node CREATED="1456729277083" ID="ID_1213992449" MODIFIED="1456729280755" TEXT="Valuation">
<node CREATED="1456729292095" ID="ID_348637522" MODIFIED="1456729345239" TEXT="val = nltk.Valuation([(&apos;P&apos;, True), (&apos;Q&apos;, True), (&apos;R&apos;, False)])&#xa;dom = set()&#xa;g = nltk.Assignment(dom)&#xa;m = nltk.Model(dom, val)&#xa;print(m.evaluate(&apos;(P &amp; Q)&apos;, g))&#xa;&#x9;True&#xa;print(m.evaluate(&apos;-(P &amp; Q)&apos;, g))&#xa;&#x9;False&#xa;print(m.evaluate(&apos;(P &amp; R)&apos;, g))&#xa;&#x9;False&#xa;print(m.evaluate(&apos;(P | R)&apos;, g))&#xa;&#x9;True"/>
</node>
<node CREATED="1456728922087" ID="ID_918060871" MODIFIED="1456728926466" TEXT="Limitation">
<node CREATED="1456728929219" ID="ID_1821036401" MODIFIED="1456729047476" TEXT="It cannot dig into the sentences themselves">
<node CREATED="1456729048831" ID="ID_149578608" MODIFIED="1456729063411" TEXT="At least no twithout an exponential explosion of rules"/>
<node CREATED="1456740496133" ID="ID_735267226" MODIFIED="1456740542380" TEXT="Capturing the argument &quot;Sylvania is to the north of Freedonia. Therefore, Freedonia is not to the north of Sylvania&quot; is very costly"/>
</node>
</node>
</node>
<node CREATED="1456729065296" ID="ID_739835512" MODIFIED="1456729069788" TEXT="First order logic">
<node CREATED="1456729077491" ID="ID_852230165" MODIFIED="1456740489882" TEXT="Can represent more complex relationships &apos;between several elements">
<node CREATED="1456729109903" ID="ID_1756178615" MODIFIED="1456729123644" TEXT="e.g., NP and VP"/>
<node CREATED="1456729144008" ID="ID_1204426813" MODIFIED="1456729146063" TEXT="Terms">
<node CREATED="1456729147584" ID="ID_515271960" MODIFIED="1456729153339" TEXT="Individual variables">
<node CREATED="1456729185985" ID="ID_1683569281" MODIFIED="1456729223675" TEXT="&apos;I&apos;"/>
<node CREATED="1456729224158" ID="ID_1845625862" MODIFIED="1456729227226" TEXT="&apos;you&apos;"/>
<node CREATED="1456729228214" ID="ID_597960939" MODIFIED="1456729229429" TEXT="..."/>
</node>
</node>
<node CREATED="1456729160482" ID="ID_999176118" MODIFIED="1456729162749" TEXT="Predicates">
<node CREATED="1456729169229" ID="ID_867954731" MODIFIED="1456729174834" TEXT="Relationships">
<node CREATED="1456729203196" ID="ID_1468726600" MODIFIED="1456729212670" TEXT="see(&apos;I&apos;,&apos;you&apos;)"/>
<node CREATED="1456729213883" ID="ID_1645868444" MODIFIED="1456729218718" TEXT="walk(&apos;I&apos;)"/>
<node CREATED="1456729230261" ID="ID_1565723472" MODIFIED="1456729231172" TEXT="..."/>
</node>
</node>
</node>
<node CREATED="1456729454470" ID="ID_1548496621" MODIFIED="1456739383381" TEXT="Symbols other than the logical operators have no intrinsic meaning">
<node CREATED="1456729466172" ID="ID_574076897" MODIFIED="1456729509689" TEXT="Can only say whether a set is consistent or whether an argument is valid"/>
<node CREATED="1456729619205" ID="ID_1388623893" MODIFIED="1456735472309" TEXT="One additional logical operator, =">
<node CREATED="1456729629378" ID="ID_957977942" MODIFIED="1456729655085" TEXT="t1 = t2 if and only if t1 and t2 refer to the same entity"/>
</node>
</node>
<node CREATED="1456735478654" ID="ID_169468980" MODIFIED="1456739467341" TEXT="Assigning &apos;types&apos; is useful to inspect the syntactic structure of expressions">
<node CREATED="1456739540802" ID="ID_1294817938" MODIFIED="1456739545193" TEXT="Basic types">
<node CREATED="1456739476985" ID="ID_389233074" MODIFIED="1456739481738" TEXT="e - entities"/>
<node CREATED="1456739482158" ID="ID_1993460205" MODIFIED="1456739516191" TEXT="t - formulas (expressions with truth values)"/>
</node>
<node CREATED="1456739550852" ID="ID_1116830764" MODIFIED="1456739553720" TEXT="Complex types">
<node CREATED="1456739555103" ID="ID_1484639502" MODIFIED="1456739578190" TEXT="&lt;e, t&gt; - unary predicates"/>
<node CREATED="1456739585870" ID="ID_1128057325" MODIFIED="1456739598660" TEXT="&lt;e, &lt;e, t&gt;&gt; - binary predicates"/>
</node>
</node>
<node CREATED="1456739709463" ID="ID_1543527374" MODIFIED="1456739723241" TEXT="Variables as arguments of predicates">
<node CREATED="1456739644558" ID="ID_391442555" MODIFIED="1456739647920" TEXT="Coreference">
<node CREATED="1456739656521" ID="ID_947587338" MODIFIED="1456739668070" TEXT="Cyril is Angus&apos;s dog.&#xa;He disappeared.">
<node CREATED="1456739679307" ID="ID_522244333" MODIFIED="1456739708047" TEXT="&apos;He&apos; is correferential with &apos;Cyril&apos;"/>
</node>
</node>
<node CREATED="1456739731267" ID="ID_832418788" MODIFIED="1456739804842" TEXT="Binding variables">
<node CREATED="1456739826284" ID="ID_1756525015" MODIFIED="1456739828107" TEXT="Unbound">
<node CREATED="1456739829969" ID="ID_390433113" MODIFIED="1456739851420" TEXT="Angus had a dog and a dog disappeared.  ">
<node CREATED="1456739876249" ID="ID_1467050935" MODIFIED="1456739887203" TEXT="~ He is a dog and he disappeared"/>
<node CREATED="1456739891885" ID="ID_80975462" MODIFIED="1456739903888" TEXT="~ dog(x) AND disappeared(X)"/>
</node>
</node>
<node CREATED="1456739821262" ID="ID_178831262" MODIFIED="1456739823194" TEXT="Bound">
<node CREATED="1456739824402" ID="ID_347883423" MODIFIED="1456739848942" TEXT="Angus had a dog and he disappeared.  ">
<node CREATED="1456739928351" ID="ID_1178682640" MODIFIED="1456739932189" TEXT="~ A dog disappeared"/>
<node CREATED="1456739932726" ID="ID_1670994753" MODIFIED="1456739951103" TEXT="~ THERE IS x.(dog(x) AND disapeared(x))"/>
</node>
</node>
<node CREATED="1456739966640" ID="ID_1230088304" MODIFIED="1456739981029" TEXT="Binding contexts are created by quantifiers">
<node CREATED="1456739982435" ID="ID_1767973636" MODIFIED="1456739984730" TEXT="THERE IS">
<node CREATED="1456739998969" ID="ID_218498067" MODIFIED="1456740001048" TEXT="exists x.(dog(x) &amp; disappear(x))"/>
</node>
<node CREATED="1456739985544" ID="ID_1014896976" MODIFIED="1456739987499" TEXT="EVERY">
<node CREATED="1456740010389" ID="ID_337328765" MODIFIED="1456740011724" TEXT="all x.(dog(x) -&gt; disappear(x))"/>
</node>
<node CREATED="1456740341807" ID="ID_282743384" MODIFIED="1456740366909" TEXT="exists x.(dog(x)) -&gt; bark(x)">
<node CREATED="1456740408230" ID="ID_1639962364" MODIFIED="1456740410533" TEXT="Unbound"/>
</node>
<node CREATED="1456740412513" ID="ID_1966018656" MODIFIED="1456740443496" TEXT="all x.(exists x.(dog(x)) -&gt; bark(x))">
<node CREATED="1456740444472" ID="ID_1479534007" MODIFIED="1456740446295" TEXT="Bound"/>
</node>
</node>
</node>
</node>
<node CREATED="1456740549536" ID="ID_1146913537" MODIFIED="1456740559464" TEXT="Capturing the argument &quot;Sylvania is to the north of Freedonia. Therefore, Freedonia is not to the north of Sylvania&quot; is straightforward">
<node CREATED="1456740571311" ID="ID_460788237" MODIFIED="1456740572571" TEXT="all x. all y.(north_of(x, y) -&gt; -north_of(y, x))"/>
<node CREATED="1456740656784" ID="ID_420771720" MODIFIED="1456740667804" TEXT="The inference can also be proven automatically">
<node CREATED="1456740693491" ID="ID_6435445" MODIFIED="1456740697273" TEXT="S &#x22a2; g">
<node CREATED="1456740698425" ID="ID_573185865" MODIFIED="1456740706859" TEXT="S: set of assumptions">
<node CREATED="1456740708192" ID="ID_241519923" MODIFIED="1456740711401" TEXT="Could be empty"/>
</node>
<node CREATED="1456740712236" ID="ID_1261961651" MODIFIED="1456740720441" TEXT="g: proof goal"/>
</node>
<node CREATED="1456740735355" ID="ID_1496012893" MODIFIED="1456740785776" TEXT="NotFnS = read_expr(&apos;-north_of(f, s)&apos;)&#xa;SnF = read_expr(&apos;north_of(s, f)&apos;)&#xa;R = read_expr(&apos;all x. all y. (north_of(x, y) -&gt; -north_of(y, x))&apos;)&#xa;prover = nltk.Prover9()&#xa;prover.prove(NotFnS, [SnF, R])&#xa;&#x9;True&#xa;FnS = read_expr(&apos;north_of(f, s)&apos;)&#xa;prover.prove(FnS, [SnF, R])&#xa;&#x9;False"/>
</node>
</node>
<node CREATED="1456740878669" ID="ID_1452405274" MODIFIED="1456740884795" TEXT="Summary of first order logic">
<node CREATED="1456740901430" ID="ID_999149838" MODIFIED="1456740920308" TEXT="&#x2329;en, t&#x232a; is the type of a predicate which combines with n arguments of type e to yield an expression of type t">
<node CREATED="1456740922905" ID="ID_969744611" MODIFIED="1456740925784" TEXT="n is the arity of the predicate"/>
</node>
<node CREATED="1456740967588" ID="ID_418861722" MODIFIED="1456740969635" TEXT="Axioms">
<node CREATED="1456740950132" ID="ID_294027648" MODIFIED="1456740978030" TEXT="If P is a predicate of type &#x2329;en, t&#x232a;, and &#x3b1;1, ... &#x3b1;n are terms of type e, then P(&#x3b1;1, ... &#x3b1;n) is of type t"/>
<node CREATED="1456740950132" ID="ID_1021011317" MODIFIED="1456740990052" TEXT="If &#x3b1; and &#x3b2; are both of type e, then (&#x3b1; = &#x3b2;) and (&#x3b1; != &#x3b2;) are of type t"/>
<node CREATED="1456740950132" ID="ID_1819101576" MODIFIED="1456740999619" TEXT="If &#x3c6; is of type t, then so is -&#x3c6;"/>
<node CREATED="1456740950132" ID="ID_769357407" MODIFIED="1456741011871" TEXT="If &#x3c6; and &#x3c8; are of type t, then so are (&#x3c6; &amp; &#x3c8;), (&#x3c6; | &#x3c8;), (&#x3c6; -&gt; &#x3c8;) and (&#x3c6; &lt;-&gt; &#x3c8;)"/>
<node CREATED="1456740950132" ID="ID_730658282" MODIFIED="1456741020499" TEXT="If &#x3c6; is of type t, and x is a variable of type e, then exists x.&#x3c6; and all x.&#x3c6; are of type t"/>
</node>
<node CREATED="1456741029644" ID="ID_736375236" MODIFIED="1456741039058" TEXT="Logical relations">
<node CREATED="1456741054407" ID="ID_1944517529" MODIFIED="1456741058144" TEXT="=&#x9;equality&#xa;!=&#x9;inequality&#xa;exists&#x9;existential quantifier&#xa;all&#x9;universal quantifier&#xa;e.free()&#x9;show free variables of e&#xa;e.simplify()&#x9;carry out &#x3b2;-reduction on e"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
</map>
