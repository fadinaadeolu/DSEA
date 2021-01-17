import pandas as pd

df_wdl = pd.read_csv("./data/WDIData.csv")
df_country = pd.read_csv("./data/country.csv")

countries = df_country.values.ravel().tolist()
df = df_wdl.copy()

df["new_index"] = df[
    ["Country Name",
     "Country Code",
     "Indicator Name",
     "Indicator Code"]
    ].agg("_".join, axis=1)

df = df.set_index("new_index")
df["Countries"] = df["Country Code"]

df.drop(columns=[
    "Country Name",
    "Country Code",
    "Indicator Name",
    "Indicator Code",
    "Unnamed: 65"],
    inplace=True)

df2 = df.iloc[:, 29:]
df2 = df2.drop(df2[df2.isnull().sum(axis=1) > 10].index)
df2 = df2[df2["Countries"].isin(countries)]
df2.drop(columns=["Countries"], inplace=True)

df_grp = df2.groupby(by="new_index")

df_new = pd.DataFrame()

for grp, grp_values in df_grp:
    transpose_vals = grp_values.transpose()
    year = transpose_vals.index
    indicator_value = transpose_vals.iloc[:, 0].values
    ind = [grp] * len(transpose_vals.values)
    transpose_vals.index = ind

    df_temp = pd.DataFrame({
        "country_indcator": ind,
        "year": year,
        "indicator_value": indicator_value
    })

    df_new = df_new.append(df_temp)
    print(grp)

df_new.to_csv("./data/WDIProcessed.csv", index=False)
