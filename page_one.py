def ask():
    counter = 0
    while True:
        try:
            val = int(input("Please provide an integer: "))
        except ValueError:
            counter += 1
            print(f"You have entered an invalid integer! Please try again!\n"
                  f"You have {3 - counter} tries left")
            if counter >= 3:
                print("Your account is blocked!")
                break
            continue
        else:
            print(f"The number {val} squared is equal: {val ** 2}")
            break
        finally:
            print("All done! Bye")


def hw1():
    try:
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except TypeError as te:
        print(f"{i} is a {type(i)} and you can`t act as an integer\n {te}")

    x = 5
    y = 0
    try:
        z = x / y
    except ArithmeticError as e:
        print(f'{x} can`t be divided by {y} \n {e}')
    else:
        print(z)
    finally:
        print("All Done.")
    ask()


def add(n1, n2):
    return sum(n1, n2)


def ex1():
    number1 = 19
    number2 = input("Please provide a number: ")
    try:
        result = add(number1, number2)
    except ValueError as ve:
        print(f"Houston we have a problem as {ve}")
    else:
        print(result)
    finally:
        print("ceva gen: \"aia e\"")


def ex2():
    try:
        f = open('testfile', 'w')
        f.write("Write a test line")
    except TypeError as te:
        print(f'There was a type error!\n'
              f'{te}')
    except OSError as oe:
        print(f'Hey you have an os Error {oe}')
    finally:
        print("I always run")

    def ask_for_int(self):
        try:
            result = int(input("Please provide a number: "))
        except ValueError as ve:
            print(f"That is not a number {ve}")
            return self.ask_for_int()
        return result


if __name__ == '__main__':
    a = 1
    b = 2
    print(a)
    print(b)
    hw1()
