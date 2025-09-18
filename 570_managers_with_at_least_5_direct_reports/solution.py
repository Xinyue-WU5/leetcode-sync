import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee['managerId'].value_counts(dropna=True)
    eligible_ids = counts[counts >= 5].index
    out = employee.loc[employee['id'].isin(eligible_ids), ['name']].reset_index(drop=True)
    return out