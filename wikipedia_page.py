import requests

def wikipedia_page(title):
    '''
    This function returns the raw text of a wikipedia page 
    given a wikipedia page title
    '''
    params = { 
        'action': 'query', 
        'format': 'json', 
        'titles': title, 
        'prop': 'extracts', 
        'explaintext': True
    }
    response = requests.get(
         'https://en.wikipedia.org/w/api.php',
         params= params
     ).json()

    
    page = next(iter(response['query']['pages'].values()))
    if 'extract' in page.keys():
        return page['extract']
    else:
        return "Page not found"
