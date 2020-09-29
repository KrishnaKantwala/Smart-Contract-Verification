method addSub(a:int, b:int)  returns (result:int)
    requires a > 5
    requires b > 10
    ensures result >= 0
{
   var addition := a + b;
   var subtraction := a - b;
   result := addition + subtraction;
   return result;
}
method test()
{
    var a := 10 ;
    var b := 20 ;
    var result := addSub(a,b);
    assert a > 5 ;
    assert b > 10 ;
}
