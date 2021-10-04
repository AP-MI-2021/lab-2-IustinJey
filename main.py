def is_prime(n):
    ok = 1
    for x in range(2, n , 1):
        if n % x == 0:
            ok = 0
    if ok == 1:
        return 1
    return 0

def size(n):
    nr = 0
    while n > 0:
        nr = nr + 1
        n = n // 10
    return nr + 1


def oglindit(n):
    r = 0
    while n > 0:
        r = r * 10 + (n % 10)
        n = n / 10
    return r

def is_superprime(n):
    p = 1
    ok = 1
    for x in range(1, size(n), 1):
        if is_prime(n // p) == 0:
            ok = 0
        p = p * 10
    if ok == 1:
        return True
    return False

def test_is_superprime():
    assert is_superprime(233) = True
    assert is_superprime(1) = False


test_is_superprime()

while True:
    n = int(input('Alege un numar: '))
    if n == -1:
        break
    print(is_superprime(n))



















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









# LAB 2 - PROBLEMA 5

def is_palindrome(n):
    c = n #copiem valoarea lui n
    nr = 0
    while n > 0:
        nr = nr * 10 + (n % 10)
        n = n // 10
    if nr == c:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(12) == False
    assert is_palindrome(11) == True
    assert is_palindrome(1)  == True

test_is_palindrome()
while True:
    n = int(input('Choose your number: '))
    if n == 0: #programul ruleaza pana la intalnirea valorii 0
        break
    print(is_palindrome(n))