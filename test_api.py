import requests
import json

# Test the new API endpoint
mobile_number = "9721266300"  # Using the example from the prompt
url = f"https://sandhu-psi.vercel.app/get_data?mobile={mobile_number}&key=data"

print(f"Testing API: {url}")
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")