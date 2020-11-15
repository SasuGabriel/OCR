# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
with open('D:/BusuiocI/Desktop/request.json', encoding='utf-8') as f:
  data = json.load(f)
text=data['fullTextAnnotation']['text'].replace('\n',' ')

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
    
from sentence_splitter import SentenceSplitter, split_text_into_sentences
splitter = SentenceSplitter(language='ro', non_breaking_prefix_file='D:/BusuiocI/Downloads/ro.txt')
sentences=splitter.split(text=text)
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


