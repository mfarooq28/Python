import csv
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj, delimter=',')
    for row in reader:
        print(" ".join(row))
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "Cities.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)