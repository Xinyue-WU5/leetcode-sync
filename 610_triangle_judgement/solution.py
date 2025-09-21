import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    tri = triangle.copy()

    cond = (
        (tri['x'] + tri['y'] > tri['z']) &
        (tri['x'] + tri['z'] > tri['y']) &
        (tri['y'] + tri['z'] > tri['x'])
    )

    tri['triangle'] = np.where(cond, 'Yes', 'No')
    return tri