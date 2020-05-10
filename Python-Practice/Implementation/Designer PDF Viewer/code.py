'''
problem URL: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def designerPdfViewer(h, word):
    maximum_height = 0
    for char in word:
        if maximum_height < h[ord(char)-97]:
            maximum_height = h[ord(char)-97]
    return len(word)*maximum_height
