from rank import rank_func
import numpy as np

alpha = np.arange(5, dtype=float)
alpha[0] = np.nan
#alpha = np.array([-1.,1.,1.,2.,3.])
rank_func(alpha)
print(alpha)
