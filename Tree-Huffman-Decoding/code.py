#! python3
'''
problem URL: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def decodeHuff(root, s):
	#Enter Your Code Here
    current = root
    ptr = 0
    message = []
    while ptr < len(s):
        while current.left != None and current.right != None:
            if s[ptr] == '1':
                current = current.right
            else:
                current = current.left
            ptr += 1
        message.append(current.data)
        current = root 
    print(''.join(message))