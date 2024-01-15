import pandas as pd
import numpy as np

dict1 = {"Name": ["Ram", "Diya", "Chandan", "James", "Alice"]}
dict2 = {"Maths": [80.0, 90.0, 77.5, 87.5, 86.5], "Physics": [81.0, 94.0, 74.5, 83.0, 82.5], "Chemistry": [91.5, 86.5, 85.5, 90.0, 91.0], "Biology": [82.5, 83.5, 84.5, 85.0, 93.0]}
df1 = pd.DataFrame(dict1, index = np.arange(1, len(dict1["Name"]) + 1))
df2 = pd.DataFrame(dict2, index = np.arange(1, len(dict2["Maths"]) + 1))
df = pd.concat([df1, df2], axis = 1)

total_marks_col = df.iloc[:, 1:].sum(axis='columns')

df["Total"] = total_marks_col
print(df)