import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    pid1 = insurance.loc[
        insurance['tiv_2015'].duplicated(keep=False), 'pid'
    ].unique()
    
    pid2 = insurance.loc[
        ~insurance.duplicated(subset=['lon', 'lat'], keep=False), 'pid'
    ].unique()

    common_pids = set(pid1) & set(pid2)

    tiv16 = insurance.loc[
        insurance['pid'].isin(common_pids), 'tiv_2016'
    ].sum()

    return pd.DataFrame({'tiv_2016': [round(tiv16, 2)]})