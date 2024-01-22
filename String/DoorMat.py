# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_door_mat(N, M):
    # Upper pattern
    for i in range(1, N, 2):
        pattern = '.|.' * i
        print(pattern.center(M, '-'))

    # Welcome message
    print('WELCOME'.center(M, '-'))

    # Lower pattern
    for i in range(N - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(M, '-'))

if __name__ == '__main__':
    N, M = map(int, input().split())
    print_door_mat(N, M)