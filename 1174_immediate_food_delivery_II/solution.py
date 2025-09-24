import pandas as pd
import numpy as np

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['order_date'] = pd.to_datetime(delivery['order_date'])
    delivery['customer_pref_delivery_date'] = pd.to_datetime(delivery['customer_pref_delivery_date'])
    earliest_idx = (delivery.sort_values(['customer_id', 'order_date']).groupby('customer_id')['order_date'].idxmin())
    earliest = delivery.loc[earliest_idx, ['delivery_id', 'order_date','customer_pref_delivery_date']].drop_duplicates()   
    earliest['imme'] = np.where(earliest['order_date'] == earliest['customer_pref_delivery_date'], 1,0)    

    immediate_percentage = round(100*sum(earliest['imme'])/earliest.shape[0] ,2)

    return pd.DataFrame({
        'immediate_percentage' : [immediate_percentage]
    })