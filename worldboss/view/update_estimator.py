from django.shortcuts import render, redirect
from django.urls import reverse
from worldboss.models import Estimated, Spawns
from django.utils import timezone
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import datetime
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
import pytz


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

    boss_names = data['boss_name'].unique().tolist()
    boss_name_to_int = {boss_name: i for i, boss_name in enumerate(boss_names)}
    int_to_boss_name = {i: boss_name for boss_name, i in boss_name_to_int.items()}

    # Convert the data to numerical format
    numerical_data = []
    for _, row in data.iterrows():
        boss_name = row['boss_name']
        if boss_name in boss_name_to_int:
            numerical_data.append([boss_name_to_int[boss_name], row['location'], row['datetime']])


    # Split the data into input (X) and output (y) sequences
    sequence_length = 3  # Adjust this value based on the desired sequence length
    X = []
    y = []
    for i in range(len(numerical_data) - sequence_length):
        sequence = numerical_data[i : i + sequence_length]
        X.append([entry[0] for entry in sequence])
        y.append(sequence[-1][0])

    # Convert X and y to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Normalize the input values
    X = X / len(boss_names)

    # Reshape X to match LSTM input shape
    X = np.reshape(X, (X.shape[0], sequence_length, 1))

    # Create the LSTM model
    model = Sequential()
    model.add(LSTM(50, input_shape=(sequence_length, 1)))
    model.add(Dense(len(boss_names), activation='softmax'))

    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(X, y, epochs=50, batch_size=1)

    # Generate a prediction for the next boss_name
    last_sequence = X[-1]
    prediction = model.predict(np.array([last_sequence]))
    predicted_boss_name = int_to_boss_name[np.argmax(prediction)]

    print("Predicted boss_name for the next timestamp:", predicted_boss_name)

    results = [predicted_boss_name]

    # Get unique locations from the 'location' column
    locations = data['location'].unique().tolist()
    location_to_int = {location: i for i, location in enumerate(locations)}
    int_to_location = {i: location for location, i in location_to_int.items()}

    # Convert the data to numerical format
    numerical_data = []
    for _, row in data.iterrows():
        location = row['location']
        if location in location_to_int:
            numerical_data.append([location_to_int[location], row['datetime']])

    # Split the data into input (X) and output (y) sequences
    sequence_length = 3  # Adjust this value based on the desired sequence length
    X = []
    y = []
    for i in range(len(numerical_data) - sequence_length):
        sequence = numerical_data[i : i + sequence_length]
        X.append([entry[0] for entry in sequence])
        y.append(sequence[-1][0])

    # Convert X and y to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Normalize the input values
    X = X / len(locations)

    # Reshape X to match LSTM input shape
    X = np.reshape(X, (X.shape[0], sequence_length, 1))

    # Create the LSTM model
    model = Sequential()
    model.add(LSTM(50, input_shape=(sequence_length, 1)))
    model.add(Dense(len(locations), activation='softmax'))

    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(X, y, epochs=50, batch_size=1)

    # Generate a prediction for the next location
    last_sequence = X[-1]
    prediction = model.predict(np.array([last_sequence]))
    predicted_location = int_to_location[np.argmax(prediction)]

    print("Predicted location for the next timestamp:", predicted_location)


    results.append(predicted_location)


    # Get unique time difference values from the 'time_difference' column
    time_diffs = data['time_difference'].unique().tolist()
    time_diffs = [pd.Timedelta(td) for td in time_diffs]
    time_diff_to_int = {time_diff: i for i, time_diff in enumerate(time_diffs)}
    int_to_time_diff = {i: time_diff for time_diff, i in time_diff_to_int.items()}

    # Convert the data to numerical format
    numerical_data = []
    for _, row in data.iterrows():
        time_diff = pd.Timedelta(row['time_difference'])
        numerical_data.append([time_diff_to_int[time_diff]])

    # Split the data into input (X) and output (y) sequences
    sequence_length = 3  # Adjust this value based on the desired sequence length
    X = []
    y = []
    for i in range(len(numerical_data) - sequence_length):
        sequence = numerical_data[i: i + sequence_length]
        X.append([entry[0] for entry in sequence])
        y.append(sequence[-1][0])

    # Convert X and y to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Normalize the input values
    X = X / len(time_diffs)

    # Reshape X to match LSTM input shape
    X = np.reshape(X, (X.shape[0], sequence_length, 1))

    # Create the LSTM model
    model = Sequential()
    model.add(LSTM(50, input_shape=(sequence_length, 1)))
    model.add(Dense(len(time_diffs), activation='softmax'))

    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    model.fit(X, y, epochs=50, batch_size=1)

    # Generate a prediction for the next time difference
    last_sequence = X[-1]
    prediction = model.predict(np.array([last_sequence]))
    predicted_time_diff = int_to_time_diff[np.argmax(prediction)]

    print("Predicted time difference for the next timestamp:", predicted_time_diff)

    new_spawn_est_time = Spawns.objects.latest('datetime').datetime + predicted_time_diff
    new_spawn_est_time = new_spawn_est_time.astimezone(pytz.timezone('America/New_York'))
    print("Potential New Spawn Time: " + str(new_spawn_est_time))


    results.append(new_spawn_est_time)





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
            # est_datetime=est_datetime,
            est_datetime=results[2],
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

