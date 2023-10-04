const button = document.querySelector(".again-button");

const overlay = document.querySelector(".overlay");

const rows = 20;

const columns = 20;

const boxSize = 25;

let board;

let ctx;

let snakeBody = [];

let snakeX = 5 * boxSize;
let snakeY = 5 * boxSize;

let moveX = 0;
let moveY = 0;
let gameOver = false;

window.onload = function () {
  board = document.getElementById("board");
  board.height = rows * boxSize;
  board.width = columns * boxSize;
  ctx = board.getContext("2d");

  randPlaceApple();
  setInterval(update, 200);
  document.addEventListener("keyup", move);
};

button.addEventListener("click", function () {
  overlay.classList.add("hidden");
  location.reload();
});

function update() {
  if (gameOver) {
    return;
  }
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, board.width, board.height);

  ctx.fillStyle = "red";
  ctx.fillRect(appleX, appleY, boxSize, boxSize);

  for (let i = snakeBody.length - 1; i > 0; i--) {
    snakeBody[i] = snakeBody[i - 1];
  }

  if (snakeBody.length) {
    snakeBody[0] = [snakeX, snakeY];
  }

  if (snakeX == appleX && snakeY == appleY) {
    snakeBody.push([appleX, appleY]);
    randPlaceApple();
  }
  ctx.fillStyle = "lime";
  snakeX += moveX * boxSize;
  snakeY += moveY * boxSize;
  ctx.fillRect(snakeX, snakeY, boxSize, boxSize);

  for (let i = 0; i < snakeBody.length; i++) {
    ctx.fillRect(snakeBody[i][0], snakeBody[i][1], boxSize, boxSize);
  }

  if (
    snakeX < 0 ||
    snakeY < 0 ||
    snakeX > columns * boxSize ||
    snakeY > rows * boxSize
  ) {
    gameOver = true;
    overlay.classList.remove("hidden");
  }

  for (i = 0; i < snakeBody.length; i++) {
    if (snakeX == snakeBody[i][0] && snakeY == snakeBody[i][1]) {
      gameOver = true;
      overlay.classList.remove("hidden");
    }
  }
}

function randPlaceApple() {
  appleX = Math.floor(Math.random() * columns) * boxSize;
  appleY = Math.floor(Math.random() * rows) * boxSize;
}

function move(e) {
  if (e.key == "ArrowUp" && moveY != 1) {
    moveX = 0;
    moveY = -1;
  } else if (e.key == "ArrowDown" && moveY != -1) {
    moveX = 0;
    moveY = 1;
  } else if (e.key == "ArrowLeft" && moveX != 1) {
    moveX = -1;
    moveY = 0;
  } else if (e.key == "ArrowRight" && moveX != -1) {
    moveX = 1;
    moveY = 0;
  }
}
