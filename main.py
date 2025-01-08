import re
from collections import Counter

def get_data():
    n = int(input())
    docs = []
    for i in range(n+1):
        docs.append(input())
    return docs
docs = get_data()

docs = [re.sub(r"[^\w\s]", "", doc.lower()).split() for doc in docs]
query = docs[-1]
docs = docs[:-1]

corpus = []
for doc in docs:
    for token in doc:
        corpus.append(token)

lambda_value = 0.5
probs = []
for doc_index, doc in enumerate(docs):
    doc_counter = Counter(doc)
    corpus_counter = Counter(corpus)
    words_num = len(doc)
    words_corpus_num = len(corpus)

    prob = 1
    for token in query:
        smoothed = lambda_value * (doc_counter[token] / words_num) + (1 - lambda_value) * (corpus_counter[token] / words_corpus_num)
        prob = prob * smoothed
    probs.append((doc_index, prob))
probs = sorted(probs, key=lambda x: x[1], reverse=True)

results = []
for result in probs:
    results.append(result[0])
print(results)