# Split strings into two Columns
new = data["Name"].str.split(" ", n = 1, expand = True)
data["First Name"]= new[0]
data["Last Name"]= new[1]

# Check if any value is NaN in a Pandas DataFrame
df.isnull().any().any()

# Create multiple dataframes in loop
# https://stackoverflow.com/questions/30635145/create-multiple-dataframes-in-loop
## method1
dfs = ['df1', 'df2', 'df3', 'df4']
for df in dfs:
     exec('{} = pd.DataFrame()'.format(df))

## method2 --> a better way     
dfs = ['df5', 'df6']     
d = {}
for name in dfs:
    d[name] = pd.DataFrame()    
for name, df in d.items():
    # operate on DataFrame 'df' for company 'name'   

# Drop columns whose name contains a specific string
# ex : Result1, Test1, Result2, Test2, Result3, Test3, etc...
df = df[df.columns.drop(list(df.filter(regex='Test')))]
