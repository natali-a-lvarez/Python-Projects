# get words

def analyzer(words):
    frequency = {}
    words = words.split()
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    return frequency

