
method singleRequire() returns(result:int)
    ensures c >= 6
{
    var a:= 0;
    var b := 3 + a;
    a := 3;
    var result := a + b;
    return result;
}
method testing2()
{
    var c2:= singleRequire();

}