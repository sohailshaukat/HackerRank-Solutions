for _ in iter(range(int(input()))):
    prisoner_count, candy_count, offset = list(map(int, input().rstrip().split()))
    print((candy_count+offset-2)%prisoner_count+1)