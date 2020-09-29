pragma solidity >=0.4.22 <0.6.0;

contract test_contract {
    function addsub(int a, int b) external pure returns (uint){
        int addition = a + b;
        int subtraction = a - b;
        int result = addition + subtraction;
        return result;
    }
}
