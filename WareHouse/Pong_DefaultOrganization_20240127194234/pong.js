'''
This is the main JavaScript file for the Pong game.
It includes the game logic and the classes for the Paddle and Ball.
Now, it also includes a simple AI for the second paddle.
'''
// Get the canvas and context
const canvas = document.getElementById('pong');
const context = canvas.getContext('2d');
// Initialize scores for both players
let score1 = 0;
let score2 = 0;
// Create the Paddle class
class Paddle {
    constructor(x, y, width, height, color, dy) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
        this.dy = dy;
    }
    draw() {
        context.fillStyle = this.color;
        context.fillRect(this.x, this.y, this.width, this.height);
    }
    move() {
        if (this.y + this.dy < 0) {
            this.y = 0;
        } else if (this.y + this.dy > canvas.height - this.height) {
            this.y = canvas.height - this.height;
        } else {
            this.y += this.dy;
        }
    }
}
// Create the Ball class
class Ball {
    constructor(x, y, radius, color, dx, dy) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = color;
        this.dx = dx;
        this.dy = dy;
    }
    draw() {
        context.beginPath();
        context.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        context.fillStyle = this.color;
        context.fill();
    }
    move() {
        if (this.x + this.dx < 0) {
            this.dx = -this.dx;
            score2++; // Player 2 scores
        } else if (this.x + this.dx > canvas.width) {
            this.dx = -this.dx;
            score1++; // Player 1 scores
        }
        if (this.y + this.dy < 0 || this.y + this.dy > canvas.height) {
            this.dy = -this.dy;
        }
        this.x += this.dx;
        this.y += this.dy;
    }
}
// Create the paddles and the ball
let paddle1 = new Paddle(20, canvas.height / 2 - 50, 20, 100, '#fff', 2);
let paddle2 = new Paddle(canvas.width - 40, canvas.height / 2 - 50, 20, 100, '#fff', 2);
let ball = new Ball(canvas.width / 2, canvas.height / 2, 10, '#fff', 2, 2);
// The draw function
function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    paddle1.draw();
    paddle2.draw();
    ball.draw();
    context.font = '30px Arial';
    context.fillText(score1, canvas.width / 4, 50); // Display Player 1's score
    context.fillText(score2, canvas.width * 3 / 4, 50); // Display Player 2's score
}
// The update function
function update() {
    paddle1.move();
    // AI for paddle2
    if(ball.y < paddle2.y) {
        paddle2.y -= paddle2.dy;
    } else if(ball.y > paddle2.y + paddle2.height) {
        paddle2.y += paddle2.dy;
    }
    ball.move();
}
// The main game loop
function main() {
    draw();
    update();
    requestAnimationFrame(main);
}
// Start the game loop
main();
// Add event listeners for the arrow keys
window.addEventListener('keydown', function(event) {
    switch (event.keyCode) {
        case 38: // Up arrow
            paddle1.dy = -2;
            break;
        case 40: // Down arrow
            paddle1.dy = 2;
            break;
    }
});
window.addEventListener('keyup', function(event) {
    switch (event.keyCode) {
        case 38: // Up arrow
        case 40: // Down arrow
            paddle1.dy = 0;
            break;
    }
});