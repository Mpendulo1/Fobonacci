def fibonacci(n):
    if (n < 0):
        return 'Please give a number that is equal or greater than Zero'
    elif (n == 0):
        return 0
    elif (n <= 2):
        return 1
    else:
        return (fibonacci(n - 2) + fibonacci(n - 1))
# user must input a number/value
n = int(input('Fibonacci Of: '))
print('Is: ', fibonacci(n))
