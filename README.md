# pre-onboarding-3rd-SNS

<br>

## ✅ 프로젝트 개요
- 원티드 프리온보딩 개인과제를 진행합니다. 
- 시나 소설 등 문학 작품의 일부분을 공유하는 SNS 서비스입니다. 
- 사용자들은 해당 서비스에서 회원가입 및 로그인 이후 본인이 좋아하는 글을 생성하고 다른 사용자들의 글을 확인할 수 있습니다.
- 해시태그로 해당 글의 주제나 단어, 작가를 기재한다면 다른 사용자들로부터 검색이 용이해집니다.

<br>

📌 **1차 개발기간** : 2022.07.20 ~ 2022.07.26

<br>

📌 **고도화 예정 Issues** 
   - **게시글 목록 4가지 기능 동시에 적용시키기 - 진행 완료**
   - Redis를 이용해 게시글 목록 정보 캐시로 가져오기
   - Docker를 이용해서 배포하기
   - 해시태그 모델을 포함한 모델링 재구성
<br>

## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?&logo=Django&logoColor=white)
![DRF badge](https://img.shields.io/badge/DRF-%23092E20?&logo=DRF&logoColor=white)
![DRF_SimpleJWT badge](https://img.shields.io/badge/DRF_SimpleJWT-%23092E20?&logo=DRF_SimpleJWT&logoColor=white)

- DB<br>
![SQLite badge](https://img.shields.io/badge/SQLite-%23092E20?&logo=SQLite&logoColor=white)

- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>


<br>

## 📌 과제 분석
<div>
<details>
<summary>과제소개</summary> 
<div markdown="1">
🗣아래 서비스 개요 및 요구사항을 만족하는 SNS 백엔드 서비스를 구현해주세요. <br>

1. **이메일을 ID로 유저 회원가입**
 
2. **유저 로그인 시 JTW 토큰을 발급하고 추후 사용자 인증으로 사용**
 
3. **제목, 내용, 해시태그 등을 입력하여 게시글 생성**
 
4. **게시글 수정**
 
5. **게시글 삭제**
 
6. **게시글 상세보기**

7. **게시글 목록**

</div>
</details>

<details>
<summary>요구사항</summary> 
<div markdown="1">

- **이메일을 ID로 유저 회원가입**
  
- **유저 로그인 시 JTW 토큰을 발급하고 추후 사용자 인증으로 사용**
  
- **제목, 내용, 해시태그 등을 입력하여 게시글 생성**
   - 제목, 내용, 해시태그는 필수 입력사항이며, 작성자 정보는 request body에 존재하지 않고, 해당 API를 요청한 인증정보에서 추출하여 등록 
   - 해시태그는 #로 시작되고 ,로 구분되는 텍스트가 입력

- **게시글 수정**
   - 작성자만 수정 가능

- **게시글 삭제**
   - 작성자만 삭제 가능
   - 작성자는 삭제된 게시글을 다시 복구할 수 있음

- **게시글 상세보기**
   - 모든 사용자는 모든 게시물에 보기권한이 있음
   - 작성자를 포함한 사용자는 본 게시글에 좋아요를 누를 수 있음
   - 좋아요된 게시물에 다시 좋아요를 누르면 취소
   - 작성자 포함한 사용자가 게시글을 상세보기 하면 조회수 1 증가(횟수 제한 없음)

- **게시글 목록**
   - 모든 사용자는 모든 게시물에 보기권한이 있음
   - 게시글 목록에는 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수가 포함
   - 아래 4가지 동작을 쿼리 파라미터로 구현 ex) ?search=..&orderBy=
     - Ordering (= Sorting, 정렬)
     - Searching (= 검색)
     - Filtering (= 필터링)
     - Pagination (= 페이지 기능)

</div>
</details>
</div>

#### ➡️ 분석결과
- 회원가입과 로그인의 권한은 누구나 접근할 수 있게 설정
- 로그인 성공 시, 클라이언트에게 access token과 refresh token을 리턴해주기 위해 DRF simplejwt 라이브러리 이용
- access token 만료 시, 재발급을 위해 DRF simplejwt의 TokenRefreshView 이용 / 재발급 시 refresh token도 갱신되게끔 settings 설정
- 좋아요 기능을 위해 User 모델과 Post 모델 M:N관계로 설정
- 게시글 목록 조회 기능 구현 시, 쿼리 파라미터에 따라 if문을 설정하고 django ORM의 filter, order_by, annotate 메서드 이용
- 게시글 수정 및 삭제 권한을 작성자 본인에게만 접근 가능하게 하기 위해 BasePermission 클래스 오버라이딩 진행
- 게시글 삭제의 경우, 복구를 위해 is_deleted 필드의 값을 Boolean으로 설정
- 좋아요 api url의 경우, POST로 로그인된 유저가 중간 테이블에 있다면 좋아요 취소, 없다면 좋아요 성공으로 설정


<br>

## :black_nib: 이슈 관리
<img width="1137" alt="image" src="https://user-images.githubusercontent.com/95380638/180358840-afcd8fe9-feee-446d-bcca-e07c1053bca3.png">

**깃허브 이슈와 간단차트를 통해 태스크 및 일정관리를 했습니다.** <br>


<br>

## ✨🍰✨ 코드 컨벤션
<img width="597" alt="image" src="https://user-images.githubusercontent.com/95380638/180358976-0e928dcf-8c33-437a-a7c5-50f50445de8e.png">

Formatter
- isort
- black

Lint
- flake8
<br>

**로컬에서 pre-commit 라이브러리를 사용해서 커밋 전 세가지 라이브러리를 한번에 실행하고 통과되지 않는다면 커밋이 불가능하게 설정합니다.**


<br>

## 🌟 API 명세서
<img width="1181" alt="image" src="https://user-images.githubusercontent.com/95380638/180913976-7b45f04a-dd2b-4d88-bc4c-0d5bd7b44e95.png">

- 회원가입은 email과 password를 입력받고 email에 대한 유효성 검사 후 진행합니다.
- 로그인은 회원가입시 입력한 email과 password를 통해서 진행하고 성공 시 access token과 refresh token를 리턴해줍니다.
- 유저가 좋아요를 누른 게시글 목록은 로그인된 유저가 좋아요를 누른 게시글의 id와 제목을 응답해줍니다.
- 유저가 삭제한 게시글 목록은 로그인된 유저가 삭제한 게시글의 id와 제목, 삭제여부를 응답해줍니다.
- access token 및 refresh token 재발급은 refresh token 입력이 필요하고 simplejwt의 settings 설정으로 요청 시 access token과 refresh token 모두 갱신해줍니다.
- 게시글 생성은 제목, 내용, 해시태그 정보를 필수로 입력해야 합니다.
- 게시글 목록 조회는 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수가 포함되며 쿼리 파라미터인 sort, search, hashtags, page&page_count에 따라 각각 정렬, 검색, 필터링, 페이지 기능을 수행합니다.
  - 정렬 기능은 작성일, 좋아요 수, 조회수에 따라 각각 오름차순, 내림차순으로 정렬이 가능합니다. 
  - 검색 기능은 입력된 키워드가 포함된 게시글 목록을 응답합니다.
  - 필터링 기능은 해시태그 하나에 대해서만 검색이 가능합니다.
  - 페이지 기능은 현재 페이지와 1 페이지 당 게시글 수를 조정할 수 있습니다.
- 게시글 상세보기는 해당 게시글이 삭제된 경우, 삭제되었다는 메세지와 함께 404 not found 에러를 발생시킵니다. 또한, 횟수 제한 없이 요청 때마다 조회수가 증가합니다.
- 게시글 수정은 제목, 내용, 해시태그만 수정이 가능합니다.
- 게시글 삭제 및 복구는 PATCH 메소드로 한 번 요청 시 해당 post의 is_deleted 필드의 값을 True 또는 False로 변경합니다. 삭제된 게시글은 조회가 불가능하고 다시 복구하기 위해서는 다시 요청을 해야합니다.
- 특정 게시글 좋아요 및 좋아요 취소는 특정 게시글의 id값을 넣고 요청했을 때 좋아요가 진행됩니다. 이미 좋아요가 된 상태에서 요청하게 되면 좋아요 취소가 진행됩니다.


<br>
<br>
<details>
<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">

- **회원가입**
<img width="858" alt="image" src="https://user-images.githubusercontent.com/95380638/180384250-ef23a478-b480-4aa5-858c-3a4eef98af69.png">

- **로그인**
<img width="861" alt="image" src="https://user-images.githubusercontent.com/95380638/180384537-e37c08a2-5075-4e70-85c1-99d94478f115.png">

- **유저가 좋아요를 누른 게시글 목록**
<img width="856" alt="image" src="https://user-images.githubusercontent.com/95380638/180387449-01a6afb2-21ab-4de6-9143-8753daf81737.png">

- **유저가 삭제한 게시글 목록**
<img width="872" alt="image" src="https://user-images.githubusercontent.com/95380638/180914109-4713b678-dc10-4faf-8832-6d0192f2af35.png">

- **access token 및 refresh token 재발급**
<img width="863" alt="image" src="https://user-images.githubusercontent.com/95380638/180384758-17c9de38-2630-4dda-8ca5-de27f56ead93.png">

- **게시글 생성**
<img width="854" alt="image" src="https://user-images.githubusercontent.com/95380638/180385321-bcda879b-9437-4125-a52a-e23266ca127e.png">

- **게시글 목록 조회**
<img width="876" alt="image" src="https://user-images.githubusercontent.com/95380638/180385517-b29a003c-0d15-4b34-9d18-d7e5188dd846.png">

- **게시글 목록 조회 정렬 기능**

- 작성일(오름차순)
<img width="875" alt="image" src="https://user-images.githubusercontent.com/95380638/180674053-f18eff19-8142-405b-a1c1-adb6d5bfefa8.png">     

- 작성일(내림차순)
<img width="881" alt="image" src="https://user-images.githubusercontent.com/95380638/180674214-aff229c4-2665-42f7-8bcf-1f5f5fab0de4.png">

- 좋아요 수(오름차순)
<img width="881" alt="image" src="https://user-images.githubusercontent.com/95380638/180674340-6a817079-6c47-410f-80c9-56c5f501834d.png">

- 좋아요 수(내림차순)
<img width="887" alt="image" src="https://user-images.githubusercontent.com/95380638/180674434-2ebd6941-e67e-4ca7-842e-d71e931bfa25.png">

- 조회수(오름차순)
<img width="883" alt="image" src="https://user-images.githubusercontent.com/95380638/180674523-f06f51fe-7d63-4941-89fc-b71adbfbe4e2.png">

- 조회수(내림차순)
<img width="881" alt="image" src="https://user-images.githubusercontent.com/95380638/180674578-44f8a0a6-99b6-4139-9cc2-3c5d9b8d9d66.png">


- **게시글 목록 조회 키워드 검색 기능**
<img width="879" alt="image" src="https://user-images.githubusercontent.com/95380638/180387138-e735de9e-de92-49a9-87c6-5b95978fb207.png">

- **게시글 목록 조회 필터링 기능**
<img width="875" alt="image" src="https://user-images.githubusercontent.com/95380638/180648796-9f656959-0046-42ce-b21f-97b04435f3cf.png">

- **게시글 목록 조회 페이지 기능**
<img width="895" alt="image" src="https://user-images.githubusercontent.com/95380638/180648848-0ed3ec0d-77aa-4782-b6d6-387de308f1bd.png">

- **게시글 상세 보기**
<img width="859" alt="image" src="https://user-images.githubusercontent.com/95380638/180385726-3d78d3f1-1541-4b31-ba09-ea3a9be98b07.png">

- **게시글 수정**
<img width="874" alt="image" src="https://user-images.githubusercontent.com/95380638/180386097-fdd37942-8334-47f1-a5c9-a0c3bd5f4050.png">

- **게시글 삭제 및 복구**
<img width="863" alt="image" src="https://user-images.githubusercontent.com/95380638/180386304-0b989a0a-1392-4ada-b498-cd7c3b3cdce3.png">
<img width="860" alt="image" src="https://user-images.githubusercontent.com/95380638/180386595-9b9c2f20-f4e2-4d94-9c89-5c216e3b1c3b.png">

- **특정 게시글 좋아요 및 좋아요 취소**
<img width="869" alt="image" src="https://user-images.githubusercontent.com/95380638/180386814-49bd58a4-6070-456e-89b6-4b1db3dad829.png">
<img width="860" alt="image" src="https://user-images.githubusercontent.com/95380638/180386850-aa50e48a-1fd0-4f24-a987-31613a26b997.png">



</div>
</details>

<br>

## 📋 ERD
<img width="870" alt="image" src="https://user-images.githubusercontent.com/95380638/180359279-83c20880-586e-40f0-b7fe-32be7b3cd6c3.png">

**최종 모델링입니다. User 모델과 Post 모델은 1:N 관계로 설정했습니다.**    
**좋아요 기능을 위해 User 모델과 Post 모델 중간 테이블이 설정되어 있습니다.**

<br>

## :open_file_folder: 어드민 페이지
<img width="1435" alt="image" src="https://user-images.githubusercontent.com/95380638/180648350-05d245cd-c285-4847-b324-03d0ec0dfe9f.png">

**django 어드민 페이지로 Post 모델의 데이터를 관리합니다.**

<br>

## ✔ 커밋 컨벤션
```terminal
# --- 제목(title) - 50자 이내로 ---
# <타입(type)> <제목(title)>
# 예시(ex) : Docs(Add) Commit docs Add

# --- 본문(content) - 72자마다 줄바꾸기  ---
# 예시(ex) :
# - Workflow
# 1. 커밋 메시지에 대한 문서 제작 추가.
# 2. commit message docs add.

# --- 꼬리말(footer) ---
# <타입(type)> <이슈 번호(issue number)>
# 예시(ex) : Fix #122

# --- COMMIT END ---
# <타입> 리스트
#   init    : 초기화
#   feat  : 기능추가
#   add     : 내용추가
#   update  : 기능 보완 (업그레이드)
#   fix     : 버그 수정
#   refactor: 리팩토링
#   style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
#   docs    : 문서 (문서 추가(Add), 수정, 삭제)
#   test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
#   chore   : 기타 변경사항 (빌드 스크립트 수정 등)
# ------------------
#     제목 첫 글자를 대문자로
#     제목은 명령문으로
#     제목 끝에 마침표(.) 금지
#     제목과 본문을 한 줄 띄워 분리하기
#     본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
#     본문에 여러 줄의 메시지를 작성할 땐 "-" 혹은 "번호"로 구분
# ------------------
```


## ✔ 코드 컨벤션
- Class
  - Pascal case
- Model
  - Pascal case
- Function
  - snake case
- Variables
  - snake case

<br>

## 🧑‍💻 브랜치 전략
- main : 최종적으로 문제가 없는 기능을 포함하는 브랜치
- feature : issue에 부여한 기능을 개발하는 브랜치로 기능 개발이 완료되면 main 브랜치에 Merge 진행

<br>

## 📝 주석 처리
```python
# url : GET, POST api/v1/posts
class PostsView(APIView):
    """
    Assignee : 상백

    GET : 게시글 목록을 조회하는 메서드입니다.
    POST : 게시글을 생성하는 메서드입니다.
    """
    ...
```
- class 하단에 해당 class에 대한 설명을 여러 줄 주석으로 기재
- API에 대한 코드라면 한 줄 주석으로 API URL 기재
