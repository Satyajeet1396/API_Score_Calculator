import pandas as pd
import streamlit as st
from io import BytesIO

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

# Title of the section
st.title("Support our Research")
st.write("Scan the QR code below to make a payment to: satyajeet1396@oksbi")

# Generate the UPI QR code
upi_url = "upi://pay?pa=satyajeet1396@oksbi&pn=Satyajeet Patil&cu=INR"
qr = qrcode.make(upi_url)

# Save the QR code image to a BytesIO object
buffer = BytesIO()
qr.save(buffer, format="PNG")
buffer.seek(0)

# Convert the image to Base64
qr_base64 = base64.b64encode(buffer.getvalue()).decode()

# Center-align the QR code image using HTML and CSS
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="data:image/png;base64,{qr_base64}" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

# Display the "Buy Me a Coffee" button as an image link
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://www.buymeacoffee.com/researcher13" target="_blank">
            <img src="https://img.buymeacoffee.com/button-api/?text=Support our Research&emoji=&slug=researcher13&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" alt="Support our Research"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
