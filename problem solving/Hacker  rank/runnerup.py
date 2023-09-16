if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    highest = second_highest = float('-inf')
    
    for a in arr:
        if a > highest:
            second_highest = highest
            highest = a
        elif a > second_highest and a < highest:
            second_highest = a
            
    print(second_highest)