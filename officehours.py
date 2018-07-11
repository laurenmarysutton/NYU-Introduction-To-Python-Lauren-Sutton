def whats_your_number():
    whats_your_number = input('What is your phone number?\n')
    return whats_your_number

def formatter(phone_number):
    area_code = phone_number[0:3]
    middle_part = phone_number[3:6]
    last_part = phone_number[6:]
    formatted_number = "({}){}-{}".format(area_code, middle_part, last_part)
    return formatted_number

def main():
    number = whats_your_number()
    formatted_number = formatter(number)
    print('Your number is:')
    print(formatted_number)

if __name__ == "__main__":
    main()
