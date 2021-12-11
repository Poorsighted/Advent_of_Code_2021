import pandas as pd
from collections import defaultdict

input = r'''input\AOC3.csv'''

df = pd.read_csv(input, dtype={'Input':str})

gamma_rate = ''
epsilon_rate = ''

# Identify maximum length in data
length = df.Input.map(lambda x: len(str(x))).max()

# Create dictionary to store values
list = []
for i in range(0, length):
    list.append(i)

dictionary = dict([(x,[]) for x in list])

for index, row in df.iterrows():
    # Find length
    length = len(str(row['Input']))

    for i in range(0, length):
        dictionary[i].append(str(row['Input'])[i])

# Figure out zero count and one count
for i in range(0, length):
    zero_count = dictionary[i].count('0')
    one_count = dictionary[i].count('1')

    if zero_count > one_count:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'
power_consumption = int(gamma_rate, 2) * int(epsilon_rate,2)
print(power_consumption)