from fetch_page import fetch_page
from parse_books import parse_books
from save_data import  save_to_sqlite
from save_excel_to_sqlite  import save_to_execel_from_sqlite

def main():
    url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    html = fetch_page(url)
    books = parse_books(html)
    save_to_sqlite(books)
    save_to_execel_from_sqlite()

    print('Dados salvos com sucesso')    




if __name__ == "__main__":
        main()