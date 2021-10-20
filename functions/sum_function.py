import file_function as ff


def sum(number):
    m = 0
    while number>0:
        x = number%10
        m+= x
        number//=10
    ff.writer('NewFile.txt',str(m))
sum(999)


def summer(numbers):
    total = 0
    for digit in str(numbers):
        total += int(digit)
    ff.writer('summer.txt',str(total))

summer(102355548)


