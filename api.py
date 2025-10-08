import requests

def fetch_page(api_key: str, query: str, year: int, page: int, state: str = "ALL") -> dict:
    url = 'https://api.legiscan.com/'
    params = {
        'key': api_key,
        'op': 'getSearch',
        'state': state,
        'query': query,
        'year': year,
        'page': page
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching page {page}: {str(e)}")


def flatten_results(results: dict) -> list:
    return [value for key, value in results.items() if key != 'summary']