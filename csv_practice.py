print("----- Exercise 1 -----")
import csv
import os

print("File exists:", os.path.exists("data/sales.csv"))

with open("data/sales.csv") as f:
    pass

print("----- Exercise 2 -----")
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



print("----- Exercise 3 -----")
print("----- Exercise 4 -----")
print("----- Exercise 5 -----")
print("----- Exercise 6 -----")
print("----- Exercise 7 -----")
print("----- Exercise 8 -----")
