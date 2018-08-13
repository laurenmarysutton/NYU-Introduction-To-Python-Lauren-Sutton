class Intro:
    def intro():
        print('Welcome to the Amazing Race game! Lets get started')
        name_intake = input('What is your name?\n')
        print('{}, best of luck as you start your journey around the world! The objective of this game is to travel around the world by answering a series of trivia questions. You will start in New York City and answer these trivia questions to move from one city to the next until you make your way back to New York City. You must answer 10 questions correctly in order to successfully make it back to New York City. If you incorrectly answer one question, you will be eliminated from the game.\n'.format(name_intake))

def question_1():
    q1 = input('This first question is to move from New York City to Reykjavik, the capital of Iceland. \n  True or False: There are more than 125 volcanic mountains in Iceland.\n  Please enter 0 for true or 1 for false.\n')
    if '{}'.format(number) == 0:
        print('Correct! You have arrived in Reykjavik.')
    elif '{}'.format(number) == 1:
        print('Incorrect. Your journey has ended in New York City.')
    else:
        print('That response is invalid. Please try again by entering 0 for true or 1 for false.')
        print(q1)

def question_2():
    q2 = input('This is the second question to move from Reykjavik to Paris, the capital of France.  \n  True or False: The Mona Lisa is a painting that is housed in the Academia Museum in Paris.\n  Please enter 0 for true or 1 for false.\n')
    if F:
        print('Correct! You have arrived in Paris.')
    else:
        print('Incorrect. Your journey has ended in Reykjavik.')

def main():
    instructions = intro()
    trip_1 = question_1()
    trip_2 = question_2()

if __name__ == '__main__':
    main()





#    print('{}'.format(r1))

#def trigger_1():
#    if response_to_q1 == true:
#        print('Correct! You have arrived in Reykjavik.')
#    else:
#        print('Incorrect! Your journey has ended in New York City.')
