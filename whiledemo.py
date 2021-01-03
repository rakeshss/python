# Program 1: To demostrate simple while
print("# Program 1: To demostrate simple while")
number = 2

while number < 5 :
    print("Hello world!!")
    number = number + 1


# Program 2: To demostrate simple while along with if else condition
print("# Program 2: To demostrate simple while along with if else condition")
#Input read
number = 2

while number < 5 :

    if number%2 == 0:
        print("Even number: " + str(number))
    else:
        print("Odd number: " + str(number))

    number = number + 1

# Program 3: Program can be constructed you loop until desired condition is met
# #floor_division, #cast, #loop, #ifelse

def collatz(number):

    if number%2 == 0 :
        print(number//2)
        return number//2

    elif number%2 == 1 :
        result = number * 3 + 1
        print(result)
        return result

# Ask for user input:
n = input("Please provide a positive number")

while n!=1 :
    n = collatz(int(n))




