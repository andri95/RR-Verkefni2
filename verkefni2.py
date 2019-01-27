
# Verkefni 2 - Andri Fannar

val = ""
while val != "6":
    print("1 - Liður 2")
    print("2 - Liður 3")
    print("3 - Liður 4")
    print("4 - Liður 5")
    print("5 - Liður 6")
    print("6 - Hætta")
    val = input("Veldu lið: ")

    if val == "1":

        def tugakerfi_binary(tala):
            if tala > 1:
                tugakerfi_binary(tala // 2)
            print(tala % 2, end="")

        tala = int(input("Enter a number: "))

        tugakerfi_binary(tala)
        print()

    elif val == "2":

        def summa(m):
            if m == 1:
                return 1
            return m ** 2 + summa(m-1)

        m = int(input("Sláðu inn náttúrulega tölu: "))
        print(summa(m))
        print()



    elif val == "3":

        def runa(m):
            if m == 1:
                print("1", end =" ")
                return 1
            else:
                rec = m + runa(m - 1)
                print(rec, end=" ")
                return rec

        m = int(input("Sláðu inn náttúrulega tölu: "))
        runa(m)
        print()


    elif val == "4":

        def thversumma(n):
            if n < 10:
                return n
            else:
                return thversumma(n // 10) + thversumma(n % 10)

        n = int(input("Sláðu inn heiltölu: "))
        print(thversumma(n))
        print()


    elif val == "5":

        def samnefnari(n, m):
            if m == 0:
                return n
            else:
                return samnefnari(m, n % m)

        n = int(input("Tala 1: "))
        m = int(input("Tala 2: "))

        print(samnefnari(n, m))
        print()

    elif val == "6":
        print("Takk fyrir komuna!")

    else:
        print("Rangur innsláttur, reyndu aftur!")

