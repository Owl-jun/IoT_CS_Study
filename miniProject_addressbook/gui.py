import tkinter as tk
from tkinter import messagebox, ttk
import core
import data_io

class AddressBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("주소록")
        self.root.geometry("500x500")
        
        self.data = data_io.load_data()
        self.create_widgets()
        self.display_contacts()

    def create_widgets(self):
        # 입력 필드
        tk.Label(self.root, text="이름").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="전화번호").pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        tk.Label(self.root, text="이메일").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        tk.Label(self.root, text="주소").pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        tk.Button(self.root, text="연락처 추가", command=self.add_contact_gui).pack(pady=5)
        # 검색 필드
        self.sFrame = tk.Frame(self.root,width=500,height=100)
        self.sFrame.pack()
        tk.Label(self.sFrame, text="검색어 (이름/전화번호)").pack(side='top')
        tk.Button(self.sFrame, text="연락처 검색", command=self.search_contacts_gui).pack(side="right",padx=5)
        self.search_entry = tk.Entry(self.sFrame)
        self.search_entry.pack(side="right")
        # 버튼
        self.bFrame = tk.Frame(self.root,width=500,height=100)
        self.bFrame.pack()
        tk.Button(self.bFrame, text="모든 연락처 보기", command=self.display_contacts).pack(side="right",padx=5,pady=5)
        tk.Button(self.bFrame, text="연락처 삭제", command=self.del_contact).pack(side="right",padx=5,pady=5)

        # 연락처 목록 표시 영역
        self.tree = ttk.Treeview(self.root, columns=("이름", "전화번호", "이메일", "주소"), show='headings')
        self.tree.heading("이름", text="이름")
        self.tree.heading("전화번호", text="전화번호")
        self.tree.heading("이메일", text="이메일")
        self.tree.heading("주소", text="주소")
        self.tree.pack(expand=True, fill='both', pady=10)
        self.tree.column("이름",width=50)
        self.tree.column("전화번호",width=100)
        self.tree.column("이메일",width=120)


    def add_contact_gui(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showwarning("입력 오류", "이름과 전화번호는 필수입니다.")
            return
        
        
        issave = messagebox.askyesno("확인","정말 추가하시겠습니까?")
        if issave:
            self.data = core.add_contact(self.data, name, phone, email, address)
            data_io.save_data(self.data)
            self.display_contacts()
            messagebox.showinfo("성공", "연락처 추가 완료!")
        else: 
            name = None
            phone = None
            email = None
            address = None
            return

    def search_contacts_gui(self):
        keyword = self.search_entry.get()
        if not keyword:
            messagebox.showwarning("검색 오류", "검색어를 입력하세요.")
            return

        results = core.search_contact(self.data, keyword)
        self.update_treeview(results)

        if not results:
            messagebox.showinfo("검색 결과", "검색된 연락처가 없습니다.")

    def del_contact(self):
        selected = self.tree.selection()
        if selected:
            idx = int(selected[0])  # iid는 항상 self.data의 인덱스
            confirm = messagebox.askyesno("확인", f"정말 삭제하시겠습니까? ({self.data[idx]['name']})")
            
            if confirm:
                del self.data[idx]
                data_io.save_data(self.data)  # 데이터 저장
                self.display_contacts()  # 최신 목록 표시
                messagebox.showinfo("성공", "연락처 삭제 완료!")
            else:
                print("삭제 취소됨.")
        else:
            messagebox.showwarning("선택 오류", "삭제할 연락처를 선택하세요.")
    

    def display_contacts(self):
        self.update_treeview(self.data)

    def update_treeview(self, contacts):
        # 기존 내용 제거
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for contact in contacts:
            real_index = self.data.index(contact)  
            self.tree.insert("", "end", iid=str(real_index), values=(
                contact["name"], 
                contact["phone"],
                contact.get('email', ''),
                contact.get('address', '')))


if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookGUI(root)
    root.mainloop()
