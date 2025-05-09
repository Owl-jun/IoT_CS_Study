### 미니프로젝트 : GUI 활용한 주소록 만들기

- 프로젝트 구상
    - GUI를통한 연락처 추가,조회,수정,삭제 기능
    - 데이터가 많아도 실행 속도가 빠르게
    - 즐겨찾기 기능
    - **서버-클라이언트 구조 맛보기**


## 2차 업데이트
- 서버-클라이언트 구조 맛보기 도전 실패;

## 1차 업데이트

https://github.com/user-attachments/assets/33edd9ba-9a2f-451e-a112-835604777625



- 개선해야할 점 : 데이터가 10000개 정도인데, treeview를 리로드 할때 연산수행시간이 오래걸린다. 최적화가 필요해보임.

- [코어](core.py)  : 파일 구현으로, 핵심 기능들을 구현

- [CLI](cli.py)    : 먼저 CLI 기반으로 기능 동작 테스트

- [GUI](gui.py)    : tkinter를 활용하여 GUI 구축 후 코어 기능 연동
    - 삭제 기능 구현에서, treeview 의 id와 실제data 의 인덱스를 동기화 시키는데 어려움을 겪었으나,
    - treeview에 데이터를 넣을때, iid 를 설정할 수 있다는 것을 알고 해결 할 수 있었다.
    - 새롭게 알게 된 사실 : data.json 파일을 메모리에 읽어놓고, 수정이 일어나면 메모리상에서 바로바로 적용이 된다는 사실!

- [JSON](data.json) : json 파일을 활용하여 데이터 저장 - 로드 구현

- [TEST](m_test.py) : 각종 테스트를 위한 더미데이터를 만들어 넣는 코드 구현
    - 랜덤한 이름과, 전화번호를 10000개 삽입할 수 있는 코드
