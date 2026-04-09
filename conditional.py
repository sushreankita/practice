 wap to check if num is even
num=int(input('enter a number: '))
if num%2==0:
    print(f"the number you choosed ie {num} it is a even number)


   

 wap to check if data is float
data=eval(input('enter a number: '))
if type (data) == float:
    print ('data entered is float value')


 

 wap to check weather the given number is multiple of 3
num=int(input('enter a number: '))
if num%3 == 0:
     print("this number is multiple of 3")

 
 wap to check weather the character is vowel
char=input('enter a char:')
vowel = 'aeiouAEIOU'
if char in vowel:
    print('this char is vowel')


 
wap to check if data is single value datatype
data=eval(input('enter a data :'))
if type(data)in [int,float,complex,bool]:
 print(f'{data} is single valued datatype')

 
wap to get the ascii value of character if it is in uppercase
char=input('enter a char: ')
if char >= 'A' and char <= 'Z' :
    print(ord(char))

wap to check whether character is digit or not
 char=input('enter a character: ')
 if char>='0' and char<='9':
     print('its a digit')
 else:
     print('its not a digit')


wap to given character is special character or not
 char=input('enter a char: ')
 if char in ('!@#$%^&*'):
     print('its a special character')
 else:
     print('its not a special character')

 char=input('enter a character: ')
 if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9'):
     print('its not a  special character')
 else:
     print('its a special character')

wap to check wheather number is positive or not
 num=int(input('enter a num: '))
 if num>0:
     print('the number is positive')
 else:
     print('the number is not positive')


wap to check if string is pallindrome or not
 s=input('enter a string: ')
 if s==s[::-1]:
    print('its a pallindrome')
 else:
     print('its not a pallindrome')


  wap to check if list is having middle value or not
 l=eval(input('enter a list'))
 if len(l)%2!=0:
     print('its having middle value')
 else:
     print('its not having middle value')

9-04-2026
wap to check the character is uppercase ,lowercase,numbers ,special characters
 char=input('enter the char: ')
 if char>='A' and char<='Z':
     print('its a uppercase')
 elif char>='a' and char<='z':
     print('its a lowercase')
 elif char>='0' and char<='9':
     print('its a number')
 else:
     print('its a special character')


wap to check wheather the integer is single digit ,double digit,triple digit,or ,more than triple digits
 num=int(input('enter a number: '))
 if num>=0 and num<=9:
     print('its a single digit number')
 elif num>=10 and num<=99:
     print('its a double digit number')
 elif num>=100 and num<=999:
     print('its a triple digit number')

wap to print fizz if user enters multiple of 3,print buzz if user enters multiple of 5,and print fiz buzz if it is multiple of 3 and 5 both
 num=int(input('enter a number: '))
 if num%3==0 and num%5==0:
     print('fizz buzz')
 elif num%3==0:
     print('fizz')
 elif num%5==0:
     print('buzz')

wap to find greatest of 3 number
 a=int(input('enter the first number: '))
 b=int(input('enter the second number: '))
 c=int(input('enter the third number: '))
 if a>=b and a>=c:
    print(f'{a} is the greatest')
 elif b>=a and b>=c:
     print(f'{b} is the greatest')
 else:
     print(f'{c} is the greatest')
    

wap to find the smallest of 3 number
 a=int(input('enter the first number: '))
 b=int(input('enter the second number: '))
 c=int(input('enter the third number: '))
 if a<=b and a<=c:
     print(f'{a} is the smallest')
 elif b<=a and b<=c:
     print(f'{b} is the smallest')
 else:
     print(f'{c} is the smallest')
    

wap to check the relation between two number
 a=int(input('enter the first number: '))
 b=int(input('enter the second number: '))
 if a>b:
     print(f'{a} is greater than b')
 elif a<b:
     print(f'{a} is less than b')
 else:
     print(f'{a}b is equal to ')






 


 
