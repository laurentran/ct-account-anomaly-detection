import numpy as np
import pandas as pd

# function to return outliers given an array of values
def outliers_modified_z_score(ys):
    threshold = 3.5 #set threshold higher if more false positives are acceptable and lower to limit false positives
    median_y = np.median(ys)
    median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ys])
    modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y for y in ys]
    return np.where(np.abs(modified_z_scores) > threshold)

# input data paths
cluster_assignments_path = 'data/cluster_assignments.npy' 
t0_data_path = 'data/featureVectors_t0.csv' 
t1_data_path = 'data/featureVectors_t1.csv' 

# output data path
outliers_path = 'data/possibleOutliers.csv'

# read in data 
cluster_assignments = np.load(cluster_assignments_path) # get plan ids and clusters
t0 = pd.read_csv(t0_data_path) # get feature vectors from t0
t1 = pd.read_csv(t1_data_path) # get feature vectors from t1

# create dictionary where key:cluster and value:list of planIDs
clusterMembers = {}
for tuple in cluster_assignments:
    value = tuple[0].decode("utf-8") 
    key = int(tuple[1])
    if key in clusterMembers:
        clusterMembers[key].append(value)
    else:
        clusterMembers[key] = [value]

# create dictionaries for t0 and t1 where key:planID and value:plan value
t0_dict = dict(zip(t0['ct_planid'],t0['ct_value']))
t1_dict = dict(zip(t1['ct_planid'],t1['ct_value']))

# iterate through clusters to find outliers
result = []
for key, value in clusterMembers.items():
    deltaList = []
    planIdList = []
    deltaPlanList = []
    for id in value: # for each planID in each cluster
        if (id in t0_dict and id in t1_dict):
            t0_val = t0_dict[id] # plan value at t0
            t1_val = t1_dict[id] # plan value at t1
            if (t0_val != 0):
                delta = (t1_val - t0_val)/t0_val
                deltaList.append(delta)
                planIdList.append(id)
                
    if(len(deltaList) <= 1): # if cluster contains fewer than 2 plans that had values at t0 and t1, no outliers can be found
        continue
    outliers = outliers_modified_z_score(deltaList)
    median = np.median(deltaList)
    stddev = np.std(deltaList)
    for outlier in outliers[0]:
        outlierId = planIdList[outlier] #find associated planID
        deltaVal = deltaList[outlier]
        result.append((outlierId, deltaVal, median, stddev))

# write possible outliers to csv        
result = pd.DataFrame(result, columns = ('PlanID','% Change','Median','Standard Deviation'))
result.to_csv(outliers_path, sep=',', index=False)
