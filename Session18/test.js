function buySomething(nowMoney) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const pay = parseInt(prompt("금액 입력"));
            const remain = nowMoney - pay;
            
            console.log(`${pay}원 지불`);
            if (remain >= 0) {
                resolve(remain);
            } else {
                reject(`잔액 부족: 현재 잔액 ${nowMoney}원`);
            }
        }, 2000);
    });
}

function remainMoney(money) {
    console.log(`잔액: ${money}원`);
}

// buySomething(1000).then((res) => {
//     console.log(`잔액: ${res}원`);
// });

// buySomething(1000).then((res) => {
//     console.log(`잔액: ${res}원`);
// });



buySomething(1000)
    .then((remain) => {
        remainMoney(remain);
        return buySomething(remain)
    })
    .then((remain) => {
        remainMoney(remain);
        return buySomething(remain);
    })
    .then((remain) => {
        remainMoney(remain);
    })
    .catch((error) => {
        console.log(error);
    }
);

// 비동기 async await
async function testAsync() {
    try {
        const remain = await buySomething(1000);
        console.log(`잔액: ${remain}원`);
        
    } catch (error) {
        console.log(error);
    }
}
