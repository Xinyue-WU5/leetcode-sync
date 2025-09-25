import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['money'] = np.where(stocks['operation']=='Buy', -stocks['price'], stocks['price'])
    plus = stocks.groupby('stock_name', as_index=False)['money'].sum().rename(columns={'money':'capital_gain_loss'})

    return plus