import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    for word in words:
        print('%s,,%s' % (word, 1))

import pandas as pd
# df = pd.read_excel('GermanCredit.xlsx', engine='openpyxl')

# for amount in df["Creditability"]:
#     print('%s,,%s' % (amount, 1))