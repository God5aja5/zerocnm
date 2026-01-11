import sys
import os
sys.path.append('/root/bot')

# Import the functions we need to test
from app import search_mobile, format_response

# Test the search_mobile function with the new API
print("Testing search_mobile function...")
result = search_mobile("9721266300")

print(f"Raw result: {result}")

# Test the format_response function
print("\nTesting format_response function...")
formatted = format_response(result, "mobile")

print(f"Formatted result: {formatted[0] if formatted else 'No results'}")