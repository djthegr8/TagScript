from TagScriptEngine import block, Interpreter, adapter
from traceback import format_exc
blocks = [
    block.MathBlock(),
    block.RandomBlock(),
    block.RangeBlock(),
    block.AnyBlock(),
    block.IfBlock(),
    block.AllBlock(),
    block.BreakBlock(),
    block.StrfBlock(),
    block.AssignmentBlock(),
    block.FiftyFiftyBlock(),
    block.ShortCutRedirectBlock("message"),
    block.LooseVariableGetterBlock(),
	block.SubstringBlock()
]
x = Interpreter(blocks)

print("====")
print("TagScriptEngine v2 Playground")
print("press Enter to submit a TSE string")
print("submit exit to leave. submit a blank to repeat previous.")
print("====")

user_input = input("> ")
previous = ""
while user_input != "exit":
    dummy_data = {
        "message": adapter.StringAdapter("Hello, my name is PySnow")
    }
    result = None
    if user_input == "":
        result = x.process(previous, dummy_data)
    else:
        result = x.process(user_input, dummy_data)
        previous = user_input
    
    print(result.body)
    user_input = input("> ")