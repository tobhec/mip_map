import requests
import xml.etree.ElementTree as ET
import pandas as pd


def get_df(url):
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
        geo = series.find(".//g:Value[@id='geo']", namespaces={"g": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic"}).attrib['value']
        # Go into each observation of each series
        for obs in series.findall(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}Obs"):
            # Get years
            year = obs.find("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsDimension").attrib['value']
            # Get values
            value = obs.find("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsValue").attrib['value']
            # Add geo, years and values to the dataset
            records.append({"Year": int(year), "Value": float(value), "Country": geo})
    df = pd.DataFrame(records)
    return df


