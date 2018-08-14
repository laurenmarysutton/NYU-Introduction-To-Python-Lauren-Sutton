def intro():
    print('Welcome to the Amazing Race game! Lets get started')
    name_intake = input('What is your name?\n')
    print('{}, best of luck as you start your journey around the world! The objective of this game is to travel around the world by answering a series of trivia questions. You will start in New York City and answer these trivia questions to move from one city to the next until you make your way back to New York City. You must answer 5 questions correctly in order to successfully make it back to New York City. If you incorrectly answer one question, you will be eliminated from the game.\n'.format(name_intake))

def question_set():
    question_1 = input('This 1st question is to travel from New York City to Reykjavik, the capital of Iceland. Enter true or false: There are more than 125 volcanic mountains in Iceland.\n')
    print('The response you entered is: {}'.format(question_1.lower()))
    formatted_1 = question_1.lower()
    if formatted_1[0] == 't':
        print('Correct! You have arrived in Reykjavik.\n')
        question_2 = input('This 2nd question is to travel from Reyjavik to Paris, the capital of France. Enter true or false: The Mona Lisa is a painting that is housed in the Louve Museum in Paris.\n')
        print('The response you entered is: {}'.format(question_2.lower()))
        formatted_2 = question_2.lower()
        if formatted_2[0] == 't':
            print('Correct! You have arrived in Paris.\n')
            question_3 = input('This 3rd question to travel from Paris to Moscow, the capital of Russia. Enter true or false: Moscow is the most heavily populated city in Russia.\n')
            print('The response you entered is: {}'.format(question_3.lower()))
            formatted_3 = question_3.lower()
            if formatted_3[0] == 't':
                print('Correct! You have arrived in Moscow.\n')
                question_4 = input('This 4th question is to travel from Moscow to Beijing, the capital of China. Enter true or false: Beijing is one of the bicycle capitals of the world.\n')
                print('The response you entered is: {}'.format(question_4.lower()))
                formatted_4 = question_4.lower()
                if formatted_4[0] == 't':
                    print('Correct! You have arrived in Beijing.\n')
                    question_5 = input('This 5th question is to travel from Beijing to arrive back in New York City. Enter true or false: The first American chess tournament was held in New York City in 1843.\n')
                    print('The response you entered is: {}'.format(question_5.lower()))
                    formatted_5 = question_5.lower()
                    if formatted_5[0] == 't':
                        print('Correct! You have arrived in New York City and completed your journey! Congratulations!')
                    elif formatted_5[0] == 'f':
                        print('This is incorrect. Your journey has ended in Beijing.')
                        exit()
                    else:
                        print('That response is invalid. Please try again.')
                elif formatted_4[0] == 'f':
                    print('This is incorrect. Your journey has ended in Moscow.')
                    exit()
                else:
                    print('That response is invalid. Please try again.')
            elif formatted_3[0] == 'f':
                print('This is incorrect. Your journey has ended in Paris.')
                exit()
            else:
                print('That response is invalid. Please try again.')
        elif formatted_2[0] == 'f':
            print('This is incorrect. Your journey has ended in Reyjavik.')
            exit()
        else:
            print('That response is invalid. Please try again.')
    elif formatted_1[0] == 'f':
        print('This is incorrect. Your journey has ended in New York City.')
        exit()
    else:
        print('That response is invalid. Please try again.')

def main():
    instructions = intro()
    trip = question_set()

if __name__ == '__main__':
    main()
