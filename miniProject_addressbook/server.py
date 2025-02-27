from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# DB 초기화 함수
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT,
        address TEXT
    )""")
    conn.commit()
    conn.close()

# 모든 연락처 가져오기
@app.route("/miniProject_addressbook\data.json", methods=["GET"])
def get_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = [{"id": row[0], "name": row[1], "phone": row[2], "email": row[3], "address": row[4]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(contacts)


# 연락처 추가
@app.route("/add_contact", methods=["POST"])
def add_contact():
    data = request.json
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", 
                   (data["name"], data["phone"], data["email"], data["address"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "연락처 추가 성공!"})

# 연락처 삭제
@app.route("/delete_contact/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "연락처 삭제 성공!"})

if __name__ == "__main__":
    init_db()  # 서버 시작 전 DB 초기화
    app.run(host="0.0.0.0", port=5000, debug=True)
