import pandas as pd

# this restricts the data to only show the 6rows .3 head and 3 column
pd.options.display.max_rows = 6

# this reads the file and stores the data in df variable
df = pd.read_csv('data.csv')
# removes empty cells 
df.dropna(inplace = True)
print(df.to_string())
# display all the data
print(df)
# displays the first 10
print(df.head(10))
# displays the last 10
print(df.tail(10))
# displays the info of the data
print(df.info())
