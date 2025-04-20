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
            records.append({"Year": int(year), "Country": geo, "Value": float(value)})
    df = pd.DataFrame(records)
    return df


def construct_url(base, dataset, dim_list, countries):
    dims = ""
    for dim in dim_list:
        dims = dims + dim + "."
    geo = ""
    for cc in countries:
        geo = geo + cc + "+"
    full_url = f"{base}/{dataset}/{dims}{geo[:-1]}"
    return full_url

import data_loading as dl


def get_ca(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    dataset = "TIPSBP10"
    freq = "A"
    unit = "PC_GDP_3Y"
    s_adj = "NSA"
    bop_item = "CA"
    stk_flow = "BAL"
    partner = "WRL_REST"
    dim_list = [freq, unit, s_adj, bop_item, stk_flow, partner]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting CA data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "Current account"
    print(df)
    return(df)

def get_niip(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    dataset = "TIPSII10"
    freq = "A"
    s_adj = "NSA"
    bop_item = "FA"
    sector10 = "S1"
    sectpart = "S1"
    stk_flow = "N_LE"
    partner = "WRL_REST"
    unit = "PC_GDP"
    dim_list = [freq, s_adj, bop_item, sector10, sectpart, stk_flow, partner, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting NIIP data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "NIIP"
    print(df)
    return(df)

def get_reer(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSER10"
    freq = "A"
    unit = "PCH_3Y"
    dim_list = [freq, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting REER data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "REER"
    print(df)
    return(df)


def get_epaae(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSBP60"
    freq = "A"
    unit = "PCH_OECD_EU_3Y"
    bop_item = "GS"
    stk_flow = "CRE"
    partner = "WRL_REST"
    dim_list = [freq, unit, bop_item, stk_flow, partner]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting EPAAE data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "EPAAE"
    print(df)
    return(df)


def get_nulc(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSLM10"
    freq = "A"
    na_item = "NULC_HW"
    unit = "PCH_3Y"
    dim_list = [freq, na_item, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting NULC data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "NULC"
    print(df)
    return(df)


def get_gggd(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSGO10"
    freq = "A"
    na_item = "GD"
    sector = "S13"
    unit = "PC_GDP"
    dim_list = [freq, na_item, sector, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting GGGD data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "GGGD"
    print(df)
    return(df)


def get_hhd(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSPD22"
    freq = "A"
    unit = "PC_GDP"
    co_nco = "CO"
    sector = "S14_S15"
    finpos = "LIAB"
    na_item = "F3_F4"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting HHD data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "HHD"
    print(df)
    return(df)


def get_nfcd(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSPD30"
    freq = "A"
    unit = "PC_GDP"
    co_nco = "CO"
    sector = "S11"
    finpos = "LIAB"
    na_item = "F3_F4"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting NFCD data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "NFCD"
    print(df)
    return(df)


def get_hhcf(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSPC40"
    freq = "A"
    na_item = "F3_F4"
    co_nco = "CO"
    sector = "S14_S15"
    finpos = "LIAB"
    unit = "PC_LE"
    dim_list = [freq, na_item, co_nco, sector, finpos, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting HHCF data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "HHCF"
    print(df)
    return(df)


def get_nfccf(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSPC30"
    freq = "A"
    unit = "PC_LE"
    co_nco = "CO"
    sector = "S11"
    finpos = "LIAB"
    na_item = "F3_F4_X_FDI"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting NFCCF data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "NFCCF"
    print(df)
    return(df)


def get_nhpi(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSHO20"
    freq = "A"
    unit = "RCH_A_AVG"
    dim_list = freq, unit

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting NHPI data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "NHPI"
    print(df)
    return(df)


def get_unem(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSUN20"
    freq = "A"
    sex = "T"
    age = "Y15-74"
    unit = "PC_ACT"
    dim_list = [freq, sex, age, unit]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting UNEM data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "UNEM"
    print(df)
    return(df)


def get_lfpr(country_list):
    ## Set base URL
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

    ## Define dimensions
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
    dataset = "TIPSLM60"
    freq = "A"
    unit = "PPCH_3Y"
    age = "Y15-64"
    sex = "T"
    dim_list = [freq, unit, age, sex]

    # Get url
    full_url = construct_url(base_url, dataset, dim_list, country_list)
    print("Getting LFPR data!")
    print(full_url)

    # Load data
    df = get_df(full_url)
    df["Indicator"] = "LFPR"
    print(df)
    return(df)