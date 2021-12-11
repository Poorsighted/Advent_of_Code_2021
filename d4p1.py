import pandas as pd
from collections import defaultdict

input = r'''\input\AOC4.txt'''

with open(input, 'r') as hello:
    for line in hello.readlines():
        print(line)
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

oxy_dict = dictionary.copy()
scrub_dict = dictionary.copy()

for i in range(0, length):
    print(i)
    if i == 0:
        temp_list = df['Input'].tolist()
        for value in temp_list:
            dictionary[i].append(str(value)[i])

        zero_count = dictionary[i].count('0')
        one_count = dictionary[i].count('1')

        #filter here
        if zero_count >= one_count:
            oxygen_df = df.loc[df['Input'].str[i] == '0'].copy()
            scrub_df = df.loc[df['Input'].str[i] == '1'].copy()
        else:
            oxygen_df = df.loc[df["Input"].str[i] == '1'].copy()
            scrub_df = df.loc[df['Input'].str[i] == '0'].copy()

    else:
        oxygen_list = oxygen_df['Input'].tolist()
        scrub_list = scrub_df['Input'].tolist()

        oxy_dict[i] = []
        scrub_dict[i] = []

        for value in oxygen_list:
            oxy_dict[i].append(value[i])

        for value in scrub_list:
            scrub_dict[i].append(str(value)[i])

        # oxygen loop
        oxy_zero_count = oxy_dict[i].count('0')
        oxy_one_count = oxy_dict[i].count('1')
        #filter here
        if oxy_one_count >= oxy_zero_count:
            oxygen_df = oxygen_df.loc[oxygen_df["Input"].str[i] == '1'].copy()
        else:
            oxygen_df = oxygen_df.loc[oxygen_df["Input"].str[i] == '0'].copy()

        #scrub loop
        scrub_zero_count = scrub_dict[i].count('0')
        scrub_one_count = scrub_dict[i].count('1')

        #filter here
        if scrub_zero_count == scrub_one_count:
            scrub_df = scrub_df.loc[scrub_df["Input"].str[i] == '0'].copy()
        elif scrub_zero_count > scrub_one_count:
            scrub_df = scrub_df.loc[scrub_df["Input"].str[i] == '1'].copy()
        else:
            scrub_df = scrub_df.loc[scrub_df['Input'].str[i] == '0'].copy()

        if len(oxygen_df) == 1:
            oxygen_final = oxygen_df['Input'].iloc[0]

        if len(scrub_df) == 1:
            scrub_final = scrub_df['Input'].iloc[0]

life_support = int(oxygen_final, 2) * int(scrub_final,2)

print(life_support)