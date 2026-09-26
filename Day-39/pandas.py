pip install pandas

import pandas as pd

prices = [2999, 15999, 52999, 4999, 1999]
products = ["Wireless Earbuds", "Smartphone", "Laptop", "Smartwatch", "Bluetooth Speaker"]

product_prices = pd.Series(prices, index=products)

print(product_prices)

print("Mean:", product_prices.mean())
print("Sum:", product_prices.sum())
print("Max:", product_prices.max())
print("Min:", product_prices.min())

print("Head (First 3 Elements):\n", product_prices.head(3))
print("\nTail (Last 2 Elements):\n", product_prices.tail(2))


print("Apply (Adding 18% GST):\n", product_prices.apply(lambda x: f'₹{x * 0.18}'))
print("Map (Formatting as Currency):\n", product_prices.map(lambda x: f'₹{x}.00'))


print(product_prices.sort_values())

print(product_prices.sort_index())

print(product_prices.sort_index(ascending=False))

print("Value Counts:\n", product_prices.value_counts())

from google.colab import files
import pandas as pd
upload = files.upload()
df = pd.read_excel("products_50_rows.xlsx")
print(df)

print(df.shape)
print(df.columns)
print(df.info())

print(df.head(5))
print(df.tail(5))

print(df.iloc[4])
print(df.iloc[8])

print(df['Product'])

print(df)
print(df.loc[2, "Brand"])
print(df.loc[3, "Product"])
print(df.loc[12,"Stock"])

print(df.iloc[4,0])
print(df.iloc[2,1])
print(df.iloc[3,3])

df_dropped = df.drop(columns=["Stock"])
#df_dropped = df.drop(columns=["Stock"],inplace=True)
print("After Dropping 'Stock' Column:\n",df_dropped)

df_renamed = df.rename(columns={"Price": "Cost"})
print(df_renamed)
#df.rename(columns={"Product": "Product name"},inplace=True)

print(df)
print(df.loc[df['BestSeller']==True])
print(df.loc[df['Stock']<40])
print(df.loc[df['Price']<10000])

df_grouped = df.groupby("Brand").agg({"Price": "mean", "Stock": "sum"})
print(df_grouped)
grouped = df.groupby("Brand").agg({"Price": ["mean", "max", "min", "sum"]})
print(grouped)
grouped = df.groupby("Brand")["Price"].mean()
print(grouped)


data2 = {
    "Brand": ["SoundMax", "TechNove", "ByteCore", "TimeTrack", "EchoBoom"],
    "Rating" : [4.2, 4.5, 4.0, 4.1, 3.9],
    "discount": [28,40,16,10,5]
}
df_ratings = pd.DataFrame(data2)
print(df_ratings)
df_merged = df.merge(df_ratings, on="Brand")
print("Merged  DataFrame (Adding Ratings):\n", df_merged)

new_data={
    "Product":["Tablet"],
    "Brand":["SmartWare"],
    "Price":[12999],
    "Stock":[25],
    "BestSeller":[True]

}
df_new =pd.DataFrame(new_data)
print(df_new)


df_concat = pd.concat([df,df_new],ignore_index=True)
print("Concatenated DataFrame:\n", df_concat)


df["Rank"]= df["Price"].rank(ascending=False)
print(df)
print(df.sort_values(by="Rank",ascending=True))
print(df.sort_values(by="Rank",ascending=False))

df.pivot_table(values="Price",index="Brand",columns="Stock",aggfunc="mean")

