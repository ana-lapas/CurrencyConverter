# Input data
value_in_reais = 100.00
dollar_rate = 5.20
euro_rate = 6.15

# Conversion calculations
value_in_dollars = value_in_reais / dollar_rate
value_in_euros = value_in_reais / euro_rate

# Display the results
print("Valor em reais: R$", value_in_reais)
print("Taxa do dólar: $", round(dollar_rate, 2))
print("Taxa do euro: €", round(euro_rate, 2))
print("Total em dólar: $", round(value_in_dollars, 2))
print("Total em euro: €", round(value_in_euros, 2))