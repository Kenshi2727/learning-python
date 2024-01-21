def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1

    except:
        print("Something went wrong...")
        return 0

    finally:
        print("This will always execute...even if function returns...")
    # print("This will always execute...")
x = func1()
print(x)