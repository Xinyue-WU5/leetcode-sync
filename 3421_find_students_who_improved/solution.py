import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    first = scores.groupby(['student_id','subject'], as_index=False)['exam_date'].min()
    df1 = first.merge(scores, on=['student_id','subject','exam_date'], how='left').rename(columns={'score':'first_score'})
    latest = scores.groupby(['student_id','subject'], as_index=False)['exam_date'].max()
    df2 = latest.merge(scores, on=['student_id','subject','exam_date'], how='left').rename(columns={'score':'latest_score'})
    df = df1.merge(df2, on=['student_id','subject'], how='left')
    out = df[df['latest_score'] > df['first_score']].copy()
    out = (out[['student_id','subject','first_score','latest_score']]
           .drop_duplicates()
           .sort_values(['student_id','subject']))    
    return out