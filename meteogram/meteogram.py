"""Helps obtain, analyze, and plot surface observations as a meteogram."""

import datetime
import urllib
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


register_matplotlib_converters()


def degF_to_degC(degF):
    """
    Convert degF to degC.

    Parameters
    ----------
    degF : float
        Temperature in Fahrenheit.

    Returns
    -------
    Temperature in Celsius

    """
    return (degF - 32) * (5 / 9)

def current_utc_time():
    """
    Return the current UTC date and time.

    Returns
    -------
    datetime.datetime: Current UTC date and time

    """
    return datetime.datetime.utcnow()


def build_asos_request_url(station, start_date, end_date):
    """
    Create a URL to request ASOS data from the Iowa State archive.

    Parameters
    ----------
    station: str
        Station identifier
    start_date: datetime.datetime
        Starting time of data to be obtained
    end_data: datetime.datetime
        Ending time of data to be obtained

    Returns
    -------
    str: URL of the data
    """

    url_str = (f'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D='
               f'{station}&tz=UTC&year1={start_date:%Y}&month1={start_date:%m}&day1'
               f'={start_date:%d}&hour1={start_date:%H}&minute1={start_date:%M}&year2={end_date:%Y}&month2='
               f'{end_date:%m}&day2={end_date:%d}&hour2={end_date:%H}&minute2={end_date:%M}&vars'
               f'%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt'
               f'&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    return url_str


def download_asos_data(url):
    """
    Download ASOS data from the Iowa State archive.

    Parameters
    ----------
    url: str
        URL of the data

    Returns
    -------
    pandas.DataFrame: Observation Data
    """
    # Data at the URL are CSV format
    df =  pd.read_csv(url)

    # There is a trailing comma, so remove the last column
    df.drop(columns=df.columns[-1], inplace=True)

    # Rename the columns to more useful names
    df.columns = ['station_id', 'station_name', 'latitude_deg',
                  'longitude_deg', 'UTC', 'temperature_degF',
                  'dewpoint_degF', 'wind_speed_knots',
                  'wind_direction_degrees']

    # Parse the valid times into real datetimes
    df['UTC'] = pd.to_datetime(df['UTC'])
    return df


def plot_meteogram(df):
    """
    Plot a meteogram with matplotlib.

    Parameters
    ----------
    df: pandas.DataFrame
        Dataframe of ASOS data

    Returns
    -------
    TODO
    """
    fig = plt.figure(figsize=(10, 5))
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    ax2b = ax2.twinx()

    temperature_ymin = min([df['temperature_degF'].min(), df['dewpoint_degF'].min()]) - 5
    temperature_ymax = max([df['temperature_degF'].max(), df['dewpoint_degF'].max()]) + 5

    ax1.fill_between(df['UTC'], df['temperature_degF'], temperature_ymin, color='tab:red')
    ax1.fill_between(df['UTC'], df['dewpoint_degF'], temperature_ymin, color='tab:green')
    ax2.fill_between(df['UTC'], df['wind_speed_knots'], df['wind_speed_knots'].min() - 5, color='tab:blue')
    ax2b.scatter(df['UTC'], df['wind_direction_degrees'], edgecolor='tab:olive', color='None')

    # Set limits
    ax1.set_xlim(df['UTC'].min(), df['UTC'].max())
    ax1.set_ylim(temperature_ymin, temperature_ymax)
    ax2.set_ylim(df['wind_speed_knots'].min() - 5, df['wind_speed_knots'].max() + 5)
    ax2b.set_ylim(-10, 370)  # Wind Direction with a bit of padding

    # Add some labels
    label_fontsize = 14
    ax2.set_xlabel('Observation Time', fontsize=label_fontsize)
    ax1.set_ylabel(u'\N{DEGREE SIGN}F', fontsize=label_fontsize)
    ax2.set_ylabel('Knots', fontsize=label_fontsize)
    ax2b.set_ylabel('Degrees', fontsize=label_fontsize)

    return fig, ax1, ax2
