function setup() {

createCanvas (1200,600);
strokeWeight(3);
noFill();
}
var x = 0, y = 0, u = 100, g = 9.8,PI = 3.14, th = PI/4, t = 0 ;

function draw()
{
clear();
x = u*cos(th)*t;
y = 600 - (u*sin(th)*t - 0.5*g*t*t);
ellipse(x,y,10,10);
t = t + 0.05;
}
