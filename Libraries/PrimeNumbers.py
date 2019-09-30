##This function returns all the prime numbers between a given range.
def getPrimeNumbers(lower, upper):
    numList = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numList.append(num)
    return numList

##This function checks a number whether it's a Prime Number or not.
def checkPrime(number):
    if number < 2:
        return False
    else:
        state = True
        for num in range(2, number):
            if number % num == 0:
                state = False
                break
        return state
