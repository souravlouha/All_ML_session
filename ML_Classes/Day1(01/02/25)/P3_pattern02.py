n = 5  

# upper half of the diamond
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#  lower half of the diamond
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''




for i in range(1,n+1):
      print("*"*i)
for i in range(n-1,0,-1):
      print("*"*i)

'''
*
**
***
****
*****
****
***
**
*
*
'''




# upper half of the diamond
for i in range(1, n+1):
    print("*" * (n - i) + " " * (2 * i - 1)+"*" * (n - i))

#  lower half of the diamond
for i in range(n-1, 0, -1):
    print("*" * (n - i) + " " * (2 * i - 1)+"*" * (n - i))

    '''
****** ******
*****   *****
****     ****
***       ***
**         **
*           *

*           *
**         **
***       ***
****     ****
*****   *****
****** ******
    '''