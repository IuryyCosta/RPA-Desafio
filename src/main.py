from fetch_page import fetch_page
from parse_books import parse_books

def main():
    url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    html = fetch_page(url)
    books = parse_books(html)

    print(books)




if __name__ == "__main__":
        main()