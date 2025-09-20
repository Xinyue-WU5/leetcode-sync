import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    child_counts = tree['p_id'].value_counts(dropna=True) 
    nchild = tree['id'].map(child_counts).fillna(0).astype(int)
    is_root = tree['p_id'].isna() | (tree['p_id'] == 'null')
    node_type = np.where(is_root, 'Root', np.where(nchild > 0, 'Inner', 'Leaf'))

    out = pd.DataFrame({'id': tree['id'], 'type': node_type})
    out = out.drop_duplicates(subset=['id']).reset_index(drop=True)
    return out