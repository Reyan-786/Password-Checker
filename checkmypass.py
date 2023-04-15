import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}, check the api and try again...")
    return res

def get_pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h , count in hashes:
        if h == hash_to_check:
            return count
        # print("hash- :   ",h,"count -: ",count)
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(sha1password.hexdigest().upper())
    first_5,tail = sha1password[:5] , sha1password[5:]
    response = request_api_data(first_5)
    # print('first_5 -: ',first_5, "tail -: ", tail ,"response -:", response)
    return get_pass_leak_count(response,tail)
# pwned_api_check('123')
