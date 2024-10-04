import requests

# URL of the PHP endpoint
url = "https://www.handicaps.co.za/wp-admin/admin-ajax.php"  # Replace with the actual URL

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
}

# Payload
payload = {
    "action": "get_player_results",
    "search_playerId": "2700240933"
}

# Sending POST request
response = requests.post(url, headers=headers, data=payload)
json_response = response.json()

# Extract the `current_hi` value
current_hi = json_response.get("current_hi", "N/A")

# Output the `current_hi` value
print(current_hi)
