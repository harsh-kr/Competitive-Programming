filename = input("Enter the file name : ")
ipfile = open(filename, 'r')
text = ipfile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + text.count('!') + text.count(':') + text.count(';')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
for word in text.split():
    for vowel in ['a','e','i','o','u'] :
        syllables = syllables + word.count(vowel)
    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables = syllables - 1
    if word.endswith('le'):
        syllables = syllables + 1

# Compute Flesch index and grade level
index = 206.835 - 1.015 * (words/float(sentences)) - 84.6 * (syllables/words)
level = int(round(0.39*(words/float(sentences))+11.8*(syllables/float(words))-15.59))

if index >= 0.0 and index <= 30.0:
    print("The Readability level is College Graduate")
elif index > 30.0 and index <= 50.0:
    print("The Readability level is College")
elif index > 50.0 and index <= 60.0:
    print("The Readability level is 10th to 12th grade")
elif index > 60.0 and index <= 70.0:
    print("The Readability level is 8th & 9th grade")
elif index > 70.0 and index <= 80.0:
    print("The Readability level is 7th grade")
elif index > 80.0 and index <= 90.0:
    print("The Readability level is 6th grade")
elif index > 90.0 and index <= 100.0:
    print("The Readability level is 5th grade")
elif not(filename.endswith('.txt')):
    print("This is not a text file")

print("The Flesch Index is ", index)
print("The grade level is ", level)
print(sentences, " sentences")
print(words, " words")
print(syllables, " syllables")