# Car-Dataset-Exploration---in-Python
Car_csv data Exploration in Python

I carried out Data exeploration to Find out more details about the dataset using python commands

**Problem Statement**

Importing csv file

car = pd.read_csv(r"C:\Users\AKHIGBE\Downloads\2. Cars Data1.csv")

Inspecting Dataset to show first 5 rows of data

car.head()

How many rows and columns does the dataset have

car.shape

#checking for null values, and if there is fill it in with the mean of that column

car.isnull().sum()

car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


#Exploring the Value Counts : What are the differnet  types of make in our dataste, and what is the count occurence  of each make in the data?

car.head(2)
car['Make'].value_counts()

#Exploring all the records where origin is Asia or Europe?

car.head(2)

car[car['Origin'].isin(['Asia', 'Europe'])]

Removing all the records where weight is above 4000

car.head(2)

car[~(car['Weight'] > 4000)]

#how many cars left that do not have the weight 4000
432 - 329

#Increase all the values of 'MPG_City' column by 3
car.head(2)

car['MPG_City'] - car['MPG_City'].apply(lambda x:x+3)
car
