# User Behavior Analysis and Business Insights

## **Overview**

This project analyzes user behavior, cooking preferences, and order trends to derive actionable business insights. The analysis is based on three datasets:

- **UserDetails**: Information about users.
- **CookingSessions**: Details of user's cooking activities.
- **OrderDetails**: Records of users' orders.

## **Objectives**

- Cleaning and merging the datasets.
- Analyzing the relationship between cooking sessions and user orders.
- Identifying popular dishes.
- Exploring demographic factors influencing user behavior.
- Creating visualizations to showcase key insights.
- Business recommendations based on findings.

## **Methodology**

### **Data Cleaning and Merging**

- **Cleaning**:
  - Handled missing values by filling with mean ratings.
  - Removed duplicate records.
  - Standardized date formats and categorical variables.
- **Merging**:
  - Combined datasets on `User ID` and `Session ID` to form a comprehensive dataset.

### **Data Analysis**

- **Cooking Sessions vs. Orders**:
  - Analyzed the frequency of cooking sessions and their association with orders.
- **Popular Dishes**:
  - Identified the top 10 most ordered dishes.
- **Demographics**:
  - Examined how age groups and favorite meals influence ordering behavior.

## **Key Findings**

### **1. Popular Dishes**

![Top 10 Popular Dishes](visualizations\popular_dishes.png)

- **Spaghetti** is the most ordered dish, followed by **Caesar Salad**.
- High popularity indicates these dishes could be featured more prominently in marketing campaigns.

### **2. Order Trends Over Time**

![Order Trends Over Time](visualizations\order_trends.png)



### **3. Demographic Influences**

![Correlation Heatmap](visualizations\correlation_heatmap.png)

- **Age** shows a moderate positive correlation with **Amount (USD)**, indicating older users spend more per order.
- **Rating** is positively correlated with **Amount (USD)**, suggesting higher spending is associated with better experiences.

![User Age vs. Average Order Amount](visualizations\age_vs_order_amount.png)

- Users aged **31-40** and **41-50** have the highest average order amounts.
- **Favorite Meal** categories influence spending patterns, with **Dinner** being the most lucrative.

### **4. Order Status Distribution**

![Order Status Distribution](visualizations\order_status_distribution.png)

- **Completed** orders constitute the majority (e.g., 90%), while **Canceled** orders are minimal.
- Low cancellation rate indicates effective order fulfillment processes.

## **Business Recommendations**

1. **Promote Popular Dishes**:
   - Feature **Spaghetti** and **Caesar Salad** in promotional materials and menu highlights.
   
2. **Target High-Spending Demographics**:
   - Focus marketing efforts on age groups **31-50**, who show higher average spending.
   
   
3. **Enhance User Experience**:
   - Maintain high ratings by ensuring quality and timely deliveries, reinforcing positive customer experiences.

## **Conclusion**

The analysis provides valuable insights into user behavior, highlighting popular dishes, demographic influences, and order trends. Implementing the recommended strategies can enhance user engagement, optimize menu offerings, and drive revenue growth.
