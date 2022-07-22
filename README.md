# pre-onboarding-3rd-SNS

<br>

## ✅ 프로젝트 개요
- 원티드 프리온보딩 개인과제를 진행합니다. 
- 시나 소설 등 문학 작품의 일부분을 공유하는 SNS 서비스입니다. 
- 사용자들은 해당 서비스에서 회원가입 및 로그인 이후 본인이 좋아하는 글을 생성하고 다른 사용자들의 글을 확인할 수 있습니다.
- 해시태그로 해당 글의 주제나 단어, 작가를 기재한다면 다른 사용자들로부터 검색이 용이해집니다.

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
<img width="991" alt="image" src="https://user-images.githubusercontent.com/95380638/180363355-6145f114-ebaf-4f88-ab88-26d969fff651.png">

- ...  

<br>
<br>
<details>
<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">

- 회원 생성


- 회원 로그인


- 회원 로그아웃


</div>
</details>

<br>

## 📋 ERD
<img width="870" alt="image" src="https://user-images.githubusercontent.com/95380638/180359279-83c20880-586e-40f0-b7fe-32be7b3cd6c3.png">

**최종 모델링입니다. User 모델과 Post 모델은 1:N 관계로 설정했습니다.**    
**좋아요 기능을 위해 User 모델과 Post 모델 중간 테이블이 설정되어 있습니다.**




