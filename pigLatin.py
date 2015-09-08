#
#   English to Pig Latin Translator
#   Elissa M Shinseki
#
#   v1.2 (2015) - Cleaned up code
#

#**************************************************************
# MODULE : getTranslatedLine
# INPUTS : text
# OUTPUTS : translatedLine
# DEF : Compiles translated words into line
#**************************************************************

def getTranslatedLine(text):
    
    translatedLine = ''
    
    # Splits text
    words = text.split()
    
    # Compiles translated line one word at a time
    for i in range(len(words)):
        translatedLine = translatedLine + translate(words[i])

    return translatedLine

#**************************************************************
# MODULE : translate
# INPUTS : word
# OUTPUTS : translatedWord
# DEF : Translates individual words to pig latin
#**************************************************************

def translate(word):

    startPunct = ''
    endPunct = ''
    
    # If only numbers or contains no mix of letters and numbers, no translation
    if word.isdigit() or not word.isalnum():
        translatedWord = word + " "
    
    # Translation for words that contain alphanumeric characters
    else:
        # Saves external punctuation to add back later
        if not word[0].isalpha():
            startText = findStartText(word)
            startPunct = word[:startText]
            word = word[startText:]         # Trims front punctuation

        if not word[len(word) - 1].isalpha():
            endText = findEndText(word)
            endPunct = word[endText:]
            word = word[:endText]           # Trims back punctuation

        # Words that begin with a vowel have "way" appended to it
        if word[0] in 'aeiouAEIOU':
            translatedWord = startPunct + word[0] + word[1:].lower() + 'way' + \
                             endPunct + ' '
            
        # Words that begin with a consonant are translated with its first vowel
        else:
            # Find the location of the first vowel
            firstV = findVowel(word)

            # If no vowel, simply adds "way" to the end of the word
            if firstV == -1:
                translatedWord = startPunct + word[0] + word[1:].lower() +\
                    'way' + endPunct + ' '
                
            # Otherwise, builds the word starting from new vowel
            else:               
                newFirstLetter = word[firstV]
                rest = (word[firstV + 1:] + word[0:firstV]).lower()
                
                if word[0].isupper():
                    newFirstLetter = newFirstLetter.upper()
                
                # Builds translated word from pieces
                translatedWord = startPunct + newFirstLetter + rest + 'ay' + \
                                 endPunct + ' '
        
    return translatedWord

#**************************************************************
# MODULE : findStartPunct
# INPUTS : word
# OUTPUTS : startPunct
# DEF : Returns location of the letter where a string of punctuation at the
# beginning of a word ends.
#**************************************************************

def findStartText(word):

    startText = 0
    startCount = 0

    # Finds first location of alphabetic characters
    while not word[startCount].isalpha():
        startText = startCount
        startCount += 1
    
    return startText + 1

#**************************************************************
# MODULE : findEndPunct
# INPUTS : word
# OUTPUTS : endPunct
# DEF : Returns location of the letter where a string of punctuation at the end
# of a word begins.
#**************************************************************

def findEndText(word):

    endText = 0
    endCount = 1

    # Finds last location of alphanumeric characters
    while not word[len(word) - endCount].isalpha():
        endText = len(word) - endCount
        endCount += 1

    return endText
    
#**************************************************************
# MODULE : findVowel
# INPUTS : word
# OUTPUTS : firstV
# DEF : Returns the numeral location of the first vowel in a word
#**************************************************************

def findVowel(word):

    vowelPlace = []
    vowels = 0
    count = 0
    
    # Finds locations for up to two vowels
    while vowels < 2 and count < len(word):
        if word[count] in 'aeiouyAEIOUY':
            vowelPlace += [count]
            vowels += 1
        count += 1

    # Assigns first vowel location to firstV, if one exists
    if word[0] not in 'Yy' and len(vowelPlace) >= 1:
        firstV = vowelPlace[0]

        # If 'QU' word, assigns second vowel location to firstV
        if len(vowelPlace) > 1 and \
            word[int(vowelPlace[0])] in 'Uu' and \
            word[int(vowelPlace[0]) - 1] in 'Qq':

            firstV = vowelPlace[1]

    # If 'Y' is the first letter, picks the second vowel position
    elif len(vowelPlace) >= 2:
            firstV = vowelPlace[1]
        
    # Otherwise, returns error code for no vowel
    else:
        firstV = -1
               
    return firstV

#**************************************************************
# MODULE : newName
# INPUTS : fileName
# OUTPUTS : newFileName
# DEF : Returns the translated file name for the new text file
#**************************************************************

def newName(fileName):
    
    # Removes the file extension
    name = fileName[:len(fileName) - 4].split()
    newFileName = ''
    
    # Translates each part of the file name
    for i in range(len(name)):
        translatedWord = translate(name[i])
        newFileName += translatedWord
    
    # Adds txt file extension
    newFileName = newFileName.rstrip() + '.txt'
    
    return newFileName
    
#**************************************************************
# MODULE : main
# DEF : Main algorithm for running the pig latin translator program
#**************************************************************

def main():
    text = ''
    translatedLine = ''

    # Opening message, gets text filename
    print("Welcome to the Pig Latin Translator!")
    fileName = input("Enter file name of text to translate: ")
    
    # Converts old filename to new name
    newFileName = newName(fileName)
    
    # Opens text file and file to write translation to
    inFile = open(fileName, 'r')
    outFile = open(newFileName + ".txt", 'w')

    # Reads translated text one line at a time,
    # writes it to the new file,
    # and prints it to the screen
    text = inFile.readline()
    print("\nTranslated text:")
    
    while text != '':
        translatedLine = getTranslatedLine(text)
        print(translatedLine)
        outFile.write(translatedLine + '\n')
        text = inFile.readline()
          
    inFile.close()
    outFile.close()

main()
