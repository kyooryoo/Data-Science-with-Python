import numpy as np
import pandas as pd

df = pd.read_csv("/Users/jiangling/Workspace/MLDSDLWP/1_PastHires.csv")
print(df.head(),"\n",
df.head(3),"\n",
df.tail(4),"\n",
df.shape,"\n",
df.size,"\n",
len(df),"\n",
df.columns,"\n",
df['Hired'],"\n",
df['Hired'][:5],"\n",
df['Hired'][5],"\n",
df[['Years Experience', 'Hired']][:5],"\n",
df.sort_values(['Years Experience']))
degree_counts = df['Level of Education'].value_counts()
degree_counts
degree_counts.plot(kind='bar')