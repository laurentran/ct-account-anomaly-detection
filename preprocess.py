import pandas as pd

# read data
dataPath = 'data/captrust_data_export_t1.csv'
raw = pd.read_csv(dataPath)

# get encoded vectors
data = pd.get_dummies(raw, columns=['ct_assetclassidname', 'ct_plantype', 'ct_macroassetclass', 'ct_investmenttype'])

# sum value column by planid
x = data[['ct_planid','ct_value']]
x = x.groupby('ct_planid').sum()

# get max of other columns by planid
y = data.groupby('ct_planid').max()
y = y.drop(['ct_value','ct_investmentidname','ct_allocationname','ct_strategyid'], axis=1)

# concat results and encode strings
result = pd.concat([x, y], axis=1)
result = pd.get_dummies(result, columns=['ct_custodianname','ct_discretionarytypename','ct_erisaname','ct_modeltypeidname','ct_plantypename'])

# write to csv
result.to_csv('data/featureVectors_t1.csv', sep=',')