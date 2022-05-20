import requests


def test_methods_availability(base_url, auth_availability):
    endpoint, method, exapected_status, description = auth_availability
    
    response = requests.request(method, f"{base_url}/auth/{endpoint}")
    
    assert response.status_code == int(exapected_status), \
        f"Wrong status code on auth {endpoint} url for {method} method. {response.status_code}"
        
    assert response.json().get("description") == description
 