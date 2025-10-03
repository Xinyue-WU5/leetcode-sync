import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    a = product_purchases.copy()
    b = product_purchases.copy()
    a = a.rename(columns={'product_id':'product1_id'})
    b = b.rename(columns={'product_id':'product2_id'})

    df = (
        a.merge(b, on='user_id', how='left')
         .merge(product_info, left_on='product1_id', right_on='product_id', how='left')
         .rename(columns={'category':'product1_category'})
         .merge(product_info, left_on='product2_id', right_on='product_id', how='left')
         .rename(columns={'category':'product2_category'})
    )

    df = df[df['product1_id'] < df['product2_id']]

    df1 = (df.groupby(['product1_id', 'product2_id', 'product1_category', 'product2_category'], as_index=False)
             ['user_id'].nunique()
             .rename(columns={'user_id': 'customer_count'}))

    df1 = df1[df1['customer_count'] >= 3]

    df1 = df1.sort_values(['customer_count', 'product1_id', 'product2_id'],
                          ascending=[False, True, True])

    return df1[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']]