import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Setting plot style
sns.set_style("darkgrid")

# loading data

file_path = 'creditcard.csv'


# loading data set using pandas

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
    print("Please ensure 'creditcard.csv' file exists.'")
    exit()




# Displaying first five rows to understand columns

print("First 5 rows of the dataset")
print(df.head(5))

# Displaying statistical summary of the dataset like min means max ....

print("Statistical Summary ")
print(df.describe())

# checking for missing values
print("Missing Values..")
print(df.isnull().sum())



# ----------VISUALIZATION 1----------

# Targeting class column: 0 means legitimate and 1 means fraud

class_counts = df['Class'].value_counts()
print(f"\nTransaction class Distribution:\n {class_counts}")

# We found 492 frauds where as 284315 is legitimate

# Creating figure plot

plt.figure(figsize=(8,6))

# using countplot of seaborn to visualize the data

sns.countplot(
    data=df,
    x='Class',
    hue='Class',  # <-- 1. EXPLICITLY ASSIGN 'Class' TO HUE
    palette=['#3498db', '#e74c3c'],
    legend=False # blue means legit, red means fraud
)

# setting labels for x-axis

plt.xticks([0,1],['Legitimate','Fraud'])

# adding plot title and labels

plt.title("Distribution of Legitimate VS Fraudulent Transactions", fontsize =16)
plt.xlabel('Transaction Type', fontsize=12)
plt.ylabel("Number of Transactions", fontsize =12)

plt.tight_layout()
plt.savefig('Class_distribution.png', dpi=600)
plt.show()


# ----------VISUALIZATION 2----------

# Creating new Figure
plt.figure(figsize=(12,8))

# using boxplot to compare Amount with Class

sns.boxplot(
    data=df,
    x='Class',
    hue='Class',
    y='Amount',
    palette=['#3498db', '#e74c3c'],
    legend=False  # blue means legit, red means fraud
)

# Setting X label

plt.xticks([0,1],['Legitimate', 'Fraud'])

plt.title("Distribution of Transaction Amount by Class", fontsize =16)
plt.xlabel("Transaction Type", fontsize=12)
plt.ylabel("Transaction Amount", fontsize =12)

# Set a logarithmic scale for the y-axis to better visualize the spread,
# as the amounts are heavily skewed by a few very large transactions.
plt.yscale('log')

plt.tight_layout()
plt.savefig('Amount_Distribution.png', dpi=600)
plt.show()



# ----------VISUALIZATION 3----------

# Transaction Distribution Over time

# Converting the time to hours

df['Hour'] = df['Time'] // 3600 % 24

# creating figure with two subplots

fig,(ax1, ax2) = plt.subplots(2, figsize=(18,6))

# Plot for legitimate transactions
sns.histplot(df[df['Class'] == 0] ['Hour'], bins = 24, ax = ax1, color='blue')
ax1.set_title('Distribution of Legitimate Transactions by Hour', fontsize=14)
ax1.set_xlabel('Hour of the Day')
ax1.set_ylabel('Number of Transactions')

# Plot for Fraud Transactions

sns.histplot(df[df['Class'] == 1]['Hour'], bins=24, ax=ax2, color='#e74c3c')
ax2.set_title('Distribution of Fraudulent Transactions by Hour', fontsize=14)
ax2.set_xlabel('Hour of the Day')
ax2.set_ylabel('Number of Transactions')


# Add a main title for the whole figure
plt.suptitle('Transaction Time Analysis', fontsize=20, y=1.02)
plt.tight_layout()
plt.savefig('time_distribution.png', dpi=600)
plt.show()

