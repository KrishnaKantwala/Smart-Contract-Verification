
method ifalone(y : int) returns (result : int)
  requires y == 2
  {
    var result := 3
    return result;
  }

method Main(){
  var z1 := 2;
  var result1 := ifalone(z1);
  assert z1 == 2;
  print result1;
}