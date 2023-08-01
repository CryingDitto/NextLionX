// 📁 cookie.js
// 쿠키 관련 함수들을 저장하고 내보낸다.
// path, domain, expires, secure 등 옵션 사용 가능
// 옵션은 key=value 뒤에 나열하고 ;로 구분
// document.cookie = "user=Next; path=/; expires=Tue, 19 Jan 2022 03:14:07 GMT"

// 만료기한을 정해 쿠키 생성하기
const setCookie = (name, value, expireDays) => {
  //현재 날짜와 시간이 저장된 Date 객체 생성
  let today = new Date();
  //setDate, getDate : Date 객체에 시간을 저장하고 가져올 때 사용하는 방법
  today.setDate(today.getDate() + expireDays); // 오늘 날짜에 expireDays 더해서 만료시간 구함
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
    // console.log(cookieArray);
    for (let index in cookieArray) {
      // 각 쿠키가 name=value 순으로 구성되어 있으므로
      let cookieName = cookieArray[index].split("=");
      if (cookieName[0] == name) {
        //쿠키의 이름이 받은 name과 일치하면 
        //그 이름에 해당하는 value 가져옴
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
