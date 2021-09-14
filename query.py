import sys
import requests

def urlbuilder():
    link = f"http://127.0.0.1:5000/?" + sys.argv[1]
    return link

def query():
    url= urlbuilder()
    try:
        res = requests.get(url).json()
    except requests.exceptions.RequestException:
        print(sys.exc_info()[0])
    print("La temperatura en", res["city"], "es de", res["temperature"], "º")


if __name__ == '__main__':
    query()
