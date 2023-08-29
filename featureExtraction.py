# feature extraction, agnostic to paragraph length

# average word length
# most common vowel
# least common vowel
# double letters ratio


englishData1 = "Hey there! Lately, things have been changing a lot thanks to technology. You know, how we talk to our pals and deal with our jobs has gone through a big shift. Smartphones and social media have made the world feel like a smaller place, bringing folks from everywhere closer together. Plus, there's all this talk about automation and AI shaking up different industries, offering up fresh and better solutions for tricky stuff"
spanishData1 = "¡Hola! Últimamente, todo ha estado cambiando un montón gracias a la tecnología. Sabes, la forma en que charlamos con nuestros amigos y manejamos nuestros trabajos ha tenido un cambio grande. Los teléfonos inteligentes y las redes sociales han hecho que el mundo parezca más pequeño, acercando a la gente de todas partes. Además, está toda esta charla sobre automatización e inteligencia artificial revolucionando diferentes industrias, ofreciendo soluciones nuevas y mejores para cosas complicadas"


def averageWordLength(paragraph):
    wordList = paragraph.split()

    total = 0
    for word in wordList:
        total += len(word)

    avg = total / len(wordList)

    return avg


#print("average")
#print(averageWordLength(englishData1))
#print(averageWordLength(spanishData1))


def mostCommonVowel(paragraph):

    aCount = 0
    eCount = 0
    iCount = 0
    oCount = 0
    uCount = 0

    for letter in paragraph:
        if letter.lower() in ['a', 'á', 'à', 'â', 'ä', 'ã', 'å', 'ā', 'æ']:
            aCount += 1
        if letter.lower() in ['e', 'é', 'è', 'ê', 'ë', 'ẽ', 'ē', 'ę']:
            eCount += 1
        if letter.lower() in ['i', 'í', 'ì', 'î', 'ï', 'ĩ', 'ī']:
            iCount += 1
        if letter.lower() in ['o', 'ó', 'ò', 'ô', 'ö', 'õ', 'ō', 'ø']:
            oCount += 1
        if letter.lower() in ['u', 'ú', 'ù', 'û', 'ü', 'ũ', 'ū']:
            uCount += 1

    counts = [aCount, eCount, iCount, oCount, uCount]

    if aCount == max(counts):
        return 1
    if eCount == max(counts):
        return 2
    if iCount == max(counts):
        return 3
    if oCount == max(counts):
        return 4
    if uCount == max(counts):
        return 5


#print("most common vowel")
#print(mostCommonVowel(englishData1))
#print(mostCommonVowel(spanishData1))


def leastCommonVowel(paragraph):

    aCount = 0
    eCount = 0
    iCount = 0
    oCount = 0
    uCount = 0

    for letter in paragraph:
        if letter.lower() in ['a', 'á', 'à', 'â', 'ä', 'ã', 'å', 'ā', 'æ']:
            aCount += 1
        if letter.lower() in ['e', 'é', 'è', 'ê', 'ë', 'ẽ', 'ē', 'ę']:
            eCount += 1
        if letter.lower() in ['i', 'í', 'ì', 'î', 'ï', 'ĩ', 'ī']:
            iCount += 1
        if letter.lower() in ['o', 'ó', 'ò', 'ô', 'ö', 'õ', 'ō', 'ø']:
            oCount += 1
        if letter.lower() in ['u', 'ú', 'ù', 'û', 'ü', 'ũ', 'ū']:
            uCount += 1

    counts = [aCount, eCount, iCount, oCount, uCount]

    if aCount == min(counts):
        return 1
    if eCount == min(counts):
        return 2
    if iCount == min(counts):
        return 3
    if oCount == min(counts):
        return 4
    if uCount == min(counts):
        return 5


#print("least common vowel")
#print(leastCommonVowel(englishData1))
#print(leastCommonVowel(spanishData1))


def doubleLettersFrequency(paragraph):

    wordList = paragraph.split()

    doubleLetterCount = 0
    for word in wordList:
        for i in range(len(word) - 2):
            if word[i] == word[i+1]:
                doubleLetterCount += 1
    freq = 0

    if doubleLetterCount != 0:

        freq = len(wordList) / doubleLetterCount

    return freq


#print("double letter frequency")
#print(doubleLettersFrequency(englishData1))
#print(doubleLettersFrequency(spanishData1))
