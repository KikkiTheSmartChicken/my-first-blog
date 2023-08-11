# I'm practicing Python here :)
#
##
###        O
####    \  |  /
#####    |  |
######################

# name = 'Y'

names = ['Mario', 'Peach', 'Yoshi', 'Mago']

def hi(name):
    if name == 'Mario':
        print("It's me Mario!")
    elif name == 'Yoshi':
        print('Hi there!')
    else:
        print("Hello " + name + "!")

# print(hi)

for name in names:
    hi(name)
    print('Next person!')


# hi('Mario')
# hi('Yoshi')
# hi('Sonja')

# volume = 33
# if volume < 20:
#     print("Volume is smaller than 20!")
# elif 20 <= volume < 40:
#     print("Volume is somewhere between 20 and 40!")
# elif 40 <= volume < 60:
#     print("Volume is smaller than 60!")
# else:
#     print("Volume is larger than 60!")



