def autocomplete(query,wordSet):
    result = []
    start = None
    for word in wordSet:
        if word[start:len(query)] == query: ##Check if substring is in query
            result.append(word)
    return result
