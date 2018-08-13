class Student:
    def __init__(self, name):
        self.name = name

    def classroom(self):
        print('{} is in class listening to lectures from Jess and pair programming')

    def frustration(self):
        print('{} is getting a lot of syntax errors, cut and pasting all the things from stack overflow')

    def happiness(self):
        print('{}, OMG, I solved the error I am so happy and smart')

    def excitement(self):
        print('Yay we are learning python.')

def main():
    yasha = Student('Yasha')
    yasha.classroom()
    yasha.frustration()
    yasha.happiness()
    joyce = Student('Joyce')
    joyce.classroom()
    joyce.frustration()
    joyce.happiness()
    angela = Student()
    angela.classroom()

if __name__ == "__main__":
    main()
    
#everything in a class is common to a group of things
