# Credit-Card-Fraud-Analysis
## 📊 Visualizations & Insights  

This project performs an exploratory data analysis (EDA) on the Credit Card Fraud Detection dataset using Python, Pandas, Matplotlib, and Seaborn. 
The goal is to uncover patterns and insights about fraudulent transactions through a series of clear and informative visualizations.

# Project Overview

Credit card fraud is a major concern for banks and financial institutions. Every day, millions of transactions occur, and a tiny fraction of them are fraudulent. The challenge is to identify these bad transactions without accidentally blocking legitimate ones. This project takes a first step in that direction by using data visualization to "see" what fraud looks like. We explore the data to answer simple but crucial questions: How often does fraud occur compared to normal transactions? Do fraudsters steal large or small amounts of money? Does fraud happen more at certain times of the day? Understanding these patterns is the foundation for building effective fraud detection systems.

# Dataset

The dataset used is the "Credit Card Fraud Detection" dataset from Kaggle, sourced from a collaboration between Worldline and the Machine Learning Group of ULB (Université Libre de Bruxelles).

- **Content:** The data contains transactions made by European cardholders in September 2013. For privacy, the original features have been transformed via Principal Component Analysis (PCA) into 28 numerical columns (V1 to V28). The only features that have not been transformed are Time, Amount, and Class.
- **Class:** This is the target variable, where 1 indicates a fraudulent transaction and 0 indicates a legitimate one.


### 1️⃣ Visualization 1: The Imbalance Problem 


![Class_Distribution](images/Class_distribution.png)


- This bar chart shows the massive difference between the number of normal and fraudulent transactions. The tall blue bar represents over 284,000 legitimate transactions, while the tiny red bar next to it represents only 492 fraudulent ones. This visual makes it clear that fraud is a "needle in a haystack" problem.

# Python 

**A seaborn.countplot was used to visualize the frequency of each category in the Class column**


### 2️⃣ Visualization 2: Transaction Amount by Class

![Transaction Amount By Class](images/Amount_Distribution.png)

- This chart compares the dollar amounts of legitimate vs. fraudulent transactions. Each "box" shows the typical range of transaction amounts (the middle 50%). We can see that while both types of transactions can have very high-value outliers (the dots), the typical range for fraudulent transactions is much tighter and centered on smaller amounts than legitimate ones.

# Python 

- **A seaborn.boxplot was created to compare the distribution of the Amount feature for both classes. A critical step was setting the y-axis to a logarithmic scale (plt.yscale('log')). Without this, the presence of a few very large transactions would compress the boxes into unreadable lines at the bottom of the plot**

  

- # Key Insight: Fraudulent transactions are not necessarily high-value.


### 3️⃣ Visualization 3: Transaction Distribution Over Time

![Transaction Distribution over time](images/time_distribution.png)


- These two charts show when transactions occur throughout a 24-hour cycle. The left chart (legitimate transactions) shows a clear daily pattern: a dip in activity during the night and peaks during the day, which is typical human behavior. The right chart (fraudulent transactions) is much more evenly spread out, suggesting that fraudulent activity doesn't follow a normal human schedule and is likely automated.

# Python 

- First, a new feature, Hour, was engineered from the Time column (in seconds) using the formula df['Time'] // 3600 % 24. Two separate histograms were then plotted side-by-side using plt.subplots(ncols=2). This side-by-side comparison is far more effective than overlaying the two histograms, given the huge difference in their scales (y-axis). seaborn.histplot with 24 bins was used to visualize the frequency of transactions for each hour of the day for each class.



# How to Run This Project
## 🛠️ Tech Stack  
- **Python**  
- **Pandas** – Data cleaning & analysis  
- **Matplotlib** – Visualizations
- **Seaborn** - Plotting


## 📂 Dataset 

- Source:  https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Format: CSV file
