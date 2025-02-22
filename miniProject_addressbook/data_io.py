import json
import os

DATA_FILE = 'miniProject_addressbook/data.json'

def load_data():
    """JSON 파일에서 데이터를 불러오기."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    """데이터를 JSON 파일에 저장하기."""
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
