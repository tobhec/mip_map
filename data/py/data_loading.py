import requests
import xml.etree.ElementTree as ET
import pandas as pd


def construct_url(base, dataset, dim_list, countries, start_year = "", end_year = ""):
    """ Constructs a URL based on: 
    - a base URL
    - a Eurostat dataset code
    - a list with dimensions
    - a list with countries
    """

    # Combine dimensions into one string
    dims = ""
    for dim in dim_list:
        dims = dims + dim + "."

    # Combine countries into one string
    geo = ""
    for cc in countries:
        geo = geo + cc + "+"

    # Combine years into one string
    params = []
    if start_year:
        params.append(f"startPeriod={start_year}")
    if end_year:
        params.append(f"endPeriod={end_year}")
    years = "?" + "&".join(params) if params else ""

    # Combine into the full URL
    full_url = f"{base}/{dataset}/{dims}{geo[:-1]}{years}"
    return full_url


def get_df(url):
    """ Calls an API GET request and converts the response into a pandas data.frame"""

    try:
        # Get API response
        response = requests.get(url)
        if response.status_code == 200:
            xml_data = ET.fromstring(response.content)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return pd.DataFrame()  # Return empty DataFrame on failure
    except requests.RequestException as e:
        print(f"Error: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

    # Go through the series and extract data for each observation, depending on where the are nested
    records = []
    for series in xml_data.findall(".//g:Series", namespaces={"g": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic"}):
        # Get the countries
        geo = series.find(".//g:Value[@id='geo']", namespaces = {"g": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic"}).attrib['value']
        # Go into each observation of each series
        for obs in series.findall(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}Obs"):
            # Get years
            year = obs.find("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsDimension").attrib['value']
            # Get values
            value = obs.find("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsValue").attrib['value']
            # Add geo, years and values to the dataset
            records.append({"Year": int(year), "Country": geo, "Value": float(value)})
    df = pd.DataFrame(records)
    return df

def get_data(dataset, dim_list, country_list, start_year = "", end_year = ""):
    """Retrieves current account data from the Eurostat MIP database"""

    ## Define dimensions and URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    full_url = construct_url(base_url, dataset, dim_list, country_list, start_year, end_year)

    # Load data
    df = get_df(full_url)
    df["Code"] = dataset
    return(df)