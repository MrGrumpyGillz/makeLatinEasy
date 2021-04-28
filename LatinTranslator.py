import sys
from wiktionaryparser import WiktionaryParser

#open file
f = open(sys.argv[1], 'r')

#make a new file to put translations in
newfile = open("latinTranslation.txt", 'w')

#type of lang you want to search in
language = sys.argv[2]

#parser
parser = WiktionaryParser()

#removeable char
badChar = [';', ':', '!', ',', '.', '?', '-']

#saved formatted words
wordPart = {}
wordText = {}
wordList = []

wordPart2 = {}
wordText2 = {}

notComparableWords = ['qua', 'factilis']
specialWords = ['qua']



for x in f:
    line = x.split()
    
    #formatting the file to make sure you can parse correctly
    for y in line:
        instring = y.lower()
        for i in badChar:
                instring = instring.replace(i, '')
        
        wordList.append(instring)
        try:
            #parse the word
            word = parser.fetch(str(instring), str(language))
            #print(word)
            definitions = word[0]['definitions']

        
            wordPart[instring] = definitions[0]['partOfSpeech']
            wordText[instring] = definitions[0]['text']
        except:
            print(instring, "not found or broken in parser")
    

      
       
for w in wordList:  

    try:

        if wordText[w][0].find("(") == -1 or w not in notComparableWords:
            newfile.writelines(w)
            newfile.writelines(" ")
            newfile.writelines(wordPart[w])
            newfile.writelines("\n")
            newfile.writelines(wordText[w][1]) #bug in this line python charmap cant handle the latin long a symbol 
            newfile.writelines("\n")
        elif w not in specialWords: 
            newfile.write('completed word')
            tempWord = wordText[w][1]
            newWords = tempWord.split()
            newWord = newWords[len(newWords) - 1]
            parseword = parser.fetch(str(newWord), str(language))
            test2 = parseword[0]['definitions']
            wordPart2[newWord] = test[0]['partOfSpeech']
            wordText2[newWord] = test[0]['text']
            

            newfile.writelines(w)
            newfile.writelines(" ")
            newfile.writelines(newWord)
            newfile.writelines(" ")
            newfile.writelines(wordPart[newWord])
            newfile.writelines("\n")
            newfile.writelines(wordText[newWord])    #bug in this line python charmap cant handle the latin long a symbol 
            newfile.writelines("\n")
    except:
        print(w, 'broke when adding to file')

