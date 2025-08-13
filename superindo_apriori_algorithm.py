from google.colab import files

uploaded = files.upload()

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Reading the dataset
df = pd.read_csv('superindo_products.csv')

# Preparing data for Apriori
# Converting data into one-hot encoding format
basket = (df.iloc[:, 1:]
          .stack()
          .groupby(level=0)
          .apply(lambda x: ','.join(x.dropna()))
          .str.get_dummies(sep=','))

# Running Apriori for 1-itemset, 2-itemset, and 3-itemset
frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True, max_len=3)

# Displaying frequent itemsets
print("Frequent Itemsets:")
display(frequent_itemsets)

# Calculating association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

# Displaying association rules
print("\nAssociation Rules:")
display(rules)

frequent_itemsets.to_csv('frequent_itemsets.csv', index=False)
rules.to_csv('association_rules.csv', index=False)

files.download('frequent_itemsets.csv')
files.download('association_rules.csv')