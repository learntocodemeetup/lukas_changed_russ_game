import random
#-----------------------
#--DEFINE CLASS OF POKEMONS
#------------------------
class Pokemon():
    gotta_catch_em_all = "Yes you do."

    def __init__(self, colour, name, ouch_statement, takethat_statement):
        self.health_points = random.randint(1,10)
        self.colour = colour
        self.name = name
        self.ouch_statement = ouch_statement
        self.takethat_statement = takethat_statement

    def alive(self):
        return self.health_points > 0

    def attack(self, attacker):
        if self.alive():
            print("You attacked:", self.name)
            self.health_points -= random.randint(2,4);
            print("Their health points are:", self.health_points)
            if self.health_points < 3:
                print(self.ouch_statement)
        else:
            print  (random.choice(attacker.phrases))
            print ("You attacked the corpse of %s, you sicko." %self.name)

    def __str__(self):
        return self.name


#--------------------------------
#--DEFINE CLASS OF TRAINER
#--------------------------------
class Me():
    gotta_catch_em_all = "Yes I do."
    def __init__(self):
        self.health_points = 10
        self.phrases = ["Me: I'ma gonna win!",
            "Me: It's now or never!",
            "Me: that ship has sailed!",
            "Me: Take that, mongrel!"]

    def attack(self, pokemon):
        pokemon.attack(self)
        self.health_points -= random.randint(1,3)

#----------------------------------
#--INSTANTIATE CLASSES FOR EMOKEPONS
#---------------------------------
pikachu = Pokemon('yellow',"Pikachu", "Peeka Peeka :c", "Pika-CHUUUU")
bulbasaur = Pokemon('green', "bulbasaur", "mrrrrrr :(", "bulba-bulba!")
charmander = Pokemon('red', "charmander", "fizzzzzzle :<", "ROAAARRR (Flames also)!")

#----------------------------------
#--ADD CLASSES TO ARRAY FOR RANDOM CHOICE
#---------------------------------
opponents = [pikachu, bulbasaur, charmander]

#----------------------------------
#--INSTANTIATE CLASSES FOR ME
#---------------------------------
me = Me()


#----------------------------------
#--WELCOME TO THE BATTLE
#---------------------------------
print("Welcome to Emokepon")
print("Pikachu's hit points are:", pikachu.health_points)
print("Bulbasaur's hit points are:", bulbasaur.health_points)
print("Charmander's hit points are:", charmander.health_points)

#----------------------------------
#--RETURN LIST OF OPPONENTS
#---------------------------------


def print_list_of_opponents(opponents):
    opponent_list = []
    for opponent in opponents:
        opponent_list.append(opponent.name)
    return opponent_list

#----------------------------------
#--ROUND LOGIC
#---------------------------------
thisround = 1
while True:
    print ("\n---------Round %d ----------" %thisround)
    opponent = random.choice(opponents)
    me.attack(opponent)
    thisround += 1
    if not opponent.alive():
        print("{} is dead!".format(opponent.name))
        opponents.remove(opponent)
    if not opponents:
        print("You kill them all!")
        break
    elif thisround >= random.randint(5,10):
        print("Game over!\n")
        print("Survived enemies: {}!\n".format(', '.join(print_list_of_opponents(opponents))))
        break
        # print("The perfect pizzas are {}".format(', '.join(correct_pizzas)))