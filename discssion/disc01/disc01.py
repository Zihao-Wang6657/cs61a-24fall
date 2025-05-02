#Q1:Race
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# one solution: x=2,y=3

#Q2:Q2: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i=1
    while i<=16:
        if i%3==0 and i%5==0:
            print('fizezbuzz')
        elif i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print(i)
        i+=1



#Q3: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return False
    if n==2:
        return True
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True


#Q4: Unique Digits
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count=0
    i=0
    while n>0:
        i=n%10
        n=n//10
        if has_digit(n,i)==False:
            count+=1
    return count

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    i=0
    while n>0:
        i=n%10
        if i==k:
            return True
        n=n//10
    return False


#Q5: Bottles
#solution:
#  (1)b  (2)d  (3)c


