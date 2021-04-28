import random
import csv
from os import path
from math import remainder


# filename (will overwrite existing or create new if none found)
filename = "pyGenItemsData.txt"

# number of items to generate in set (can't do more than 6801 as that's the number of words available to draw from)
n = 100   # if zero, will empty file

# maximum price in dollars for generated items
max_price = 500

# price increments in cents (for prices to appear less random)
price_increments = 0.05





# LEAVE THIS ALONE IF YOU DON'T HAVE YOUR OWN FILE!
# path for word bank to draw from (csv format)
words_file_name = "nounlist.csv"


"""



THE REST IS GENERATION CODE!!!

(don't need to do anything below this point)



"""


# generate items
words_file = open(words_file_name, 'r')
words = list(csv.reader(words_file))
random.shuffle(words)
generated_file = open(filename, "w")
order_string = ""
for x in range(n):
    item = words.pop()
    x1 = (round(random.random() * max_price, 2)) * 100
    x2 = price_increments * 100
    price = round((x1 - remainder(x1, x2)) / 100, 2)
    order_string += f'{item[0]} '
    if price_increments != 0:
        order_string += f'{price:.2f}'
    else:
        order_string += f'{x1}'
    if(x != n-1):
        order_string += '\n'


generated_file.write(order_string)
print(f'File generated at: {path.realpath(generated_file.name)}')
generated_file.close()