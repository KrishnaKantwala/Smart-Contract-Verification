pragma solidity >=0.4.0 <0.7.0;

contract test_contract {
    function ifelsenested (int x) public returns (int) {
        if(x < 10) {
            if (x == 8){
                result = 9;
            }
            else {
                result = 10;
            }
        } else {
            result = 11;
        }
        return result;
    }
}

