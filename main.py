from data_loading import get_df
import pandas as pd

## CREATE LIST WITH COUNTRIES
country_list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", 
                "EE", "FI", "FR", "DE", "EL", "HU", "IE", 
                "IT", "LV", "LT", "LU", "MT", "NL", "PL", 
                "PT", "RO", "SK", "SI", "ES", "SE"]

## CREATE URL
#base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?format=JSON&lang=EN&geo=SE&unit=CP_MEUR&na_item=P6"
#base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?format=JSON&lang=EN&"
output_folder = "C://Users/Tobia/mip_map/output_folder/"

#### CURRENT ACCOUNT ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSBP10"
freq = "A"
unit = "PC_GDP_3Y"
s_adj = "NSA"
bop_item = "CA"
stk_flow = "BAL"
partner = "WRL_REST"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{s_adj}.{bop_item}.{stk_flow}.{partner}.{geo[:-1]}"
print("Getting CA data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "Current account"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}ca_data.csv", index = False)
print("CA data saved to:", f"{output_folder}ca_data.csv \n")

#### NET INTERNATIONAL INVESTMENT POSITION ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSII10"
freq = "A"
s_adj = "NSA"
bop_item = "FA"
sector10 = "S1"
sectpart = "S1"
stk_flow = "N_LE"
partner = "WRL_REST"
unit = "PC_GDP"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{s_adj}.{bop_item}.{sector10}.{sectpart}.{stk_flow}.{partner}.{unit}.{geo[:-1]}"
print("Getting NIIP data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NIIP"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}niip_data.csv", index = False)
print("NIIP data saved to:", f"{output_folder}niip_data.csv \n")


#### REAL EFFECTIVE EXCHANGE RATE ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSER10"
freq = "A"
unit = "PCH_3Y"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{geo[:-1]}"
print("Getting REER data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "REER"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}reer_data.csv", index = False)
print("REER data saved to:", f"{output_folder}reer_data.csv \n")


#### EXPORT PERFORMANCE AGAINST ADVANCED ECONOMIES ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSBP60"
freq = "A"
unit = "PCH_OECD_EU_3Y"
bop_item = "GS"
stk_flow = "CRE"
partner = "WRL_REST"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{bop_item}.{stk_flow}.{partner}.{geo[:-1]}"
print("Getting EPAAE data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "EPAAE"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}epaae_data.csv", index = False)
print("EPAAE data saved to:", f"{output_folder}epaae_data.csv \n")


#### NOMINAL UNIT LABOUR COST ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSLM10"
freq = "A"
na_item = "NULC_HW"
unit = "PCH_3Y"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{na_item}.{unit}.{geo[:-1]}"
print("Getting NULC data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NULC"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}nulc_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}nulc_data.csv \n")


#### GENERAL GOVERNMENT GROSS DEBT ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSGO10"
freq = "A"
na_item = "GD"
sector = "S13"
unit = "PC_GDP"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{na_item}.{sector}.{unit}.{geo[:-1]}"
print("Getting GGGD data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "GGGD"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}gggd_data.csv", index = False)
print("GGGD data saved to:", f"{output_folder}gggd_data.csv \n")


#### HOUSEHOLD DEBT ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSPD22"
freq = "A"
unit = "PC_GDP"
co_nco = "CO"
sector = "S14_S15"
finpos = "LIAB"
na_item = "F3_F4"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{co_nco}.{sector}.{finpos}.{na_item}.{geo[:-1]}"
print("Getting HHD data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "HHD"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}hhd_data.csv", index = False)
print("HHD data saved to:", f"{output_folder}hhd_data.csv \n")


#### NON-FINANCIAL CORPORATIONS DEBT ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSPD30"
freq = "A"
unit = "PC_GDP"
co_nco = "CO"
sector = "S11"
finpos = "LIAB"
na_item = "F3_F4"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{co_nco}.{sector}.{finpos}.{na_item}.{geo[:-1]}"
print("Getting NFCD data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NFCD"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}nfcd_data.csv", index = False)
print("NFCD data saved to:", f"{output_folder}nfcd_data.csv \n")


#### HOUSEHOLD CREDIT FLOW ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSPC40"
freq = "A"
na_item = "F3_F4"
co_nco = "CO"
sector = "S14_S15"
finpos = "LIAB"
unit = "PC_LE"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{na_item}.{co_nco}.{sector}.{finpos}.{unit}.{geo[:-1]}"
print("Getting HHCF data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "HHCF"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}hhcf_data.csv", index = False)
print("HHCF data saved to:", f"{output_folder}hhcf_data.csv \n")


#### NON-FINANCIAL CORPORATIONS CREDIT FLOW EXCLUDING FDI ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSPC30"
freq = "A"
unit = "PC_LE"
co_nco = "CO"
sector = "S11"
finpos = "LIAB"
na_item = "F3_F4_X_FDI"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{co_nco}.{sector}.{finpos}.{na_item}.{geo[:-1]}"
print("Getting NFCCF data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NFCCF"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}nfccf_data.csv", index = False)
print("NFCCF data saved to:", f"{output_folder}nfccf_data.csv \n")


#### NOMINAL HOUSE PRICE INDEX ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSHO20"
freq = "A"
unit = "RCH_A_AVG"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{geo[:-1]}"
print("Getting NHPI data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NHPI"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}nhpi_data.csv", index = False)
print("NHPI data saved to:", f"{output_folder}nhpi_data.csv \n")


#### UNEMPLOYMENT RATE ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSUN20"
freq = "A"
sex = "T"
age = "Y15-74"
unit = "PC_ACT"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{sex}.{age}.{unit}.{geo[:-1]}"
print("Getting UNEM data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "UNEM"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}unem_data.csv", index = False)
print("UNEM data saved to:", f"{output_folder}unem_data.csv \n")


#### LABOUR FORCE PARTICIPATION RATE ####
## SDMX URL
base_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"
dataset = "TIPSLM60"
freq = "A"
unit = "PPCH_3Y"
age = "Y15-64"
sex = "T"
geo = ""
for country in country_list:
    geo = geo + country + "+"
full_url = base_url + f"/{dataset}/{freq}.{unit}.{age}.{sex}.{geo[:-1]}"
print("Getting LFPR data!")
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "LFPR"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}lfpr_data.csv", index = False)
print("LFPR data saved to:", f"{output_folder}lfpr_data.csv \n")




#df = df[df["Year"] == 2023]
#df = df.drop(columns=['Year', 'Indicator'])
#df.to_csv(f"{output_folder}test_data.csv", index = False)