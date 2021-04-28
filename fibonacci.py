# define your function
def fibonacci(n):
  #
  if n <= 1:
    return n
  else:
    return ( fibonacci(n - 1) +  fibonacci(n - 2))
#   user must input a value/number
terms_1 = int(input('number of terms: '))
#  validating the terms if the run
if terms_1 <= 0:
  print('please input a positive number: ')
else:
  print('Fibonacci Seq: ')
# looping through the n range
for i in range(terms_1):
    print(fibonacci(i), end="" )
