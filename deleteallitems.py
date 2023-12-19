import requests

# Replace with your actual API token and collection ID
api_token = ''
collection_id = ''

def get_authenticated_headers():
    """Prepare headers for authenticated API requests."""
    return {
        'Authorization': f'Bearer {api_token}',
        'accept': 'application/json'
    }

def fetch_collection_items(collection_id, headers):
    """Fetch all items from a specific collection."""
    url = f'https://api.webflow.com/v2/collections/{collection_id}/items'
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    return response.json()['items']

def delete_collection_item(collection_id, item_id, headers):
    """Delete a specific item from the collection."""
    url = f'https://api.webflow.com/v2/collections/{collection_id}/items/{item_id}'
    response = requests.delete(url, headers=headers)
    response.raise_for_status()  
    return response.status_code

def main():
    headers = get_authenticated_headers()
    try:
        collection_items = fetch_collection_items(collection_id, headers)
        for item in collection_items:
            status = delete_collection_item(collection_id, item['id'], headers)
            print(f'Item {item["id"]} deleted, status code: {status}')
    except requests.HTTPError as e:
        print(f'An HTTP error occurred: {e.response.text}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
