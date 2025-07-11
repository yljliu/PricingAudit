import pandas

def read_excel():
    dictionary = pandas.read_excel("Pricing.xlsx", sheet_name=None)
    df = (pandas.merge(left=dictionary["Tukio"], right=dictionary["Safari Booking"], how="inner", on=["Destination"]))
    return df
