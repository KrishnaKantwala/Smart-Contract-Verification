pragma solidity >=0.4.0 <0.7.0;

contract test_contract {

    function ifelse (int x) public returns (int) {
        if(x == 0) {   // if else statement
            result = 1;
        } else {
            result = 2;
        }
        return result;
    }
}



