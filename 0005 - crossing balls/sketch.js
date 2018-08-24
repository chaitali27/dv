function setup() {

createCanvas (600,400);
strokeWeight(3);
}
var x = 60, s = 5;

function draw()
 {

   clear();
   x = x + s;

  ellipse(x, 200, 100, 100);
  ellipse(600-x, 200, 100, 100);

  if(x>540)
  {s = 0
  }

  if(x<60)
  {s = 0
  }
}
