# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

newList = []
def findStringsWithCharacter ( wordList, character ):
    wordListLength = len(wordList)
    for i in range ( 0, wordListLength ):
        if character in wordList[i]:
            newList.append(wordList[i])
    print newList

findStringsWithCharacter( word_list, char )