import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'c': r'C:\Users\asmaa\OneDrive\Desktop\Udacity\test.py\.vscode\chicago.csv',
              'n': r'C:\Users\asmaa\OneDrive\Desktop\Udacity\test.py\.vscode\new_york_city.csv',
              'w': r'C:\Users\asmaa\OneDrive\Desktop\Udacity\test.py\.vscode\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    name = input('\nCan you enter your name please: ')
    while True:
        print('\nHello! {} Let\'s explore some US bikeshare data!'.format(name).lower().title())
        break

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nTo view bikeshare data , type:\n (c) for chicago\n (n) for new york city \n (w) for washington\n\n ').lower()
    # validate the city input
    while city not in ['c' , 'n' , 'w']:
        print('\nError: incorrect value inputted, please enter (c) or (n) or (w).\n')
        city = input('To view bikeshare data , type:\n (c) for chicago\n (n) for new york city \n (w) for washington\n\n ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)    
    months = ['january', 'february', 'march', 'april', 'may', 'june']    
    #validate the month input
    for month in months:
        month = input("\nTo filter data by month , please type the month or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n").lower() 
        if month != 'all' and month not in months:
            print('\nError: incorrect value inputted, Please enter month from january to june or all to not filter.')
        else:
            break # to break the for loop 
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # validate the day input
    days = ['saturday', 'sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    for day in days:
        day = input('\nTo filter the data by day, please type the day or all for not filtering by day:\n-Saturday\n-Sunday\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-All\n\n').lower()
        if day != 'all' and day not in days:
            print('\nError: incorrect value inputted, please enter day of week or all to not filter.')
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert start time column into datetime so after that we can add month, day and hour column from it.

    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month # add month column form start time 
    df['day_of_week'] = df['Start Time'].dt.day_name() # weekday_name is updated by day_name in pandas
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    # filter by month to show the month the user chose
        df = df[df['month'] == month]
    

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to show the day the user chose
        df = df[df['day_of_week'] == day.title()]   
        
    return df
   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0] 
    month_name = calendar.month_name[common_month] # used calender to convert number of month into the name of month
    print('The most common month is :', month_name)
        

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day is :', common_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour # add an hour column to know the most common hour 
    common_hour = df['Hour'].mode()[0]
    print('\nThe most common hour is :', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is : ', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is : ', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' _ ' + df['End Station'] # first lets add a column that combine the start with the end and split them with (_) 
    most_start_and_end = df['Station Combination'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip is : ', most_start_and_end)                                                                            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_time = df['Trip Duration'].sum()
    print('Total travel time :   in seconds' ,'(',total_trip_time,')',', in minutes','(',total_trip_time/60,')', ', in hours' ,'(',total_trip_time/3600,')','.')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean travel time :   in seconds' ,'(',mean_time,')',', in minutes','(',mean_time/60,')',', in hours' ,'(',mean_time/3600,')','.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user type:\n',user_types)

    # Display counts of gender and display earliest, most recent, and most common year of birth

    if 'Gender' in df and 'Birth Year' in df :  # I do this step bc washington does not have a gender column and birth year column
        
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender_counts)  
     
        earliest_birth = df['Birth Year'].min()
        print('\nThe earliest year of birth is : ', earliest_birth)

        most_recent_birth = df['Birth Year'].max()
        print('\nThe most recent year of birth is : ', most_recent_birth)

        most_common_year = df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is : ', most_common_year)
    else:
        print('\nUnfortunately gender and birth year does not appear in washington dataframe if you want to see the gender and birth year stats please restart and then choose another city.') 
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):

    print('\nRaw data is available to check \n')
    
    display_raw = input('To view the first 5 rows in the available raw data please enter [yes / no]: \n').lower()
    
    while display_raw == 'yes':
        try:
             for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input('\nTo view more 5 rows in the available raw data please enter [yes / no]: \n').lower() # it keeps showing 5 rows if the user say yes until the user say no to break the loop.
                if display_raw != 'yes':
                    print('\nThank you I wish you enjoyed')
                    break #breaking out of the for loop
             break
        except KeyboardInterrupt:
             print('Thank you')


def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main() 
