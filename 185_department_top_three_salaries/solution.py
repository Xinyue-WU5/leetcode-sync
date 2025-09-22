import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.rename(columns={'name':'Employee'})
    employee = employee.rename(columns={'salary':'Salary'})
    department = department.rename(columns={'name':'Department'})
    df = employee.merge(department, how='left', left_on='departmentId', right_on='id')
    df['rank'] = df.groupby('departmentId')['Salary'].rank(method="dense", ascending=False)

    salary = df[df['rank']<=3]

    return salary[['Department', 'Employee', 'Salary']]