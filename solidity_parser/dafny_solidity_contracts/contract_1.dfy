method ifelse(x: int) returns (result : int)
requires x >= 0
{
  if(x == 0){
    result :=1 ;
  }
  else{
    result :=2 ;
  }
  assert result > 0;
  return result;
}

method Main(){
  var z1 :=0;
  assert z1 == 0;
  var result1 := ifelse(z1);

  print result1;
  print "\n";
  var z2 :=1;
  assert z2 >0 ;
  var result2 := ifelse(z2);

  print result2;
}
