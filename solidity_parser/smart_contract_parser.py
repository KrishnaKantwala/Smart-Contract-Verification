import pprint

from solidity_parser import parser


class SmartContractParser:
    def __init__(self, contract_path):
        self.contract_path = contract_path
        self.parsed_contract = None

    def parse_contract(self):
        self.parsed_contract = parser.parse_file(self.contract_path)

    def print_parse_tree(self):
        pprint.pprint(self.parsed_contract)

    def create_dafny_file(self):
        self.parse_contract()
        dafny_function_code = str()
        dafny_function_code = self.create_function_definition(dafny_function_code)
        function_node = self.parsed_contract.get("children")[1]
        dafny_function_code = self.create_function_body(dafny_function_code, function_node)
        dafny_function_code += "\n}"
        return dafny_function_code

    def create_function_body(self, dafny_function_code, function_node):
        function_statements = function_node.get("subNodes")[0].get("body").get("statements")
        for statement in function_statements:
            if statement.type == "IfStatement":
                dafny_function_code = self.translate_if_statement(dafny_function_code, statement)

            elif statement.get("type") == "Identifier":
                dafny_function_code = self.translate_identifier(dafny_function_code, statement)

            elif statement.get("type") == "NumberLiteral":
                dafny_function_code = self.translate_numerical_literal(dafny_function_code, statement)

            elif statement.get("type") == "VariableDeclarationStatement":
                dafny_function_code = self.translate_variable_declaration_statement(dafny_function_code, statement)
            elif statement.get("type") == "ExpressionStatement":
                dafny_function_code = self.translate_experssion_statement(dafny_function_code, statement)
        return dafny_function_code

    def translate_experssion_statement(self, dafny_function_code, statement):
        expression = ""
        if statement.get("expression").get("type") == "BinaryOperation":
            expression = self.translate_binary_operation_expression(expression, statement)
        if not dafny_function_code.endswith("\n"):
            dafny_function_code += "\n\t" + expression + ";\n"
        else:
            dafny_function_code += "\t" + expression + ";\n"
        return dafny_function_code

    def translate_binary_operation_expression(self, expression, statement):
        if statement.get("expression").get("left").get("type") == "NumberLiteral":
            expression += str(statement.get("expression").get("left").get("number"))
        elif statement.get("expression").get("left").get("type") == "Identifier":
            expression += str(statement.get("expression").get("left").get("name"))
        expression += " :" + str(statement.get("expression").get("operator")) + " "
        if statement.get("expression").get("right").get("type") == "NumberLiteral":
            expression += str(statement.get("expression").get("right").get("number"))
        elif statement.get("expression").get("right").get("type") == "Identifier":
            expression += str(statement.get("expression").get("right").get("name"))
        if statement.get("expression").get("right").get("type") == "BinaryOperation":
            if statement.get("expression").get("right").get("left").get("type") == "NumberLiteral":
                expression += str(statement.get("expression").get("right").get("left").get("number"))
            elif statement.get("expression").get("right").get("left").get("type") == "Identifier":
                expression += str(statement.get("expression").get("right").get("left").get("name"))
            expression += " " + str(statement.get("expression").get("right").get("operator")) + " "
            if statement.get("expression").get("right").get("right").get("type") == "NumberLiteral":
                expression += str(statement.get("expression").get("right").get("right").get("number"))
            elif statement.get("expression").get("right").get("right").get("type") == "Identifier":
                expression += str(statement.get("expression").get("right").get("right").get("name"))
        return expression

    def translate_variable_declaration_statement(self, dafny_function_code, statement):
        variable_declaration = ""
        if statement.get("initialValue"):
            variable_declaration = self.translate_initial_value_of_variable_declaration(statement, variable_declaration)
        else:
            variable_declaration += "var " + statement.variables[0].get("name")
        if not dafny_function_code.endswith("\n"):
            dafny_function_code += "\n\t" + variable_declaration + ";\n"
        else:
            dafny_function_code += "\t" + variable_declaration + ";\n"
        return dafny_function_code

    def translate_initial_value_of_variable_declaration(self, statement, variable_declaration):
        variable_declaration += "var " + statement.variables[0].get("name") + " := "
        if statement.get("initialValue").get("type") == "BinaryOperation":
            if statement.get("initialValue").get("left").get("type") == "NumberLiteral":
                variable_declaration += str(statement.get("initialValue").get("left").get("number"))
            elif statement.get("initialValue").get("left").get("type") == "Identifier":
                variable_declaration += str(statement.get("initialValue").get("left").get("name"))
            variable_declaration += " " + str(statement.get("initialValue").get("operator")) + " "
            if statement.get("initialValue").get("right").get("type") == "NumberLiteral":
                variable_declaration += str(statement.get("initialValue").get("right").get("number"))
            elif statement.get("initialValue").get("right").get("type") == "Identifier":
                variable_declaration += str(statement.get("initialValue").get("right").get("name"))
        elif statement.get("initialValue").get("type") == "NumberLiteral":
            variable_declaration += str(statement.get("initialValue").get("number"))
        elif statement.get("initialValue").get("type") == "Identifier":
            variable_declaration += str(statement.get("initialValue").get("name"))
        elif statement.get("initialValue").get("type") == "UnaryOperation":
            variable_declaration += " " + str(statement.get("initialValue").get("operator"))
            if statement.get("initialValue").get("subExpression").get("type") == "NumberLiteral":
                variable_declaration += str(
                    statement.get("initialValue").get("subExpression").get("number"))
            elif statement.get("initialValue").get("left").get("type") == "Identifier":
                variable_declaration += str(statement.get("initialValue").get("subExpression").get("name"))
        return variable_declaration

    def translate_numerical_literal(self, dafny_function_code, statement):
        if not dafny_function_code.endswith("\n"):
            dafny_function_code += "\n\treturn " + statement.get("number") + ";\n"
        else:
            dafny_function_code += "\treturn " + statement.get("number") + ";\n"
        return dafny_function_code

    def translate_identifier(self, dafny_function_code, statement):
        if not dafny_function_code.endswith("\n"):
            dafny_function_code += "\n\t return " + statement.get("name") + ";\n"
        else:
            dafny_function_code += "\treturn " + statement.get("name") + ";\n"
        return dafny_function_code

    def translate_if_statement(self, dafny_function_code, statement):
        if_condition = ""
        if_condition = str(statement.get("condition").get("left").get("name")) + " " + str(
            statement.get("condition").get("operator")) + " " + str(
            statement.get("condition").get("right").get("number"))
        inside_if_block = ""
        if statement.get("TrueBody").get("type") == "Block":
            inside_if_block = self.translate_true_body_of_simple_ifelse_statement(inside_if_block, statement)
        inside_else_block = ""
        if statement.get("FalseBody").get("type") == "Block":
            dafny_function_code = self.translate_false_body_of_simple_ifelse_statement(dafny_function_code,
                                                                                       if_condition, inside_else_block,
                                                                                       inside_if_block, statement)

        elif statement.get("FalseBody").get("type") == "IfStatement":
            dafny_function_code = self.translate_nested_ifelse_in_else_part_of_ifelse_statement(dafny_function_code,
                                                                                                if_condition,
                                                                                                inside_if_block,
                                                                                                statement)
        return dafny_function_code

    def translate_nested_ifelse_in_else_part_of_ifelse_statement(self, dafny_function_code, if_condition,
                                                                 inside_if_block, statement):
        inside_else_if_block = ""
        if statement.get("FalseBody").get("TrueBody").get("type") == "Block":
            else_if_block_statements = statement.get("FalseBody").get("TrueBody").get("statements")
            for else_if_block_statement in else_if_block_statements:
                if else_if_block_statement.get("type") == "ExpressionStatement":
                    inside_else_if_block += str(
                        else_if_block_statement.get("expression").get("left").get("name")) + " :" + str(
                        else_if_block_statement.get("expression").get("operator")) + " " + str(
                        else_if_block_statement.get("expression").get("right").get("number")) + ";\n"

                elif else_if_block_statement.get("type") == "Identifier":
                    if not inside_else_if_block.endswith("\n"):
                        inside_else_if_block += "\n\treturn " + else_if_block_statement.get("name") + ";\n"
                    else:
                        inside_else_if_block += "\treturn " + else_if_block_statement.get("name") + ";\n"

                elif else_if_block_statement.get("type") == "NumberLiteral":
                    null = self.translate_numerical_literal(inside_else_if_block, else_if_block_statement)
        inside_else_if_else_block = ""
        if statement.get("FalseBody").get("FalseBody").get("type") == "Block":
            else_if_else_block_statements = statement.get("FalseBody").get("FalseBody").get("statements")
            for else_if_else_block_statement in else_if_else_block_statements:
                if else_if_else_block_statement.get("type") == "ExpressionStatement":
                    inside_else_if_else_block += str(
                        else_if_else_block_statement.get("expression").get("left").get(
                            "name")) + " :" + str(
                        else_if_else_block_statement.get("expression").get("operator")) + " " + str(
                        else_if_else_block_statement.get("expression").get("right").get("number")) + ";\n"

                elif else_if_else_block_statement.get("type") == "Identifier":
                    if not inside_else_if_else_block.endswith("\n"):
                        inside_else_if_else_block += "\n\treturn " + else_if_else_block_statement.get(
                            "name") + ";\n"
                    else:
                        inside_else_if_else_block += "\treturn " + else_if_else_block_statement.get(
                            "name") + ";\n"

                elif else_if_else_block_statement.get("type") == "NumberLiteral":
                    null = self.translate_numerical_literal(inside_else_if_else_block, else_if_else_block_statement)
        else_if_condition = ""
        else_if_condition = str(
            statement.get("FalseBody").get("condition").get("left").get("name")) + " " + str(
            statement.get("FalseBody").get("condition").get("operator")) + " " + str(
            statement.get("FalseBody").get("condition").get("right").get("number"))
        dafny_function_code += "if({}){{ \n\t {} }}else if ({}){{\n\t {}}}else{{\n\t {} }}".format(
            if_condition,
            inside_if_block,
            else_if_condition,
            inside_else_if_block,
            inside_else_if_else_block)
        return dafny_function_code

    def translate_false_body_of_simple_ifelse_statement(self, dafny_function_code, if_condition, inside_else_block,
                                                        inside_if_block, statement):
        else_block_statements = statement.get("FalseBody").get("statements")
        for else_block_statement in else_block_statements:
            if else_block_statement.get("type") == "ExpressionStatement":
                inside_else_block += str(
                    else_block_statement.get("expression").get("left").get("name")) + " :" + str(
                    else_block_statement.get("expression").get("operator")) + " " + str(
                    else_block_statement.get("expression").get("right").get("number")) + ";\n"

            elif else_block_statement.get("type") == "Identifier":
                if not inside_else_block.endswith("\n"):
                    inside_else_block += "\n\treturn " + else_block_statement.get("name") + ";\n"
                else:
                    inside_else_block += "\treturn " + else_block_statement.get("name") + ";\n"

            elif else_block_statement.get("type") == "NumberLiteral":
                null = self.translate_numerical_literal(inside_else_block, else_block_statement)
        dafny_function_code += "if({}){{ \n\t {} }}else{{\n\t {}}}".format(if_condition,
                                                                           inside_if_block,
                                                                           inside_else_block)
        return dafny_function_code

    def translate_true_body_of_simple_ifelse_statement(self, inside_if_block, statement):
        if_block_statements = statement.get("TrueBody").get("statements")
        for if_block_statement in if_block_statements:
            if if_block_statement.get("type") == "ExpressionStatement":
                inside_if_block = inside_if_block + str(
                    if_block_statement.get("expression").get("left").get("name")) + " :" + str(
                    if_block_statement.get("expression").get("operator")) + " " + str(
                    if_block_statement.get("expression").get("right").get("number")) + ";\n"

            elif if_block_statement.get("type") == "IfStatement":
                inside_if_block_if_condition = ""
                inside_if_block_if_condition = str(
                    if_block_statement.get("condition").get("left").get("name")) + " " + str(
                    if_block_statement.get("condition").get("operator")) + " " + str(
                    if_block_statement.get("condition").get("right").get("number"))

                inside_if_block_if_block = ""
                if if_block_statement.get("TrueBody").get("type") == "Block":
                    inside_if_block_if_block_statements = if_block_statement.get("TrueBody").get(
                        "statements")
                    for inside_if_block_if_block_statement in inside_if_block_if_block_statements:
                        if inside_if_block_if_block_statement.get("type") == "ExpressionStatement":
                            inside_if_block_if_block += "\t" + str(
                                inside_if_block_if_block_statement.get("expression").get("left").get(
                                    "name")) + " :" + str(
                                inside_if_block_if_block_statement.get("expression").get(
                                    "operator")) + " " + str(
                                inside_if_block_if_block_statement.get("expression").get("right").get(
                                    "number")) + ";\n"

                        elif inside_if_block_if_block_statement.get("type") == "Identifier":
                            if not inside_if_block_if_block.endswith("\n"):
                                inside_if_block_if_block += "\n\treturn " + inside_if_block_if_block_statement.get(
                                    "name") + ";\n"
                            else:
                                inside_if_block_if_block += "\treturn " + inside_if_block_if_block_statement.get(
                                    "name") + ";\n"

                        elif inside_if_block_if_block_statement.get("type") == "NumberLiteral":
                            null = self.translate_numerical_literal(inside_if_block_if_block,
                                                                    inside_if_block_if_block_statement)

                inside_if_block_else_block = ""
                if if_block_statement.get("FalseBody").get("type") == "Block":
                    else_block_statements = if_block_statement.get("FalseBody").get("statements")
                    for else_block_statement in else_block_statements:
                        if else_block_statement.get("type") == "ExpressionStatement":
                            inside_if_block_else_block += "\t" + str(
                                else_block_statement.get("expression").get("left").get(
                                    "name")) + " :" + str(
                                else_block_statement.get("expression").get("operator")) + " " + str(
                                else_block_statement.get("expression").get("right").get("number")) + ";\n"

                        elif else_block_statement.get("type") == "Identifier":
                            if not inside_if_block_else_block.endswith("\n"):
                                inside_if_block_else_block += "\n\treturn " + else_block_statement.get(
                                    "name") + ";\n"
                            else:
                                inside_if_block_else_block += "\treturn " + else_block_statement.get(
                                    "name") + ";\n"

                        elif else_block_statement.get("type") == "NumberLiteral":
                            null = self.translate_numerical_literal(inside_if_block_else_block,
                                                                    else_block_statement)

                    inside_if_block += "if({}){{ \n\t {} \t}}else{{\n\t {}\t}}\n".format(
                        inside_if_block_if_condition,
                        inside_if_block_if_block,
                        inside_if_block_else_block)

            elif if_block_statement.get("type") == "Identifier":
                if not inside_if_block.endswith("\n"):
                    inside_if_block += "\n\treturn " + if_block_statement.get("name") + ";\n"
                else:
                    inside_if_block += "\treturn " + if_block_statement.get("name") + ";\n"

            elif if_block_statement.get("type") == "NumberLiteral":
                null = self.translate_numerical_literal(inside_if_block, if_block_statement)
        return inside_if_block

    def create_function_definition(self, dafny_function_code):
        for child in self.parsed_contract.get("children"):
            if child.get("subNodes", None):
                for sub_node in child.get("subNodes"):
                    if sub_node.get("type") == "FunctionDefinition" and not sub_node.get("isConstructor"):
                        function_name = sub_node.get("name")
                        dafny_function_code = "method " + function_name + " ("
                        if (sub_node.get("parameters").get("parameters")):
                            for index, parameter in enumerate(sub_node.get("parameters").get("parameters")):
                                if index != len(sub_node.get("parameters").get("parameters")) - 1:
                                    dafny_function_code = dafny_function_code + parameter.get(
                                        "name") + ": " + parameter.get("typeName").get("name") + ", "
                                else:
                                    dafny_function_code = dafny_function_code + parameter.get(
                                        "name") + ": " + parameter.get("typeName").get("name")
                        dafny_function_code = dafny_function_code + ")"
                        # TODO need to add the return value
                        dafny_function_code = dafny_function_code + " returns (result : int)"
                    dafny_function_code = dafny_function_code + "\n { \n"
        return dafny_function_code
