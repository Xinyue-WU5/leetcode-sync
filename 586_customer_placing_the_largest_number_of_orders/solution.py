import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty or 'customer_number' not in orders.columns:
        return pd.DataFrame({'customer_number': []})
    
    df = (
        orders.groupby('customer_number')
              .size()
              .reset_index(name='order_count')
              .sort_values(by='order_count', ascending=False)
    )
    
    if df.empty:
        return pd.DataFrame({'customer_number': []})
    
    top = df.iloc[0]['customer_number']
    return pd.DataFrame({'customer_number': [top]})
