// 📁 index.js
import { openModal, closeModal } from "./modal.js";
import { getCookie, setCookie } from "./cookie.js";

// JS에서 DOM element 가져올 때 관용적으로 $표시를 사용한다.
// $표시로 DOM element return해서 반복 줄이는 함수
const $ = (selector) => document.querySelector(selector);

function App() {
  this.schedule = {
    session: [
      {
        title: "Javascript UI 모달 세션",
        time: "8월 1일",
        place: "경영본관 2층",
      },
      {
        title: "Javascript 동작 원리 및 비동기 복습",
        time: "8월 8일",
        place: "경영본관 2층",
      },
      {
        title: "AWS EC2 배포 세션",
        time: "8월 11일",
        place: "경영본관 2층",
      },
      {
        title: "디자인 스페셜 세션",
        time: "8월 25일",
        place: "경영본관 2층",
      },
      {
        title: "개발자도구 활용법 및 프론트,백 개괄 세션",
        time: "8월 29일",
        place: "경영본관 2층",
      },
    ],
    event: [
      {
        title: "서울대X고려대 연합 아이디어톤",
        time: "8월 13일",
        place: "어디",
      },
      {
        title: "서울대X고려대 연합 해커톤",
        time: "8월 20일",
        place: "어디어디",
      },
    ],
    study: [],
  };

  this.currentCategory = "session";

  this.init = () => {
    //스케줄 불러오는 함수를 호출해 첫 페이지 렌더링시 화면에 보여준다.
    renderScheudule();
    // 모달을 닫는 쿠키가 있는지 확인한다.

    if (getCookie("closeModal")) {
      closeModal();
      return;
    }
    // 모달을 닫는 쿠기가 없다면 무조건 모달을 열어둔다.
    openModal();
  };

  $(".btn-open-modal").addEventListener("click", () => {
    openModal();
  })

  $(".modal-close").addEventListener("click", () => {
    closeModal();
  })

  $(".modal-container").addEventListener("click", (event) => {
    if (event.target === $(".modal-container")) {
      // 자식의 이벤트까지 부모의 이벤트로 생각하는 bubbling 방지를 위해
      // 모달 영역 외, 배경 부분 클릭할 때만 모달 close
      closeModal();
    }
  });

  
  // 오늘 보지 않기 버튼을 누르면 만료기간이 1일인 쿠키를 생성하고 모달을 닫는다.
  $(".modal-stop-button").addEventListener("click", () => {
    // 하루 기한의 쿠키를 생성한다. (쿠키 생성시 이름은 modal-closed, 값은 true로 설정한다.)
    // setCookie(name, value, expireDay)
    setCookie('modalClose', 'true', 1);
    // 모달을 닫는다.
    closeModal();
  });

  const renderScheudule = () => {
    const scheduleListTemplate = this.schedule[this.currentCategory]
      .map((item, index) => {
        return `<li data-schedule-id="${index}" class="flex flex-col items-center p-10">
          <span class="p-10 schedule-title text-purple">${item.title}</span>
          <div>
            <span class="p-10 schedule-time">${item.time}</span>
            <span class="p-10 schedule-place">${item.place}</span>
          </div>
        </li>`;
      })
      .join("");
    // HTML에 추가해서 넣어준다.
    $("#schedule-list").innerHTML = scheduleListTemplate;
  };

  // 카테고리바 선택에 따른 UI 변경
  // 참고: 이벤트 위임
  $("nav").addEventListener("click", (e) => {
    const isCategoryButton = e.target.classList.contains("category-name");
    if (isCategoryButton) {
      const categoryName = e.target.dataset.categoryName;
      // 카테고리 변경 업데이트
      this.currentCategory = categoryName;
      $(".category-title").innerText = e.target.innerText;
      renderScheudule();
    }
  });
}

// 페이지 최초로 접근했을 때 app 이라는 객체를 생성한다.
// new 연산자로 생성된 인스턴스는 하나의 라이프사이클을 가지고, 이거에 대한 개별적인 상태 관리가 가능해진다.
const app = new App();
// 그 app의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 한다.
app.init();
