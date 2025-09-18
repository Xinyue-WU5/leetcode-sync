import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.copy()
    activity['event_date'] = pd.to_datetime(activity['event_date'])

    first = (
        activity.groupby('player_id', as_index=False)['event_date']
        .min()
        .rename(columns={'event_date': 'first_login'})
    )

    merged = activity.merge(first, on='player_id', how='left')
    merged['day1'] = merged['event_date'] == (merged['first_login'] + pd.Timedelta(days=1))

    day1_by_player = merged.groupby('player_id')['day1'].any()

    fraction = round(day1_by_player.mean(), 2)

    return pd.DataFrame({'fraction': [fraction]})