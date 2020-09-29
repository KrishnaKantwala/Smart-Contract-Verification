pragma solidity >=0.4.0 <0.7.0;

contract test_contract {


    function noBranches() external pure returns (uint){
        int var1 = -10 ;
        int a = 10 ;
        int aa = 11 ;
        int aaa = 12 ;
        int ba = 20 ;
        int baa = 21 ;
        int baaa = 22 ;
        int total = 0;

        // feature 1
        int a1 = 1 ;
        int b2 = 2;
        a = a + 10 ;
        a1 = a1 + ba ;
        total = total + a;
        total = total + a1;
        total = total + b2;

        //feature 2
        int a12 = 1;
        int b22 = 2;
        aa = a12 + 20;
        a12 = aa + ba + baa ;
        total = total + aa + a12 + b22;

        //feature 3
        int a13 = 1;
        int b23 = 2;
        aaa = aaa + 30;
        a13 = baa + aa + a + aaa + baa + ba;
        total = total + a13 + aaa + b23;

        // feature 4
        total = total + var1;
        int result = total;
        return result;
    }
}