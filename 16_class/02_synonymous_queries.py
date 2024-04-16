# There are an array of pairs of synonym words
# and an array of queries where each query
# consists of two sentences.
# Write a function that takes these two arrays
# and returns for each query
# if two sentences in the query are synonyms.
#
# Example
# Input:
#   [("love", "like"), ("cat", "kitten"), ("meat", "chicken")],
#   [("cat love meat", "cat like chicken"), ("cat hate meat", "kitten love chicken")]
# Output:
#   [True, False]


from collections import defaultdict


# Assumptions:
# - word can have multiple synonyms
# - order matters
# - synonyms are not transitive
# - synonyms can only map from one word to another (not to multiple words)
def synonymous_queries_non_transitive(synonym_words, queries):
    synonyms = defaultdict(set)
    for w1, w2 in synonym_words:
        synonyms[w1].add(w2)

    result = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            result.append(False)
            continue
        is_synonym = True
        for w1, w2 in zip(q1, q2):
            if w1 == w2:
                continue
            elif (w1 in synonyms and w2 in synonyms[w1]) or (w2 in synonyms and w1 in synonyms[w2]):
                continue
            is_synonym = False
            break
        result.append(is_synonym)

    return result


# O(S + Q * W) -- time
# O(S + Q) -- space


# Assumptions:
# - word can have multiple synonyms
# - order matters
# - synonyms are transitive
# - synonyms can only map from one word to another (not to multiple words)
def synonymous_queries(synonym_words, queries):
    dsu = {}

    def create(x):
        dsu[x] = x

    def find(x):
        if dsu[x] == x:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        dsu[root_x] = root_y

    for w1, w2 in synonym_words:
        if w1 not in dsu:
            create(w1)
        if w2 not in dsu:
            create(w2)
        union(w1, w2)

    result = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            result.append(False)
            continue
        is_synonym = True
        for w1, w2 in zip(q1, q2):
            if w1 == w2:
                continue
            elif w1 in dsu and w2 in dsu and find(w1) == find(w2):
                continue
            is_synonym = False
            break
        result.append(is_synonym)

    return result

# O(S + Q * W) -- time
# O(S + Q) -- space
