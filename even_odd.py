def enter_number():
    number = int(input('Enter a number.\n'))
    if (number % 2) == 0:
        print('This number is even.')
    else:
        print('This number is odd.')
    return number

def main():
    your_number = enter_number()

if __name__ == '__main__':
    main()
