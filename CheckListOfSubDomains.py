import requests

def check_subdomain_status(subdomains):
    results = {}
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            if response.status_code == 200:
                results[subdomain] = 'Up'
            else:
                results[subdomain] = 'Down'
        except requests.exceptions.RequestException:
            results[subdomain] = 'Down'
    return results

# List of subdomains to check
subdomains = [
    
]
while True:
    status_results = check_subdomain_status(subdomains)
    for subdomain, status in status_results.items():
        print(f"{subdomain} is {status}")
