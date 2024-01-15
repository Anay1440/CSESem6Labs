import pandas as pd
import numpy as np

dict = {"Name": ["Annie", "Diya", "Charles", "James", "Emily"], "Quiz_1/10": [8.0, 9.0, 7.5, 8.5, 6.5], "In-Sem_1/15": [11.0, 14.0, 14.5, 13.0, 12.5], "Quiz_2/10": [9.5, 6.5, 8.5, 9.0, 9.0], "In-Sem_2/15": [12.5, 13.5, 14.5, 15.0, 13.0]}
df = pd.DataFrame(dict)

total_marks_col = df.iloc[:, 1:].sum(axis='columns')
df["Total"] = total_marks_col

mean_marks_row = df.iloc[:, 1:].mean() # axis = 'index' default

df.loc[len(df)] = [np.NaN] + list(mean_marks_row)
print(df)