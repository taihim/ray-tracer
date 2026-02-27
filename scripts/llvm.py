from llvmlite import ir

module = ir.Module(name="addition_module")

int32 = ir.IntType(32)
fnty = ir.FunctionType(int32, [int32, int32])

func = ir.Function(module, fnty, name="add")

block = func.append_basic_block(name="entry")

builder = ir.IRBuilder(block)

a, b = func.args

result = builder.add(a, b)
builder.ret(result)

print(module)