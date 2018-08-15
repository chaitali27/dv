float x , y;
void setup()
{
  size(400,400);
  strokeWeight(3);
}
void draw()
{
  translate(0,200);
  x = x +PI/3600;
  y = 40*sin(40*x + PI);

  point(x*500,y);
  
  
}
