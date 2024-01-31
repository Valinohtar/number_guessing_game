import random

def conversion(number):
    if number.isdigit():
        number = int(number)
    else:
        print("That is not a number, next time you play, please give number!")
        while number.isdigit() == 0:
            number = input("Please give a number: ")
    return int(number)
            


min = input("Please give lower limit: ")
min = conversion(min)
max = input("Please give upper limit: ")
max = conversion(max)

while min >= max:
    print("Lower limit cannot be bigger then upper limit.")
    decision = input("Do you want to swap limits? [YES] for swap. Everything else for new input: ")
    if decision.lower() == "yes".lower():
        temp = min
        min = max
        max = temp
        break
    min = input("Please give lower limit: ")
    conversion(min)
    max = input("Please give upper limit: ")
    conversion(max)

random_number = random.randint(min, max)

guess = input('Zgadnij liczbę: ')
guess = conversion(guess)
counter = 1
if guess > max or guess < min:
    print("Guess is out of range, please try again! ")
    guess = int(input('Zgadnij liczbę: '))


while guess != random_number:
    counter += 1
    print("Incorrect")
    if guess > random_number:
        print("Too big")
    else:
        print("Too small")
    guess = int(input('Zgadnij liczbę: '))

print("Great, it took you", counter ,"tries to guess the number")


            
