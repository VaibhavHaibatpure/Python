import random

while True:
    z=random.randint(1,6)
    print(z)
    if z==1:
        print('|       |\n|   O   |\n|       |')
    elif z==2:
        print('|   O   |\n|   O   |')
    elif z==3:
        print('|    O    |\n| O     O |')
    elif z==4:
        print('|  O   O  |\n|  O   O  |')
    elif z==5:
        print('|  O   O  |\n|    O    |\n|  O   O  |')
    elif z==6:
        print('|  O   O  |\n|  O   O  |\n|  O   O  |')
    print(z)
    zz=input('for continue "any key" and break "b"\nenter:-')
    if zz=='b' :
        break
    else:
        continue
