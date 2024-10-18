
def main():
    food_dict = read_file()
    #print(food_dict)
    food = input("Item: ")
    food = food.title()
    if food in food_dict:
        print(f'Calories: {food_dict[food]}')

def read_file():
    food_dict = {}
    with open ('fruits.csv') as f:
        for line in f:
            line = line.strip()
            if line != '':
                #print(line)
                fruit, price = line.split()
                #print(f'{fruit}:{price}')
                food_dict[fruit] = int(price)
    return food_dict




if __name__ == '__main__':
    main()
