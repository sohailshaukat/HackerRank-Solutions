'''
problem URL: https://www.hackerrank.com/challenges/nested-list/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    students_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name,score])
        score_list.append(score)
    last = min(score_list)
    i = 0
    while(i<len(score_list)):
        if score_list[i]==last:
            del score_list[i]
            i -= 1
        i+=1
    second_from_bottom = (min(score_list))
    second_from_bottom_list = []
    for i,el in enumerate(students_list):
        if el[1] == second_from_bottom:
            second_from_bottom_list.append(el[0])
    print(*sorted(second_from_bottom_list), sep="\n")
