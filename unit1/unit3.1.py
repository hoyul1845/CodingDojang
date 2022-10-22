# IDLE에서 Hello Python 출력해보기
 # print( ) 안에 'Hello, Python'을 넣으면 됨
print("Hello, Python")
# 에러
 # NameError: name ... is not defined: 함수 이름을 잘못 입력했을 때 발생하는 에러
 # 파이썬은 대소문자를 구분하므로 대소문자를 정확히 입력
 # print처럼 전부 소문자로 입력했는지 확인
 # SyntaxError: invalid syntax: print( )안에 Hello, world!를 넣을 때 ' '(작은따옴표)로 묶지 않아서 발생하는 구문 에러(syntax error)
 # 작은 따옴표로 묶어줌
 # SyntaxError: EOL while scanning string literal: 따옴표를 잘못 사용했을 때 발생하는 구문 에러
 # 'Hello, world!'와 같이 앞 뒤로 작은따옴표 쌍이 맞는지 확인
#  IDLE에서 Hello, world! 출력해보기
 # 코드를 한 줄 한 줄 실행하여 결과를 얻는 방식을 인터프리터(interpreter) 방식
 # IDLE처럼 파이썬 코드를 직접 입력해서 실행하는 프로그램을 파이썬 셸(Python Shell)이라고 함
 #  >>> 부분을 파이썬 프롬프트(Python prompt)라고 부름
# 참고 | 대화형 셸
 # 파이썬 셸은 파이썬 인터프리터와 대화하듯이 코드를 처리한다고 해서 대화형 셸(interactive shell)또는 인터렉티브 모드(interactive mode)라고함
 # 이런 방식을 코드를 읽고, 평가(계산, 실행)하고, 출력한다고 해서 REPL(Read-Eval-Print Loop)이라고함
# 참고 | IDLE의 파이썬 셸에서 에러가 났을때
 # IDLE의 파이썬 셸에서 코드를 잘못 입력하여 에러가 나면 올바른 코드를 다시 입력
 # IDLE의 파이썬 셸에서는 ↑ 방향 키를 누르면 이전 코드로 쉽게 돌아갈 수 있음
 # 이전 코드에서 엔터 키를 누르면 해당 코드를 다시 사용할 수 있음