pragma solidity >=0.4.0 <0.7.0;

contract test_contract {

    function ifelseifelse (int x) public returns (int) {
        if(x == 3) {   // if else statement
            result = 4;
            return result;
        } else if(x == 4){
            result = 5;
            return result;
        } else {
            result = 6;
            return result;
        }
    }
}