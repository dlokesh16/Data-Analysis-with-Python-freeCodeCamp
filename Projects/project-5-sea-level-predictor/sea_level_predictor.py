import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x = np.arange(1880, 2050, step = 1, dtype = int)
    y = reg.slope * x + reg.intercept
    
    plt.plot(x, y, 'r')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000].copy()
    reg_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    x_2000 = np.arange(2000, 2050, step = 1, dtype = int)
    y_2000 = reg_2000.slope * x_2000 + reg_2000.intercept

    plt.plot(x_2000, y_2000, 'g')
  
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()