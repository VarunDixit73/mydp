def triangle(b,h):
    return 0.5*b*h

#triangle() :- TypeError: triangle() missing 2 required positional arguments: 'b' and 'h'

def bike(petrol):
    while petrol > 0:
        print('Wrr Wrr Wrroooom')
        petrol-=1
    print('phir se petrol bharo')

bike(21)
#TypeError: bike() missing 1 required positional argument: 'petrol'