import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv')

# Attempt to parse 'Time' column with a flexible approach
df['hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour

# Display the dataframe information
print(df.info())

# Display the statistical summary of the numerical columns
print(df.describe())

# Distribution of Accidents by Hour
plt.figure(figsize=(15, 7))
sns.countplot(x='hour', data=df, palette='viridis')
plt.title('Distribution of Accidents by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# Distribution of Accidents by Road Surface Conditions
plt.figure(figsize=(20, 10))  # Increase the figure size further
sns.countplot(x='Road_surface_conditions', data=df, palette='viridis')
plt.title('Distribution of Accidents by Road Surface Conditions')
plt.xlabel('Road Surface Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate labels, align them to the right, and set fontsize
plt.subplots_adjust(bottom=0.3)  # Adjust the bottom margin
plt.show()

# Distribution of Accidents by Weather Conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='Weather_conditions', data=df, palette='viridis')
plt.title('Distribution of Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()

# Distribution of Accidents by Type of Collision
plt.figure(figsize=(12, 6))
sns.countplot(x='Type_of_collision', data=df, palette='viridis')
plt.title('Distribution of Accidents by Type of Collision')
plt.xlabel('Type of Collision')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.subplots_adjust(bottom=0.4)
plt.show()


# Distribution of Accidents by Types of Junction
plt.figure(figsize=(12, 6))
sns.countplot(x='Types_of_Junction', data=df, palette='viridis')
plt.title('Distribution of Accidents by Types of Junction')
plt.xlabel('Types of Junction')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()
