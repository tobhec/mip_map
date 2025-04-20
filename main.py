import data_loading as dl


## SET OUTPUT FOLDER
output_folder = "C://Users/Tobia/mip_map/output_folder/"

## SET COUNTRY LIST
country_list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", 
                "EE", "FI", "FR", "DE", "EL", "HU", "IE", 
                "IT", "LV", "LT", "LU", "MT", "NL", "PL", 
                "PT", "RO", "SK", "SI", "ES", "SE"]

#### CURRENT ACCOUNT ####
df = dl.get_ca(country_list)
df.to_csv(f"{output_folder}ca_data.csv", index = False)
print("CA data saved to:", f"{output_folder}ca_data.csv \n")

#### NET INTERNATIONAL INVESTMENT POSITION ####
df = dl.get_niip(country_list)
df.to_csv(f"{output_folder}niip_data.csv", index = False)
print("NIIP data saved to:", f"{output_folder}niip_data.csv \n")

#### REAL EFFECTIVE EXCHANGE RATE ####
df = dl.get_reer(country_list)
df.to_csv(f"{output_folder}reer_data.csv", index = False)
print("REER data saved to:", f"{output_folder}reer_data.csv \n")

#### EXPORT PERFORMANCE AGAINST ADVANCED ECONOMIES ####
df = dl.get_epaae(country_list)
df.to_csv(f"{output_folder}nulc_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}nulc_data.csv \n")

#### GENERAL GOVERNMENT GROSS DEBT ####
df = dl.get_gggd(country_list)
df.to_csv(f"{output_folder}gggd_data.csv", index = False)
print("GGGD data saved to:", f"{output_folder}gggd_data.csv \n")

#### HOUSEHOLD DEBT ####
df = dl.get_hhd(country_list)
df.to_csv(f"{output_folder}hhd_data.csv", index = False)
print("HHD data saved to:", f"{output_folder}hhd_data.csv \n")

#### NON-FINANCIAL CORPORATIONS DEBT ####
df = dl.get_nfcd(country_list)
df.to_csv(f"{output_folder}nfcd_data.csv", index = False)
print("NFCD data saved to:", f"{output_folder}nfcd_data.csv \n")

#### HOUSEHOLD CREDIT FLOW ####
df = dl.get_hhcf(country_list)
df.to_csv(f"{output_folder}hhcf_data.csv", index = False)
print("HHCF data saved to:", f"{output_folder}hhcf_data.csv \n")

#### NON-FINANCIAL CORPORATIONS CREDIT FLOW EXCLUDING FDI ####
df = dl.get_nfccf(country_list)
df.to_csv(f"{output_folder}nfccf_data.csv", index = False)
print("NFCCF data saved to:", f"{output_folder}nfccf_data.csv \n")

#### NOMINAL HOUSE PRICE INDEX ####
df = dl.get_nhpi(country_list)
df.to_csv(f"{output_folder}nhpi_data.csv", index = False)
print("NHPI data saved to:", f"{output_folder}nhpi_data.csv \n")

#### UNEMPLOYMENT RATE ####
df = dl.get_unem(country_list)
df.to_csv(f"{output_folder}unem_data.csv", index = False)
print("UNEM data saved to:", f"{output_folder}unem_data.csv \n")

#### LABOUR FORCE PARTICIPATION RATE ####
df = dl.get_lfpr(country_list)
df.to_csv(f"{output_folder}lfpr_data.csv", index = False)
print("LFPR data saved to:", f"{output_folder}lfpr_data.csv \n")




#df = df[df["Year"] == 2023]
#df = df.drop(columns=['Year', 'Indicator'])
#df.to_csv(f"{output_folder}test_data.csv", index = False)