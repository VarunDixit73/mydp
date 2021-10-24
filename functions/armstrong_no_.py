def armstrong_numb(number):
    sum = 0
    size = len(str(number))
    digit= int(number)
    while digit>0:
        c = digit%10
        sum+= (c**size)
        digit//=10
    if number == sum:
        print(f'{number} is an Armstron Number.')
    else:
        print(f'{number} is not an Armstrong Number.')

armstrong_numb(int(input('Enter a number: ')))