import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print df
print ' '
print df.index
print ' '
print df.columns
print ' '
print df.ix['c']
print ' '
print df.ix[['a', 'd']]
print ' '
print df.ix[df.index[1:3]]
print ' '
print df.sum()
print ' '
print df ** 2
print ' '
df['floats'] = (1.5, 2.5, 3.5, 4.5)
print df
print ' '