#modified

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('-'*40)
    cities = ['chicago','new york city' , 'washington']
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
    
    while True:
        city = input('\nPlease enter the city name: \n')
        city=city.lower()
        if city in cities:
            break
        else:
            print("Please enter 3 of these cities  new york city - chicago - washington")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month=input('\nPlease enter the month\n')
        month=month.lower()
        if month in months:
            break
        else:
            print("Your input is not a relevant month. ")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day=input('\nPlease enter the day of week: \n')
        day=day.lower()
        if day in days:
            break
        else:
            print("Your input is not a relevant day. ")
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
    
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
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

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print('Most Popular Month:',most_month)
    
    # TO DO: display the most common day of week
    most_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Week:',most_day_of_week)
    
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour =df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station:',most_start_station)

    # TO DO: display most commonly used end station

    most_stop_station = df['End Station'].mode()[0]
    print('most commonly used stop  station:',most_stop_station)
    # TO DO: display most frequent combination of start station and end station trip
    
    df['Start_Stop'] = df['Start Station'] +  " - "  + df['End Station']
    
    most_start_stop_station = df['Start_Stop'].mode()[0]
    print('most frequent combination of start station and end station trip:',most_start_stop_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('total travel time is :', total_duration)

    # TO DO: display mean travel time
    avarage_duration = df['Trip Duration'].mean()
    print('Avarage travel time is :', avarage_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types=df['User Type'].nunique()
    print('Number of user types are : ', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender_types=df['Gender'].nunique()
        print('Number of gender types are : ', gender_types)
    except KeyError:
        print("Birth information is not accessible for Washington")
        
        
   
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        date_min=df['Birth Year'].min()
        date_max=df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest Year of Birth is : ',date_min )
        print('Most Recent Year of Birth is : ',date_max )
        print('Most Common Year of Birth is : ',common_year )
    except KeyError:
        print("Birth information is not accessible for Washington")   
        
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def row_data(df):
    i=0
    j=6
    while True:
        showdata = input ('\nWould you like to see 5 examples? Enter yes or no.\n')
        if showdata.lower()!='yes':
            break
        print(df.iloc[i:j])
        i=j
        j=j+5
        
  
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()