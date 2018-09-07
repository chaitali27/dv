function setup() {

createCanvas (600,400);
strokeWeight(3);
}
var r = 100, a = 1, x, y;

function draw()
{
clear();
translate(200,200);
  x = r*sin(a*PI/100);
  y = r*cos(a*PI/100);
  a = a +1;
  ellipse(x,y,40,40);
}
