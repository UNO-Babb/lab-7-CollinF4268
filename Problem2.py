#Problem2.py
#Project Euler problem 2

from NumberTests import isEven
from NumberTests import fibonacciSequence
from NumberTests import isPrime  

def findNthPrime(n):
    """Finds the nth prime number."""
    count = 0  
    num = 1  

    while count < n:  
        num += 1
        if isPrime(num):  
            count += 1

    return num  

def main():
    result = findNthPrime(10001)  
    print(result)  

if __name__ == "__main__":
    main()