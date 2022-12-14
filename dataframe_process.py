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

# Drop columns whose name contains a specific string (_id,_time)
# ex : ['scan_report_time', 'scan_sheet_id', 'scan_tool_id', 'scan_lot_id',
       'scan_cst_id', 'scan_operation_id', 'scan_mes_id', 'track_report_time',
       'track_sheet_id', 'track_tool_id', 'track_lot_id', 'track_cst_id',
       'track_operation_id', 'track_mes_id', 'meth_report_time',
       'meth_sheet_id', 'meth_tool_id', 'meth_lot_id', 'meth_cst_id',
       'meth_operation_id', 'meth_mes_id']
df = df[df.columns.drop(list(df.filter(regex='_id|_time')))]
