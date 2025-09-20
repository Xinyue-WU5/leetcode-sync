import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_com = company.loc[company['name'] == 'RED', ['com_id']]
    red_orders = orders.merge(red_com, on='com_id', how='inner')
    red_sales_ids = set(red_orders['sales_id'].unique())

    return sales_person.loc[~sales_person['sales_id'].isin(red_sales_ids), ['name']]