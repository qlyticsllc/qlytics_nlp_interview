text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way-in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

def capture_text():
    splits = text.split(',')
    start = 'it was the '
    cap_after = ' of '
    filtered = []

    for s in splits:
        if s.lower().find(start) != -1:
            s = s[len(start):]
            index = s.find(cap_after)
            if index != -1:
                word = s[index + len(cap_after):]
                if not word.istitle():
                    filtered.append(word)
    return filtered

if __name__ == "__main__":
    print(capture_text())