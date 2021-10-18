import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """ detrimination of city """
    print("Hello! Let's explore some US bikeshare data!\n")
    cities=['chicago','new york city','washington']
    while True:
         city=input ("which city would you like to see data about bikeshare about?\nchoose from following list\n      [chicago,new york city,washington]\n:")
         if city.lower() in cities:
             return city.lower()
             break
         else:
             print("your city is not inculeded in the list ,please choose city from given list")
        
    
def get_filters():
    '''detrimination of filter base'''
    while True:
        choice= input("do you want to filter data based on month or day or both or not at all? type [not] for not at all")
        if choice.lower() =="month" :
            day="all"
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']
            while True :
                month=input("name of the month to filter by, or [all] to apply no month filter[ex:january] :")
                if month.lower() in months or month.lower()=="all":
                    break
                else:
                    print("wrong month,enter correct month name")  
            break
        elif choice.lower() == "day" :
            month="all"
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            while True:
                day=input("name of the day of week to filter by, or [all] to apply no day filter[ex:sunday]:")
                if day.lower() in days or day.lower()=="all":
                    break
                else:
                    print("wrong day,enter correct dayname")
            break
        elif choice.lower() == "not" :
            month="all"
            day="all"
            break
        elif choice.lower()=="both":
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            while True :
                month=input("name of the month to filter by, or [all] to apply no month filter[ex:january] :")
                if month.lower() in months or month.lower()=="all":
                    break
                else:
                    print("wrong month,enter correct month name")  
            
            while True:
                day=input("name of the day of week to filter by, or [all] to apply no day filter[ex:sunday]:")
                if day.lower() in days or day.lower()=="all":
                    break
                else:
                    print("wrong day,enter correct dayname")
            break        
            
        else :
            print("you don't give us information about fileration base")
       
    print('-'*40)
    return month.lower(), day.lower()

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if (month.lower())!="all":
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
       
    else:
        popular_month =df['month'].value_counts().idxmax()
        print('Most Frequent month :', popular_month)
    if (day.lower())!="all":
        df = df[df['day_of_week'] == day.title()]
    else:
        popular_day =df['day_of_week'].value_counts().idxmax()
        print('Most Frequent day :', popular_day)
    df['hour'] =df['Start Time'].dt.hour
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_hour =df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """displays raw data """
    choice=input("do you want to display the data [yes or no]?")
    i=0
    x=5
    while choice.lower()=="yes" :
        print(df.iloc[i:x,:])
        i+=5
        x+=5
        choice=input("do you want to continue in displaying data[yes or no]")
      
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    print("the popular start station :{}".format(popular_start_station))
    popular_end_station = df['End Station'].mode()[0]
    print("the popular end station :{}".format(popular_end_station))
    most_frequent_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print("the most frequent trip :{}".format(most_frequent_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    Total_duration = df['Trip Duration'].sum()
    print("total duration :{}".format(Total_duration))
    average_duration = df['Trip Duration'].mean()
    print("average duration :{}".format(average_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    User_Type=df['User Type'].value_counts()
    print("user type:\n{}".format(User_Type))
    try:
        User_gender=df['Gender'].value_counts()
        print("user gender:\n{}".format(User_gender))
    except:
        print("there's no gender data")
    try:
        common_birth_year = df['Birth Year'].mode()[0]
        print("most common year of birth:\n{}".format(common_birth_year))
    except:
        print("there's no birth year data")
    try:
        earliest=df['Birth Year'].min()
        print("the earliest of year of birth:\n{}".format(earliest))
    except:
        print("there's no birth year data")
    try:
        recent=df['Birth Year'].max()
        print("most recent year of birth:\n{}".format(recent))
    except:
        print("there's no birth year data")
        
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    while True:
        city=get_city()
        month, day = get_filters()
        while True:
            try:
                df = load_data(city, month, day)
                time_stats(df) 
                break
            except:
                new_month=input("enter new month , the data of entred month not given")
                month=new_month.lower()
               
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
