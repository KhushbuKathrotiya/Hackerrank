def average(array):
    unique_heights = set(array)
    total_height = sum(unique_heights)
    distinct_heights_count = len(unique_heights)
    average_height = total_height / distinct_heights_count
    return round(average_height, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)