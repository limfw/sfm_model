import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)  # Read uploaded file
    st.write("Data Preview:", df.head())  # Show data preview


st.title("Interactive Dashboard for U_it Analysis")

region_options = df["Region"].unique()
year_options = sorted(df["Year"].unique())
ec_options = df["EC"].unique()

selected_region = st.selectbox("Select Region:", ["All"] + list(region_options))
selected_year = st.selectbox("Select Year:", ["All"] + list(year_options))
selected_ec = st.selectbox("Select EC:", ["All"] + list(ec_options))


filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["Year"] == selected_year]
if selected_ec != "All":
    filtered_df = filtered_df[filtered_df["EC"] == selected_ec]

filtered_df["exp(-U_it)"] = np.exp(-filtered_df["U_it_hat_1"])

fig, ax = plt.subplots()
ax.plot(filtered_df["Year"], filtered_df["exp(-U_it)"], marker="o", linestyle="-")
ax.set_xlabel("Year")
ax.set_ylabel("exp(-U_it)")
ax.set_title("exp(-U_it) Over Time")
ax.grid()

st.pyplot(fig)

st.write("Filtered Data:")
st.dataframe(filtered_df)
