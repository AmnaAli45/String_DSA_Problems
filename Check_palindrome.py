str=input("Enter a string: ")

start = 0
end = len(str) - 1
palindrome = True

while start < end:
    if str[start] != str[end]:
        palindrome = False
        break
    start += 1
    end -= 1

if (palindrome):
    print ("String is a valid Palindrome")
else:
    print("String is not a valid  Palindrome")