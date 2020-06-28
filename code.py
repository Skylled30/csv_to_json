import csv
import json

csvfile = open('googleplaystore.csv', encoding='utf-8')
jsonfile = open('userdata.json', 'w')

fieldnames = ("App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres", "Last Updated", "Current Ver", "Android Ver")
reader = csv.DictReader(csvfile, fieldnames)

record = {}

i = 0

versions = ["1", "5", "11", "14", "21", "23", "24", "26", "28"]

jsonfile.write("[")

for row in reader:
    for name in fieldnames:
        record[name] = row[name]
    record['Installs'] = record['Installs'][:-1].replace(",", "") if record['Installs'][:-1] is not None else record['Installs'][:-1]
    if str(record['Android Ver']).split(" ")[0].isalpha():
        record['Android Ver'] = row['Android Ver']
    else:
        api = int(str(record['Android Ver']).split()[0].split(".", maxsplit=1)[0])
        record['Android Ver'] = versions[api-1]
    record['Price'] = True if record['Type'] == "Free" else False
    record['Genres'] = "[" + ", ".join(record['Genres'].split(";")) + "]"
    line = json.dumps(record)
    jsonfile.write("\t" + line + ",\n")

jsonfile.write("]")

csvfile.close()
jsonfile.close()
