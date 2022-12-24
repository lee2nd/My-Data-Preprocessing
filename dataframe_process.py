# Split strings into two Columns
new = data["Name"].str.split(" ", n = 1, expand = True)
data["First Name"]= new[0]
data["Last Name"]= new[1]

# Check if any value is NaN in a Pandas DataFrame
df.isnull().any().any()

# Drop NAN
https://www.digitalocean.com/community/tutorials/pandas-dropna-drop-null-na-values-from-dataframe

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

# Drop columns whose name contains a specific string (_id,_time)
# ex : ['scan_report_time', 'scan_sheet_id', 'scan_tool_id', 'scan_lot_id',
#       'scan_cst_id', 'scan_operation_id', 'scan_mes_id', 'track_report_time',
#       'track_sheet_id', 'track_tool_id', 'track_lot_id', 'track_cst_id',
#       'track_operation_id', 'track_mes_id', 'meth_report_time',
#       'meth_sheet_id', 'meth_tool_id', 'meth_lot_id', 'meth_cst_id',
#       'meth_operation_id', 'meth_mes_id']
df = df[df.columns.drop(list(df.filter(regex='_id|_time')))]

# Giving a column multiple indexes/headers
header = pd.MultiIndex.from_product([['location1','location2'],
                                     ['S1','S2','S3']],
                                    names=['loc','S'])
df = pd.DataFrame(np.random.randn(5, 6), 
                  index=['a','b','c','d','e'], 
                  columns=header)
# loc location1                     location2                    
# S          S1        S2        S3        S1        S2        S3
# a   -1.245988  0.858071 -1.433669  0.105300 -0.630531 -0.148113
# b    1.132016  0.318813  0.949564 -0.349722 -0.904325  0.443206
# c   -0.017991  0.032925  0.274248  0.326454 -0.108982  0.567472
# d    2.363533 -1.676141  0.562893  0.967338 -1.071719 -0.321113
# e    1.921324  0.110705  0.023244 -0.432196  0.172972 -0.50368

# Drop a column from a multi-level column index
# https://stackoverflow.com/questions/25135578/python-pandas-drop-a-column-from-a-multi-level-column-index
#    a         x   
#    b  c  f   c  f
# 0  1  3  7  21  8
# 1  2  4  9  21  8

df.drop(('a', 'c'), axis = 1)
#    a      x   
#    b  f   c  f
# 0  1  7  21  8
# 1  2  9  21  8

# Construct dataframe from dict
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)

#    col_1 col_2
# 0      3     a
# 1      2     b
# 2      1     c
# 3      0     d

# Convert dataframe to 2d Array
df.values
# array([[3, 'a'],
#        [2, 'b'],
#        [1, 'c'],
#        [0, 'd']]

# flatten multi columns to one column
data = {
    "priceA": [17, 35, 87],
    "priceB": [47, 45, 65],
    "priceC": [pd.NA, 15, 64],
}
df = pd.DataFrame(data)
data_trans = (df
             .values  # to_numpy()
             .T       # transpose
             .ravel() # flatten
              )
df_trans = pd.DataFrame(data_trans, copy=False)

# 選包含某 string 的 columns to list
target_col = df.columns[df.columns.str.contains("Ylabel_")].to_list()
