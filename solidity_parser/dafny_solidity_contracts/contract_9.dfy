method functionality() returns(result:int)
{
    var var1 := -10 ;
    var a := 10 ;
    var aa := 11 ;
    var aaa := 12 ;
    var ba := 20 ;
    var baa := 21 ;
    var baaa := 22 ;
    var total := 0;

    // feature 1
    var a1 := 1 ;
    var b2 := 2;
    a := a + 10 ;
    a1 := a1 + ba ;
    total := total + a;
    total := total + a1;
    total := total + b2;

    assert a1 > a;

    //feature 2
    var a12 := 1;
    var b22 := 2;
    aa := a12 + 20;
    a12 := aa + ba;
    a12 := a12 + baa;
    total := total + aa;
    total := total + a12;
    total := total + b22;

    assert a12 > aa ;

    //feature 3
    var a13 := 1;
    var b23 := 2;
    aaa := aaa + 30;
    a13 := baa + aa;
    a13 := a13 + a;
    a13 := a13 + aaa;
    a13 := a13 + baa;
    total := total + a13;
    total := total + aaa;
    total := total + b23;

    assert a13 > aaa;

    // feature 4
    total := total + var1;
    assert total > a13 ;
    var result := total;
    return result;
}
method test2()
{
    var result := functionality();
    //assert functionality() == 307;

}