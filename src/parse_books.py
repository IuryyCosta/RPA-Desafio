from bs4 import BeautifulSoup

def parse_books(html):
    print('Entrou na função parse_books')

    """ Extrair os dados dos Livros da Página. """
    soup = BeautifulSoup(html, 'html.parser') # Criação do Objeto soup para manipular o HTML 

    books = []

    # Adicionando os dados dos livros ao array books 
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text.strip()
        availability = article.find('p', class_='instock availability').text.strip()
        
        #inseindo os dados no array books
        books.append({
            'title': title,
            'price': price,
            'availability':availability,
            
        })
    return books 