def armstrong_numb(number):
    m = 0
    count = 0
    x=number
    while x>0:
        c = x/10
        m+= (c*10)
        count+=1


armstrong_numb(555)