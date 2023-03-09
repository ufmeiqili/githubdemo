def encode(): # might have parameters
    # write encode function up here
    # might return something
    pass

def func():
    print(x)

def main():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Please enter a non negative number")

    except ValueError as problem:
        print(problem)

    i_sum = 0
    for i in range(num):
        i_sum += 1
        func(i)
    # print menu using a while loop
    # ask for menu input
    # ask for a password if input is 1
    pass

if __name__ == "__main__":
    main()
