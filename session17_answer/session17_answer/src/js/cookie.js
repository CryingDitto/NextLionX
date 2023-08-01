// 📁 cookie.js
// 쿠키 관련 함수들을 저장하고 내보낸다.

// 만료기한을 정해 쿠키 생성하기
const setCookie = (name, value, expireDays) => {
  let today = new Date();
  today.setDate(today.getDate() + expireDays);
  document.cookie = `${name}=${value};expires=${today.toGMTString()}`;
};

// 쿠키를 가져오기
const getCookie = (name) => {
  // 로컬에 저장된 모든 쿠키 읽어오기
  let cookie = document.cookie;
  // 쿠키가 있으면 쿠키들을 배열에 저장
  // 배열을 순회하면서 쿠키의 name에 대한 value값을 리턴
  if (document.cookie) {
    let cookieArray = cookie.split("; ");
    for (let index in cookieArray) {
      let cookieName = cookieArray[index].split("=");
      if (cookieName[0] == name) {
        return cookieName[1];
      }
    }
  }
  return;
};

// 쿠키를 삭제하기
const delCookie = (name) => {
  // expires 옵션값을 과거로 지정하면 쿠키가 삭제된다.
  // document.cookie = 'user-id=; expires=Sat, 01 Jan 1972 00:00:00 GMT'
  console.log(name);
  setCookie(name, "", 0);
  alert("쿠키를 삭제했습니다.");
};

export { setCookie, getCookie, delCookie };
