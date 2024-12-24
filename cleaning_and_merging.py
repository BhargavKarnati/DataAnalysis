import pandas as pd

# File paths
user_details_path = r"D:/UserBehaviourAnalysis/Data/Userdetails.xlsx"
cooking_sessions_path = r"D:/UserBehaviourAnalysis/Data/CookingSessions.xlsx"
order_details_path = r"D:/UserBehaviourAnalysis/Data/OrderDetails.xlsx"

# Loading datasets
user_details = pd.read_excel(user_details_path)
cooking_sessions = pd.read_excel(cooking_sessions_path)
order_details = pd.read_excel(order_details_path)

# Data Cleaning

# 1. Checking for missing values
print("Missing values in UserDetails:\n", user_details.isnull().sum())
print("Missing values in CookingSessions:\n", cooking_sessions.isnull().sum())
print("Missing values in OrderDetails:\n", order_details.isnull().sum())

# 2. Removing duplicates
user_details = user_details.drop_duplicates()
cooking_sessions = cooking_sessions.drop_duplicates()
order_details = order_details.drop_duplicates()

# 3. Converting date columns to datetime
user_details['Registration Date'] = pd.to_datetime(user_details['Registration Date'])
cooking_sessions['Session Start'] = pd.to_datetime(cooking_sessions['Session Start'])
cooking_sessions['Session End'] = pd.to_datetime(cooking_sessions['Session End'])
order_details['Order Date'] = pd.to_datetime(order_details['Order Date'])

# 4. Standardize categorical columns
user_details['Favorite Meal'] = user_details['Favorite Meal'].str.strip().str.capitalize()
cooking_sessions['Meal Type'] = cooking_sessions['Meal Type'].str.strip().str.capitalize()
order_details['Meal Type'] = order_details['Meal Type'].str.strip().str.capitalize()
order_details['Order Status'] = order_details['Order Status'].str.strip().str.capitalize()

# 5. Handling missing ratings by filling with mean
order_details['Rating'].fillna(order_details['Rating'].mean(), inplace=True)

# Saving cleaned data (optional)
user_details.to_excel('D:/UserBehaviourAnalysis/Data/Cleaned_Userdetails.xlsx', index=False)
cooking_sessions.to_excel('D:/UserBehaviourAnalysis/Data/Cleaned_CookingSessions.xlsx', index=False)
order_details.to_excel('D:/UserBehaviourAnalysis/Data/Cleaned_OrderDetails.xlsx', index=False)

# Merging Data

# Merge CookingSessions and OrderDetails on Session ID
sessions_orders = pd.merge(cooking_sessions, order_details, on='Session ID', how='inner')


#rename column for merging
sessions_orders.rename(columns={'User ID_y':'User ID'},inplace=True)



# Merge with UserDetails on User ID
merged_data = pd.merge(sessions_orders, user_details, on='User ID', how='inner')

# Save merged data
merged_data.to_excel('D:/UserBehaviourAnalysis/Data/Merged_data.xlsx', index=False)

print("Data cleaning and merging completed successfully.")

print(merged_data.columns)