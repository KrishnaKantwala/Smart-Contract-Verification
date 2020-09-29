pragma solidity >=0.4.0 <0.7.0;

contract test_contract {
    function noBranches() external pure returns (uint){
        int a = 3;
        int b = 3 + a;
        int c = a + b;

        int b1 = 3 + a1;
        int c1 = a1 + b1;

        int a2 = 0;
        int b2 = 3 + a2;
        a2 = 3;
        c2 = a2 + b2;
        int result = c2;

        return result;
    }
}
