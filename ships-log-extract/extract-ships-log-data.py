"""Extract key value data and comments from ships log"""
import re

count = 0

DAYDATE='([0-9]{8})\;'

daylog = []

# open text file containing one month of ships log data
text = open('month.txt', 'r')

# iterate through every line
for line in text:
    foundday = re.findall(DAYDATE, line)
    if foundday:
        daylog.append(foundday)
    count = ++count
# for each day date extract comments and key value data in a list

# if the list is not empty write the list to a csv file with column 1 as the date, column 2 as the key name and column 3 as the key value
if len(daylog) != 0:
    print(len(daylog))
    print(daylog)
else:
    print('no match')
