import tkinter as tk
from tkinter import messagebox, ttk
import requests

SERVER_URL = "http://127.0.0.1:5000"  # Flask 서버 주소

class AddressBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("주소록 (서버 모드)")
        self.root.geometry("500x500")
        self.create_widgets()
        self.display_contacts()

    def create_widgets(self):
        tk.Label(self.root, text="이름").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="전화번호").pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        tk.Button(self.root, text="연락처 추가", command=self.add_contact_gui).pack(pady=5)
        tk.Button(self.root, text="모든 연락처 보기", command=self.display_contacts).pack(pady=5)

        self.tree = ttk.Treeview(self.root, columns=("이름", "전화번호"), show='headings')
        self.tree.heading("이름", text="이름")
        self.tree.heading("전화번호", text="전화번호")
        self.tree.pack(expand=True, fill='both', pady=10)

    def add_contact_gui(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if not name or not phone:
            messagebox.showwarning("입력 오류", "이름과 전화번호는 필수입니다.")
            return
        
        response = requests.post(f"{SERVER_URL}/add_contact", json={"name": name, "phone": phone, "email": "", "address": ""})
        if response.status_code == 200:
            messagebox.showinfo("성공", "연락처 추가 완료!")
            self.display_contacts()
        else:
            messagebox.showerror("오류", "연락처 추가 실패!")

    def display_contacts(self):
        response = requests.get(f"{SERVER_URL}/contacts")
        if response.status_code == 200:
            contacts = response.json()
            self.update_treeview(contacts)
        else:
            messagebox.showerror("오류", "연락처 목록을 불러올 수 없습니다.")

    def update_treeview(self, contacts):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for contact in contacts:
            self.tree.insert("", "end", values=(contact["name"], contact["phone"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookGUI(root)
    root.mainloop()
