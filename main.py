if __name__ == '__main__':
    import pandas as pd
import numpy as np
data = {
    'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C001', 'C006', 'C007'],
    'Name': ['  Nguyen Van A ', 'Tran Thi B', 'Le Van C', 'Pham Thi D', 'Hoang Van E', '  Nguyen Van A ', 'Vu Thi F', 'Doan Van G'],
    'Age': [25, 30, np.nan, -5, 45, 25, 150, 28],
    'Gender': ['Nam', 'Nu', 'male', 'Female', 'Nam', 'Nam', 'Nữ', 'Nam'],
    'Join_Date': ['2023-01-15', '2023/02/20', '15-03-2023', '2023-04-01', None, '2023-01-15', '2023-06-10', '2023-07-05'],
    'Total_Spend': ['1000000', '2500000', ' 1500000 ', '3000000', 'invalid_amount', '1000000', '500000', None]
}
df_clean = pd.DataFrame(data)

df_clean['Name'] = df_clean['Name'].str.strip()
df_clean['Total_Spend'] = df_clean['Total_Spend'].str.strip()

gender_mapping = {'Nu': 'Nữ', 'male': 'Nam', 'Female': 'Nữ'}
df_clean['Gender'] = df_clean['Gender'].replace(gender_mapping)

df_clean['Total_Spend'] = pd.to_numeric(df_clean['Total_Spend'], errors= 'coerce')

median_spend = df_clean['Total_Spend'].median()
df_clean['Total_Spend'] = df_clean['Total_Spend'].fillna(median_spend)

df_clean.loc[(df_clean['Age'] < 0) | (df_clean['Age'] > 100), 'Age'] = np.nan

median_age = df_clean['Age'].median()
df_clean['Age'] = df_clean['Age'].fillna(median_age)

df_clean['Age'] = df_clean['Age'].astype(int)

df_clean['Join_Date'] = pd.to_datetime(df_clean['Join_Date'], errors='coerce')

df_clean['Join_Date'] = df_clean['Join_Date'].ffill()

df_clean['Join_Date'] = df_clean['Join_Date'].dt.strftime('%Y-%m-%d')

# Thong tin df.info()
df_clean.info()

# Du lieu bang
print(df_clean)

