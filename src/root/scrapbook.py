'''
Created on Sep 8, 2015

@author: ggomarr
'''

def compute_lexical_diversity(wds):
    if len(wds)==0:
        return False
    lexdiv=1.0*len(set(wds))/len(wds)
    return lexdiv

def compute_ari(wds, sents):
    if len(wds)==0:
        return False
    wd_len=[ len(wd) for wd in wds ]
    cpw=1.0*sum(wd_len)/len(wd_len)
    num_wds=len(wds)
    num_sents=len(sents)
    wps=1.0*num_wds/num_sents
    ari=4.71*cpw+0.5*wps-21.43
    return ari

def test_pdf(filenom='test_file_to_check.pdf',
             plot_graph=False):
    import slate, nltk, pylab
    with open(filenom) as f:
        doc=slate.PDF(f)
    auxout=[]
    for page in doc:
        page=unicode(page,"utf-8")
        wds=nltk.word_tokenize(page)
        wds=[ wd.lower() for wd in wds if wd.isalpha()==True ]
        sents=nltk.PunktSentenceTokenizer().tokenize(page)
        auxout= auxout + [ [ len(page), len(wds), len(sents),
                             compute_lexical_diversity(wds), compute_ari(wds, sents) ] ]
    if plot_graph:
        x_lab = range(1,len(auxout))
        lexdiv=[ page[3] for page in auxout ]
        pylab.plot(x_lab,lexdiv)
    return auxout