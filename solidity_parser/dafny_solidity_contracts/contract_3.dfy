method ifelseifelse(x : int) returns (result : int)
  ensures result > 0
  requires x > 0
{
  if(x == 3){
    result :=4 ;
  }

  else if(x == 4){
    result := 5;
  }

  else{
    result := 6;
  }
  assert result > 0;
  return result;
}

method Main(){
  var z1 :=3;
  assert z1 == 3;
  var result1 := ifelseifelse(z1);

  print result1;
  
}
