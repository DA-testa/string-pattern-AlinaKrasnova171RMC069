# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    select = input()[0]
    if "I" in select:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in select:
        with open('./tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    
def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    prime = 10**9+7
    # and return an iterable variable
    return RB_algorithm(pattern, text, prime)    

def RB_algorithm(pattern, text, prime):
    M = len(pattern)
    N = len(text)
    d = 256
    q = prime
    h = pow(d, M-1, q)
    P = 0
    T = 0
    result = []
    
    for i in range(M):
        P = (P*d + ord(pattern[i])) % q
        T = (T*d + ord(text[i])) % q

    for i in range(N-M+1):
        if P == T:
            if pattern == text[i:i+M]:
                result.append(i)

        if i < N-M:
            T = (d*(T-ord(text[i])*h) + ord(text[i+M])) % q

    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

    
  