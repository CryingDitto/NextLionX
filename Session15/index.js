const login = () => {

    const id = getId();
    //제대로 id를 입력해야만 id가 제대로 된 값이 들어있음.
    //아니면 underined.
    //!undefined => true
    if (!id) return;

    const password = getPassword();
}

const getId = () => {
    const id = prompt('아이디를 입력해주세요.');
    if (!id) {
        alert("취소되었습니다.");
        return;
    }
    if (id !== "likelion") {
        alert("아이디를 찾을 수 없습니다.");
        return;
    }

    return id;
}

const getPassword = () => {
    const password = prompt("비밀번호를 입력해주세요.");

    if (!password) {
        alert('취소되었습니다.');
        return;

    }
    if (password == "220704") {
        alert("환영합니다!");
        return password;
    }

    alert("인증에 실패했습니다.");
    getPassword(); //다시 비밀번호 받기 호출
}

const loginButton = document.querySelector("button");
