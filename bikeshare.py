import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\n Please provide your choice of cities from Chicago, New York City and Washington to view bikeshare data\n')
    city = city.lower()
    while True:
        if city == 'chicago':
            print('Your choice of city is Chicago\n')
            break
        elif city == 'new york city':
            print('Your choice of city is New York City\n')
            break
        elif city == 'washington':
            print('Your choice of city is Washington\n')
            break
        else:
            print("Provide valid response\n")
            city = input('\n Please provide your choice of cities from Chicago, New York City and Washington to view bikeshare data\n')
            city = city.lower()

    #user input for month (all, january, february, ... , june)
    month = input("Choose from: January, February, March, April, May, June ;type 'all' if you do not have any preference?\n")
    month = month.lower()
    while True:
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Invalid Response!! Try again.\n")
            continue
        else:
            break
    #user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose day from Monday,Tuesday, Wednesday, Thursday, Friday , Saturday and Sunday or 'all'\n")
    day = day.lower()
    while True:
        if day not in ('monday','tuesday', 'wednesday','thursday', 'friday', 'saturday','sunday', 'all'):
            print("Invalid Response!! Try different one.\n")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe //from pratice 3
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracts month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #the most common month
    popular_month = df['month'].mode()[0]
    print('Popular month is {}. \n'.format(popular_month))


    # the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Popular day of the week is {}. \n'.format(popular_day))

    #the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Popular hour in day is {}. \n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Common Start Station is {}.\n '.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Common End Station is {}.\n '.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    comb_station = df.groupby(['Start Station', 'End Station']).count()
    print('Common combination of start station and end station trip:', start_station, " and ", end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time :{}.\n'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average travel time :{}.\n'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    gender_types = df['Gender'].value_counts()
    print('\nGender Types:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth

    Earliest_Year = df['Birth Year'].min()
    print('\nEarliest Year:', Earliest_Year)

    Most_Recent_Year = df['Birth Year'].max()
    print('\nMost Recent Year:', Most_Recent_Year)

    Most_Common_Year = df['Birth Year'].value_counts().idxmax()
    print('\nMost Common Year:', Most_Common_Year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

	main()
