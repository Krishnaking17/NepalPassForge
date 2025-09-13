import random
from mutations import mutate
from utils import load_list

def generate_passwords(size=100000, mutate_flag=False):
    names = load_list("data/names.txt")
    cities = load_list("data/cities.txt")
    districts = load_list("data/districts.txt")
    castes = load_list("data/castes.txt")
    festivals = load_list("data/festivals.txt")
    symbols = ["@", "#", "&", "!", "$"]
    years = [str(y) for y in range(1990, 2026)]

    wordlist = set()

    while len(wordlist) < size:
        name = random.choice(names)
        city = random.choice(cities)
        district = random.choice(districts)
        caste = random.choice(castes)
        festival = random.choice(festivals)
        symbol = random.choice(symbols)
        year = random.choice(years)
        digits = str(random.randint(100, 9999))

        pattern = random.choice([
            f"{name}{year}{symbol}",
            f"{city}{symbol}{festival}{year}",
            f"{caste}{digits}{symbol}",
            f"{name}{digits}{symbol}",
            f"{district}{year}{symbol}",
            f"{city}{year}{symbol}{digits}",
            f"{festival}{year}{symbol}",
            f"{name}@{city}{year}",
        ])

        if mutate_flag:
            pattern = mutate(pattern)

        wordlist.add(pattern)

    return list(wordlist)