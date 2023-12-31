import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df = df.drop_duplicates()
plt.hist(df['id'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Column')
plt.xlabel('Column Values')
plt.ylabel('Frequency')
plt.show()
sns.scatterplot(x='radius_mean', y='area_mean', data=df)
plt.title('Scatter Plot between Column1 and Column2')
plt.show()
