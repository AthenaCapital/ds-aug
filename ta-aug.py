import pandas as pd
import ta

# Load datas
df = pd.read_csv('spy.csv', sep=',')

# Clean NaN values
df = ta.utils.dropna(df)

# Add all ta features
df = ta.add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume")

df.to_csv(r"spy-ta.csv")