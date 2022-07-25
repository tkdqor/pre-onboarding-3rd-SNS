# pre-onboarding-3rd-SNS

<br>

## ✅ 프로젝트 개요
- 원티드 프리온보딩 개인과제를 진행합니다. 
- 시나 소설 등 문학 작품의 일부분을 공유하는 SNS 서비스입니다. 
- 사용자들은 해당 서비스에서 회원가입 및 로그인 이후 본인이 좋아하는 글을 생성하고 다른 사용자들의 글을 확인할 수 있습니다.
- 해시태그로 해당 글의 주제나 단어, 작가를 기재한다면 다른 사용자들로부터 검색이 용이해집니다.

📌 **개발기간** : 2022.07.20 ~ 2022.07.26

<br>

## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?&logo=Django&logoColor=white)

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
<img width="1195" alt="image" src="https://user-images.githubusercontent.com/95380638/180648653-4d568178-0e62-403d-82a9-b92dcf170aa6.png">

- ...  

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


