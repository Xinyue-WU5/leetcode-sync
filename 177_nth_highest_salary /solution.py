import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame: 
    if N <= 0: 
        return pd.DataFrame({f'getNthHighestSalary({N})': [np.nan]}) 
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False) 

    if len(unique_salaries) < N: 
        return pd.DataFrame({f'getNthHighestSalary({N})': [np.nan]}) 
    else: 
        return pd.DataFrame({f'getNthHighestSalary({N})': [unique_salaries.iloc[N-1]]}) 