def Main(num):
    result = int2str(num)
    return result


def int2str(num):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    firstRun = True

    while num > 0:
        remainder = num % 10
        num = num / 10
        digit = digits[remainder]

        if firstRun:
            result = digit
            firstRun = False
        else:
            result = concat(digit, result)

    return result
