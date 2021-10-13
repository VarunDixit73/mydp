#1. Create a srting and print it.
intro = input('Enter your name and tell us something about yourself:\n')
print(intro)

#2. Take a string input and print it's length.
intro_x= input('Enter a string of your choice:\n')
print('The size of the string =',len(intro_x))

#3. Print the last word of the string `Python is great` using slices.
x='Python is great'
print(x[-5:])

#4. Print the each word in different line of string `python is everywhere`.
x= 'python is everywhere'
for i in x:
    if i==' ':
        continue
    else:
        print(i)

#5. Print the string `Hello World!` in reverse.
str='Hello World!'
print('String in Reverse:\n',str[::-1])

#6. Convert the string `How are you?` in uppercase.
str='How are you?'
print('String in Upper Case:\n',str.upper())

#7. Convert the string `How Is It Going?` in lowercase.
lcase = 'How Is It Going?'
print('String in Lower Case:\n',lcase.casefold())

#8. Join the following list by spaces(` `) and print the result.
# words = ['Python', 'is', 'easy', 'to', 'learn']
words = ['Python', 'is', 'easy', 'to', 'learn']
content = " ".join(words)
print(content)

#9. Print a multiline string using a single `print`
mul_str= '''
Artists producing banknotes in Colonial America began experimenting with copper 
plates as an alternative to wood engraving in the early 18th century.
Applied to the production of paper currency, copper-plate engraving, 
and later steel engraving, enabled banknote design and printing to rapidly advance during the 19th century.
This engraved vignette appeared on certain United States five-dollar bills issued in 1875.
Produced for the Department of the Treasury's Bureau of Engraving and Printing, the engraving is of John Vanderlyn's 
painting Landing of Columbus, which hangs in the United States Capitol rotunda.
It depicts Christopher Columbus landing on San Salvador Island on October 12, 1492, on the first of his voyages to the New World.
'''
print('Multiline String using single string is as follows:\n',mul_str)

#10. Print this string `to move to newline '\n' is used.` (results should look exactly like the provided string)
#print(f'to move to newline \n is used.')
print('to move to newline \\n is used.')

#11. Print a variable with some text using a single print function, output should look like following.
#    ```
#    the variable is 15
#    ```
var = 'the variable is 15'
print(var)

#12. concatenate the following strings and print the result
#    ```py
#    s1 = 'python '
#    s2 = 'is '
#    s3 = 'great.'
#    ```
s1 = 'python '
s2 = 'is '
s3 = 'great.'
s_sum = s1+s2+s3
print(s_sum)

#13. Print `#` 20 times without using a loop
print('#'*20)

#14. Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
#    ```
#    1.
#    2.
#    3.
#
#    ```
i=1
while i<=20:
    print(i,end='.')
    print('')
    i+=1

#15. Ask user to input a sentence and print each word on a different line.
u_input= input("Enter a senterce:\n")
inp_len= len(u_input)

#16. Ask user to input a string and check if the string ends with '?'
u_input=input('Enter a string:\n')
if u_input=='?':
    print('True')
else:
    print('False')

#17. Ask user to input a string and print how many times `e` appeared in the string
u_input=input('Enter a string to search:\n')
x= u_input.casefold()
check= 0
for i in x:
    if i=='e':
        check+=1
print(f'e appeared {check} times in the given string.')

#18. Check if the user input is a number.
check_x = input('Enter a Number->>>')
ans=check_x.isnumeric()
print(ans)

#19. Remove the extra spaces in beginning and in the end of the following string-
#    ```py
#    text = '   this is not a good string           '
#    ```
text = '   this is not a good string           '
print(text)
corrected = text.strip()
print('String after correction :\n',corrected)

#20. Ask user to input string, print `found` if any of the character is upper case.
value= input("Enter something: ")
n_val=list(value)
check=0
for i in n_val:
    if i.isupper():
        check+=1
    else:
        continue
if check>0:
    print('found')


#21. Extract names from the following string and store them in a list.
#    ```py
#    names = 'Joe, David, Mark, Tom, Chris, Robert'
#    ```
#22. In the following string, add `aye` in the end of every word and print the results.
#    ```py
#    text = 'this is some text'
#    ```
#23. ask user to enter a string and check if the string contains `fyi`
#24. Remove all the special characters and numbers from the following string
#   ```py
#   text = '%p34@y!*-*!t68h#&on404'
#   ```
#25. calculate the average word length of the following paragraph.
#   ```
#   this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated
#   ```

