    pr = performance_reviews.copy()
    pr['review_date'] = pd.to_datetime(pr['review_date'])

    # Sort so most recent rows come first per employee (tie-break by review_id)
    pr = pr.sort_values(['employee_id', 'review_date', 'review_id'],
                        ascending=[True, False, False])

    # Rank within employee: 1=most recent, 2=second, 3=third
    pr['rn'] = pr.groupby('employee_id').cumcount() + 1

    # Keep only the last 3 per employee
    last3 = pr[pr['rn'] <= 3]

    # Pivot ratings into columns rn=1,2,3 (latest, middle, earliest among last three)
    wide = last3.pivot(index='employee_id', columns='rn', values='rating')

    # Require all three and strictly increasing: r3 < r2 < r1
    mask = wide.notna().all(axis=1) & (wide[3] < wide[2]) & (wide[2] < wide[1])

    out = (wide.loc[mask]
               .assign(improvement_score=wide[1] - wide[3])  # latest - earliest among last 3
               .reset_index()[['employee_id', 'improvement_score']]
               .merge(employees[['employee_id', 'name']], on='employee_id', how='left')
               .sort_values(['improvement_score', 'name'], ascending=[False, True])
               .reset_index(drop=True))

    return out[['employee_id', 'name', 'improvement_score']]