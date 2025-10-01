import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = user_activity.groupby(['user_id','activity_type'], as_index=False)['activity_duration'].mean().round({'activity_duration': 2})
    p = df[df['activity_type'] ==  'paid'].rename(columns={'activity_duration': 'paid_avg_duration'})
    t = df[df['activity_type'] ==  'free_trial'].rename(columns={'activity_duration': 'trial_avg_duration'})

    out = p.merge(t, how='left', on='user_id')

    return out[['user_id', 'trial_avg_duration', 'paid_avg_duration']]