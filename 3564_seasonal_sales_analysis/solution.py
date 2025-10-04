import pandas as pd
import numpy as np

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    m = sales['sale_date'].dt.month
    sales['season'] = np.select(
        [
            m.isin([12, 1, 2]),
            m.isin([3, 4, 5]),
            m.isin([6, 7, 8]),
            m.isin([9, 10, 11]),
        ],
        ['Winter', 'Spring', 'Summer', 'Fall']
    )


    sales['revenue'] = sales['quantity'] * sales['price']

    prod_season = (
        sales.groupby(['product_id', 'season'], as_index=False)
             .agg(quantity=('quantity', 'sum'),
                  revenue =('revenue',  'sum'))
    )

    df = prod_season.merge(products[['product_id', 'category']], on='product_id', how='left')
    cat_season = (
        df.groupby(['season', 'category'], as_index=False)
          .agg(total_quantity=('quantity', 'sum'),
               total_revenue =('revenue',  'sum'))
    )

    top = (
        cat_season.sort_values(
            ['season', 'total_quantity', 'total_revenue', 'category'],
            ascending=[True, False, False, True]
        )
        .drop_duplicates(['season'], keep='first')
    )

    season_order = pd.CategoricalDtype(['Fall', 'Spring', 'Summer', 'Winter'], ordered=True)
    top['season'] = top['season'].astype(season_order)
    top = top.sort_values('season').reset_index(drop=True)

    return top[['season', 'category', 'total_quantity', 'total_revenue']]