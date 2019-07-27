'''
problem URL:https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    word_list = wrapper.wrap(string)
    return '\n'.join(word_list)
