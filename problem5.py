
# user input
number = input("Enter a number: ")

# Do not forget to check that the input is valid (ie. the input is a number).
try:
    number_check = int(number)
except ValueError:
    print ("Please enter a whole positive number.")
else:

    # separate the number by each digit

    digit = 0
    sum = 0
    while digit < len(number):
        # when digit is an odd number, add the digit to the sum
        if digit % 2 == 0:
            sum += int(number[digit])
            digit = digit + 1
        # when digit is an even number, subtract the digit from the sum
        else:
            sum -= int(number[digit])
            digit = digit + 1

    if sum % 11 == 0:
        print("This is divisible by 11")
    else:
        print("This is not divisible by 11")

    # check if the number is divisible by 11
    # if int(number) % 11 == 0:
    #    print("Double checked. This is divisible by 11")
    # else:
    #    print("Double checked. This is not divisible by 11")