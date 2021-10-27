def is_leap_year(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                return True
            else:
                return False
        else:
            return True 
    else:
        return False

while True:
    c_year= int(input("Enter the year to check->>>"))
    while c_year>=1900 and c_year<= 10**5:
        print(is_leap_year(c_year))
        break