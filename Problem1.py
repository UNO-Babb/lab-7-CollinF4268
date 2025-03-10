# Problem1.py
# Project Euler Problem 1

import NumberTests 

def isPalindrome(n):
    """Checks if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def main():
    largest_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if isPalindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                
    print(largest_palindrome)  

if __name__ == "__main__":
    main()