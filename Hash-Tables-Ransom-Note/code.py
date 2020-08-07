input()

result = "Yes"

dictionary = {}

words = input().rstrip().split()
for word in iter(words):
    if dictionary.get(word, False):
        dictionary[word] += 1
    else:
        dictionary[word] = 1

para = {}

words = input().rstrip().split()
for word in iter(words):
    if dictionary.get(word,False):
        dictionary[word] -= 1
    else:
        result = "No"

print(result)