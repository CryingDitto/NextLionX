// 📁 index.js
import { openModal, closeModal } from "./modal.js";
import { setCookie, getCookie } from "./cookie.js";

// JS에서 DOM element 가져올 때 관용적으로 $표시를 사용한다.
// $표시로 DOM element return해서 반복 줄이는 함수
const $ = (selector) => document.querySelector(selector);
// const modal = $(".modal-container"); // $(선택자) 넣어주면 됨.


function App() {

  // App 이라는 객체를 생성하고 그 App의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 초기화 메소드를 만든다.
  this.init = () => {
    // 모달을 닫는 쿠키가 있는지 확인한다.
    if (getCookie("modalClose") === "true") {
      // closeModal();
      return;
    }
    // 모달을 닫는 쿠기가 없다면 무조건 모달을 열어둔다.
    openModal();
  };

  // modal.js 에서 넘어옴
  // //모달 여는 함수
  // const openModal=() => {
  //   modal.classList.add("open");
  // };
  // //모달 닫는 함수
  // const closeModal=() => {
  //   modal.classList.remove("open");
  // };


  
  //모달 열기 버튼 눌렀을 때 모달 여는 함수 실행
  $(".modal-open").addEventListener("click", () => {
    openModal();
  });

  $(".modal-container").addEventListener("click", (event) => {
    if (event.target === $(".modal-container")) {
      // 자식의 이벤트까지 부모의 이벤트로 생각하는 bubbling 방지를 위해
      // 모달 영역 외, 배경 부분 클릭할 때만 모달 close
      closeModal();
    }
  });

  //모달 닫기 버튼 눌렀을 때 모달 닫는 함수 실행
  $(".modal-close").addEventListener("click", () => {
    closeModal();
  });

  // 오늘 보지 않기 버튼을 누르면 만료기간이 1일인 쿠키를 생성하고 모달을 닫는다.
  $(".modal-stop-button").addEventListener("click", () => {
    // 하루 기한의 쿠키를 생성한다. (쿠키 생성시 이름은 modal-closed, 값은 true로 설정한다.)
    // setCookie(name, value, expireDay)
    setCookie('modalClose', 'true', 1);
    // 모달을 닫는다.
    closeModal();
  });

}

// 페이지 최초로 접근했을 때 app 이라는 객체를 생성한다.
const app = new App();
// 그 app의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 한다.
app.init();
