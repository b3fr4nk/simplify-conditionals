# by Kami Bigdely
# Consolidate conditional expressions

def dice(ingredients):
    print("diced all ingredients.")


def mix_all(diced_ingredients):
    print("mixed all.")


def add_salt():
    print('added salt.')


def pour(liquid):
    print('poured', liquid + '.',)


def all_ingredients_exist(ingredients):
    return ('cucumber' in ingredients or 'tomato' in ingredients or 'onion'
            in ingredients or 'lemon juice' in ingredients)


def make_shirazi_salad(ingredients):
    if not all_ingredients_exist(ingredients):
        print("lacks ingredient")
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
