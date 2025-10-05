import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    pr = performance_reviews.copy()
    pr['review_date'] = pd.to_datetime(pr['review_date'])
    pr = pr.sort_values(['employee_id', 'review_date', 'review_id'],
                        ascending=[True, False, False])

    pr['rn'] = pr.groupby('employee_id').cumcount() + 1

    last3 = pr[pr['rn'] <= 3]

    wide = last3.pivot(index='employee_id', columns='rn', values='rating')

    mask = wide.notna().all(axis=1) & (wide[3] < wide[2]) & (wide[2] < wide[1])

    out = (wide.loc[mask]
               .assign(improvement_score=wide[1] - wide[3])
               .reset_index()[['employee_id', 'improvement_score']]
               .merge(employees[['employee_id', 'name']], on='employee_id', how='left')
               .sort_values(['improvement_score', 'name'], ascending=[False, True])
               .reset_index(drop=True))

    return out[['employee_id', 'name', 'improvement_score']]