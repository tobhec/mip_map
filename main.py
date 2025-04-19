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
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "Current account"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}ca_data.csv", index = False)
print("Current account data saved to:", f"{output_folder}ca_data.csv")

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
print(full_url)

# Load data
df = get_df(full_url)
df["Indicator"] = "NIIP"
print(df)

# Save to CSV
df.to_csv(f"{output_folder}niip_data.csv", index = False)
print("NIIP data saved to:", f"{output_folder}niip_data.csv")