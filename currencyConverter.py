import requests
fromCurr=str(input("Input the currency name:")).upper()
toCurr=str(input("Input the currency name which you want to convert:")).upper()
amount=float(input("Input the amount to convert:"))
response=requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={fromCurr}&to={toCurr}")
print(f"{amount}{fromCurr} is {response.json() ['rates'][toCurr]}{toCurr}")
