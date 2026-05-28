# test_insecure_example.py
API_KEY = "sk_test_corridor_dummy_key_123456789"

def fetch_data():
    import requests
    return requests.get("https://example.com", verify=False, timeout=5).text