from django.shortcuts import render
import requests

def index(request):
    api_key = "51afb3d802c4b9dd0e76009a"
    currency_url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    currency_request = requests.get(currency_url)
    currency_response = currency_request.json()
    supported_codes = currency_response.get('supported_codes', [])
    currencies = [(code[0], code[1]) for code in supported_codes]  # Store as (short code, full name)
    
    if request.method == "POST":
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')
        endpoint = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
        end_request = requests.get(endpoint)
        end_response = end_request.json()
        result = end_response.get('conversion_result', 'Error fetching result')
        
        context = {
            "currencies": currencies,
            "result": result,
        }
        return render(request, 'index.html', context)
    
    context = {
        "currencies": currencies,
    }
    return render(request, 'index.html', context)
