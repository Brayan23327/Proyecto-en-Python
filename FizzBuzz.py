print("Welcome to FizzBuzz!")
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 7 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"    
    if numero % 7 == 0:
        return "Buzz"
    else:
        return str(numero) 
entrada = input("")
limite = int(entrada)
for i in range(1, limite + 1):
    print(fizzbuzz (i))
