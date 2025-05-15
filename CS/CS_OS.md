# 운영체제 - 최린 교수님 강의 정리

#### 목차
1. OS Overview
2. Process
3. Thread
4. Mutual Exclusion and Synchronization
5. Deadlock and Starvation
6. Memory Management
7. Virtual Memory
8. Uniprocessor Scheduling
9. Multiprocessor and Realtime Scheduling
10. IO
11. File Management
12. Virtual Machine

### 1. OS Overview

- 1강(250515)
    - 디지털 시스템이 컴퓨터가 되기 위한 조건?
        ```txt
        " 조건 -> 계산 -> 판단을 할 수 있는 CPU 같은 장치가 존재하며 프로세싱이 가능해야한다. "
        " 상태 값을 가져야한다. "

        - 쉽게 설명해보기
        : 컴퓨팅 (연산, 상태값 저장 등을 하는 행위) 작업이 가능해야한다.
        즉, 사람처럼 어떠한 기준으로 판단을 할 수  있어야한다. 
        (조건에 따라 다른 동작을 할 수 있어야 한다)
        그걸 할 수 있게 해주는 것이 CPU 와 같은 장치이다.
        ```
    - 컴퓨터 시스템에서 OS란 무엇이냐?
        ```txt
        " 하드웨어 리소스를 쉽게 조작할 수 있도록 도움을 주고, "
        " 하드웨어와 유저레벨 사이에서 인터페이스를 제공해주는 것이다. "

        - 쉽게 설명해보기
        : 우리가 컴퓨터를 조작하기위해 본체를 뜯어서 전기신호를 직접 주지않고 
        키보드, 마우스 등의 입력, 출력 장치를 가지고 조작할 수 있는 이유이다.
        Windows , Linux , MacOS , UNIX 등이 있다.
        ```
---
- 2강