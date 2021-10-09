# remove
# searching value

colors= ['Yellow','Green','Blue','Purple','Pink','Black','Pink']
colors.remove('Yellow')
print(colors)
if 'jellow' in colors:
    colors.remove('jellow')
print(colors)
if 'Pink' in colors:
    colors.remove('Pink')
print(colors)


# POP
# remove value by idx- if not given removes last
# the removed value through pop can be stored in a variable
colors.pop(1)
print(colors)

seperated_value= colors.pop()
print(colors)
print(seperated_value)

colors.pop()
print(colors)

# Clear

colors.clear()
print(colors)
