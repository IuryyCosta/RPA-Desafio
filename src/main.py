from src.fetch_page import fetch_page

def main():
    url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    html = fetch_page(url)
    print(html)

if __name__ == "__main__":
        main()