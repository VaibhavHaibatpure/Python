
class food:
    class hotel:
        def hotel_food(self):
            k={}
            while True:
                print('if entering food name is done type done')
                z=input('enter food name:')
                if z=='done':
                    break
                else:
                    x=int(input(f'enter price of {z} :'))
                k[z]=[x]
            print(k)
    class user:
        z=input('hotel names are :- kc')
        def show_food(self):
            print(kc)
kc=food.hotel()
print(food.hotel.hotel_food(kc))