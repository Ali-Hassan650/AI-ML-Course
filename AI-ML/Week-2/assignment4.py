import pandas as pd
import matplotlib.pyplot as plt

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)


# Panda series

# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar)

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

# Key/Value Objects as Series

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)


# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)

# # DataFrames

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)

# # Locate row

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df.loc[0])

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df.loc[[0, 1]])

# # Named Indexes

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df)


# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df.loc["day2"])


# df = pd.read_csv('data.csv')

# print(df.to_string()) 


df = pd.read_csv('data.csv')

print(df) 

# cleaning data

# df = pd.read_csv('data.csv')

# new_df = df.dropna()

# print(new_df.to_string())


# df = pd.read_csv('data.csv')

# df.dropna(inplace = True)

# print(df.to_string())

# Replace Empty Values

# df = pd.read_csv('data.csv')

# df.fillna(130, inplace = True)

# Replace Only For Specified Columns

# df = pd.read_csv('data.csv')

# df.fillna({"Calories": 130}, inplace=True)

# Replace Using Mean, Median, or Mode

# df = pd.read_csv('data.csv')

# x = df["Calories"].mean()

# df.fillna({"Calories": x}, inplace=True)


# df = pd.read_csv('data.csv')

# x = df["Calories"].median()

# df.fillna({"Calories": x}, inplace=True)

# df = pd.read_csv('data.csv')

# x = df["Calories"].mode()[0]

# df.fillna({"Calories": x}, inplace=True)


# Pandas - Data Correlations

# df = pd.read_csv('data.csv')

# print(df.corr())

# Plotting

# df = pd.read_csv('data.csv')

# df.plot()

# plt.show()

# Scatter Plote

# df = pd.read_csv('data.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# plt.show()


# df = pd.read_csv('data.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

# plt.show()


df = pd.read_csv('data.csv')

df.plot(kind = 'hist', x = 'Duration', y = 'Maxpulse')

plt.show()