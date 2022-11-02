# drop columns with missing value > 0.60
df_X = df_X.loc[:, df_X.isnull().mean()<.60]

# sort
df.sort_values(by='col1', ascending=False)

# impute with MICE
X_size_row, X_size_column = df_X.shape
X_features_list = df_X.columns.tolist()

imp = IterativeImputer(
	estimator=ExtraTreesRegressor(random_state=42),
	missing_values=np.nan,
	max_iter=1,
	verbose=2,
	n_nearest_features=int(np.log(X_size_column+1)),
	random_state=42)
df_X = imp.fit_transform(df_X)
df_X = pd.DataFrame(df_X, columns=X_features_list)

# drop unique value columns
df_X = df_X[[col for col in list(df_X) if len(df_X[col].unique())>1]]

# label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data.loc[:,"xxx"] = label_encoder.fit_transform(data.loc[:,"xxx"]).astype('float64')

# one-hot encoding
df_one_hot = pd.get_dummies(df_X['xxx'],prefix='xxx')
df_X = df_X.drop(columns='xxx')
df_X = pd.concat([df_X,df_one_hot],axis=1)

# correlation
import seaborn as sns
corr = df_X.corr()
sns.heatmap(corr)
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False
selected_columns = df_X.columns[columns]
df_X = df_X[selected_columns]

# get the feature importances 
from sklearn.ensemble import RandomForestRegressor
import numpy as np

regr_rf = RandomForestRegressor(n_estimators=1024, random_state=42) 
regr_rf = regr_rf.fit(df_X, df_y)

df_feature_rank = pd.DataFrame(
	{"feature": list(df_X.columns),
	 "importance": list(regr_rf.feature_importances_)
	}).sort_values(by="importance", ascending=False) 
df_feature_rank["importance"] = 100 * df_feature_rank["importance"]	

cum_pctg = np.cumsum(list(regr_rf.feature_importances_))

# xgb model in classification problem
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = XGBClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_probs = model.predict_proba(X_test)[:, 1]

cm = confusion_matrix(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_probs)
accuracy_score(y_test, y_pred)
