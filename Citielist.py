from fuzzywuzzy import fuzz
from fuzzywuzzy import process

with open("Cities.csv", "r") as f:
    Cities = f.read().split('\n')
def get_matches(query, choices, limit=3):
    result = process.extract(query, choices, limit=limit)
    return result
print(get_matches("lahore", Cities))
