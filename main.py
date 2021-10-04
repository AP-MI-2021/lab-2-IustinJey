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