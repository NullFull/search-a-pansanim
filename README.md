# 썻쳐판사님 search-a-pansanim
사건 판례 정보 모음. (설명 추가 필요) 

### 간단 아키텍쳐
- Python 3.10 / Django 4.0
- Django Admin 으로 데이터 입력
- DB : Heroku postgreSQL
- CI/CD : Heroku Sentry 

** Heroku 설정은 nullfull google 계정으로 할 수 있음. 

### model 구조
* Case: 사건 (사건명, 간략 설명)
* Decision : 판결 정보
* Quote : 사건 관련 인용구 (판결문, 가해자 발언, 기사 등)
* Judge : 판사 정보
* Company : 소속 (예. 대법원)

![ERD](https://user-images.githubusercontent.com/17819874/156876058-e279a3f7-f8c9-436b-8086-c5011e2447b5.png)  
*models to ERD 로 자동생성된 이미지. 참고- [issue #12](https://github.com/NullFull/anijung/issues/12#issuecomment-1059723473)*

### Django Admin 
- 데이터 입력을 위해 Django Admin 로그인이 필요함. 새로운 계정 생성은 Admin 관리자가 할 수 있음.   
#### 새로운 계정 생성 방법
1. {사이트주소}/admin 에 접속해 로그인 (예. https://search-a-pansanim.herokuapp.com/admin)  
2. '인증 및 권한 - 사용자(들)' 메뉴 옆 '+ 추가' 버튼 클릭해서 정보 입력 후 저장. 
3. '1'의 주소로 새로운 계정으로 로그인 후, 우측 상단 비밀번호 변경을 눌러 꼭 비밀번호를 변경하기.  

### 프로젝트 세팅
- local 에서 Django 구동
  - Django tutorial 참고 - [공식 문서 링크](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#the-development-server) 
  1. virtual environment 생성  
  2. [Django 실행](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#the-development-server) `python manage.py runserver`  
  3. [DB migration](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#database-setup) : `python manage.py migrate`  
  4. [admin 접속을 위한 superuser 생성](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#creating-an-admin-user) : `python manage.py createsuperuser`  
  ** nested_inline 패키지 관련 오류 발생시 참고 : https://github.com/NullFull/anijung/issues/14#:~:text=solution
