import click
from smart_contract_parser import SmartContractParser


@click.command()
@click.option('--input', default="", help='Path to input Solidity file')
@click.option('--output', default="", help='Output Dafny file name')
@click.option('--bulk', default="false", help='Translate all Solidity files')
def translate(input, output, bulk):
    if bulk == "true":
        for i in range(1, 11):
            contract_parser = SmartContractParser(contract_path="dafny_solidity_contracts/contract_{}.sol".format(i))
            dafny_function_code = contract_parser.create_dafny_file()
            print(dafny_function_code)
            print("\n-------------------------------  {}  -------------------------------------\n".format(i))
    else:
        contract_parser = SmartContractParser(contract_path="{}".format(input))
        dafny_function_code = contract_parser.create_dafny_file()
        if output:
            output_dafny_file = open(str(output), "w")
            output_dafny_file.write(dafny_function_code)
            output_dafny_file.close()
        else:
            print(dafny_function_code)
            print("\n--------------------------------------------------------------------\n")


if __name__ == "__main__":
    translate()
