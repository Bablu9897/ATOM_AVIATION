import requests

def get_client_ip(request):
    # Extract the client's IP from the request
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    return ip

def get_public_ip():
    # Get the current public IP using an external api
    try:
        response = requests.get("https://api.ipify.org?format=json")
        public_ip = response.json().get('ip')
        return public_ip
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

def get_user_country(request):
    # Check if the request is coming from localhost or public domain
    ip = None
    if get_client_ip(request):
        ip =get_client_ip()
    else:
        ip = get_public_ip
    url = 'https://geolocation-db.com/json/'+str(ip)+'&position=true'
    response = requests.get(url).json()
    country = response['country_name']
    return country
