def print_rangoli(size):
    import string
    
    alphabet = string.ascii_lowercase
    
    top_rangoli = []
    
    # Create the top part of the rangoli
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        top_rangoli.append((s.center(size * 4 - 3, '-')).center(size * 2 - 1, '-'))
    
    # Combine the top and bottom parts of the rangoli
    complete_rangoli = top_rangoli[::-1] + top_rangoli[1:]
    
    # Print each line with newline character
    for line in complete_rangoli:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)