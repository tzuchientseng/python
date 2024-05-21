def make_icecream(*toppings):
    # 列出製作冰淇淋的材料
    print('這個冰淇淋的配料')
    for topping in toppings:
            print("--- ", topping)

def make_drink(size, drink):
    # 輸入飲料規格與種類，然後輸出飲料
    print("所點飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())


def main():
    print("Executing my own code!!")

if __name__ == '__main__':
    main()