import requests
import re
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p','--port', type=str, help='port to connect to')
parser.add_argument('-u','--url',type=str, help='ip address to connect')
args = parser.parse_args()
url = args.url
port = args.port
req = requests.session()

address = 'http://' + url + ':' + port

def get_page(address, req):
    response = req.get(url=address)
    return response

def extract_string(response):
    raw_text = response.text
    pattern = r'<h3 align=\'center\'>(.*?)</h3>'
    match = re.search(pattern, raw_text)
    if match:
        random_string = match.group(1)
        return random_string
    else:
        return Exception

def hash_string(random_string):
    hash_object = hashlib.md5()
    encoded_string = random_string.encode('UTF-8')
    hash_object.update(encoded_string)
    hex_hash = hash_object.hexdigest()
    return hex_hash

def post_hash(address, req, hex_hash):
    data = dict(hash=hex_hash)
    response = req.post(address, data=data)
    return response

def get_flag(response):
    raw_text = response.text
    pattern = r'<p align=\'center\'>(.*?)</p>'
    match = re.search(pattern=pattern, string=raw_text)
    if match:
        flag_string = match.group(1)
        return print(flag_string)
    else:
        return print("something went wrong, please try again")

try:
    get_flag(post_hash(address=address, req=req, hex_hash=hash_string(random_string=extract_string(response=get_page(address=address, req=req)))))
except Exception as e:
    print(f"Something went wrong: {e}")
