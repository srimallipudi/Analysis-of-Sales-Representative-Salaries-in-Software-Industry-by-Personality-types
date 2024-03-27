#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:46:31 2024

@author: srilu
"""

# import libraries for data manipulation
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('/Users/srilu/Documents/Financial Modelling/Case Study/Case 4.3 Sales Reps Salaries Dataset.csv')
df.head()

# Overview of the dataset shape and datatypes
df.shape
df.info()

# Checking for missing values in the dataset
df.isnull().sum()

# Statistical Summary of the data
round(df.describe(),2)

# Exploratory Data Analysis 

# Sales_Rep Salaries
# Histogram
sns.histplot(data=df, x='Salary', kde= True)
plt.title('Histogram: Sales Representatives Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='Salary')
plt.title('Boxplot: Sales Representatives Salary')

# Salary by Gender
g=sns.boxplot(data=df, x ='Female', y='Salary')
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Boxplot: Sales Representatives Salary by Gender')
plt.xlabel('Gender')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])

# Salary by Personality
g=sns.boxplot(data=df, x ='Personality', y='Salary')
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Boxplot: Sales Representatives Salary by Personality')

# Sales_Rep NPS
# Histogram
sns.histplot(data=df, x='NPS', kde= True, binwidth=1, binrange=(1,11))
plt.title('Histogram: Sales Representatives NPS')
plt.xlabel('Net Promoter Score')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='NPS')
plt.title('Boxplot: Sales Representatives NPS')
plt.xlabel('Net Promoter Score')

# NPS by Gender
g=sns.boxplot(data=df, x ='Female', y='NPS')
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Boxplot: Sales Representatives NPS by Gender')
plt.xlabel('Gender')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])

# NPS by Personality
g=sns.boxplot(data=df, x ='Personality', y='NPS')
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Boxplot: Sales Representatives NPS by Personality')

# Sales_Rep Years of Experience
# Histogram
sns.histplot(data=df, x='Years', kde= True,binwidth=1)
plt.title('Histogram: Sales Representatives Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='Years')
plt.title('Boxplot: Sales Representatives Experience')
plt.xlabel('Years of Experience')


# Sales_Rep Age
# Histogram
sns.histplot(data=df, x='Age', kde= True)
plt.title('Histogram: Sales Representatives Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='Age')
plt.title('Boxplot: Sales Representatives Age')
plt.xlabel('Age')


# Sales_Rep Feedback
# Histogram
sns.histplot(data=df, x='Feedback', kde= True)
plt.title('Histogram: Sales Representatives Feedback')
plt.xlabel('Feedback')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='Feedback')
plt.title('Boxplot: Sales Representatives Feedback')
plt.xlabel('Feedback')

# Sales_Rep Certificates
# Histogram
sns.histplot(data=df, x='Certificates', kde= True, binwidth=1, binrange=(0,7))
plt.title('Histogram: Sales Representatives Certificates')
plt.xlabel('Number of Certificates')
plt.ylabel('Frequency')

# Boxplot
sns.boxplot(data=df, x='Certificates')
plt.title('Boxplot: Sales Representatives Certificates')
plt.xlabel('Certificates')

# Categorical Variables

# Number of Sales Representatives by Personality
g=sns.histplot(data=df, x='Personality')
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Sales Representatives Count by Personality')

# Number of Sales Representatives by Gender
g=sns.histplot(data=df, x='Female', binwidth=0.5)
plt.setp(g.get_xticklabels(), rotation=0)
plt.title('Sales Representatives Count by Gender')
plt.xlabel('Gender')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])

# Top Personality in terms of NPS
avg_NPS = df.groupby('Personality')['NPS'].mean().round(2).sort_values(ascending=False)

# Plot the average NPS for each personality type
sns.barplot(x=avg_NPS.index, y=avg_NPS.values)
plt.title('Top Personality in terms of NPS')
plt.xlabel('Personality')
plt.ylabel('Average NPS')

# Average Salary by Personality
avg_Salary = df.groupby('Personality')['Salary'].mean().round(2).sort_values(ascending=False)

# Plot the average Salary for each personality type
sns.barplot(x=avg_Salary.index, y=avg_Salary.values)
plt.title('Average Salary by Personality')
plt.xlabel('Personality')
plt.ylabel('Average Salary')

# Average Salary by Gender
avg_salary_gender = df.groupby('Female')['Salary'].mean().round(2).sort_values(ascending=False)

# Plot the average Salary for each personality type
sns.barplot(x=avg_salary_gender.index, y=avg_salary_gender.values)
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])
plt.ylabel('Average Salary')

# Correlation Analysis
sns.heatmap(data=df[['Age','Years','Certificates','Feedback', 'Salary', 'NPS']].corr(), annot=True, fmt=".2f", cmap='PuBu')


