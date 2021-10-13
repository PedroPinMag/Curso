"""
Dictionaries are like MAPS
If doesn't exist it will return none
It's modifiable
"""
dict = {"key": "data"}
countries = {"br": "Brazil", "us": "United States"}
names = {"Ma": "Matheus"}
months = {"jan": "january", "feb": "february", "mar": "march"}
locations = {
    "br:": [42.123, 15.123],  # Brazil Office
    "us ": [-23.123, 12.125]  # USA Office
}

def dictionary():
    print(countries["br"])  # Can create errors

    print(countries.get("br"))  # Don't create errors
    print(countries.get("ru"))  # Only return NONE statement


def if_dict():
    country = countries.get("br")
    if country:
        print("Country")
    else:
        print("Error")

    country2 = countries.get("py", "Not founded")
    print(country2)


def in_dict():
    print("br" in countries)
    print("py" in countries)


def add_dict():
    countries["ru"] = "Russia"
    print(countries)

    newdata = {"Ma": "Matheus"}
    print(names)
    names["Ma"] = "Marcos"
    print(names)
    names.update(newdata)
    print(names)
    names.update({"Ma": "Matheus"})
    print(names)


def pop_dict():
    print(months)
    pop = months.pop("mar")
    print(months)
    print(pop)


def del_dict():
    print(months)
    del months["mar"]
    print(months)

def clear_dict():
    months.clear()

def deep_copy_dict():
    months2 = months.copy()
    print(months, months2)
    months.pop("jan")
    print(months, months2)

def shallow_copy_dict():
    months2 = months
    print(months, months2)
    months2.pop("jan")
    print(months, months2)

