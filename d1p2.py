import pandas as pd

input = r'''input\AOC1.csv'''

df = pd.read_csv(input)

# Count of values greater than the last
count = 0
for index, row in df.iterrows():
    if index == 0 or index == 1:
        pass
    else:
        # count for window dimension
        try:
            df.at[index, 'window_total'] = df.at[index, 'Number'] + df.at[index-1, 'Number'] + df.at[index-2, 'Number']
        except:
            df.at[index, 'window_total'] = 0
        if df.at[index, 'window_total'] > df.at[index-1, 'window_total']:
            count+=1
print(count)