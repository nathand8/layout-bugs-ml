from data import getBooleanAttributeRows
from scipy.cluster.hierarchy import linkage, dendrogram, to_tree
import matplotlib.pyplot as plt
import pandas as pd

samples, attrs = getBooleanAttributeRows()

mergings = linkage(samples, method='complete')

tree, nodes = to_tree(mergings, rd=True)

print(1)

# dendrogram(mergings, leaf_rotation=90, leaf_font_size=6)
# plt.show()
