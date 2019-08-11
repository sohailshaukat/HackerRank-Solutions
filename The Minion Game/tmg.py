'''
problem URL: https://www.hackerrank.com/challenges/the-minion-game/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def isVowel(char):
    vowels = ['a','e','i','o','u']
    return char.lower() in vowels

def minion_game(string):
    kevin = 0
    stuart = 0
    length = len(string)
    for i,char in enumerate(string):
        if isVowel(char):
            kevin += length - i
        else:
            stuart += length - i
    if (kevin) > (stuart):
        print('Kevin '+str(kevin))
    elif (kevin) < (stuart):
        print('Stuart '+str(stuart))
    else:
        print('Draw')

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
