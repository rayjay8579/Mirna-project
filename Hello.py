import pandas as pd


with open("mirna list", "r") as f:
    mirna_list = [line.strip() for line in f if line.strip()]


encori_data = pd.read_csv("encori raw data", sep="\t")


filtered_data = encori_data[encori_data['miRNA'].isin(mirna_list)]


filtered_data.to_csv("filtered_encori_data.tsv", sep="\t", index=False)

print("Done! Filtered data saved as 'filtered_encori_data.tsv'")

