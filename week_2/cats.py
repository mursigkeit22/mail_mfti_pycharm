class Cat:
    def __init__(self, name, weight, color, sound, hungry):
        self.name = name
        self.weight = weight
        self.color = color
        self.sound = sound
        self.hungry = hungry

    def meow(self, mouthWidth):
        print('Я ' + self.color + ' кот ' + self.name + ', я вешу ' + str(self.weight) + ' кг и я ' + self.hungry)
        print('Ширина зевка рта ' + str(mouthWidth) + ' см')

    # ширина рта это свойство/параметр конкретного мяукания
    def status(self, hungry):
        print(hungry)


timosha = Cat('Тимоша', 9, 'темный', 'фшшшшш', 'голоден')
timosha.meow(12)
timosha.status('все гуд')
shaya = Cat('Шая', 5, 'серый', 'мяу', 'сыт')
shaya.meow(10)
