from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line['Serial#']),
        print(line['City']),
        print(line['Province']),
        print(line['Abbrivation'])

#----------------------------------------------------------------------
if __name__ == "__main__":
    with open("Cities.csv") as f_obj:
        csv_dict_reader(f_obj)

# New Program
print()
print
pass
with open("Cities.csv", "r") as f:
    Cities = f.read().split('\n')
def get_matches(query, choices, limit=3):
    result = process.extract(query, choices, limit=limit)
    return result
print(get_matches("punja", Cities))
