import pandas as pd 
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame: 
    employee_sorted = employee.sort_values(by='salary', ascending=False)
    unique_salaries = employee_sorted['salary'].drop_duplicates()
 
    if len(unique_salaries) < 2: 
        # no second highest salary 
        return pd.DataFrame({'SecondHighestSalary': [np.nan]}) 
    else: 
        # take the second highest 
        return pd.DataFrame({'SecondHighestSalary': [unique_salaries.iloc[1]]})