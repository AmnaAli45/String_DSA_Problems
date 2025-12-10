## Checking for balanaced strings - if the sum of numbers at even indices is equal to the sum of odd indices
def isBalanced( num):
        oddsum = 0
        evensum = 0
        itr = len(num)
        for i in range(itr):
            n = int(num[i])
            if i% 2 ==0:
                
                evensum = evensum + n
            else:
                oddsum = oddsum + n
        if evensum == oddsum:
            return True
        else:
            return False

inp = input("Enter the string: ")
res = isBalanced(inp)
if res:
     print("String is balanced")
else:
     print("String is not balanaced")