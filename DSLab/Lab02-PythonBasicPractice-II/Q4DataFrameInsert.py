import pandas as pd

dict = {"Name": ["Anay", "Aman", "Ashok"], "Height": [178, 176, 180], "Qualification": ["Student", "Teacher", "Student"]}
df = pd.DataFrame(dict)
address_col = ["Room 2237 Block 26", "Room 1120 Teacher's Block", "Room 1199, Block 26"]
df.insert(loc=len(df), value=address_col, column="Address")
print(df)