method noBranches(a1:int, a3:int) returns(result: int)
    ensures c2 > 5
{
    var a:= 3;
    var b := 3 + a;
    var c:= a + b;
    
    assert c == a + b;
    assert c > a ;
    assert c > b ;

    // functionality 2
    //var a1 := 2;
    var b1 := 3 + a1;
    var c1 := a1 + b1;
    assert c1 == a1 + b1;

    //assertion violation occurs as we don't know the value of a1
    // assert c1 > a1; 
    // assert b1 < c1;

    // functionality 3
    var a2 := 0;
    var b2 := 3 + a2;
    a2 := 3;
    c2 := a2 + b2;
    result := c2;
    assert c2 > 5;
    return result;
}
method test1()
{
    var a1 := 10;
    var a3 := 20;
    var result := noBranches(a1,a3);
    assert a1 < a3; 
    assert result > 5;
}