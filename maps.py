recipe = {"jan": 100, "feb": 250, "mar": 400}


def key_dict():
    for key in recipe.keys():
        print(key)

    for key in recipe:
        print(key)


def data_dict():
    for data in recipe:
        print(recipe[data])

    for data in recipe.values():
        print(data)


def dual():
    for dual in recipe:
        print(f"In {dual} i received {recipe[dual]}")


data_dict()
