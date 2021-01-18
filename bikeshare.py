import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input( ' Write a city name: Chicago, New York City or Washington! : ').lower()
        if city not in city_data:
             print('\n Invild answer\n')
             continue
        else:
             break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a specific month or choose all:').lower()
        if month not in  ['january' , 'feburary' , 'march' , 'april' , 'may' , 'june','all']:
             print('please pick the listed months or choose all')
             continue
        else:
             break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please put a specific day or choose all:').lower()
        if day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            print('please pick the correct name or choose all')
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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    if day != 'all':

        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print(f'the most common month is {common_month}')

    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    common_day=df['day_of_week'].mode()[0]
    print(f'the most common day is : {common_day}')
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print(f'the most common hour is :{common_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df["Start Station"].mode()[0]
    print(f'the most common start station is : {common_start}')

    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print(f'the most common end station is : {common_end}')
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(f'the most frequent combination of start station and end station trip is:{common_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(f'total travel time is :{total_travel} seconds')

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(f'the mean travel time is :{mean_travel} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_types = df['User Type'].value_counts()
    print(f'number of user type is {User_types}')

    #f 'Gender' in df and 'Birth Year' in df:
        #rint(f"Genders  of user types {df['Gender'].value_counts()}")
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(f'the gender is {gender}')
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = int(df['Birth_Year'].min())
        print(f'earliest birthdate is {earliest}')
        recent = int(df['Birth_Year'].max())
        print(f'most recent birthdate is {recent}')
        common_birth = int(df['Birth Year'].mode()[0])
        print(f'the most common birthdate is{common_birth}')
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    view_display = False
    if view_data == 'yes':
        view_display= True
    while (view_display):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input('Do you wish to continue? :  ').lower()
        if view_data =='yes':
           view_display = True
        else:
           view_display = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
