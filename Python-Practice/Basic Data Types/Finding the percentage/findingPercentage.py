'''
problem URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/3
    query_name = input()
    print("{0:.2f}".format(student_marks[query_name]))
