# NumberTests.py

def isThreeOrFive(n):
    """Returns boolean determination if number is multiple of 3 or 5"""
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

def isPrime(p):
    """Returns boolean (True/False) if the value given is prime."""
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def isEven(n):
    """Returns boolean about given value being even."""
    return n % 2 == 0

def addNum(numList, num):
    """Adds the given number to the given list. Does not add duplicate values."""
    if num not in numList:
        numList.append(num)

def fibonacciSequence(value):
    """Returns a list of numbers in the Fibonacci sequence up to the given value"""
    nums = [1, 2]
    while nums[-1] + nums[-2] < value:
        nums.append(nums[-1] + nums[-2])
    return nums

# Test functions in this main block
def main():
    knownPrimes = [3, 7, 11, 13, 17]

    num = int(input("Enter a number: "))

    if isPrime(num):
        print(f"{num} is a prime number")

    if isEven(num):
        print(f"{num} is an even number")

if __name__ == "__main__":
    main()