import requests

# Set up the API endpoint and authentication headers
url = "https://api.grammarly.com/v1/check"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# Define the text to check
text = "I has a cat."

# Send a request to the API endpoint
data = {
    "text": text,
    "language": "en-US",
    "dialect": "GENERAL",
    "domain": "GENERAL"
}
response = requests.post(url, headers=headers, json=data)

# Parse the response and print the corrected text
json_data = response.json()
if json_data["result"]["status"] == "ok":
    corrected_text = json_data["result"]["corrections"]["text"]
    print(corrected_text)
else:
    print("Error: ", json_data["result"]["message"])
