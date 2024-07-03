import requests
import csv

class CrimeDataFetcher:
    """
    A class to fetch and handle crime data from a given URL.

    Methods
    -------
    fetch_crime_data(url='https://data.lacity.org/api/views/2nrs-mtv8/rows.json?accessType=DOWNLOAD')
        Fetches crime data from the provided URL and returns column names, data, and the number of rows.
    
    lists_to_csv(data, filename, collist)
        Converts a list of lists to a CSV file, including headers.
    """

    @staticmethod
    def fetch_crime_data(url):
        """
        Fetch crime data from the provided URL.

        This method requests access to the "Crime Data from 2020 to Present" from
        the USA data gov website and processes it to extract column names and data.

        Args:
            url (str): The URL to fetch the crime data from. Defaults to the provided URL.

        Returns:
            tuple: A tuple containing a list of column names, the data, and the number of data rows.
                   - collist (list of str): List of column names.
                   - data (list): List of data rows.
                   - num_rows (int): Number of data rows.
        """
        response = requests.get(url)

        # Get column names
        collist = [col['name'] for col in response.json()["meta"]["view"]["columns"]]

        # Save data
        data = response.json()['data']

        # Number of data rows
        num_rows = len(data)

        return collist, data, num_rows

    @staticmethod
    def lists_to_csv(data, filename, collist):
        """
        Converts a list of lists to a CSV file, including headers.

        Parameters:
        data (list of lists): The data to write to the CSV file.
        filename (str): The name of the CSV file to write to.
        collist (list): The list of column headers.
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(collist)  # Write the headers first
            writer.writerows(data)    # Write the data
