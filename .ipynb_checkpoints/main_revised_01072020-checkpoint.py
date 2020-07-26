# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Set file paths for menu_data.csv and sales_data.csv
with open("../Resources/menu_data.csv", 'r') as menufile:  
    menufile = open("../Resources/menu_data.csv", "r")

# Read csv in csvreader & skip the first line of titles
menu = csv.reader(menufile, delimiter=',')

next(menu) # Question: Why would it print the header?

# In menu:
items = []
categories = []
descriptions = []
prices = []
costs = []

for row in menu:
    items.append(str(row[0]))
    categories.append(row[1])
    descriptions.append(row[2])
    prices.append(row[3])
    costs.append(row[4])
    
price = float(row[3])
cost = float(row[4])

# define profit
profit = price - cost

# test:
type(price)

# Open sales_data.csv
with open("../Resources/sales_data.csv", 'r') as salesfile:  
    salesfile = open("../Resources/sales_data.csv", "r")

# Read csv in csvreader & skip the first line of titles
sales = csv.reader(salesfile, delimiter=',')

next(sales)

# in sales

IDs = []
dates = []
cards = []
quantities = []
sales_item = []
quantity = []

# @TODO: Loop over every row in the sales list object

for row in sales:
   
    IDs.append(row[0])
    dates.append(row[1])
    cards.append(row[2])
    quantities.append(row[3])
    sales_item.append(str(row[4]))
    
quantity = float(row[3])
type(quantity)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}


# Initialize a row counter variable
row_count = 0

# @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

count = []
revenue = []
cogs = []

cogs = cost * quantity
type(cogs)

revenue = price * quantity
type(revenue)

for i in items:
    if i in sales_item:
        quantity += quantity
        revenue += revenue
        cogs += cogs
        profit += profit 
        report = {"01-count": quantity, "02-revenue": revenue, "03-cogs": cogs, "04-profit": profit}
        print(f"{i}: {report}")
    
    else: 
        report = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
        print(f'{i}: NO MATCH!')
"""
Output

edamame: NO MATCH!
house salad: NO MATCH!
cucumber sunomono salad: NO MATCH!
hiyashi wakame seaweed salad: NO MATCH!
agedashi tofu: NO MATCH!
hiyayakko tofu: NO MATCH!
pork floss bao: NO MATCH!
kakuni bao: NO MATCH!
edamame fried gyoza (vegan): NO MATCH!
fried gyoza: NO MATCH!
takoyaki: NO MATCH!
rock shrimp tempura: NO MATCH!
soft-shell crab tempura: NO MATCH!
ebi katsu shrimp bao: NO MATCH!
nagomi shoyu: {'01-count': 4.0, '02-revenue': 24.0, '03-cogs': 12.0, '04-profit': 6.0}
shio ramen: {'01-count': 8.0, '02-revenue': 48.0, '03-cogs': 24.0, '04-profit': 12.0}
spicy miso ramen: {'01-count': 16.0, '02-revenue': 96.0, '03-cogs': 48.0, '04-profit': 24.0}
vegetarian spicy miso: {'01-count': 32.0, '02-revenue': 192.0, '03-cogs': 96.0, '04-profit': 48.0}
miso crab ramen: {'01-count': 64.0, '02-revenue': 384.0, '03-cogs': 192.0, '04-profit': 96.0}
soft-shell miso crab ramen: {'01-count': 128.0, '02-revenue': 768.0, '03-cogs': 384.0, '04-profit': 192.0}
tori paitan ramen: {'01-count': 256.0, '02-revenue': 1536.0, '03-cogs': 768.0, '04-profit': 384.0}
tonkotsu ramen: {'01-count': 512.0, '02-revenue': 3072.0, '03-cogs': 1536.0, '04-profit': 768.0}
burnt garlic tonkotsu ramen: {'01-count': 1024.0, '02-revenue': 6144.0, '03-cogs': 3072.0, '04-profit': 1536.0}
vegetarian curry + king trumpet mushroom ramen: {'01-count': 2048.0, '02-revenue': 12288.0, '03-cogs': 6144.0, '04-profit': 3072.0}
truffle butter ramen: {'01-count': 4096.0, '02-revenue': 24576.0, '03-cogs': 12288.0, '04-profit': 6144.0}
green tea: NO MATCH!
coke: NO MATCH!
black sesame ice cream: NO MATCH!
matcha ice cream: NO MATCH!
mango mochi ice cream: NO MATCH!
strawberry mochi ice cream: NO MATCH!
black sesame creme brulee: NO MATCH!
"""      

# Set the output file path
output_path = Path('../python-homework/PyRamen/PyRamen_Report.txt')

# Open the file in "read" mode ('r') and store the
# contents in the variable "text"
with open(output_path, 'w') as file:
    file.write("PyRamen Report\n")
    file.write(str(report))
    
# Open the file in "read" mode ('r') and store the
# contents in the variable "text"
# Open the file in "read" mode ('r') and store the
# contents in the variable "text"
for i in items:
    if i in sales_item:
        with open(output_path, 'w') as file:
            file.write(str(report))
        
# open file to read       
        file = open(output_path, 'r')
        for line in file:
            row_count += 1
        print(f"{row_count}. {i} : {line}")
        
"""
Output:

1. nagomi shoyu : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
2. shio ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
3. spicy miso ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
4. vegetarian spicy miso : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
5. miso crab ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
6. soft-shell miso crab ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
7. tori paitan ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
8. tonkotsu ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
9. burnt garlic tonkotsu ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
10. vegetarian curry + king trumpet mushroom ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
11. truffle butter ramen : {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}

"""

# They sold 11 types of ramen listed on menu 
        
"""
References:

* "csv_reader.py", UC GitLab Repository 
* https://stackoverflow.com/questions/35350086/argument-1-must-be-an-iterator-what-am-i-doing-wrong
* https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
* https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
* https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
* https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/
* https://docs.python.org/3/
* https://www.tutorialspoint.com/python/python_dictionary.htm
* https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/

"""