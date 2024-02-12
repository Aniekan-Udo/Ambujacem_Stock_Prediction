# Ambuja Cements Stock Price Prediction

## Overview
This repository contains code for predicting stock prices of Ambuja Cements (NSE: AMBUJACEM). The goal is to develop a model that can accurately forecast the future price movements of Ambuja Cements stock based on historical data.

## Features
- Utilizes historical stock price data for training and testing.
- Implements machine learning algorithms `(arch_model)` for prediction.

## Getting Started
To get started with using or contributing to this project, follow these steps:

1. **Create AlphaVantageAPI Class:**
    The AlphaVantageAPI class gets the data by sending a get request to Alphavantage and preprocesses the data.

2. **Create SQL Class**
    Create an SQL class that connects to ```sqlite3 database```, send the preprocessed data to the database

3. **Train the Model:**
   Train your chosen machine learning model using the prepared data.

4. **Predict Stock Prices:**
   Once the model is trained, use it to predict future stock prices.
