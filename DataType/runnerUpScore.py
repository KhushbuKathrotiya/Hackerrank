if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    List = set([x for x in arr])
    unique = sorted(List, reverse=True)
    print(unique[1])