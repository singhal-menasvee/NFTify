import requests
import csv
from datetime import datetime

# List of NFT collections you want to fetch
collections = ["cryptopunks", "boredapeyachtclub", "artblocks"]

# URL to fetch NFT data from OpenSea API
url = "https://api.opensea.io/api/v1/assets"

# File to store the dataset
csv_file = 'nft_data.csv'

# Open the CSV file to write data
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header if the file is empty
    if file.tell() == 0:
        writer.writerow(['timestamp', 'nft_name', 'token_id', 'owner_address', 'collection', 'image_url', 'last_sale_price'])

    try:
        for collection in collections:
            # Parameters to filter data for each collection
            querystring = {
                "order_direction": "desc",
                "offset": "0",
                "limit": "10",  # Limit to 10 NFTs per request (you can increase this)
                "collection": collection  # Current collection from the list
            }

            # Fetch the NFT data
            response = requests.get(url, params=querystring)

            # Debugging: Check the status code and response text
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text[:500]}")  # Print the first 500 characters of the response

            # Raise an error if the response was unsuccessful
            response.raise_for_status()

            # Attempt to decode the JSON response
            data = response.json()

            # Check if 'assets' key is in the response
            if 'assets' not in data:
                print(f"No assets found for collection: {collection}")
                continue

            # Loop through each asset in the response and store it
            for asset in data['assets']:
                nft_name = asset['name'] if 'name' in asset else 'Unnamed'
                token_id = asset['token_id']
                owner_address = asset['owner']['address'] if 'owner' in asset else 'Unknown'
                collection_name = asset['collection']['name']
                image_url = asset['image_url']
                last_sale_price = asset['last_sale']['total_price'] if asset.get('last_sale') else 'Not Sold'

                # Get the current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Write the data to the CSV
                writer.writerow([timestamp, nft_name, token_id, owner_address, collection_name, image_url, last_sale_price])

            print(f"Fetched {len(data['assets'])} NFTs from the {collection} collection.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"Error occurred: {e}")
