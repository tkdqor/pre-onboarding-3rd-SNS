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
<img width="1176" alt="스크린샷 2022-07-15 오후 4 35 39" src="https://user-images.githubusercontent.com/76423946/179175389-367d73d6-b0dc-4131-9bec-20cf4f73fad8.png">

- ...  

<br>
<br>
<details>
<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">

- 회원 생성
<img width="994" alt="image" src="https://user-images.githubusercontent.com/89897944/179219478-9dfc392f-33b2-4ab1-b5c9-1cf079ee362d.png">

- 회원 로그인
<img width="1149" alt="image" src="https://user-images.githubusercontent.com/89897944/179219524-86991749-5838-4780-86cf-7a1dc88fc11f.png">

- 회원 로그아웃
<img width="977" alt="image" src="https://user-images.githubusercontent.com/89897944/179219994-549bd82a-d54d-4e0e-8277-36c4a972d9a4.png">

- 회원 로그아웃( 토큰 유지 )
<img width="891" alt="image" src="https://user-images.githubusercontent.com/89897944/179220054-cc50ccae-20da-4616-b40d-af7248da9198.png">

- 전체 회원 조회 : admin 유저만 가능
<img width="910" alt="image" src="https://user-images.githubusercontent.com/89897944/179220138-67f24c97-4b3a-433b-b9f9-f003041c8fec.png">
<img width="987" alt="image" src="https://user-images.githubusercontent.com/89897944/179220324-65764b7d-f03e-4c8c-8f3e-b751a285a730.png">

- 회원 단건 조회 : 회원정보와 해당 회원의 레이드 레코드가 같이 출력
<img width="1082" alt="image" src="https://user-images.githubusercontent.com/89897944/179220461-15805b45-65ee-4eeb-b6ae-c29c13f2887d.png">

- 보스레이드 상태 조회
<img width="932" alt="image" src="https://user-images.githubusercontent.com/89897944/179220513-e4a4734c-5710-4d2f-8448-fbf11393c641.png">

- 보스레이드 시작
<img width="889" alt="image" src="https://user-images.githubusercontent.com/89897944/179220550-ca4c9498-d0aa-4440-8b93-d936cf01ee74.png">

- 보스레이드 종료
<img width="752" alt="스크린샷 2022-07-17 오후 10 14 31" src="https://user-images.githubusercontent.com/76423946/179400113-bad5850d-1fa1-4a40-ae5d-82426f0bb575.png">

- 랭킹 확인
<img width="1053" alt="image" src="https://user-images.githubusercontent.com/89897944/179220633-fa53af23-38b1-48ac-9eef-93664112f734.png">


</div>
</details>

<br>

## 📋 ERD
<img width="870" alt="image" src="https://user-images.githubusercontent.com/95380638/180359279-83c20880-586e-40f0-b7fe-32be7b3cd6c3.png">

**최종 모델링입니다. User 모델과 Post 모델은 1:N 관계로 설정했습니다.**    
**좋아요 기능을 위해 User 모델과 Post 모델 중간 테이블이 설정되어 있습니다.**




