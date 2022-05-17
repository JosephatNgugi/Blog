import requests
from models import Quote

API = 'http://quotes.stormconsultancy.co.uk/random.json'
def get_quote():
    """
    Function to fetch random quotes returning a quote class instance
    """
    response = requests.get(API).json()
    
    random_quote = Quote(**response)
    return random_quote