import numpy as np
import pandas as pd

def sum_sales(df):
    index = df.Store.index
    sum_sales = []
    
    for idx in index:
        sum_sales.append(df.loc['Store' == idx, 'Weekly_Sales'])
    
    return sum_sales