while True:
    try:
        input = int(raw_input('Please enter a three-digit number: '))
        break
    except ValueError:
        print "Please enter a number!"


def fizzbuzz(input):
    print "Fizz buzz counting up to {}".format(input)
    for number in range(1, input):
        if (number % 3 == 0) and (number % 5 == 0):
            print "fizzbuzz"

        elif number % 3 == 0:
            print "fizz"

        elif number % 5 == 0:
            print "buzz"

        else:
            print number

fizzbuzz(input)
