import pandas as pd
df1 = pd.read_csv("ahmed_nagar_holding_data.csv")
print(df1)

holding_numbers = df1["concat"]
print(holding_numbers)

# for col in df1.columns:
#     if df1[col].dtype == 'object':
#         df1[col] = df1[col].str.replace(',', '')

# df1['holding'] = df1[df1.columns[0]]
# print(df1['holding'])

# df2 = pd.read_csv("ahmed_nagar_desco_data.csv")
# print(df2)
# df2 = pd.read_csv("ahmedNagar_desco_data_v2.csv")
df2 = pd.read_csv("ahmed_nagar_desco_data.csv")
print(df2)

address = df2["parsed_address"]
print(address)

#df2['status'] = 'missed' 
# for index, row in df2.iterrows():
#     address = row['parsed_address']
#     if address in df1['concat'].values:
#         df2.at[index, 'status'] = 'not missed'
# print(df2)

# df2['status'] = df2['parsed_address'].apply(lambda x: 'not missed' if x in df1['concat'].values else 'missed')
# print(df2)


import re
df1["concat"] = df1["concat"].str.replace(',', '')
holding_numbers_set = set(df1["concat"])
def check_holding_number(address):
    for holding_number in holding_numbers_set:
        if re.search(r'\b{}\b'.format(re.escape(holding_number)), address):
            return 'not missed'
    return 'missed'

df2['status'] = df2['parsed_address'].apply(check_holding_number)
print(df2)


df2.to_csv('ahmed_nagar_soolution.csv', index=False)
print("CSV file saved successfully.")




