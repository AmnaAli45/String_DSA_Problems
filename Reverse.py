str = input("Enter a string: ")

start = 0
end = len(str)-1 #because indexing starts with 0

reversed_str=str[end::-1]

print("--------------------Reversed String ---------------")
print(reversed_str)
