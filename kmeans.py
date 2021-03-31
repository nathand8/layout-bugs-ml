from data import getBooleanAttributeRows
from sklearn.cluster import KMeans
from sklearn import datasets

model = KMeans(n_clusters=3)

data = getBooleanAttributeRows()

model.fit(data)

all_predictions = model.predict(data)

print(all_predictions)