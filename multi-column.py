import pandas as pd

dict1 = {'a':[1,2,3],'b':[4,5,6]}

df=pd.DataFrame(dict1)

columns=[('c','a'),('d','b')]

df.columns=pd.MultiIndex.from_tuples(columns)
print(df)

print(df.columns.get_level_values(1))

