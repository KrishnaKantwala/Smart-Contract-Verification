# Smart Contract Verfication system using Dafny

Developed a command line application that verifies the smart contract using static verification to ensure bug free contracts. Contracts will be parsed using ANTLR which will generate the parse tree which will be further translated to another programming language called Dafny as it supports formal verification, using Python.


## Smart Contracts:

A smart contract is a self-executing contract with the terms of the agreement between buyer and seller being directly written into lines of code. The code controls the execution, and transactions are trackable and irreversible. Smart contracts permit trusted transactions and agreements to be carried out among disparate, anonymous parties without the need for a central authority, legal system, or external enforcement mechanism.

## Experiments:

- Smart contracts are a kind of safety-critical systems. As smart contracts failure leads to catastrophic consequences, it is very important to do formal verification on them before deploying them on blockchains.

- In order to implement the Smart contract verification tool, our approach is:
  - Create a sample solidity smart contract.
  - Feed ANTLR with smart contract solidity code and a proper grammar file to generate parse tree in a specific target lanaguage Python.
  - The parse tree of ANTLR can be used by Python to create a command-line user interface as interface of our solidity smart contract formal verification tool.
  - Dafny being a supporter of formal verification tool which will verify the translated code, thus giving an output in the form of a report with a list of detected error, if any.

