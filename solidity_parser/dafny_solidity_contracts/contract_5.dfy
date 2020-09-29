method contract1(x :  int ) returns ( result : int)
    requires x == 0 ;
    ensures result > 3;
{
    if x == 3
    {
        result := 4;
        return result;
    }
    else if x == 4
    {
        result := 5 ;
        return result ;
    }
    else
    {
        result := 6;
        return result;
    }
}