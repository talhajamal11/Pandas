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

print(read_file)
print(read_file.shape)

