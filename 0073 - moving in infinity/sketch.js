function setup() {

createCanvas (800,800);
strokeWeight(3);
}
var r = 100, a = 1, x, y;

function draw()
{
clear();
translate(400,400);
  x = r*sin(2*a*PI/100);
  y = r*cos(a*PI/100);
  a = a +1;
  ellipse(2*y,x,40,40);
}
