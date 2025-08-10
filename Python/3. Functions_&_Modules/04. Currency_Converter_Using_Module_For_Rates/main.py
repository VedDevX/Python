from rates import exchange_rates

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "ERROR: Currency code not found."
    
    converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    
    return converted_amount

amount = float(input("Enter amount: "))
from_curr = input("Enter source currency code (e.g., USD, INR): ").upper()
to_curr = input("Enter target currency code (e.g., USD, INR): ").upper()

result = convert_currency(amount, from_curr, to_curr)

if isinstance(result, str):
    print(result)  # Error message
else:
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")