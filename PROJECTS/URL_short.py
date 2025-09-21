import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

if __name__ == "__main__":
    url = input("Enter the URL to shorten: ")
    try:
        print("Shortened URL:", shorten_url(url))
    except Exception as e:
        print("Error:", e)