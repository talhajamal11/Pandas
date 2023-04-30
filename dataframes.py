import pandas as pd
import os

dictionary = {
    "Names" : ["Talha", "Zainab"],
    "Age" : [26, 26]
}

df = pd.DataFrame(dictionary, 
                  index=["Male", "Female"]
                  )

series = pd.Series(["Talha", 26, "Male"], 
                   index=["Name", "Age", "Sex"],
                   name="Talha metadata"
                   )
#print(df)
#print("-----------")
#print(series)

#print("-----------")
path = str(os.getcwd()) + "/sample.csv"
read_file = pd.read_csv(path)
read_file.columns = ["Product_A", "Product_B","Product_C"]

#print(read_file)
#print(read_file.shape)

# Save df to file

read_file.to_csv("read_file.csv")


# using the Loc method on Pandas DF
#print(read_file.iloc[:, 1])

new_df = read_file.loc[(read_file.Product_A > 30)]

print("*******************")
#print(new_df)

print(new_df)

def square(x):
    return x**2


print("*******************")

row_1 = new_df.Product_A.map(square)
row_2 = new_df.Product_B.map(square)
print(row_1)
print("*****************")
print(row_2)

print(new_df.describe())