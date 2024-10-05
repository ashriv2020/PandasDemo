import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan, 6,8])
print(s)

dates = pd.date_range('20241001', periods=5)
print(dates)

df = pd.DataFrame(np.random.randn(5,4), index=dates, columns=list('ABCD'))
print(df)