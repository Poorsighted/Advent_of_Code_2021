import pandas as pd

input = r'''input\AOC2.csv'''

df = pd.read_csv(input)

horizontal_position = 0
depth_position = 0

for index, row in df.iterrows():
    if row['Direction'] == 'forward':
        horizontal_position += row['Amount']
    elif row['Direction'] == 'down':
        depth_position += row['Amount']
    elif row['Direction'] == 'up':
        depth_position -= row['Amount']
    else:
        print("What else could there be??")

print(horizontal_position * depth_position)