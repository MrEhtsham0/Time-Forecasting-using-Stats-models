# Time Series Forecasting with ARIMA and SARIMA


This repository contains a project focused on time series forecasting using ARIMA and SARIMA models implemented with the statsmodels library in Python. The primary objective is to predict future values of a given time series based on historical data.


	Data preprocessing and visualization
	Model building and fitting using ARIMA and SARIMA
	Model evaluation with metrics such as AIC, BIC, and RMSE
	Forecasting future values
	Plotting and visualization of forecasts
	Installation

Model Explanation
ARIMA (AutoRegressive Integrated Moving Average)
ARIMA is a popular statistical method for time series forecasting. It combines three components:

AR (AutoRegressive): Model that uses the dependent relationship between an observation and some number of lagged observations.I (Integrated): Uses differencing of raw observations to make the time series stationary.MA (Moving Average): Model that uses dependency between an observation and a residual error from a moving average model applied to lagged observations.

SARIMA (Seasonal ARIMA)
SARIMA extends ARIMA by explicitly supporting univariate time series data with a seasonal component. It includes:

Seasonal Differencing: Making the time series stationary in the seasonal component.
Seasonal AR and MA: AutoRegressive and Moving Average components for the seasonal part of the series.
Results
The notebook includes detailed steps to:

Visualize the original time series
Perform necessary transformations and checks for stationarity
Fit ARIMA and SARIMA models
Evaluate models using criteria like AIC, BIC, and RMSE
Generate and visualize forecasts
Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change or add.



Your Name - mr_ehtsham@yahoo.com
GitHub: MrEhtsham0
