import requests

api_key = "061cbab3da504065b33cea0f74134012"
base_url = 'https://newsapi.org/v2/top-headlines?country=id'

categories = {
    '1': ('Teknologi', 'technology'),
    '2': ('Bisnis', 'business'),
    '3': ('Olahraga', 'sports'),
    '4': ('Kesehatan', 'health'),
    '5': ('Sains', 'science')
}

def get_news(category):
    params = {
        'country': 'id',
        'category': category,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles'][:5]
        return articles
    
def display_news(articles):
    for i, article in enumerate(articles, 1):
        print(f"{i} - {article['title']}")


def main():
    print("Selamat datang, mau tahu berita apa hari ini?")
    for key, (name, _) in categories.items():
        print(f"[{key}]. Berita seputar {name}")
    
    choice = input('Masukkan pilihan anda [1/2/3/4/5] : ')

    if choice in categories:
        category_name, category_key = categories[choice]
        print(f"Top 5 berita hari ini seputar {category_name} di Indonesia:")
        articles = get_news(category_key)
        display_news(articles)

main()