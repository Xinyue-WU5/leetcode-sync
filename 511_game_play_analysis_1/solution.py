import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    activity = activity.sort_values(by=['player_id', 'event_date'])
    result = activity.drop_duplicates(subset='player_id', keep='first')
    
    return result[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})