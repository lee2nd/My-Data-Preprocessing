# Split strings into two Columns
new = data["Name"].str.split(" ", n = 1, expand = True)
data["First Name"]= new[0]
data["Last Name"]= new[1]

# Check if any value is NaN in a Pandas DataFrame
df.isnull().any().any()
