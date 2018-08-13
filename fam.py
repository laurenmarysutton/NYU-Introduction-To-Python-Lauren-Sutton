class Fam:
    def __init__(self, first_name, last_name='Sutton', hair='brown', tounge_roll=True):
        self.first_name = first_name
        self.last_name = last_name
        self.hair = hair
        self.tounge_roll = tounge_roll

    def vacation(self):
        print('We go swimming on the lake every year during our vacation.')

    def dinner(self):
        print('Family dinner is at 7pm every night.')

class Bro(Fam):
    pass

def main():
    kelly.first_name = 'Kelly'
    print('{} {}'.format(kelly.first_name, kelly.last_name))
    print(kelly.city)
    kelly.vacation()
