pragma solidity >=0.4.0 <0.7.0;

contract contract3 {

    function noBranches() external pure returns (uint){
        int b = 3 + a;
        int result = a + b;
        int answer = a * b;
        result = result * answer;
        return result;
    }
}