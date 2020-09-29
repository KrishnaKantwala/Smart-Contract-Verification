method noBranch(a:int , c:int) returns (result:int)
    requires a > c
    requires c > 5
    ensures result > 0
{
    var b := 3 + a;
    var result1 := c + b;
    var answer := a * b;
    assert answer > 0;
    result := result1 * answer;
    return result;
}
method testing()
{
    var a:= 20 ;
    var c:= 10 ;
    var Result := noBranch(a,c);
    assert a > c ;
    assert c > 5 ;
    assert a > 0 ;
    
}

