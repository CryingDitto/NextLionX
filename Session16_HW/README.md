# 실험/알바/과외 등록 및 신청
## 기능
- 일할 사람은 일을 찾아 신청
- 게시글을 올려 구인, 들어온 신청에 대해 승인

## 구현한 기능 (Apps)
### main 
- 메인 화면
    - 안내용 모달
        - 기능에 대한 간단한 설명을 첫 화면에서 제시함
        - 오늘은 더 이상 보지 않기를 누르면 쿠키가 생성되어 하루 동안 모달이 보이지 않음
        - 메인 화면에서 안내 사항을 누를 경우 다시 모달의 내용을 확인할 수 있음
    ![modal](https://user-images.githubusercontent.com/101262081/183332311-0c94c7b2-8489-4c00-8acb-7c0b852c660a.jpg)

    - 게시글 제목, 작성자, 작성 날짜, 게시글 카테고리 보여줌
        - 로그인 안 한 경우 (회원가입, 로그인 메뉴)
        ![main wo login](https://user-images.githubusercontent.com/101262081/183332098-b5b9b1f6-b419-4b01-98c4-a74a617e7798.jpg)
        - 로그인 한 경우 (글 쓰러 가기, 마이페이지, 로그아웃 메뉴)
        ![main with login](https://user-images.githubusercontent.com/101262081/183332187-74ee4723-3a60-4548-8197-4d88d1d74135.jpg)


- 게시글 상세
    - 게시글의 내용을 볼 수 있고, 댓글 작성/삭제 가능
    - 게시글의 일 신청 가능
    ![남의 글](https://user-images.githubusercontent.com/101262081/183332503-9630d68c-c7b1-410e-900c-b7a2bd18057c.jpg)

    
    - 게시글 작성자의 경우 게시글 수정, 삭제 가능. 또한 댓글 아래에 신청서 정보를 볼 수 있음
    ![자기 글](https://user-images.githubusercontent.com/101262081/183332345-5fcf6576-981a-42f1-8742-b8b6ba489d32.jpg)
    ![신청목록](https://user-images.githubusercontent.com/101262081/183332372-ce787cd8-005b-4d0d-8f1b-3ad2202ec66b.jpg)

    
- 게시글 작성
    - 카테고리(실험/알바/과외), 제목, 일 설명을 적은 뒤 게시물을 만들 수 있음.
    ![게시물 작성](https://user-images.githubusercontent.com/101262081/183332484-661efa88-2df7-4a29-9e58-e5864c6a41ba.jpg)


### accounts 
- 회원가입
- 로그인
- 마이페이지
    - 개인정보 (이메일, 성별, 나이, 손잡이 등등) 보여줌
    - 신청한 알바(게시글)의 제목과 자신이 신청한 시간을 보여줌
    ![mypage](https://user-images.githubusercontent.com/101262081/183336213-acdc38b1-fe0d-4d67-89c7-bba6b82c8150.jpg)
    ![신청 목록](https://user-images.githubusercontent.com/101262081/183336222-36b008d1-44f6-4392-b6ef-dc0834cea4a8.jpg)

- 마이페이지 수정
    - 기존에 등록한 정보 수정 가능

### register
- 실험/알바/과외 신청
    - 신청자의 이름, 이메일, 성별, 나이, 손잡이 등의 정보는 등록된 내용을 기반으로 전달
    - 신청자는 1개 이상, 최대 3개의 날짜만 입력해 제출하면 됨 (Date & Time 1은 필수, 나머지 2개는 선택 입력)
    ![register](https://user-images.githubusercontent.com/101262081/183335199-f85b2537-33dc-451e-8cc6-4bf03cb7494f.jpg)

    
- 담당자 승인 및 날짜 확정
    - 승인 시 확정 날짜를 적어줌.
    ![image](https://user-images.githubusercontent.com/101262081/183335340-c9bac206-f6e6-41d0-98dc-9e32e34c6521.png)



### 더 만들고 싶은 기능
- 게시물 끌올 기능 (update 시점으로 게시물 정렬)
- 게시물 별 신청서 모아보기 기능
- 신청 거절 기능
- 신청 철회(삭제) 기능
- 이메일 보내기 기능
- javascript를 활용한... 무언가...


## 후기
1. 만들어보고 싶은 기능을 만들어보는 좋은 시간이었다. 근데 아직 미완인 게 함정.
2. CSS가 안 먹혀서 이래저래 헤맸는데 incognito 모드로 브라우저를 새로 열어 링크를 입력해보면 잘 된다. 근데 잘 되는 걸 확인했는데 왜 빡치지? ~~그동안 헤맨 게 억울해서~~ 
3. 에러 메시지에 대한 이해도가 상승했다. 비행기 타고 다니면서 비행기 안에서 만들었는데 인터넷이 되지 않는 환경이라 에러 메시지를 확인해가며 어떻게든 에러를 해결했다. 
4. 웹 폰트는 인터넷 안 되는 환경에서는 사라지더라. ~~당연하지 WEB폰트니까...~~ 근데 비행기에서 어라 왜 폰트 안 먹지??? 이러면서 헤맴...ㅎ
5. main -> accounts -> register 순으로 개발했는데, 큰 그림만 가지고 만든 것치고는 그래도 차근차근 잘 만든 것 같다. 좀 더 상세하게 기능을 나눠서 체크리스트로 하나씩 지워가며 개발하면 기능을 놓치지 않고 꼼꼼하게 개발할 수 있을 것 같다.
