for i in range (1,6):
    q=(6-i)/2
    for j in range (i):
        p=" "
        print(p*round(q),"*",end="")
    print()
# for i in range(1, 7, 2):  # Increment by 2 to print odd rows (1, 3, 5)
#     q = (6 - i) // 2  # Number of leading spaces
#     print(" " * q + "*" * i)  # Print spaces + stars
