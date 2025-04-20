import data_loading as dl
import pandas as pd


## SET OUTPUT FOLDER
output_folder = "C://Users/Tobia/mip_map/output_folder/"

## SET COUNTRY LIST
country_list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", 
                "EE", "FI", "FR", "DE", "EL", "HU", "IE", 
                "IT", "LV", "LT", "LU", "MT", "NL", "PL", 
                "PT", "RO", "SK", "SI", "ES", "SE"]

## SET YEAR RANGE
start_year = "2015"
end_year = "2024"

#### CURRENT ACCOUNT ####
ca = dl.get_ca(country_list, start_year, end_year)
ca.to_csv(f"{output_folder}ca_data.csv", index = False)
print("CA data saved to:", f"{output_folder}ca_data.csv \n")

#### NET INTERNATIONAL INVESTMENT POSITION ####
niip = dl.get_niip(country_list, start_year, end_year)
niip.to_csv(f"{output_folder}niip_data.csv", index = False)
print("NIIP data saved to:", f"{output_folder}niip_data.csv \n")

#### REAL EFFECTIVE EXCHANGE RATE ####
reer = dl.get_reer(country_list, start_year, end_year)
reer.to_csv(f"{output_folder}reer_data.csv", index = False)
print("REER data saved to:", f"{output_folder}reer_data.csv \n")

#### EXPORT PERFORMANCE AGAINST ADVANCED ECONOMIES ####
epaae = dl.get_epaae(country_list, start_year, end_year)
epaae.to_csv(f"{output_folder}epaae_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}epaae_data.csv \n")

#### NOMINAL UNIT LABOUR COST ####
nulc = dl.get_nulc(country_list, start_year, end_year)
nulc.to_csv(f"{output_folder}nulc_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}nulc_data.csv \n")

#### GENERAL GOVERNMENT GROSS DEBT ####
gggd = dl.get_gggd(country_list, start_year, end_year)
gggd.to_csv(f"{output_folder}gggd_data.csv", index = False)
print("GGGD data saved to:", f"{output_folder}gggd_data.csv \n")

#### HOUSEHOLD DEBT ####
hhd = dl.get_hhd(country_list, start_year, end_year)
hhd.to_csv(f"{output_folder}hhd_data.csv", index = False)
print("HHD data saved to:", f"{output_folder}hhd_data.csv \n")

#### NON-FINANCIAL CORPORATIONS DEBT ####
nfcd = dl.get_nfcd(country_list, start_year, end_year)
nfcd.to_csv(f"{output_folder}nfcd_data.csv", index = False)
print("NFCD data saved to:", f"{output_folder}nfcd_data.csv \n")

#### HOUSEHOLD CREDIT FLOW ####
hhcf = dl.get_hhcf(country_list, start_year, end_year)
hhcf.to_csv(f"{output_folder}hhcf_data.csv", index = False)
print("HHCF data saved to:", f"{output_folder}hhcf_data.csv \n")

#### NON-FINANCIAL CORPORATIONS CREDIT FLOW EXCLUDING FDI ####
nfccf = dl.get_nfccf(country_list, start_year, end_year)
nfccf.to_csv(f"{output_folder}nfccf_data.csv", index = False)
print("NFCCF data saved to:", f"{output_folder}nfccf_data.csv \n")

#### NOMINAL HOUSE PRICE INDEX ####
nhpi = dl.get_nhpi(country_list, start_year, end_year)
nhpi.to_csv(f"{output_folder}nhpi_data.csv", index = False)
print("NHPI data saved to:", f"{output_folder}nhpi_data.csv \n")

#### UNEMPLOYMENT RATE ####
unem = dl.get_unem(country_list, start_year, end_year)
unem.to_csv(f"{output_folder}unem_data.csv", index = False)
print("UNEM data saved to:", f"{output_folder}unem_data.csv \n")

#### LABOUR FORCE PARTICIPATION RATE ####
lfpr = dl.get_lfpr(country_list, start_year, end_year)
lfpr.to_csv(f"{output_folder}lfpr_data.csv", index = False)
print("LFPR data saved to:", f"{output_folder}lfpr_data.csv \n")

#### TOTAL DATA OF THE MIP SCOREBOARD ####
tot = pd.concat([ca, niip, reer, epaae, 
                      nulc, gggd, hhd, nfcd, 
                      hhcf, nfccf, nhpi, unem, 
                      lfpr], ignore_index = True)
tot.to_csv(f"{output_folder}mip_sb_data.csv", index = False)
print("Total Scoreboard data saved to:", f"{output_folder}mip_sb_data.csv \n")



#df = df[df["Year"] == 2023]
#df = df.drop(columns=['Year', 'Indicator'])
#df.to_csv(f"{output_folder}test_data.csv", index = False)