import requests

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4xx or 5xx status codes
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        #locals returns a dictionary containing the current scope of the local variables
        if "response" in locals():
            return response.json(), response.status_code
        return None, None