import data_io
import core

def welcome():
    """메뉴 출력 및 사용자 입력 받기."""
    print("\n|1 추가|2 조회|3 삭제|4 목록 보기|9 종료|")
    try:
        return int(input("명령 선택: "))
    except ValueError:
        print("숫자로 입력하세요.")
        return 0

def main():
    """메인 실행 함수."""
    data = data_io.load_data()

    while True:
        command = welcome()

        if command == 1:
            data = core.add_contact(data)
        elif command == 2:
            data = core.search_contact(data)
        elif command == 3:
            data = core.delete_contact(data)
        elif command == 4:
            core.show_contacts(data)
        elif command == 9:
            data_io.save_data(data)
            print("👋 프로그램 종료!")
            break
        else:
            print("❌ 올바른 명령을 입력하세요.")

if __name__ == "__main__":
    main()
