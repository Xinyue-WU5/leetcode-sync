import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    users["join_date"] = pd.to_datetime(users["join_date"], errors="coerce")
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
    orders_2019 = orders.loc[orders["order_date"].dt.year == 2019]
    df1 = (orders_2019.groupby("buyer_id", as_index=False).size().rename(columns={"size": "orders_in_2019"}))
    out = users.merge(df1, how="left", left_on="user_id", right_on="buyer_id")
    out["orders_in_2019"] = out["orders_in_2019"].fillna(0).astype(int)
    out["buyer_id"] = out["user_id"]

    return out[["buyer_id", "join_date", "orders_in_2019"]]