# API Score Calculator

This Streamlit app calculates the Academic Performance Indicator (API) scores for research papers based on impact factor, number of authors, and author role. The app supports bulk calculations from an uploaded Excel file and provides an option to download the results.

## Features
- Calculates API scores based on specified conditions:
  - **Impact Factor Scoring**:
    - No impact factor: 5 points
    - Impact factor < 1: 10 points
    - Impact factor between 1 and 2: 15 points
    - Impact factor between 2 and 5: 20 points
    - Impact factor between 5 and 10: 25 points
    - Impact factor > 10: 30 points
  - **Author Scoring**:
    - Single author: 100% of points
    - Two authors: 70% for each author
    - More than two authors: 70% for Principal/Corresponding author, 30% for each Co-author
- **File Upload and Download**:
  - Upload an Excel file in the specified format
  - Download the processed file with API scores

## File Format
Please use [this Format.xlsx file](https://github.com/Satyajeet1396/API_Score_Calculator/blob/7208766232ba3c9a3c96a2fdff7c876834300efa/Format.xlsx) as a template for uploading your data. This ensures correct data columns and structure.

