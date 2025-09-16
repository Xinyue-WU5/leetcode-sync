import pandas as pd 

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame: 
    logs = logs.sort_values('id').reset_index(drop=True)  # ensure order 
    result = [] 

    for i in range(len(logs) - 2):   
        if logs.loc[i, 'num'] == logs.loc[i+1, 'num'] == logs.loc[i+2, 'num']: 
            result.append(logs.loc[i, 'num']) 
    return pd.DataFrame({'ConsecutiveNums': pd.Series(result).drop_duplicates()}) 