from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
data_file = StringIO(data)
dict_reader = csv.DictReader(data_file)
print(dict_reader.fieldnames)
for row in dict_reader:
    print(row)
