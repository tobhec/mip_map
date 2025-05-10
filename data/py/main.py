import data_loading as dl
import pandas as pd


## SET OUTPUT FOLDER
output_folder = "../output/"
config_folder = "../config/"

## SET COUNTRY LIST
country_list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", 
                "EE", "FI", "FR", "DE", "EL", "HU", "IE", 
                "IT", "LV", "LT", "LU", "MT", "NL", "PL", 
                "PT", "RO", "SK", "SI", "ES", "SE"]

## SET YEAR RANGE
start_year = "2015"
end_year = "2024"

if __name__ == "__main__":

    indics = []
    
    #### CURRENT ACCOUNT ####
    freq = "A"
    unit = "PC_GDP_3Y"
    s_adj = "NSA"
    bop_item = "CA"
    stk_flow = "BAL"
    partner = "WRL_REST"
    dim_list = [freq, unit, s_adj, bop_item, stk_flow, partner]
    ca = dl.get_data("TIPSBP10", dim_list, country_list, start_year, end_year)
    ca["Indicator"] = "Current account"
    ca = ca.drop('Code', axis = 1)
    #ca.to_csv(f"{output_folder}ca_data.csv", index = False)
    indics.append(ca)

    #### NET INTERNATIONAL INVESTMENT POSITION ####
    freq = "A"
    s_adj = "NSA"
    bop_item = "FA"
    sector10 = "S1"
    sectpart = "S1"
    stk_flow = "N_LE"
    partner = "WRL_REST"
    unit = "PC_GDP"
    dim_list = [freq, s_adj, bop_item, sector10, sectpart, stk_flow, partner, unit]
    niip = dl.get_data("TIPSII10", dim_list, country_list, start_year, end_year)
    niip["Indicator"] = "Net international investment position"
    niip = niip.drop('Code', axis = 1)
    #niip.to_csv(f"{output_folder}niip_data.csv", index = False)
    indics.append(niip)

    #### REAL EFFECTIVE EXCHANGE RATE ####
    freq = "A"
    unit = "PCH_3Y"
    dim_list = [freq, unit]
    reer = dl.get_data("TIPSER10", dim_list, country_list, start_year, end_year)
    reer["Indicator"] = "Real effective exchange rate"
    reer = reer.drop('Code', axis = 1)
    #reer.to_csv(f"{output_folder}reer_data.csv", index = False)
    indics.append(reer)

    #### EXPORT PERFORMANCE AGAINST ADVANCED ECONOMIES ####
    freq = "A"
    unit = "PCH_OECD_EU_3Y"
    bop_item = "GS"
    stk_flow = "CRE"
    partner = "WRL_REST"
    dim_list = [freq, unit, bop_item, stk_flow, partner]
    epaae = dl.get_data("TIPSBP60", dim_list, country_list, start_year, end_year)
    epaae["Indicator"] = "Export performance against advanced economies"
    epaae = epaae.drop('Code', axis = 1)
    #epaae.to_csv(f"{output_folder}epaae_data.csv", index = False)
    indics.append(epaae)

    #### NOMINAL UNIT LABOUR COST ####
    freq = "A"
    na_item = "NULC_HW"
    unit = "PCH_3Y"
    dim_list = [freq, na_item, unit]
    nulc = dl.get_data("TIPSLM10", dim_list, country_list, start_year, end_year)
    nulc["Indicator"] = "Nominal unit labour cost index"
    nulc = nulc.drop('Code', axis = 1)
    #nulc.to_csv(f"{output_folder}nulc_data.csv", index = False)
    indics.append(nulc)

    #### GENERAL GOVERNMENT GROSS DEBT ####
    freq = "A"
    na_item = "GD"
    sector = "S13"
    unit = "PC_GDP"
    dim_list = [freq, na_item, sector, unit]
    gggd = dl.get_data("TIPSGO10", dim_list, country_list, start_year, end_year)
    gggd["Indicator"] = "General government gross debt"
    gggd = gggd.drop('Code', axis = 1)
    #gggd.to_csv(f"{output_folder}gggd_data.csv", index = False)
    indics.append(gggd)

    #### HOUSEHOLD DEBT ####
    freq = "A"
    unit = "PC_GDP"
    co_nco = "CO"
    sector = "S14_S15"
    finpos = "LIAB"
    na_item = "F3_F4"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]
    hhd = dl.get_data("TIPSPD22", dim_list, country_list, start_year, end_year)
    hhd["Indicator"] = "Household debt"
    hhd = hhd.drop('Code', axis = 1)
    #hhd.to_csv(f"{output_folder}hhd_data.csv", index = False)
    indics.append(hhd)

    #### NON-FINANCIAL CORPORATIONS DEBT ####
    freq = "A"
    unit = "PC_GDP"
    co_nco = "CO"
    sector = "S11"
    finpos = "LIAB"
    na_item = "F3_F4"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]
    nfcd = dl.get_data("TIPSPD30", dim_list, country_list, start_year, end_year)
    nfcd["Indicator"] = "NFC debt"
    nfcd = nfcd.drop('Code', axis = 1)
    #nfcd.to_csv(f"{output_folder}nfcd_data.csv", index = False)
    indics.append(nfcd)

    #### HOUSEHOLD CREDIT FLOW ####
    freq = "A"
    na_item = "F3_F4"
    co_nco = "CO"
    sector = "S14_S15"
    finpos = "LIAB"
    unit = "PC_LE"
    dim_list = [freq, na_item, co_nco, sector, finpos, unit]
    hhcf = dl.get_data("TIPSPC40", dim_list, country_list, start_year, end_year)
    hhcf["Indicator"] = "Household credit flow"
    hhcf = hhcf.drop('Code', axis = 1)
    #hhcf.to_csv(f"{output_folder}hhcf_data.csv", index = False)
    indics.append(hhcf)

    #### NON-FINANCIAL CORPORATIONS CREDIT FLOW EXCLUDING FDI ####
    freq = "A"
    unit = "PC_LE"
    co_nco = "CO"
    sector = "S11"
    finpos = "LIAB"
    na_item = "F3_F4_X_FDI"
    dim_list = [freq, unit, co_nco, sector, finpos, na_item]
    nfccf = dl.get_data("TIPSPC30", dim_list, country_list, start_year, end_year)
    nfccf["Indicator"] = "NFC credit flow excluding FDI"
    nfccf = nfccf.drop('Code', axis = 1)
    #nfccf.to_csv(f"{output_folder}nfccf_data.csv", index = False)
    indics.append(nfccf)

    #### NOMINAL HOUSE PRICE INDEX ####
    freq = "A"
    unit = "RCH_A_AVG"
    dim_list = [freq, unit]
    nhpi = dl.get_data("TIPSHO20", dim_list, country_list, start_year, end_year)
    nhpi["Indicator"] = "Nominal house price index"
    nhpi = nhpi.drop('Code', axis = 1)
    #nhpi.to_csv(f"{output_folder}nhpi_data.csv", index = False)
    indics.append(nhpi)

    #### UNEMPLOYMENT RATE ####
    freq = "A"
    sex = "T"
    age = "Y15-74"
    unit = "PC_ACT"
    dim_list = [freq, sex, age, unit]
    unem = dl.get_data("TIPSUN20", dim_list, country_list, start_year, end_year)
    unem["Indicator"] = "Unemployment rate"
    unem = unem.drop('Code', axis = 1)
    #unem.to_csv(f"{output_folder}unem_data.csv", index = False)
    indics.append(unem)

    #### LABOUR FORCE PARTICIPATION RATE ####
    freq = "A"
    unit = "PPCH_3Y"
    age = "Y15-64"
    sex = "T"
    dim_list = [freq, unit, age, sex]
    lfpr = dl.get_data("TIPSLM60", dim_list, country_list, start_year, end_year)
    lfpr["Indicator"] = "Labour force participation rate"
    lfpr = lfpr.drop('Code', axis = 1)
    #lfpr.to_csv(f"{output_folder}lfpr_data.csv", index = False)
    indics.append(lfpr)

    #### TOTAL DATA OF THE MIP SCOREBOARD ####
    tot = pd.concat([ca, niip, reer, epaae, 
                        nulc, gggd, hhd, nfcd, 
                        hhcf, nfccf, nhpi, unem, 
                        lfpr], ignore_index = True)
    tot.to_csv(f"{output_folder}mip_sb_data.csv", index = False)
    print("Total Scoreboard data saved to:", f"{output_folder}mip_sb_data.csv \n")


    # Calculate colour-thresholds for each indicator 
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

        # Add a breaking point from positive to negative for the closest value
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
    with open(f"{config_folder}scale_dict.json", "w") as f:
        json.dump(thresholds_dict, f, indent=4)
