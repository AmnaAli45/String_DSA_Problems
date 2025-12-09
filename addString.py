# Given two non negative integers represented as string , return their sum as a string

def addString(num1,num2):
    n1 = int(num1)
    n2 = int(num2)
    sum = n1+n2
    return str(sum)

str1 = input("ENTER FIRST NUM: ")
str2 = input("ENTER SECOND NUM: ")
print("RESULT IS: ", addString(str1,str2))
