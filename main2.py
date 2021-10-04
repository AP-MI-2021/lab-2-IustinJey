# LAB 2 - PROBLEMA 1

def isPrime(n):
    nr = 0
    for x in range(2, n, 1):
        if n % x == 0 :
            nr = nr + 1
    if nr == 0 :
        return True
    return False


def get_largest_prime_below(n):
    for x in range(n-1, 2, -1):
        if isPrime(x) == True:
            return x
    return -1

def test_get_largest_prime_below():
    assert get_largest_prime_below(-1) == -1
    assert get_largest_prime_below(2) == -1
while True:
    n = int(input('Choose your number:'))
    ''' programul ruleaza pana la introducerii valorii "0" '''
    if n == 0:
        break
    test_get_largest_prime_below()
    print(get_largest_prime_below(n))