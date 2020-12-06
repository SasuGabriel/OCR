# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
with open('D:/BusuiocI/Desktop/request.json', encoding='utf-8') as f:
  data = json.load(f)
text=data['fullTextAnnotation']['text'].replace('\n',' ')

dataFile = open('inputfactura.txt', 'w', encoding='utf-8')
dataFile.write(text)
dataFile.close() 

#pip install spacy
import spacy
from spacy import displacy
#python -m spacy download ro_core_news_md/ro_core_news_lg/ro_core_news_sm
nlp = spacy.load('ro_core_news_lg')
#nlp2=spacy.load('ro_core_news_md')
#nlp3=spacy.load('ro_core_news_sm')

doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.is_stop)
for sent in enumerate(doc.sents):
    print(sent)
from nltk import tokenize
tokenize.sent_tokenize(text)
import re
telephone=re.findall("(\d{4}\d{3}\d{3}\s)", text)[0].strip()
postalcodesender=re.findall("\s\d{6}\s", text)[0].strip()
CIF=re.findall("[A-Z][A-Z]\d{6,10}\s", text)[0].strip()
code=re.findall("\s\d{5}\s", text)[0].strip()
numepersoana=re.findall("([A-Z\-]{4,})\s+([A-Z\-]{5,})??\s?([A-Z\-]{5,})", text)
numepersoana
perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)[0].strip()
datafacturare=re.findall("\Data facturării\:\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)[0].strip()
duedate=re.findall("Total de plată pană la\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)[0].strip()
IBAN=re.findall("\s[A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s", text)
IBAN2=IBAN[1].strip()
codfacturare=re.findall("[0-9]{14}", text)[0]

import unicodedata
textwithoutdiacritics=unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf8')
textwithoutdiacritics

abbreviations = {'nr.': 'Numar',
                 'Et.': 'Etaj',
                 'Contab.': 'Contabilitate',
                 'Publ.': 'Publica',
                 'Activ.': 'Activitate',
                 'Nr.': 'Numar',
                 'Sc.': 'Scara',
                 'Ap.': 'Apartament',
                 'Jud.': 'Judet'}
terminators = ['.', '!', '?', ';', telephone, postalcodesender, CIF, code, IBAN2, perioadafacturare, datafacturare]
wrappers = ['"', "'", ')', ']', '}', ':']
    
def find_sentences(paragraph):
   end = True
   sentences = []
   while end > -1:
       end = find_sentence_end(paragraph)
       if end > -1:
           sentences.append(paragraph[end:].strip())
           paragraph = paragraph[:end]
   sentences.append(paragraph)
   sentences.reverse()
   return sentences

def find_sentence_end(paragraph):
    [possible_endings, contraction_locations] = [[], []]
    contractions = abbreviations.keys()
    sentence_terminators = terminators + [terminator + wrapper for wrapper in wrappers for terminator in terminators]
    for sentence_terminator in sentence_terminators:
        t_indices = list(find_all(paragraph, sentence_terminator))
        possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))
    for contraction in contractions:
        c_indices = list(find_all(paragraph, contraction))
        contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
    possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
    if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
        max_end_start = max([pe[0] for pe in possible_endings])
        possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
    possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
    end = (-1 if not len(possible_endings) else max(possible_endings))
    return end

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

sentences=find_sentences(text)

for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)
    
from sentence_splitter import SentenceSplitter, split_text_into_sentences
splitter = SentenceSplitter(language='ro', non_breaking_prefix_file='D:/BusuiocI/Downloads/ro.txt')
sentences=splitter.split(text=textwithoutdiacritics)
sentences2=split_text_into_sentences(
    text=text,
    language='ro',
    non_breaking_prefix_file='D:/BusuiocI/Downloads/ro.txt')

def show_ents(doc):
    if doc.ents:
            for ent in doc.ents: print(ent.text+' - ' +str(ent.start_char) +' - '+ str(ent.end_char) +' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_ents(doc)

for i in range(len(sentences)):
    doc=nlp(sentences[i])
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.is_stop)
        
for i in range(len(sentences)):
    doc=nlp(sentences[i])
    for ent in doc.ents:
        print(ent.text, ent.label_)
html=[]

doc=nlp(sentences[5])
html=displacy.render(doc, style="ent",jupyter=False) #NER

html #View in HTML Viewer

# Write a function to display basic entity info:

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
    
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    return sent
sent = preprocess(text)
fd = nltk.FreqDist(sent)
most_freq_words = fd.most_common(100)
print(most_freq_words)

from collections import Counter
words = [token.text for token in doc
          if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
common_words = word_freq.most_common(5)
print (common_words)
  
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent
sent = preprocess(text)
sent
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('romanian'))  # nltk stopwords list
nltk_tokens = nltk.word_tokenize(text)
texts = [i for i in nltk_tokens if i not in stop_words] #tokens without stopwords

#LDA = Latent Dirichlet Allocation
#pip install pyLDAvis
import re
import numpy as np
import pandas as pd
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import spacy
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
nlp = spacy.load('ro_core_news_lg', disable=['parser', 'ner'])

bigram = gensim.models.Phrases(texts, min_count=5, threshold=100)
trigram = gensim.models.Phrases(bigram[texts], threshold=100)
bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)
def make_bigrams(texts):
   return [bigram_mod[texts]]
def make_trigrams(texts):
   [trigram_mod[bigram_mod[texts]]]
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
   texts_out = []
   for sent in texts:
      doc = nlp(" ".join(sent))
      texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
   return texts_out
data_words_bigrams = make_bigrams(texts)
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=[
   'NOUN', 'ADJ', 'VERB', 'ADV'
])
id2word = corpora.Dictionary(data_lemmatized)
lemmatized = data_lemmatized
corpus = [id2word.doc2bow(text) for text in lemmatized]
[[(id2word[id], freq) for id, freq in cp] for cp in corpus[:4]] 
#it will print the words with their frequencies.
lda_model = gensim.models.ldamodel.LdaModel(
   corpus=corpus, id2word=id2word, num_topics=20, random_state=100, 
   update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True
)
for i,topic in lda_model.show_topics(formatted=True, num_topics=20, num_words=10):
    print(str(i)+": "+ topic)
    print()


from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("romanian") # Choose a language
for word in nltk_tokens:
    print("{0:20}{1:20}".format(word,stemmer.stem(word)))
    
#pip install wordcloud
from wordcloud import WordCloud
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
wordcloud.generate(text)
wordcloud.to_image()

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
def extract_full_name(nlp_doc):
   pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
   matcher.add('FULL_NAME', None, pattern)
   matches = matcher(nlp_doc)
   for match_id, start, end in matches:
       span = nlp_doc[start:end]
       return span.text
extract_full_name(doc)




