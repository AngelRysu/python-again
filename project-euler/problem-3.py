"""Largest prime factor
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143

https://www.mathsisfun.com/prime-factorization.html
"""

def prime (n):
    largest = None
    
    while n % 2 == 0:
        largest = 2
        n//=2
        
    factor = 3
    
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
        
    if n > 2:
        largest = n
    
    return largest

print(prime(600851475143))