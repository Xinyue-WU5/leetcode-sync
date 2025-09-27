import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    odd = transactions[transactions['transaction_id']%2 == 1]
    even = transactions[transactions['transaction_id']%2 == 0]
    odd = odd.groupby('transaction_date', as_index=False)['amount'].sum().rename(columns={'amount':'odd_sum'})
    even = even.groupby('transaction_date', as_index=False)['amount'].sum().rename(columns={'amount':'even_sum'})

    df = odd.merge(even, how='outer', on='transaction_date').fillna(0)

    return df[['transaction_date', 'odd_sum', 'even_sum']]