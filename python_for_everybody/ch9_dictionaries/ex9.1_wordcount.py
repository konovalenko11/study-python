"""

    Exercise 9.1
    
        Write a program that reads the words in words.txt and stores them as keys in a dictionary.
        It doesn’t matter what the values are.
        Then you can use the in operator as a fast way to check whether a string is in the dictionary.

"""

file_data = open("../assets/words.txt")
words = {}

for line in file_data:
    print(line.strip())

    line_words = line.strip().split()
    print(line_words)

    for word in line_words:

        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1

file_data.close()

print(words.items())

result = list(words.keys())
result.sort()

print(type(result))

print(result)