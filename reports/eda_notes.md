\# EDA Takeaways — Polyhouse Sensor Data



\## Correlation Heatmap Findings

\- temperature\_c shows positive correlation with yield\_kg

\- humidity\_pct shows moderate positive correlation with yield\_kg

\- co2\_ppm shows slight negative correlation with yield\_kg

\- No two features are perfectly correlated (no multicollinearity risk)



\## Scatter Plot Observations

\- Humidity vs Yield: positive trend, data clusters between 75-98%

\- Temperature vs Yield: clear positive linear relationship

\- CO2 vs Yield: slight negative trend, higher CO2 reduces yield slightly



\## Key Biological Insights

\- Higher temperature within safe range boosts mushroom growth

\- Humidity must stay high (75%+) for optimal yield

\- CO2 buildup above 1000ppm may inhibit yield slightly

\- Linear model should capture temperature and humidity effects well

