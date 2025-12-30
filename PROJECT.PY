import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('bike_sales_india.csv')
df.head(10) #first 10 rows
df.info()   #dataset information
df.describe() #checking numeric values
df.shape #showing the shape of dataset 
df.dropna(inplace=True) #removes null values in the dataset
df.drop_duplicates(inplace=True)
df.columns #checking columns so that we can remove unneccessary columns
df.columns=(
    df.columns.str.strip()
)
df.drop(['Price (INR)','Registration Year','Insurance Status','City Tier','Resale Price (INR)', 'Seller Type'] , axis=1, inplace=True)
df.columns
royal_enfiled_sales=df[df['Brand']=='Royal Enfield']['Brand'].count() #Here we can choose brand and know the sales
print('NO.OF Royal_Enfiled sold:',royal_enfiled_sales)
Bajaj_sales=df[df['Brand']=='Bajaj']['Brand'].count()
print('NO.OF Bajaj sold:',Bajaj_sales)
KTM_sales=df[df['Brand']=='KTM']['Brand'].count()
print('NO.OF KTM sold:',KTM_sales)
Yamaha_sales=df[df['Brand']=='Yamaha']['Brand'].count()
print('NO.OF Yamaha sold:',Yamaha_sales)
Kawasaki_sales=df[df['Brand']=='Kawasaki']['Brand'].count()
print('NO.OF Kawasaki sold:',Kawasaki_sales)
Hero_sales=df[df['Brand']=='Hero']['Brand'].count()
print('NO.OF Hero sold:',Hero_sales)
Honda_sales=df[df['Brand']=='Honda']['Brand'].count()
print('NO.OF Honda sold:',Honda_sales)
TVS_sales=df[df['Brand']=='TVS']['Brand'].count()
print('NO.OF TVS sold:',TVS_sales)
sales_df = pd.DataFrame({
    'brand': ['Royal Enfield', 'Bajaj', 'KTM', 'Yamaha', 'Kawasaki', 'Hero', 'Honda', 'TVS'],
    'sales': [royal_enfiled_sales, Bajaj_sales, KTM_sales, Yamaha_sales, Kawasaki_sales, Hero_sales, Honda_sales, TVS_sales]
})
sns.barplot(data=sales_df, x='brand', y='sales', width=0.4)
plt.title('Bike Sales: From 2015 to 2024')
plt.xticks(rotation=45, fontsize=6.1)
plt.show()

enfield_sales = (
    df[df['Brand'] == 'Royal Enfield']   
      .groupby('State')                   
      .size()
      .reset_index(name='sales')
)
print(enfield_sales)

bajaj_sales = (
    df[df['Brand'] == 'Bajaj']   
      .groupby('State')                   
      .size()
      .reset_index(name='sales')
)
print(bajaj_sales)

tvs_sales = (
    df[df['Brand'] == 'TVS']   
      .groupby('State')                   
      .size()
      .reset_index(name='sales')
)
print(tvs_sales)

ktm_sales = (
    df[df['Brand'] == 'KTM']   
      .groupby('State')                   
      .size()
      .reset_index(name='sales')
)
print(ktm_sales)

sns.lineplot(data=enfield_sales, x='State', y='sales', marker='o')
plt.title('Royal Enfield Sales')
plt.xticks(rotation=45, fontsize=5.5)
plt.show()

sns.scatterplot(data=bajaj_sales, x='State', y='sales', marker='o', size='sales')
plt.title('Bajaj Sales')
plt.xticks(rotation=45, fontsize=5.5)
plt.show()

pivot_tvs = tvs_sales.set_index('State')
plt.figure(figsize=(6,6))
sns.heatmap(
    pivot_tvs,
    annot=True,  
    fmt='d',      
    cmap='Blues'  
)
plt.title('TVS Sales by State')
plt.show()










