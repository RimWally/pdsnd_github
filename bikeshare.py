@@ -143,7 +143,8 @@ def load_data(city, month, day):
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]

    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df
@@ -153,6 +154,8 @@ def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #temporary_df = pd.read_csv(city)
    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]