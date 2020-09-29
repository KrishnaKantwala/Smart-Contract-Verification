pragma solidity >=0.4.0 <0.7.0;

contract test_contract {

    function singleRequire() public pure returns (uint){
        uint a;
        uint b = 3 + a;
        a = 3;
        uint result = a + b;
        return result;
    }

}