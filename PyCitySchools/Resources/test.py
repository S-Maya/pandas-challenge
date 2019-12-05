import pandas as pd
import os
path = os.path.join('Resource','schools_complete.csv')
df = pd.read_csv(path)
df.head()
df.shape