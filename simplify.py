text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way-in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

# What the script does is find those clause with "it was the "(case insensitive).
# And find the words after the " of ".
# At last filter out those With capitals.
# So I rewrite them all from scratch.


def capture_text():
    clauses = text.split(',')
    filtered = []
    for clause in clauses:
        if clause.lower().find('it was the') != -1:
            word = clause[len('it was the '):]
            word = word[word.find(' of ') + len(' of '):]
            if not word.istitle():
                filtered.append(word)
    return filtered


if __name__ == "__main__":
    print(capture_text())