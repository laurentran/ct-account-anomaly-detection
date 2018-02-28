from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

data = 'data/featureVectors_t0.csv'
X_raw = pd.read_csv(data)
X = X_raw.drop(['ct_planid','ct_valuedate'], axis=1)

kmeans = KMeans(n_clusters=50, random_state=0).fit(X)
kmeans.cluster_centers_
kmeans.labels_

planIds = X_raw['ct_planid'].as_matrix()
cluster_assignments = np.array(list(zip(planIds,kmeans.labels_)))

np.save('./data/cluster_assignments.npy', cluster_assignments)
