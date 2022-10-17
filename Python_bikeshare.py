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
    print('\n Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('\n Please enter the name of city which would you like to analyse?(chicago, new york city, washington)\n').strip().lower()
        if city in CITY_DATA:
            break
        else:
            print('\n You have entered wrong city name.\n')
            
    # TO DO:Disply raw data of selectd city.
    count=0;
    while True:
        raw_data=input('Do you want to see 5 lines of raw data of selected city(Yes or No):\n').strip().lower()
        if raw_data == 'yes':
            df=pd.read_csv(CITY_DATA[city])
            print(df.iloc[count:count+5])
            count=count+5
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('\n Please enter the month of the year which would you like to see?(All, Jan, Feb, Mar, Apr, May, Jun)\n').strip().lower()
        if month=='all' or month == 'jan' or month == 'feb' or month == 'mar' or month =='apr' or month =='may' or month =='jun':
            break
        else: 
            print('\nYou have entered wrong month.\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('\nPlease enter the day of week which would you like to see?(All, Monday, Tuesday, Wednesday, Thurday, Friday, Satday, Sunday)\n').strip().lower()
        if day=='all' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday':
            break
        else:
            print('\nYou have entered wrong day.\n')

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
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
       df = df[df['day_of_week']== day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months_dict = {1:'January', 2:'February', 3: 'March', 4 : 'April', 5:'May', 6:'June'}
    most_common_month = df['month'].mode()[0]
    if most_common_month in months_dict.keys():
       print('Most common month:',months_dict[most_common_month])
     
    # TO DO: display the most common day of week
    print('Most common Day of Week is:', df['day_of_week'].value_counts().nlargest(1))
    
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    print('Most Common Start hour is:', df['hour'].value_counts().nlargest(1)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used Start station :',df['Start Station'].value_counts().nlargest(1))

    # TO DO: display most commonly used end station
    print('Most commonly used End station :',df['End Station'].value_counts().nlargest(1))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start Station and End Station:\n', df.groupby(['Start Station','End Station']).size().nlargest(1))
    
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time (in seconds):', (df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean Travel Time (in seconds):', (df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Number of users:',df['User Type'].count())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Number of Male and females:',df['Gender'].count())
        print('Number of Male users:', sum(df['Gender']=='Male'))
        print('Number of Female users:',sum(df['Gender']=='Female'))
    else:
        print('No Gender information is available in the data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\n\nMost Earliest Year of Birth:',int(min(df['Birth Year'])))
        print('Most Recent Year of Birth:',int(max(df['Birth Year'])))
        print('Most Common Year of Birth:', int(df['Birth Year'].mode()[0]))
    else:
        print('No birth year information is available in the data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    

def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
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

