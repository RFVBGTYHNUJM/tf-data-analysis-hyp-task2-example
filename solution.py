import pandas as pd
import numpy as np
from scipy import stats
import scipy.stats
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 813595623 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    return stats.ks_2samp(x, y)>0.03 
