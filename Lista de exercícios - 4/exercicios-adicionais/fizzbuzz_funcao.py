def fizzbuzz(x):
    if (x % 15 == 0):
        msg = 'FizzBuzz'
    else:
        if (x % 3 == 0):
            msg = 'Fizz'
        else:
            if (x % 5 == 0):
                msg = 'Buzz'
            else:
                msg = x
    return msg
