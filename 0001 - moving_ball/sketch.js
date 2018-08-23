function setup() {

createCanvas (1000,600);
strokeWeight(3);

}
var x = 200, s = 5;

function draw()
 {

   clear();
   x = x + s;

  ellipse(x, 300, 200, 200);

  if(x>850)
  {s = s - 5
  }

  if(x<150)
  {s = s + 5
  }
}
