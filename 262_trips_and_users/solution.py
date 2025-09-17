import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    u_client = users.add_suffix('_client')
    u_driver = users.add_suffix('_driver')

    df = (trips
          .merge(u_client, left_on='client_id', right_on='users_id_client', how='left')
          .merge(u_driver, left_on='driver_id', right_on='users_id_driver', how='left'))

    df = df[(df['banned_client'] == 'No') & (df['banned_driver'] == 'No')]

    df = df[(df['request_at'] >= '2013-10-01') & (df['request_at'] <= '2013-10-03')]

    df['is_cancelled'] = (df['status'] != 'completed').astype(float)

    out = (df.groupby('request_at', as_index=False)['is_cancelled']
             .mean()
             .rename(columns={'request_at': 'Day', 'is_cancelled': 'Cancellation Rate'}))

    out['Cancellation Rate'] = out['Cancellation Rate'].round(2)
    return out.sort_values('Day')