import pandas as pd
import streamlit as st

# Function to calculate base score based on impact factor
def calculate_base_score(impact_factor):
    if pd.isna(impact_factor):  # If there is no impact factor
        return 5
    elif impact_factor < 1:
        return 10
    elif 1 <= impact_factor < 2:
        return 15
    elif 2 <= impact_factor < 5:
        return 20
    elif 5 <= impact_factor < 10:
        return 25
    elif impact_factor >= 10:
        return 30
    return 0  # Default case

# Function to adjust score based on the number of authors and author role
def calculate_api_score(row):
    impact_factor = row.iloc[0]  # Column 1: Impact Factor
    num_authors = row.iloc[1]    # Column 2: No. of Authors
    author_role = row.iloc[2]    # Column 3: Author role

    base_score = calculate_base_score(impact_factor)

    if num_authors == 1:
        return base_score
    elif num_authors == 2:
        return base_score * 0.7  # 70% for each author if two authors
    else:
        if author_role in ['p', 'P']:  # Principal or corresponding author
            return base_score * 0.7
        else:  # Co-author
            return base_score * 0.3

# Streamlit app layout
st.title("API Score Calculator")
st.write("Upload an Excel file to calculate the API score based on impact factors and author roles.")

# Download template file button
with open("Format.xlsx", "rb") as file:
    st.download_button(
        label="Download Template File",
        data=file,
        file_name="Format.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Load the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Convert the impact factor column to numeric
    df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

    # Calculate API Score and add it as a new column
    df['API Score'] = df.apply(calculate_api_score, axis=1)

    # Display the DataFrame with the new 'API Score' column
    st.write("Calculated API Scores:")
    st.dataframe(df)

    # Provide an option to download the modified DataFrame as an Excel file
    output_file = "Calculated_API_Scores.xlsx"
    df.to_excel(output_file, index=False)

    with open(output_file, "rb") as file:
        st.download_button(
            label="Download Excel file with API Scores",
            data=file,
            file_name=output_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


st.info("Created by Dr. Satyajeet Patil")
st.info("For more cool apps like this visit: https://patilsatyajeet.wixsite.com/home/python")



# Display custom "Buy Me a Coffee" button
bmc_button = """
<div align="center">
    <a href="https://www.buymeacoffee.com/researcher13" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Support our Research" style="height: 50px; width: 217px;">
    </a>
</div>
"""
