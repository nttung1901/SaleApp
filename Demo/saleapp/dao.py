import json

def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)