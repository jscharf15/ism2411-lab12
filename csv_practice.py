print("----- Exercise 1 -----")
import csv
from datetime import datetime
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
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

print("----- Exercise 4 -----")
total_revenue = 0

with open("data/sales.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:,.2f}")

print("----- Exercise 5 -----")
rows_read = 0
rows_written = 0

with open("data/sales.csv") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        rows_read += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            rows_written += 1

print(f"Rows in original: {rows_read}")
print(f"Rows written to cleaned.csv: {rows_written}")

print("----- Exercise 6 -----")
# I'd use csv.reader for a quick script on a simple file where I only need a
# few columns by position. I'd use csv.DictReader when the file has many columns, since row["price"] is clearer than row[1].

dict_total = 0

with open("data/sales.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue (DictReader): ${dict_total:,.2f}")

print("----- Exercise 7 -----")
product_totals = {}

with open("data/sales.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        product_totals[product] = product_totals.get(product, 0) + revenue

for product in sorted(product_totals):
    print(f"{product}: ${product_totals[product]:,.2f}")

print("----- Exercise 8 -----")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} | Total revenue: ${total_revenue:,.2f}\n")