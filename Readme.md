# 📌 Desafio RPA - Scraping Books

Este projeto faz scraping de dados do site [Books to Scrape](https://books.toscrape.com/) e armazena as informações em um banco de dados SQLite e em um relatório Excel.

## 📂 Estrutura do Projeto

```
DESAFIO_RPA/
│-- data/                  # Banco de dados SQLite
│-- reports/               # Relatórios gerados em Excel
│-- src/                   # Código-fonte do projeto
│   │-- fetch_page.py       # Captura a página com Selenium
│   │-- parse_books.py      # Faz o parsing dos dados com BeautifulSoup
│   │-- save_data.py        # Salva os dados no SQLite e gera Excel
│   │-- save_excel_to_sqlite.py  # Exporta do SQLite para Excel
│   │-- main.py             # Arquivo principal do projeto
│-- .gitignore             # Arquivos ignorados pelo Git
│-- requirements.txt       # Dependências do projeto
```

## 🚀 Como Executar

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/IuryyCosta/RPA-Desafio.git
cd DESAFIO_RPA
```

### 2️⃣ Criar um Ambiente Virtual (Opcional, mas Recomendado)
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as Dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Executar o Código
```sh
python src/main.py
```

## 📊 Gerando Relatório do SQLite
Para gerar um relatório Excel a partir do banco de dados SQLite, execute:
```sh
python src/save_excel_to_sqlite.py
```

---

## 📦 Dependências (`requirements.txt`)
```
selenium
webdriver-manager
beautifulsoup4
pandas
sqlalchemy
openpyxl
```

## 📝 .gitignore
```
# Ambiente Virtual
venv/

# Arquivos do SQLite
data/*.db

# Cache do Python
__pycache__/
*.pyc
*.pyo

# Relatórios gerados
reports/*.xlsx
```

