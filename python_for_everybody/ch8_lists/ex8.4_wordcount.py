"""

    Exercise 8.4
    
        Download a copy of the file from www.py4inf.com/code/romeo.txt
        Write a program to open the file romeo.txt and read it line by line. For each line,
        split the line into a list of words using the split function.

        For each word, check to see if the word is already in a list. If the word is not in the
        list, add it to the list.
        When the program completes, sort and print the resulting words in alphabetical order.

        Enter file: romeo.txt
        ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is',
        'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window',
        'with', 'yonder']

"""

romeo_data = open("../assets/romeo.txt")
words = {}

for line in romeo_data:
    print(line.strip())

    line_words = line.strip().split()
    print(line_words)

    for word in line_words:
        words[word] = words.get(word, 0) + 1

print(words.items())

result = list(words.keys())
result.sort()

print(type(result))

print(result)