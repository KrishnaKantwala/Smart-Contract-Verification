method ifelsenested(x : int) returns (result : int)
ensures result > 7
requires x > 6
{
   if(x < 10) {   // if else statement
     if(x == 8) {   // if else statement
        result := 9;
      } else {
                result := 10;
            }
      }
   else {
            result := 11;
        }
   return result;
}

method Main(){
  var z1 :=8;
  assert z1 == 8;
  var result1 := ifelsenested(z1);

  print result1;

}