# 3.4

for i in range(2):
    for l in range(7):
        print("@", end="")
    print()


#3.9
num = int(input("Please enter a number between 7 and 10 digits >"))

while num <= 1000000 or num >= 9999999999:
    print("Not a number between 7 and 10 digits")
    num = int(input("Please enter a number between 7 and 10 digits >"))

for i in str(num):
    print(i)

# 3.11
list = []
list2 = []

while True:
    miles = float(input("Enter how many miles traveled >"))
    if miles == 0:
        print(f"The overall average miles/gallon was: {sum(list)/sum(list2)}")
        break
    gas = float(input("Enter amount of gas used >"))
    list.append(miles)
    list2.append(gas)

    print(f"The miles/gallon for this tank was {miles/gas}")
        

# 3.12
num = int(input("Please input a 5-digit integer >"))
orig = num
backwards = 0

while num > 0:
    first = num % 10
    backwards = reversed * 10 + first
    num //= 10

if orig == reversed:
    print("Palindrome!!")
else:
    print("Not a Palindrome")

# 3.14
sum = 0
denominator = 1
for i in range(1, 3000):
    if i % 2 == 0:
        sum -= 4/denominator
    else:
        sum += 4/denominator
    denominator += 2

print(sum)