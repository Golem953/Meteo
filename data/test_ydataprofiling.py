import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_json("42-station-meteo-toulouse-parc-compans-cafarelli.json")

profile = ProfileReport(df, title="Profil du JSON")
profile.to_file("profil_json.html")
