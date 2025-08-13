# SuperIndo-Market-Basket-Analysis
Calculate product affinity in retail supermarket using apriori algorithm in Python with Colab.

## About Super Indo
Super Indo carries the concept of a daily needs supermarket with a proximity retail approach. This means that they open outlets close to residential areas so that consumers can easily access their products.

## About Market Basket Analysis
• It helps identify meaningful connections (affinities) between variables such as products or events. As a result, it can support strategies like cross-selling related items and boosting the overall value of a transaction.  
• In retail environments, it can also inform store layout planning. Items with strong associations can be placed close together to enhance customer convenience.  
• Alternatively, they may be positioned further apart to encourage customers to walk through more of the store, increasing their exposure to other products along the way.

## Data Source
In this project, the data source used is dummy data on purchases of equipment and household goods sold at Super Indo.
<pre>customer_id	product_1	product_2	product_3	product_4	product_5	product_6	product_7
28634	Detergen - Rinso	Tisu Gulung - Nice	Kain Lap Meja - QuickWipe	Ember - AquaTuff			
62057	Pembersih Lantai - Wipol	Tisu Gulung - Nice	Keset - DoorMate	Pel Lantai - KleanPro			
43029	Spons Cuci - ScrubPro	Lap Serbaguna - MicroWipe					
46551	Kain Pel - SoftDry	Tempat Sampah - EcoBin	Keset - DoorMate				
72621	Spons Cuci - ScrubPro	Pembersih Kaca - GlassBright	Sabun Cuci Tangan - Lifebuoy</pre>

## Python Libraries
Market Basket Analysis using Pandas and Mlxtend.
<pre>import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules</pre>

## Apriori Algorithm
In this project, the algorithm used is the Apriori Algorithm with the following objectives:  
• To find three-item subsets.  
After several trials, three-item subsets appeared when the following thresholds were applied:  
• Minimum support: 1%  
• Minimum confidence: 20%

## Results
<pre>antecedents	consequents	antecedent support	consequent support	support	confidence	lift	representativity	leverage	conviction	zhangs_metric	jaccard	certainty	kulczynski
frozenset({'Detergen - Rinso'})	frozenset({'Alat Pel Spray - SwifterJet'})	0.254	0.228	0.068	0.267716535	1.174195331	1	0.010088	1.054236559	0.198864532	0.164251208	0.051446289	0.282981075
frozenset({'Alat Pel Spray - SwifterJet'})	frozenset({'Detergen - Rinso'})	0.228	0.254	0.068	0.298245614	1.174195331	1	0.010088	1.06305	0.192167022	0.164251208	0.059310475	0.282981075
frozenset({'Kain Lap Meja - QuickWipe'})	frozenset({'Alat Pel Spray - SwifterJet'})	0.226	0.228	0.048	0.212389381	0.931532371	1	-0.003528	0.980179775	-0.086725664	0.118226601	-0.02022101	0.211457848
frozenset({'Alat Pel Spray - SwifterJet'})	frozenset({'Kain Lap Meja - QuickWipe'})	0.228	0.226	0.048	0.210526316	0.931532371	1	-0.003528	0.9804	-0.08693081	0.118226601	-0.01999184	0.211457848
frozenset({'Alat Pel Spray - SwifterJet'})	frozenset({'Kain Pel - SoftDry'})	0.228	0.254	0.07	0.307017544	1.208730488	1	0.012088	1.076506329	0.223686158	0.169902913	0.071069094	0.291304048</pre>
| name | description |
| --- | --- |
| antecedents | item or itemset on the “if” side of the rule (items purchased first). |
| consequents | item or itemset on the “then” side of the rule (items that tend to be purchased afterwards). |
| support | the proportion of transactions containing both antecedents and consequents. |
| confidence | the probability that consequents will be purchased when antecedents are purchased. |
| lift | measures how much more likely consequents are to be purchased when antecedents are purchased, compared to the likelihood of consequents being purchased independently. value > 1 indicates a positive relationship, < 1 a negative relationship, and = 1 no relationship. |

In this project, lift was used for analysis purposes for the following reasons:
1. Support is not sufficient to assess the strength of the relationship, because popular combinations do not necessarily have a strong correlation (they may appear by chance).
2. Similarly, if we only refer to confidence, the bias towards consequents is very high. If consequents are frequently purchased in general, confidence can be high even though there is no strong relationship with antecedents.
3. In this case, lift measures the actual strength of the relationship, not just frequency.
4. Lift also corrects for bias in confidence.
5. Meanwhile, other attributes are not yet required for the current analysis needs.

## Top 5 Product Combinations with Strongest Affinity
| | if buy | then also likely to buy | lift |
| --- | --- | --- | --- |
| 1 | Wipol Pembersih Lantai, SoftDry Kain Pel | SuperClean Sapu | 2.314815 |
| 2 | AquaTuff Ember, HandySafe Sarung Tangan Karet | SuperClean Sapu | 2.234994 |
| 3 | HandySafe Sarung Tangan Karet, QuickWipe Kain Lap Meja | ToiletMate Sikat WC | 2.16972 |
| 4 | Lifebuoy Sabun Cuci Tangan, SwifterJet Alat Pel Spray | MicroWipe Lap Serbaguna | 2.164502 |
| 5 | Lifebuoy Sabun Cuci Tangan, GlassBright Pembersih Kaca | DoorMate Keset | 2.12585 |

## Notes
• Minimum support ≥ 1% is usually considered the minimum threshold worth considering in Market Basket Analysis. But the higher the support, the more relevant it is to the business.  
• A minimum confidence of 20% is relatively low. But if the Lift is high (e.g., >1.5), then the rule can still be considered interesting, as it indicates a stronger relationship than random expectations.  
• Nevertheless, this threshold is still useful for initial exploration.
