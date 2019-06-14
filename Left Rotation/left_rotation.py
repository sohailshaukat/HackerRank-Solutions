'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(str, input().rstrip().split()))

    times = d%n
    while times:
        temp = a[0]
        del a[0]
        a.append(temp)
        times -= 1
    print(' '.join(a))
