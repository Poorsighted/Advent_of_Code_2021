import pandas as pd

input = r'''input\AOC1.csv'''

df = pd.read_csv(input)

# Count of values greater than the last
count = 0
for index, row in df.iterrows():
    if index == 0:
        pass
    else:
        if row['Number'] > df.at[index-1, 'Number']:
            count+=1
print(count)