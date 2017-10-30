
def lines(a, b):
    """Return lines in both a and b"""
    # Split up the strings by line
    first = list(set(a.split("\n")))
    second = set(b.split("\n"))
    length = len(first)
    # Declare a list in which to store common lines
    similar = []
    # If a line is common, add it to new list
    for i in range(length):
        if first[i] in second:
            similar.append(first[i])
    return similar


from nltk.tokenize import sent_tokenize


def sentences(a, b):
    """Return sentences in both a and b"""
    # Split up the strings by line
    first = list(set(sent_tokenize(a)))
    second = set(sent_tokenize(b))
    length = len(first)
    # Declare a list in which to store common sentences
    similar = []
    # If a line is common, add it to new list
    for i in range(length):
        if first[i] in second:
            similar.append(first[i])
    return similar


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # Split up the strings by user-selected substring
    length = len(a)
    # Declare a list in which to store common substrings
    similar = []

    # If a line is common, add it to new list
    for i in range(length - n + 1):
        if a[i:i + n] in b:
            similar.append(a[i:i + n])

    return set(similar)
