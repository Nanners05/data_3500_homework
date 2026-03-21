# for i in range(2):
#     for j in range(7):
#         print("@", end=(""))
#     print("@")


# num = int(input("Please enter and integer between 7 and 10 digits >"))
# while True:
#     if num >= 1000000 and num <= 9999999999:
#         for i in str(num):
#             print(i)
#         break
#     else:
#         print("Not the correct amount of digits")
#         num = int(input("Please enter and integer between 7 and 10 digits >"))


while True:
    num = input("Please enter and integer between 7 and 10 digits >")
    if num.isdigit() and 7 <= len(num) <= 10:
        for i in str(num):
            print(i)
        break
    else:
        num = input("Please enter and integer between 7 and 10 digits >")

# lst = []
# lst2 = []

# while True:
#     miles = float(input("Enter miles driven >"))
#     if miles == -1:
#         break
#     print(f"Miles/gallon: {miles/gallons}")
#     lst.append(gallons)
#     lst2.append(miles)
#     gallons = float(input("Enter gallons used >"))
        

# print(f"Overall average miles/gallon: {(sum(lst2)/len(lst2)/(sum(lst)/len(lst)))}")