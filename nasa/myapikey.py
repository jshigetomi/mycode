import os

apikey = os.getenv("API_KEY")

apikey = "api_key=" + apikey

if __name__ == '__main__':
    print(apikey)
