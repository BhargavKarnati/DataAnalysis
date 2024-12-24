import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path for merged data
merged_data_path ="D:/UserBehaviourAnalysis/Data/Merged_data.xlsx"

merged_data = pd.read_excel(merged_data_path, parse_dates=['Registration Date', 'Session Start', 'Session End', 'Order Date'])

# Data Analysis

# 1. Analyzing relationships between cooking sessions and orders
sessions_per_user = merged_data.groupby('User ID').size()
orders_per_user = merged_data.groupby('User ID')['Order ID'].nunique()

# 2. Identifying popular dishes
popular_dishes = merged_data['Dish Name_y'].value_counts()

# 3. Exploring demographic factors
age_group_bins = [0, 20, 30, 40, 50, 60]
age_group_labels = ['0-20', '21-30', '31-40', '41-50', '51-60']
merged_data['Age Group'] = pd.cut(merged_data['Age'], bins=age_group_bins, labels=age_group_labels)

age_group_orders = merged_data.groupby('Age Group',observed=True)['Order ID'].nunique()

# Summary statistics
user_summary = merged_data.groupby('User ID').agg({
    'Order ID': 'nunique',
    'Amount (USD)': 'mean',
    'Age': 'first',
    'Favorite Meal': 'first'
}).reset_index()

# Data Visualization

# 1. Bar chart for top 10 popular dishes
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_dishes.head(10).values, hue=popular_dishes.head(10).index, legend=True)
plt.title('Top 10 Popular Dishes')
plt.xlabel('Number of Orders')
plt.ylabel('Dish Name')
plt.tight_layout()
plt.savefig('D:/UserBehaviourAnalysis/visualizations/popular_dishes.png')
plt.close()

# 2. Correlation heatmap
plt.figure(figsize=(8, 6))
corr = merged_data[['Age', 'Amount (USD)', 'Rating']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('D:/UserBehaviourAnalysis/visualizations/correlation_heatmap.png')
plt.close()

# 3. Line plot for order trends over time
merged_data['Order Month'] = merged_data['Order Date'].dt.to_period('M')
orders_over_time = merged_data.groupby('Order Month')['Order ID'].nunique().reset_index()
orders_over_time['Order Month'] = orders_over_time['Order Month'].dt.to_timestamp()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Order Month', y='Order ID', data=orders_over_time, marker='o', color='green')
plt.title('Order Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('D:/UserBehaviourAnalysis/visualizations/order_trends.png')
plt.close()

# 4. Pie chart for distribution of order statuses
order_status_counts = merged_data['Order Status'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(order_status_counts, labels=order_status_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribution of Order Statuses')
plt.tight_layout()
plt.savefig('D:/UserBehaviourAnalysis/visualizations/order_status_distribution.png')
plt.close()

# 5. Scatter plot: User age vs. average order amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Amount (USD)', data=user_summary, hue='Favorite Meal', palette='deep')
plt.title('User Age vs. Average Order Amount')
plt.xlabel('Age')
plt.ylabel('Average Order Amount (USD)')
plt.legend(title='Favorite Meal')
plt.tight_layout()
plt.savefig('D:/UserBehaviourAnalysis/visualizations/age_vs_order_amount.png')
plt.close()

print("Data analysis and visualizations completed successfully.")
