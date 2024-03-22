// function sayHello() {
//   console.log('hi');
// }

// 1초마다 1번씩 실행
// setInterval(sayHello, 1000);

// 1회성 5초뒤에 1번 실행
// setTimeout(sayHello, 5000);

// console.log(startTime);

let startBtn = document.querySelector('.start');
let stopBtn = document.querySelector('.stop');
let startTime, timer;

function setTime() {
  const currentTime = new Date();
  const totalTime = new Date(currentTime - startTime);
  // let hour = totalTime.getHours();
  let minutes = totalTime.getMinutes().toString();
  let seconds = totalTime.getSeconds().toString();
  let time = document.querySelector('.time');
  // time.innerHTML = hour + ':' + minutes + ':' + seconds;
  time.innerHTML = `${minutes.padStart(2, '0')}:${seconds.padStart(2, '0')}`;
}

startBtn.addEventListener('click', function () {
  startTime = new Date();
  timer = setInterval(setTime);
});

stopBtn.addEventListener('click', function () {
  clearInterval(timer);
});
