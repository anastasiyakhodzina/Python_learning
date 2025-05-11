import random
from PIL import Image

class Location():
    def play(self):
        input("""
              Now please create a file with 2 words :
              First word should has the same number of letters as you got on the dice, 
              Second word should be your favorite city :3
              Save it as two_words.txt and press Enter
              """)
        print('THaNKs for the file! YuMmY yUmmY!')
        print('Now I am going to count the number of vowels and name Belorussian city with the same number of vowels(let\'s say that y is not a vowel)')

        with open('two_words.txt') as file:
            words = []
            for line in file:
                for word in line.split():
                    words.append(word.upper())

        vowels = {'A','E','U','I','O','A'}
        vowels_num = 0
        for i in range(len(words)):
            vowels_num += sum(1 for letter in words[i] if letter in vowels)
        
        cities = {
            0: 'There is no city with 0 vowels in Belarus',
            1: 'Minsk',
            2: 'Grodno',
            3: 'Mogilev',
            4: 'Maladzyechna',
            5: 'Staryya Darohi',
            6: 'Buda-Kashalyova',
            '>6': ' There is no city in Belarus with more than 6 vowels' 
        }
        
        if vowels_num < 7:
            print(cities[vowels_num])
            if vowels_num != 0: 
                self.have_you_been(cities[vowels_num])
            else:
                self.have_you_been('Pinsk')
        else:
            print(cities['>6'])
            self.have_you_been('Vitebsk')

    def have_you_been(self,city):
        answer = ''
        while answer != 'YES' and answer != 'NO':
            answer = str(input(f'Have you been in {city}?(YES or NO)')).upper()

        location = type(self).__name__
        if answer == 'YES':
            if location == 'Airplane':
                print('You get unlimited credit card for 3 days to explore this city, where you arrive in 10 min. Get ready!')
            elif location == 'Train':
                self.first_task()
        else:
            if location == 'Train':
                print('You get unlimited credit card for 3 days to explore this city, where you will arrive in 10 min. Get ready!')
            elif location == 'Airplane':
                self.first_task()
    
    def first_task(self):
        print('You are arriving to this city to work as the military criminalist.')
        print('You\'ve already recieved the first task! Take a look on it!')

        image = Image.open('game_image.png')
        image.show()

class Start(Location):
    def start(self):
        print('Hello! Welcome to LooPy PooPy Game!')
        input('To start press Enter')
        print('Firstly, we\'re going to throw a dice, which will decide where you will get')
        input('Press Enter to throw it')

        dice_num = random.randint(1,6)
        print('Oh God! You got ',dice_num,' 0o0')
        if dice_num % 2 == 0 or dice_num % 3 == 0:
            print('So, You got to the airplane!')
            return Airplane()
        else:
            print('So, You got to the train!')
            return Train()


class Airplane(Location):
    pass

class Train(Location):
    pass