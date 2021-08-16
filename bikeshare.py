@@ -143,7 +143,8 @@ def load_data(city, month, day):
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]

    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df