# core.py


def add_contact(data):
    """연락처 추가."""
    name = input("이름: ")
    phone = input("전화번호: ")
    email = input("이메일: ")
    address = input("주소: ")

    new_contact = {"name": name, "phone": phone, "email": email, "address": address}
    data.append(new_contact)
    print("연락처 추가 완료!")
    return data

def search_contact(data,keyword = None):
    """연락처 검색."""
    if keyword == None:
        keyword = input("검색어 (이름/전화번호): ")
    results = [c for c in data if keyword.lower() in c['name'].lower() or keyword in c['phone']]

    if results:
        print("\n🔎 검색 결과:")
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    else:
        print("해당 연락처를 찾을 수 없습니다.")
    return data

def show_contacts(data):
    """모든 연락처 보기."""
    if not data:
        print("저장된 연락처가 없습니다.")
        return
    print("\n연락처 목록:")
    for c in data:
        print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def delete_contact(data):
    """연락처 삭제."""
    keyword = input("삭제할 연락처 이름/전화번호: ")
    results = [c for c in data if keyword.lower() in c['name'].lower() or keyword in c['phone']]

    if not results:
        print("해당 연락처가 없습니다.")
        return data

    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

    try:
        choice = int(input("삭제할 번호 선택 (취소: 0): "))
        if choice == 0:
            print("삭제 취소.")
        elif 1 <= choice <= len(results):
            data.remove(results[choice - 1])
            print("삭제 완료!")
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("숫자로 입력하세요.")
    return data
