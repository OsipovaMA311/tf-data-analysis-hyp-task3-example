import pandas as pd
import numpy as np
from scipy.stats import permutation_test

chat_id = 468819439 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    pval = permutation_test((x, y), lambda x, y, axis: np.median(x, axis=axis) - np.median(y, axis=axis),
                                             vectorized=True,
                                             n_resamples=1000,
                                             permutation_type="independent",
                                             alternative="greater").pvalue
    return pval < 0.07 # Ваш ответ, True или False
