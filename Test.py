import pandas as pd

df = pd.DataFrame.from_dict({
    'Age': [10, 35, 34, 23, 70, 55, 89],
    'Height': [130, 178, 155, 133, 195, 150, 205],
    'Weight': [80, 200, 220, 150, 140, 95, 180]
})

print (df)

def absolute_maximum_scale(series):
    return series / series.abs().max()

#for col in df.columns:
#    df[col] = absolute_maximum_scale(df[col])

#df['Age'] = df['Age'].apply(for col in df.columns:
  #  df[col] = absolute_maximum_scale(df[col]))

#for col in df.iloc[:,1]:
 #   df[col] = absolute_maximum_scale(df[col])

df.iloc[:,1] = df.iloc[:,1].apply(lambda x: x / abs(max(df.iloc[:,1])))

print(df)

