function setup() {

createCanvas (600,600);
strokeWeight(3);
}
var r = 100, a = 1, x, y;

function draw()
{
clear();
translate(300,300);
  x = r*sin(a*PI/100);
  y = r*cos(a*PI/100);
  a = a +1;
  ellipse(2*x,y,40,40);
  ellipse(0,0,40,40);
}
