import csv
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
day.title())

def get_filters():

    #(str) city - name of the city to analyze
    #(str) month - name of the month to filter by, or "all" to apply no month filter
    #(str) day - name of the day of week to filter by, or "all" to apply no day filter

    monthlist = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    daylist = ['monday','thuesday','wednesday','thursday','friday','satureday','sunday','all']

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('\nWhat are the city you want to explore? (Chicago, New York City, Washington): ')).lower()
            if city in CITY_DATA.keys():
                break
            else:
                print('Unvalid city. Please choose between: Chicago, New York City, Washington')
        except ValueError:
            print('Maybe there is a typo. Please choose between: Chicago, New York City, Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('\nWhat month you want to explore? ("all" for no restriction): ')).lower()
            if month in monthlist:
                break
            else:
                print('Unvalid month. Please choose between: ', monthlist)
        except ValueError:
            print('Maybe there is a typo. Please choose between: ', monthlist)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('\nWhat day of the week you want to explore? ("all" for no restriction): ')).lower()
            if day in daylist:
                break
            else:
                print('Unvalid day. Please choose between: ', daylist)
        except ValueError:
            print('Maybe there is a typo. Please choose between: ', daylist)



    print('\n')
    print('-'*40)
    print('We are now exporer following data:\nCity: {}\nMonth: {}\nDay: {}'.format(city.title(), month.title(), day.title()))
    print('-'*40)
    return city, month, day
#-------------------------------------------------------------------

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

    # load data file into pandas dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
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
#-------------------------------------------------------------------

def time_stats(df, month, day): #time_stats - ts
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        ts_month = df['month'].mode()[0]
        print('\n- Most popular rental month: ', ts_month)

    # TO DO: display the most common day of week
    if day == 'all':
        ts_day = df['day_of_week'].mode()[0]
        ts_dcount = df['day_of_week'].value_counts()[0]
        print('\n- Most popular rental day: ', ts_day, 'with', ts_dcount, 'rentals')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    ts_hour = df['hour'].mode()[0]
    print('\n- Most popular rental hour: ', ts_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------------------------------

def station_stats(df): #station_stats - ss
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss_start = df['Start Station'].mode()[0]
    print('\n- Most popular start station of rental: ', ss_start)

    # TO DO: display most commonly used end station
    ss_end = df['End Station'].mode()[0]
    print('\n- Most popular end station of rental: ', ss_start)

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = (df['Start Station']+' -> '+df['End Station'])
    ss_route = df['Route'].mode()[0]
    print('\n- Most popular route of rental: ', ss_route)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------------------------------

def trip_duration_stats(df): #duration_stats - ds
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ds_totalhour = int(df['Trip Duration'].sum() / 3600)
    ds_totalday = int(df['Trip Duration'].sum() / 86400)
    print('\n- The total time of rental is: ',ds_totalhour,' hours which are about ',ds_totalday,' days')

    # TO DO: display mean travel time
    ds_mean = int(df['Trip Duration'].mean() / 60)
    print('\n- The mean travel time of rental is: ',ds_mean,' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------------------------------

def user_stats(df): #user_stats - us
    """Displays statistics on bikeshare users."""

    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        us_user = df['User Type'].value_counts().to_string()
        print('\nThe distribution of our user types is:')
        print(us_user)

        # TO DO: Display counts of gender
        us_gender = df['Gender'].value_counts().to_string()
        print('\nThe distribution by gender of our customers is:')
        print(us_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        us_birthmin = int(df['Birth Year'].min())
        us_birthmax = int(df['Birth Year'].max())
        us_birthcom = int(df['Birth Year'].mode()[0])

        print('\nFacing the year of birth of our customers:')
        print('Year of birth of our oldest customers: ',us_birthmin)
        print('Year of birth of our youngest customers: ',us_birthmax)
        print('Most common year of birth of our customers: ',us_birthcom)

    except:
        print('\n>>> Some corrupt data causes an error. Not all user statistic values are available with the selected filter. <<<')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-------------------------------------------------------------------

def rawdata(df): #view raw data from csv file

    i = 0
    req = 'the'
    while True:
        try:
            request = input('\nDo you want to view {} raw data from your selection? ("yes" or "no"): ' .format(req))
            if request.lower() == 'yes':
                print(df[i:i+5])
                i += 6
                req = 'more'
            elif request == 'no':
                break
            else:
                print('Please type "yes" or "no"')
        except:
            print('Something went wrong')
#-------------------------------------------------------------------

def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? ("yes" or "no"): ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
