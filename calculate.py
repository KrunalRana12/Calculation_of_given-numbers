K = int(input("ENTER THE FIRST VALUE (1) :- "))
A = int(input("ENTER THE SECOND VALUE (2) :- "))


mylist = (K, A)

mylist = int(input("ENTER YOUR CHOISE :- "))

if (mylist == 1 or mylist == 2 or mylist == 3 or mylist == 4 or mylist == 5 or mylist == 6):
    print("THE CHOISE IS = ",mylist)

match mylist:
    case 1:
        print("the addition is = ", K + A)
    case 2:
        print("the substraction is = ", K - A)
    case 3:
        print("the multiplication is = ", K * A)
    case 4:
        print("the division is = ", K / A)
    case 5:
        print("the floor division is = ",K // A)
    case 6:
        print("the multiplication power is = ",K ** A)