import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products['change_date'] = pd.to_datetime(products['change_date'])
    eligible = products[products['change_date'] <= '2019-08-16']
    latest_idx = (eligible.sort_values(['product_id', 'change_date']).groupby('product_id')['change_date'].idxmax())
    latest = eligible.loc[latest_idx, ['product_id', 'new_price']]
    prod_ids = products[['product_id']].drop_duplicates()
    out = prod_ids.merge(latest, on='product_id', how='left')
    out['price'] = out['new_price'].fillna(10).astype(float)

    return out[['product_id', 'price']]