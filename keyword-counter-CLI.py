import csv
import sys
terms = []
clean_terms = []
final_list = []

# read terms csv into list
with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        terms.append(row)

#remove header row
terms = terms[1:]

# clean terms list to get minimum number
for row in terms:
    term = row[0]
    num = row[1]
    num = num.replace('+', '')
    num = num.split('-')
    num = num[0]
    clean_terms.append([term, num])

# open text draft and convert to all lower case
text = open(sys.argv[2], 'r').read()
text = text.lower()

# count the terms in the text 
# and calculate min - actual, etc.
for row in clean_terms:
    term = row[0]
    minimum = int(row[1])
    count = text.count(term)
    if count >= minimum:
        min_met = True
    else:
        min_met = False
    diff = minimum - count
    if diff <= 0:
        diff = 0
    final_list.append([term, minimum, count, min_met, diff])

# put it into pandas for a nicer output
import pandas as pd
df = pd.DataFrame(final_list, columns = ['term', 'minimum', 'actual', 'min_met', 'diff'])
df = df.sort_values('min_met')
print(df)
