############### RIGHT-ANGLED TRIANGLE ###############

# Input = int(input("Please enter the number of rows: "))
#
# for i in range(1,Input + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

############### RIGHT-ANGLED TRIANGLE (Tilt) ###############   (Control or Control Flow is the order in which the program executes itself)

# x = int(input("Please enter the number of rows: "))
# y = 1
#
# for i in range(1, x + 1):
#     for j in range(1, y + 1):
#         print("*", end=" ")
#     y += 2
#     print()

############### PYRAMID ###############

# x = int(input("Please enter the number of rows: "))
#
# for i in range(0, x):
#     for j in range(0, x - i - 1):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print()

############### PYRAMID (UPSIDE DOWN) ###############

# x = int(input("Please enter the number of rows: "))
#
# for i in range(0, x):
#     for j in range(0, i):
#         print(end=" ")
#     for j in range(0, x - i):
#         print("*", end=" ")
#     print()

############### DIAMOND ###############

# x = int(input("Please enter the number of rows: "))
#
# for i in range(0,x):
#     print( (" " * (x - i - 1)) + (("* ") * (i+1)))
# for j in range(x - 1, 0, -1):
#     print((" ") * (x - j) + (("* ") * (j)))
