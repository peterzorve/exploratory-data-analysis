
"""
# Exercise 13: Different linkage, different hierarchical clustering!

In the video, you saw a hierarchical clustering of the voting countries at the Eurovision song contest using `'complete'` linkage. Now, perform a hierarchical clustering of the voting countries with `'single'` linkage, and compare the resulting dendrogram with the one in the video.  Different linkage, different hierarchical clustering!

First, we need to do a little pre-processing to account for one of the Eurovision rules: countries are not allowed to vote for themselves.
"""


import pandas as pd

scores_df = pd.read_csv('../datasets/eurovision-2016-televoting.csv', index_col=0)
country_names = list(scores_df.index)



"""
**Step 2:** Display the DataFrame, and have a look.  Each row represents a country that _voted_, while each column represents a country that _performed_.

Notice the NaN ("not-a-number") values.  These correspond to missing scores in the original CSV file.  These scores are missing because countries that performed were not allowed to vote for themselves.

"""

df_country = pd.DataFrame(scores_df)
df_country


"""
**Step 3:** Fill in the NaNs with the highest possible score (12) - we are assuming that countries would vote for themselves, if they had been allowed to do so.  _(This bit written for you)._
"""

filtered_data = df_country.fillna(12)
filtered_data


"""
**Step 4:** Import the `normalize` function from `sklearn.preprocessing`.
"""

from sklearn.preprocessing import normalize



"""
**Step 5:** Apply the normalize function to `scores_df.values`, assigning the result to `samples`.

(Why do we need to normalize?  Because now that the missing values are filled with 12 points, some countries (those that performed) given a greater total number of points when voting.  The `normalize` function corrects for this.) 
"""

samples = normalize(filtered_data.values)
samples 

"""**
Step 6:** Import:
 + `linkage` and `dendrogram` from `scipy.cluster.hierarchy`.
 + `matplotlib.pyplot` as `plt`."""

from scipy.cluster.hierarchy import linkage, dendrogram 
import matplotlib as plt 


"""
**Step 7:** Perform hierarchical clustering on `samples` using the `linkage()` function with the `method='single'` keyword argument. Assign the result to `mergings`.
"""
mergings = linkage(samples, method='single')
mergings


"""
**Step 8:** Plot a dendrogram of the hierarchical clustering, using the list `country_names` as the `labels`. In addition, specify the `leaf_rotation=90`, and `leaf_font_size=6` keyword arguments as you have done earlier.
"""

fig = plt.figure(figsize=(12, 10))
dendrogram_fig = dendrogram(mergings, leaf_rotation=90, leaf_font_size=6)



"""
# Exercise 14: Intermediate clusterings - how many clusters?

Consider the dendrogram below - it is the result of your hierarchical clustering of some of the grain samples.

**Question:** If the hierarchical clustering were stopped at height 6 on the dendrogram, how many clusters would there be?

**Hint:** Imagine a horizontal line at this height.
"""

import pandas as pd

seeds_df = pd.read_csv('../datasets/seeds-less-rows.csv')

# remove the grain species from the DataFrame, save for later
varieties = list(seeds_df.pop('grain_variety'))

# extract the measurements as a NumPy array
samples = seeds_df.values

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

mergings = linkage(samples, method='complete')

dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()











