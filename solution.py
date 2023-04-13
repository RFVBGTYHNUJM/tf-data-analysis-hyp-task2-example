import pandas as pd
import numpy as np


chat_id = 813595623 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    return stats.ks_2samp(x, y)>0.03 # Ваш ответ, True или False
