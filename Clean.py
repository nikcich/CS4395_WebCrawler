import nltk
from nltk import word_tokenize

from nltk.corpus import stopwords
import math

num_docs = 50
stopwords = stopwords.words('english')
texts = []

for i in range(num_docs):
    f = open('url_number_'+str(i+1)+'.txt', 'r', encoding="utf-8")

    text = f.read()

    text = text.replace("\n", ' ')
    text = text.replace('  ', ' ')
    text = text.lower()
    texts.append(text)
    f.close()

#stuff = sent_tokenize(text)
vocab = set()  # set of words

def create_tf_dict(doc):
    tf_dict = {}
    tokens = word_tokenize(doc)

    tokens = [w for w in tokens if w.isalpha() and w not in stopwords]

    # get term frequencies
    for t in tokens:
        if t in tf_dict:
            tf_dict[t] += 1
        else:
            tf_dict[t] = 1
            
    # get term frequencies in a more Pythonic way
    token_set = set(tokens)
    tf_dict = {t:tokens.count(t) for t in token_set}
    
    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


tf_list = []
for i in range(num_docs):
    tf_temp = create_tf_dict(texts[i])
    keys = list(tf_temp.keys())
    keys = set(keys)
    if(len(vocab) == 0):
        vocab = keys
    else:
        vocab = set.union(vocab, keys)
    tf_list.append(tf_temp)


print("Unique words:", len(vocab))
print('tf for "motorcycle" in first file=', tf_list[0].get('motorcycle'))

idf_dict = {}
vocab_by_topic = []

for i in range(num_docs):
    tf_curr = tf_list[i]
    vocab_by_topic.append(tf_curr.keys())

for term in vocab:
    temp = ['x' for voc in vocab_by_topic if term in voc]
    idf_dict[term] = math.log((1+num_docs) / (1+len(temp)))


print('idf for motorcycle:', idf_dict['motorcycle'])

def create_tfidf(tf, idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t] 
        
    return tf_idf

tf_idf_first = create_tfidf(tf_list[0], idf_dict)

doc_term_weights = sorted(tf_idf_first.items(), key=lambda x:x[1], reverse=True)
print("\nFirst file: ", doc_term_weights[:5])