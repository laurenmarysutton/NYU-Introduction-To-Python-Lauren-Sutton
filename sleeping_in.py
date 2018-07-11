import datetime

def day_of_the_week():
    weekday = datetime.datetime.today().weekday()
    if weekday < 5:
        print('It is a weekday - you can not sleep in!')
    else:
        print('It is a weekend - you can sleep in!')

def main():
    response = day_of_the_week()

if __name__ == '__main__':
    main()
