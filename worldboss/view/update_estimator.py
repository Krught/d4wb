from django.shortcuts import render, redirect
from django.urls import reverse
from worldboss.models import Estimated, Spawns
from django.utils import timezone
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import datetime


def update_estimator(request=""):
    # Delete all existing data in the Estimated model
    Estimated.objects.all().delete()

    # Import data from the Spawns model and order by datetime
    spawns = Spawns.objects.order_by('datetime')

    # Create a DataFrame to hold the data
    data = pd.DataFrame(list(spawns.values()))
    # print(data)
    
   

    # Calculate time differences
    data['time_difference'] = data['datetime'].diff()

    # Filter out entries with time differences over 9 hours or under 3 hours
    data = data[(data['time_difference'] >= pd.Timedelta(hours=3)) & (data['time_difference'] <= pd.Timedelta(hours=9))]



    X = data[['boss_name', 'datetime', 'location']]
    test = ['boss_name', 'location', 'datetime']
    results = []
    for i in test:
        y = data[i]  # Assuming 'boss_name' is the column containing the boss names
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        vectorizer = CountVectorizer()

        if i == 'datetime':
            y_train = y[:-1].apply(lambda x: x.timestamp())
            X_train = vectorizer.fit_transform(X[:-1].apply(lambda x: ' '.join(str(i) for i in x), axis=1))
            X_test = vectorizer.transform(X[-1:].apply(lambda x: ' '.join(str(i) for i in x), axis=1))
        else:
            y_train = y[:-1]
            X_train = vectorizer.fit_transform(X[:-1].apply(lambda x: ' '.join(str(i) for i in x), axis=1))
            X_test = vectorizer.transform(X[-1:].apply(lambda x: ' '.join(str(i) for i in x), axis=1))

        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)

        latest_spawn = Spawns.objects.latest('datetime')
        new_data = pd.DataFrame({'boss_name': [latest_spawn.boss_name], 'datetime': [latest_spawn.datetime], 'location': [latest_spawn.location]})

        new_data_vectorized = vectorizer.transform(new_data.apply(lambda x: ' '.join(str(i) for i in x), axis=1))
        predictions = classifier.predict(new_data_vectorized)

        predictions_df = pd.DataFrame({'boss_name_prediction': predictions, 'datetime': new_data['datetime'], 'location': new_data['location']})
        if i == 'datetime':
            predictions_df.boss_name_prediction = pd.to_datetime(predictions_df.boss_name_prediction, unit='s')
            test_x = predictions_df.boss_name_prediction.to_string(index=False)
        else:
            test_x = predictions_df.boss_name_prediction.to_string(index=False)
        results.append(test_x)
    # print(results)

  

    # Calculate average, minimum, and maximum time differences
    average_diff = data['time_difference'].mean()
    min_diff = data['time_difference'].min()
    max_diff = data['time_difference'].max()

    # Get the most recent spawn
    most_recent_spawn = Spawns.objects.latest('datetime')

    # Calculate the estimated, minimum, and maximum datetimes
    est_datetime = most_recent_spawn.datetime + average_diff
    min_datetime = most_recent_spawn.datetime + min_diff
    max_datetime = most_recent_spawn.datetime + max_diff

    new_item = Estimated(
            boss_name= results[0],
            est_datetime=est_datetime,
            min_datetime=min_datetime,
            max_datetime=max_datetime,
            location= results[1]
        )
    # print(new_item.est_datetime)
    new_item.save()


    # # New item was created, perform your desired actions here
    # print("A new item was added to Estimated model")


    if hasattr(request, 'method'):
        if request.method == 'POST':    
            return redirect(reverse('admin:index'))

