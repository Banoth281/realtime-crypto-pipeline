import streamlit as st
import pandas as pd
import glob
import time

st.title("📈 Real-Time Bitcoin Price Tracker")

# Create a placeholder for the live chart
placeholder = st.empty()

while True:
    try:
        # Read all generated CSV files from PySpark output
        all_files = glob.glob("./output_data/*.csv")
        if all_files:
            df_list = [pd.read_csv(f, names=["symbol", "price_usd", "timestamp"]) for f in all_files]
            df = pd.concat(df_list, ignore_index=True)
            
            # Sort by timestamp
            df = df.sort_values(by="timestamp")
            
            # Update the dashboard view
            with placeholder.container():
                st.metric(label="Latest Bitcoin Price (USD)", value=f"${df['price_usd'].iloc[-1]:,.2f}")
                st.line_chart(df.set_index("timestamp")["price_usd"])
    except Exception as e:
        pass
    
    time.sleep(2)
