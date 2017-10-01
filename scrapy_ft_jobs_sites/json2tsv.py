import sys
import json

if len(sys.argv) < 2:
    print("Please specify json input")
    sys.exit(-1)

file_to_read = sys.argv[1]
data = json.loads(open(file_to_read).read())

file_to_save_name = file_to_read.replace(".json", ".tsv")
file_to_save = open(file_to_save_name, "w")
black_listed_companies = [company.strip() for company in open("black_listed_companies.txt").readlines()]

for rec in data:
    if rec["company"].strip() != "" and rec["company"] in black_listed_companies:
        continue

    row = []
    row.append(rec["title"])
    row.append(rec["company"])
    row.append(rec["location"])
    row.append(rec["blurb"])
    row.append(rec["source_url"])
    result = "%s\n" % ("\t".join(row))
    file_to_save.write(result)

print("Saved output to:%s" % file_to_save_name)