import sys
import pandas as pd
# def read_input(file):
#     for line in file:
#         yield line.split('\t')

# def main(separator=',,'):
#         data = read_input(sys.stdin)
#         for words in data:
#             for word in words:
#                 if (word[-1] == '\n'):
#                     continue
#                 print ('%s%s%d' % (word, separator, 1))

# for german credit dataset:
def main(separator=',,'):
    df = pd.read_excel('GermanCredit.xlsx', engine='openpyxl')

    for amount in df["DurationOfCreditInMonths"]:
        print('%s%s%d' % (amount, separator, 1))

if __name__ == "__main__":
    main()