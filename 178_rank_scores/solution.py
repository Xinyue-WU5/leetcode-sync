import pandas as pd 

def order_scores(scores: pd.DataFrame) -> pd.DataFrame: 
    sorted_score = scores.sort_values(by='score',ascending=False) 
    sorted_score['rank'] = sorted_score['score'].rank(method='dense', ascending=False) 

    return pd.DataFrame({ 
        'score': sorted_score['score'], 
        'rank': sorted_score['rank'] 
    }) 