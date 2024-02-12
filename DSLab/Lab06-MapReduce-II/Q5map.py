import fileinput

# for line in fileinput.input():
#     data = line.strip().split("\t")
#     if len(data)==6:
#         date, time, location, item, cost, payment = data
#         print("{0}\t{1}".format(location, cost))

# for heart disease dataset:
for line in fileinput.input():
    data = line.strip().split(",")
    if len(data) == 14:
        age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal, target = data
        print ("{0}\t{1}".format(age, chol))