# 명령 프롬프트에서 파이썬 사용하기
 # Win R+을 누른뒤 cmd를 입력하여 명령 프롤프트를 실행
 # python을 입력하여 파이썬 셸을 실행
 # print("Hello world!")를 입력한 뒤 엔터키를 누름
 # 명령 프롬프트에서도 파이썬 셸을 실행하여 파이썬을 사용할수 있음
 # 멸령 프롬프트에서 파이썬 셸을 끝내려면 exit()를 입력하거나 Ctrl+Z를 누름
# 에러 | 명령 프롬프트에서 파이썬이 실행되지 않을때
 # 파이썬을 삭제한 뒤 다시설치
 # 제어판 > 프로그램 > 프로그램 제거 > pYTHON 3.6.0 (32-BIT)를 클릭(버전과 비트수는 자신이 설치한 버전과 비트수에 따라 달라짐)
 # Uninstall 클릭
 # 'Unit 2 파이썬 설치하기'를 참고하여 파이썬을 다시 설치합니다. 단, 설치할 때 반드시 Add Python 3.6 to PATH에 체크
 # 제어판 > 시스템 및 보안 > 시스템 > 고급 시스템 설정 > 환경 변수(N)...에서 <사용자이름>에 대한 사용자 변수(U)에서 Path를 선택하고 편집(E)..를 클릭
 # 새로 만들기(N)을 클릭한 뒤 다음 두 경로를 추가
 # <사용자이름>은 자신의 Windows 계정 이름을 넣기
 # Python36은 파이썬 3.6 32비트를 설치했을 때의 경로임
 # 각자 설치한 버전과 비트수에 맞는 경로를 입력
 # 32비트:
 # C:\Users\<사용자이름>\AppData\Local\Programs\Python\Python36-32\
 # C:\Users\<사용자이름>\AppData\Local\Programs\Python\Python36-32\Scripts\
 # 64 비트:
 # C:\Users\<사용자이름>\AppData\Local\Programs\Python\Python36\
 # C:\Users\<사용자이름>\AppData\Local\Programs\Python\Python36\Scripts\
# 참고 | 리눅스와 macOS에서 Hello world! 출력하기!
 # 리눅스와 macOS에서는 보통 콘솔(터미널)에서 python3를 사용
 # 콘솔에서 python3를 입력하여 파이썬 셸을 실행
 # print("Hello world")를 입력한 뒤 엔터 키를 누름
# 명령 프롬프트에서 스크립트 파일 실행하기
 # 명령 프롬프트에서 hello.py 파일을 실행(hello.py 파일에는 print('Hello, world!')가 저장되어 있음
 # Win+R을 누른 뒤 cmd를 입력하여 명령 프롬프트를 실행
 # C:\project 폴더로 이동합니다.
 # python hello.py를 입력하여 스크립트 파일을 실행