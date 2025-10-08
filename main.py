# simple calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def main():
    print("select oeration")
    print("1. add")
    print("2. subract")
    print("3. multiply")
    print("4. divide ")
    choice =input("enter choice 1/2/3/4")
    x=float(input("enter the first number"))
    y=float(input("enter the second number"))
    if choice =='1':
        print(add)
    elif choice=='2':
        print(subtract)
    elif choice=='3':
        print(multiply)
    elif choice=='4':
        print(divide)
    else:
        print("invalid input")
if __name__=="__main__":
    main()
    





















    