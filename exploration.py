import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from numpy.polynomial.polynomial import polyfit

def main():
    rookie_df = pd.read_csv("NBADrafts.csv")
    #a = rookie_df.iloc[:,12:].values
    #b = rookie_df.iloc[:,21:].values
    #c, m = polyfit(a, b, 1)

    plt.scatter(rookie_df.Assists,rookie_df.Win_SharesS_48,s=10)
    plt.xlabel('Assists per game')
    plt.ylabel('Win Shares per 48 min')
    plt.title('2016 NBA Draft Class\' College Careers - Assists vs Win Shares')
    #plt.plot(a, c + m * a, '-')
    plt.show()


    return 0

if __name__ == '__main__':
    main()
