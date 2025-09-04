import zipfile

zip_path = "API_SP.POP.TOTL_DS2_en_csv_v2_563791.zip"
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall()  # Extracts all files into the current folder
print("✅ ZIP file extracted successfully!")
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (CSV must be in same folder)
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_563791.csv", skiprows=4)

# Pick latest year
latest_year = "2022"

# --- BAR CHART: Top 10 Most Populated Countries ---
top10 = data[["Country Name", latest_year]].dropna().nlargest(10, latest_year)

plt.figure(figsize=(10,6))
plt.bar(top10["Country Name"], top10[latest_year] / 1e9, color='skyblue')
plt.title("Top 10 Most Populated Countries in 2022")
plt.xlabel("Country")
plt.ylabel("Population (Billions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_population_bar.png")
plt.show()

# --- HISTOGRAM: Population Distribution ---
plt.figure(figsize=(10,6))
plt.hist(data[latest_year].dropna() / 1e6, bins=20, color='orange', edgecolor='black')
plt.title("Distribution of Country Populations in 2022")
plt.xlabel("Population (Millions)")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("population_histogram.png")
plt.show()

