byte = int(input("enter number of bytes : "))
bites = 8
n = bites * byte

length1 =  (2**n)//2
length2 = (2**n)//2 -1
print(f"range of {byte} bytes is -{length1} to {length2}")