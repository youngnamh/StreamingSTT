message = [['0', 'Hello', 0.965], [None, '.', None], ['0', 'My', 1.0], ['0', 'name', 1.0], ['0', 'is', 1.0],
           ['0', 'Dave', 1.0], [None, '.', None], [
               '0', 'I', 0.8768], ['0', 'like', 1.0], ['0', 'to', 1.0],
           ['0', 'go', 1.0], ['0', 'to', 1.0], ['0', 'the', 1.0], [
               '0', 'movies', 1.0], ['0', 'and', 1.0],
           ['0', 'eat', 1.0], ['0', 'lots', 1.0], ['0', 'of', 1.0], [
    '0', 'popcorn', 1.0], ['0', 'and', 1.0],
    ['0', 'drink', 1.0], ['0', 'lots', 1.0], ['0', 'of', 1.0], ['0', 'soda', 1.0], [None, '.', None]]

message2 = [['0', 'Hello', 0.965], [None, '.', None], ['0', 'My', 1.0], ['0', 'name', 1.0], ['0', 'is', 1.0],
            ['0', 'Dave', 1.0], [None, '.', None], [
    '1', 'I', 0.8768], ['1', 'like', 1.0], ['1', 'to', 1.0],
    ['1', 'go', 1.0], ['1', 'to', 1.0], ['1', 'the', 1.0], [
    '1', 'movies', 1.0], [None, '.', None], ['0', 'And', 1.0],
    ['0', 'eat', 1.0], ['0', 'lots', 1.0], ['0', 'of', 1.0], [
    '0', 'popcorn', 1.0], ['0', 'and', 1.0],
    ['0', 'drink', 1.0], ['0', 'lots', 1.0], ['0', 'of', 1.0], ['0', 'soda', 1.0], [None, '.', None]]


messageColors = {
    'S0': [255, 0, 0],
    'S1': [0, 255, 0],
    'S2': [0, 0, 255],
}

speakersArr = ['S0', 'S1', 'S2']


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# takes in json and returns a dictionary of speaker: words


def speakerCategorizer(msg):
    if (len(msg) == 0):
        return 'ERROR: empty message'

    bank = []
    # set first speaker and start a string
    currentSpeaker = msg[0][0]
    currentString = ""
    # add all words each speaker said to the bank dictionary
    for word in msg:
        speaker = word[0]
        content = word[1]
        confidence = word[2]
        if isinstance(confidence, float):
            if confidence < 0.9:
                content = '*' + content + '*'
        # print(f"({speaker},{content},{confidence})")
        # if the next word is the same speaker
        if speaker == currentSpeaker:
            if currentString == "":
                currentString += content
            else:
                currentString += " "+content
        # if punctuation
        elif speaker == None:
            currentString += content
        # if switch speakers
        elif speaker != currentSpeaker:
            bank.append([currentSpeaker, currentString])
            currentSpeaker = speaker
            currentString = content
    bank.append([currentSpeaker, currentString])
    return bank


# takes in dictionary and prints colored strings for each speaker


def printAllSpeakers(bank):
    if (len(bank) == 0):
        return 'ERROR: empty bank'

    for sentence in bank:
        print(
            f"[Speaker {sentence[0]}]: {printDifferentColors('S'+sentence[0], sentence[1])}")
        # if speaker != 'S1':
        # print(f"[{speaker}]: {printDifferentColors(speaker, sentence)}")

# returns a string in a specific color


def printDifferentColors(speaker, words):
    global speakersArr
    isValidSpeaker = speaker in speakersArr

    # if its a valid speaker, return in color, otherwise return as is
    if isValidSpeaker:
        global messageColors
        colorCode = messageColors.get(speaker)
        return colored(colorCode[0], colorCode[1], colorCode[2], words)
    return words


def execute(msg):
    bank = speakerCategorizer(msg)
    printAllSpeakers(bank)


def test():
    execute(message)
    print()
    execute(message2)
