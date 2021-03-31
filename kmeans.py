import os
from data import getBooleanAttributeRows
from sklearn.cluster import KMeans
from sklearn import datasets

OUT_DIR = "./kmeans_output"

data, row_attrs = getBooleanAttributeRows()

for n_clusters in range(100, 1001):

    # Learn the algorithm with n_clusters
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)

    # Get the list of attributes for each cluster
    results = dict([(c, []) for c in range(n_clusters)])
    for row in data:
        prediction = model.predict([row])[0]
        attrs = [row_attrs[i] for i in range(len(row)) if row[i] == 1]
        results[prediction].append(', '.join(attrs))
        
    # Output the list of attributes for cluster size
    n_dir = os.path.join(OUT_DIR, str(n_clusters))
    os.makedirs(n_dir, exist_ok=True)
    for cluster_i, attr_lists in results.items():
        filepath = os.path.join(n_dir, f"cluster_{cluster_i}_of_{n_clusters}.log")
        attr_lists.sort()
        with open(filepath, 'w') as fh:
            fh.write("\n".join(attr_lists))
