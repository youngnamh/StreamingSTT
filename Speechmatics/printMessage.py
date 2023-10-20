
import string
# from termcolor import colored


message = {'message': 'AddTranscript', 'format': '2.9', 'results': [{'alternatives': [{'confidence': 1.0, 'content': 'house', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.159999987930059, 'start_time': 13.620000000000001, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'and', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.309999984577297, 'start_time': 14.159999987930059, 'type': 'word'}, {'alternatives': [{'confidence': 0.7592900991439819, 'content': 'I', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.334179690610325, 'start_time': 14.309999984577297, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'have', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.459999981224536, 'start_time': 14.339999983906745, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'some', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.609999977871775, 'start_time': 14.459999981224536, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'time', 'language': 'en', 'speaker': 'S2'}], 'end_time': 14.999999969154596, 'start_time': 14.609999977871775, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': ',', 'language': 'en', 'speaker': 'S2'}], 'attaches_to': 'previous', 'end_time': 14.999999969154596, 'is_eos': False, 'start_time': 14.999999969154596, 'type': 'punctuation'}, {'alternatives': [{'confidence': 1.0, 'content': 'maybe', 'language': 'en', 'speaker': 'S2'}], 'end_time': 15.32999996177852, 'start_time': 14.999999969154596, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': "I'll", 'language': 'en', 'speaker': 'S2'}], 'end_time': 15.47999995842576, 'start_time': 15.32999996177852, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'take', 'language': 'en', 'speaker': 'S2'}], 'end_time': 15.719999953061341, 'start_time': 15.47999995842576, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'them', 'language': 'en', 'speaker': 'S2'}], 'end_time': 15.929999948367476,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'start_time': 15.719999953061341, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': '.', 'language': 'en', 'speaker': 'S2'}], 'attaches_to': 'previous', 'end_time': 15.929999948367476, 'is_eos': True, 'start_time': 15.929999948367476, 'type': 'punctuation'}, {'alternatives': [{'confidence': 1.0, 'content': 'Okay', 'language': 'en', 'speaker': 'S1'}], 'end_time': 16.289999940320847, 'start_time': 16.062518637422052, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': '.', 'language': 'en', 'speaker': 'S1'}], 'attaches_to': 'previous', 'end_time': 16.289999940320847, 'is_eos': True, 'start_time': 16.289999940320847, 'type': 'punctuation'}, {'alternatives': [{'confidence': 1.0, 'content': 'Well', 'language': 'en', 'speaker': 'S1'}], 'end_time': 16.52999993495643, 'start_time': 16.289999940320847, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': ',', 'language': 'en', 'speaker': 'S1'}], 'attaches_to': 'previous', 'end_time': 16.52999993495643, 'is_eos': False, 'start_time': 16.52999993495643, 'type': 'punctuation'}, {'alternatives': [{'confidence': 1.0, 'content': 'anyways', 'language': 'en', 'speaker': 'S1'}], 'end_time': 17.42999991483986, 'start_time': 16.52999993495643, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': ',', 'language': 'en', 'speaker': 'S1'}], 'attaches_to': 'previous', 'end_time': 17.42999991483986, 'is_eos': False, 'start_time': 17.42999991483986, 'type': 'punctuation'}, {'alternatives': [{'confidence': 1.0, 'content': 'moving', 'language': 'en', 'speaker': 'S1'}], 'end_time': 17.939999903440473, 'start_time': 17.42999991483986, 'type': 'word'}, {'alternatives': [{'confidence': 1.0, 'content': 'on', 'language': 'en', 'speaker': 'S1'}], 'end_time': 18.479999891370532, 'start_time': 17.939999903440473, 'type': 'word'}], 'metadata': {'end_time': 18.48, 'start_time': 13.620000000000001, 'transcript': "house and I have some time, maybe I'll take them. Okay. Well, anyways, moving on "}}


messageColors = {
    'S1': [255, 0, 0],
    'S2': [0, 255, 0],
    'S3': [0, 0, 255],
}


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# takes in json and returns a dictionary of speaker: words


def speakerCategorizer(msg):

    bank = {}
    words = msg['results']

    # add all words each speaker said to the bank dictionary
    for word in words:
        speaker = word['alternatives'][0]['speaker']
        content = word['alternatives'][0]['content']
        confidence = word['alternatives'][0]['confidence']
        # content = content + "({confidence})"
        if isinstance(confidence, float):
            if confidence < 0.9:
                percent = round(confidence*100, 1)
                content = f"*{content}* ({percent}%)"

        if speaker not in bank:
            # Initialize a list for the speaker if not already present
            bank[speaker] = []

        bank[speaker].append(content)

    return bank


def speakerDivider(msg):
    words = msg['results']
    if (len(words) == 0):
        return 'ERROR: empty message'
    bank = []
    # set first speaker and start a string
    currentSpeaker = words[0]['alternatives'][0]['speaker']

    currentString = ""
    # add all words each speaker said to the bank dictionary
    for word in words:
        speaker = word['alternatives'][0]['speaker']
        content = word['alternatives'][0]['content']
        confidence = word['alternatives'][0]['confidence']
        if isinstance(confidence, float):
            if confidence < 0.9:
                percent = round(confidence*100, 1)
                content = f"*{content}* ({percent}%)"
        # print(f"({speaker},{content},{confidence})")
        # if the next word is the same speaker
        wordType = word['type']
        if speaker == currentSpeaker:
            if currentString == "" or wordType == "punctuation":
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


def printDivide(bank):
    # if (len(bank) == 0):
    #   return 'ERROR: empty bank'

    for sentence in bank:
        print(
            f"[{sentence[0]}]: {printDifferentColors(sentence[0], sentence[1])}")
# takes in dictionary and prints colored strings for each speaker


def printAllSpeakers(bank):
    for speaker in bank:
        words = bank.get(speaker)
        sentence = ''
        for i, word in enumerate(words):
            if (len(word) == 1 and word in string.punctuation):
                sentence += word
            else:
                if i == 0:
                    sentence += word
                else:
                    sentence += " "+word
        print(f"[{speaker}]: {printDifferentColors(speaker, sentence)}")
        # if speaker != 'S1':
        # print(f"[{speaker}]: {printDifferentColors(speaker, sentence)}")

# returns a string in a specific color


def printDifferentColors(speaker, words):
    global messageColors
    colorCode = messageColors.get(speaker)
    return colored(colorCode[0], colorCode[1], colorCode[2], words)


def execute(msg):
    bank = speakerCategorizer(msg)
    printAllSpeakers(bank)


def executeDivide(msg):
    bank = speakerDivider(msg)
    printDivide(bank)
