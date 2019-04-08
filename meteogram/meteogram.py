"""Helps obtain, analyze, and plot surface observations as a meteogram."""

import datetime
import urllib
import numpy as np
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


def potential_temperature(pressure, temperature):
    """Calculate the potential temperature.

    Uses the Poisson equation to calculation the potential temperature
    given `pressure` and `temperature`.

    Parameters
    ----------
    pressure
        The total atmospheric pressure
    temperature
        The temperature in kelvin

    Returns
    -------
    The potential temperature corresponding to the temperature and
    pressure.

    Notes
    -----
    Formula:

    .. math:: \Theta = T (P_0 / P)^\kappa

    For inputs of 800 hPa and 273 Kelvin, output should be 290.96 K

    """
    return temperature / exner_function(pressure)


def exner_function(pressure, reference_pressure=1000):
    r"""Calculate the Exner function.
    .. math:: \Pi = \left( \frac{p}{p_0} \right)^\kappa
    This can be used to calculate potential temperature from temperature (and visa-versa),
    since
    .. math:: \Pi = \frac{T}{\theta}

    Parameters
    ----------
    pressure
        The total atmospheric pressure
    reference_pressure : `pint.Quantity`, optional
        The reference pressure against which to calculate the Exner function, defaults to 1000 hPa

    Returns
    -------
    The value of the Exner function at the given pressure.

    """
    return (pressure / reference_pressure)**0.28562982892500527


def build_asos_request_url(station, start_date=None, end_date=None):
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

    # If there is no ending date specified, use the current date and time
    if end_date is None:
        end_date = current_utc_time()

    # If there is no starting date specified, use 24 hours before the ending date and time
    if start_date is None:
        start_date = end_date - datetime.timedelta(hours=24)

    # Make sure the starting and ending dates are not reversed
    if start_date > end_date:
        raise ValueError('Unknown option for direction: {0}'.format(str(direction)))

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


def plot_meteogram(df, direction_markers=False):
    """
    Plot a meteogram with matplotlib.

    Parameters
    ----------
    df: pandas.DataFrame
        Dataframe of ASOS data

    Returns
    -------
    matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot,
    matplotlib.axes._subplots.AxesSubplot, matplotlib.axes._subplots.AxesSubplot
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

    # Add direction lines if requested
    if direction_markers:
        for value_degrees in [0, 90, 180, 270]:
            ax2b.axhline(y=value_degrees, color='k', linestyle='--', linewidth=0.25)

    return fig, ax1, ax2, ax2b


def wind_components(speed, direction):
    """
    Calculate the U, V wind vector components from the speed and direction.

    Parameters
    ----------
    speed : array_like
        The wind speed (magnitude)
    wdir : array_like
        The wind direction, specified as the direction from which the wind is
        blowing (0-360 degrees), with 360 degrees being North.

    Returns
    -------
    u, v : tuple of array_like
        The wind components in the X (East-West) and Y (North-South)
        directions, respectively.

    """
    direction = np.radians(direction)
    u = -speed * np.sin(direction)
    v = -speed * np.cos(direction)
    return u, v
