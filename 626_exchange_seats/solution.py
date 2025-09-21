import pandas as pd
import numpy as np

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:

    n = len(seat)
    odd = seat['id'] % 2 == 1
    nid = seat['id'] + np.where(odd, 1, -1)
    nid = np.where((seat['id'] == n) & (n % 2 == 1), seat['id'], nid)

    out = seat.copy()
    out['id'] = nid
    return out[['id', 'student']].sort_values('id', ignore_index=True)