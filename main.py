from read_file import read_excel
import pandas

def main():
    dataframe = read_excel()

    """Get all the unique Destination spots"""
    unique_destination_spots = dataframe['Destination'].unique()
    unique_destination_spots = list(unique_destination_spots)
    
    final_df = []

    for destination in unique_destination_spots:

        """Get the rows of the dataframe that match the destination key, then get the column of the AveragePrice_y, get the median of that column, then directly get the value from the Series"""
        median = dataframe[dataframe['Destination'] == destination][['AveragePrice_y']].median()['AveragePrice_y']
        tukio_price = dataframe[dataframe['Destination'] == destination][['AveragePrice_x']].iloc[0]['AveragePrice_x']
        
        below_median = median * .85
        after_median = median * 1.15

        result = ""
        if tukio_price > after_median:
            result = "We are charging too much, we are above the median by at least 15%"
        elif tukio_price < below_median:
            result = "We are charging too little, we are below the median by at least 15%"
        else:
            result = "We are charging within the median of our competitors"

        final_df.append([destination, tukio_price, median, result])
    
    final_df = pandas.DataFrame(final_df, columns=["Destination", "Tukio Price", "Median Price", "Result"])
    final_df.to_csv("PricingResults.csv")        

if __name__ == "__main__":
    main()
