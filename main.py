import data_loading as dl
import pandas as pd


## SET OUTPUT FOLDER
output_folder = "./output_folder/"

## SET COUNTRY LIST
country_list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", 
                "EE", "FI", "FR", "DE", "EL", "HU", "IE", 
                "IT", "LV", "LT", "LU", "MT", "NL", "PL", 
                "PT", "RO", "SK", "SI", "ES", "SE"]

## SET YEAR RANGE
start_year = "2015"
end_year = "2024"

indics = []
#### CURRENT ACCOUNT ####
ca = dl.get_ca(country_list, start_year, end_year)
ca.to_csv(f"{output_folder}ca_data.csv", index = False)
print("CA data saved to:", f"{output_folder}ca_data.csv \n")
indics.append(ca)

#### NET INTERNATIONAL INVESTMENT POSITION ####
niip = dl.get_niip(country_list, start_year, end_year)
niip.to_csv(f"{output_folder}niip_data.csv", index = False)
print("NIIP data saved to:", f"{output_folder}niip_data.csv \n")
indics.append(niip)

#### REAL EFFECTIVE EXCHANGE RATE ####
reer = dl.get_reer(country_list, start_year, end_year)
reer.to_csv(f"{output_folder}reer_data.csv", index = False)
print("REER data saved to:", f"{output_folder}reer_data.csv \n")
indics.append(reer)

#### EXPORT PERFORMANCE AGAINST ADVANCED ECONOMIES ####
epaae = dl.get_epaae(country_list, start_year, end_year)
epaae.to_csv(f"{output_folder}epaae_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}epaae_data.csv \n")
indics.append(epaae)

#### NOMINAL UNIT LABOUR COST ####
nulc = dl.get_nulc(country_list, start_year, end_year)
nulc.to_csv(f"{output_folder}nulc_data.csv", index = False)
print("NULC data saved to:", f"{output_folder}nulc_data.csv \n")
indics.append(nulc)

#### GENERAL GOVERNMENT GROSS DEBT ####
gggd = dl.get_gggd(country_list, start_year, end_year)
gggd.to_csv(f"{output_folder}gggd_data.csv", index = False)
print("GGGD data saved to:", f"{output_folder}gggd_data.csv \n")
indics.append(gggd)

#### HOUSEHOLD DEBT ####
hhd = dl.get_hhd(country_list, start_year, end_year)
hhd.to_csv(f"{output_folder}hhd_data.csv", index = False)
print("HHD data saved to:", f"{output_folder}hhd_data.csv \n")
indics.append(hhd)

#### NON-FINANCIAL CORPORATIONS DEBT ####
nfcd = dl.get_nfcd(country_list, start_year, end_year)
nfcd.to_csv(f"{output_folder}nfcd_data.csv", index = False)
print("NFCD data saved to:", f"{output_folder}nfcd_data.csv \n")
indics.append(nfcd)

#### HOUSEHOLD CREDIT FLOW ####
hhcf = dl.get_hhcf(country_list, start_year, end_year)
hhcf.to_csv(f"{output_folder}hhcf_data.csv", index = False)
print("HHCF data saved to:", f"{output_folder}hhcf_data.csv \n")
indics.append(hhcf)

#### NON-FINANCIAL CORPORATIONS CREDIT FLOW EXCLUDING FDI ####
nfccf = dl.get_nfccf(country_list, start_year, end_year)
nfccf.to_csv(f"{output_folder}nfccf_data.csv", index = False)
print("NFCCF data saved to:", f"{output_folder}nfccf_data.csv \n")
indics.append(nfccf)

#### NOMINAL HOUSE PRICE INDEX ####
nhpi = dl.get_nhpi(country_list, start_year, end_year)
nhpi.to_csv(f"{output_folder}nhpi_data.csv", index = False)
print("NHPI data saved to:", f"{output_folder}nhpi_data.csv \n")
indics.append(nhpi)

#### UNEMPLOYMENT RATE ####
unem = dl.get_unem(country_list, start_year, end_year)
unem.to_csv(f"{output_folder}unem_data.csv", index = False)
print("UNEM data saved to:", f"{output_folder}unem_data.csv \n")
indics.append(unem)

#### LABOUR FORCE PARTICIPATION RATE ####
lfpr = dl.get_lfpr(country_list, start_year, end_year)
lfpr.to_csv(f"{output_folder}lfpr_data.csv", index = False)
print("LFPR data saved to:", f"{output_folder}lfpr_data.csv \n")
indics.append(lfpr)

#### TOTAL DATA OF THE MIP SCOREBOARD ####
tot = pd.concat([ca, niip, reer, epaae, 
                      nulc, gggd, hhd, nfcd, 
                      hhcf, nfccf, nhpi, unem, 
                      lfpr], ignore_index = True)
tot.to_csv(f"{output_folder}mip_sb_data.csv", index = False)
print("Total Scoreboard data saved to:", f"{output_folder}mip_sb_data.csv \n")


#ca = ca[ca["Year"] == 2023]
#ca = ca.drop(columns=['Year', 'Indicator'])
#ca.to_csv(f"{output_folder}test_data.csv", index = False)
thresholds_dict = {}
for indic in indics:
    #print(indic["Value"])
    print(indic)
    sorted_values = indic["Value"].sort_values()
    lowest_5 = sorted_values.head(6)[3:]
    highest_5 = sorted_values.tail(6)[:-3]
    avg_low = lowest_5.mean()
    avg_high = highest_5.mean()
    print(f"Average of lowest 5: {avg_low}")
    print(f"Average of highest 5: {avg_high}")

    step = (avg_high - avg_low) / 6
    quintiles = [avg_low + step * i for i in range(1, 6)]  # 6 points creates 5 intervals
    print("quintiles:", quintiles)

    if (indic["Indicator"].unique()[0] == "Current account" or 
        indic["Indicator"].unique()[0] == "Net international investment position" or 
        indic["Indicator"].unique()[0] == "Real effective exchange rate" or
        indic["Indicator"].unique()[0] == "Export performance against advanced economies" or
        indic["Indicator"].unique()[0] == "Nominal unit labour cost index" or
        indic["Indicator"].unique()[0] == "Household credit flow" or
        indic["Indicator"].unique()[0] == "NFC credit flow excluding FDI" or 
        indic["Indicator"].unique()[0] == "Nominal house price index" or
        indic["Indicator"].unique()[0] == "Labour force participation rate"):
                                        
        closest_to_zero = min(quintiles, key = abs)
        print(closest_to_zero)
        quintiles[quintiles.index(closest_to_zero)] = 0
        print(quintiles)

    print(indic["Indicator"].unique()[0])
    thresholds_dict[indic["Indicator"].unique()[0]] = quintiles

# Save a json file with the thresholds
import json
print(thresholds_dict)
with open('colour_thresholds.json', 'w') as f:
    json.dump(thresholds_dict, f, indent=4)

"""





# Round
thresholds_ca = [round(x, 1) for x in thresholds_ca]
thresholds_niip = [round(x, 1) for x in thresholds_niip]
thresholds_reer = [round(x, 1) for x in thresholds_reer]
thresholds_epaae = [round(x, 1) for x in thresholds_epaae]
thresholds_nulc = [round(x, 1) for x in thresholds_nulc]
thresholds_gggd = [round(x, 1) for x in thresholds_gggd]
thresholds_hhd = [round(x, 1) for x in thresholds_hhd]
thresholds_nfcd = [round(x, 1) for x in thresholds_nfcd]
thresholds_hhcf = [round(x, 1) for x in thresholds_hhcf]
thresholds_nfccf = [round(x, 1) for x in thresholds_nfccf]
thresholds_nhpi = [round(x, 1) for x in thresholds_nhpi]
thresholds_unem = [round(x, 1) for x in thresholds_unem]
thresholds_lfpr = [round(x, 1) for x in thresholds_lfpr]

# Convert to 0 for the ones that ara closest
closest_to_zero = min(thresholds_ca, key=abs)
thresholds_ca[thresholds_ca.index(closest_to_zero)] = 0

closest_to_zero = min(thresholds_reer, key=abs)
thresholds_reer[thresholds_reer.index(closest_to_zero)] = 0

closest_to_zero = min(thresholds_epaae, key=abs)
thresholds_epaae[thresholds_epaae.index(closest_to_zero)] = 0

closest_to_zero = min(thresholds_hhcf, key=abs)
thresholds_hhcf[thresholds_hhcf.index(closest_to_zero)] = 0

closest_to_zero = min(thresholds_nfccf, key=abs)
thresholds_nfccf[thresholds_nfccf.index(closest_to_zero)] = 0

closest_to_zero = min(thresholds_lfpr, key=abs)
thresholds_lfpr[thresholds_lfpr.index(closest_to_zero)] = 0


# Map the quantile values to your custom keys
thresholds_dict = {"Current account": thresholds_ca,
                   "Net international investment position": thresholds_niip,
                   "Real effective exchange rate": thresholds_reer,
                   "Export performance against advanced economies": thresholds_epaae,
                   "Nominal unit labour cost": thresholds_nulc,
                   "General government gross debt": thresholds_gggd,
                   "Household debt": thresholds_hhd,
                   "NFC debt": thresholds_nfcd,
                   "Household credit flow": thresholds_hhcf,
                   "NFC credit flow excluding FDI": thresholds_nfccf,
                   "Nominal house price index": thresholds_nhpi,
                   "Unemployment rate": thresholds_unem,
                   "Labour force participation rate": thresholds_lfpr}



"""