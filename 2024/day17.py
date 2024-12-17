def combo_map(n):
    if 0<= n <= 3:
        return n
    elif n == 4:
        return A
    elif n == 5:
        return B
    elif n == 6:
        return C

def adv(A,co):
    return A // (2**co)

def bxl(B,lo):
    return B ^ lo

def bst(co):
    return co % 8

def jnz(A):
    if A != 0:
        return True
    else:
        return False

def bxc(B,C):
    return B ^ C

def out(co):
    return co % 8

def bdv(A,co):
    return A // (2**co)

def cdv(A,co):
    return A // (2**co)

A = 66752888
B = 0
C = 0
program = [2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0]
pointer = 0
outputs = []
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer+1]
    if opcode == 0:
        operand = combo_map(operand)
        A = adv(A,operand)
        pointer += 2
    elif opcode == 1:
        B = bxl(B, operand)
        pointer += 2
    elif opcode == 2:
        operand = combo_map(operand)
        B = bst(operand)
        pointer += 2
    elif opcode == 3:
        if jnz(A):
            pointer = operand
        else:
            pointer += 2
    elif opcode == 4:
        B = bxc(B,C)
        pointer += 2
    elif opcode == 5:
        operand = combo_map(operand)
        outputs.append(out(operand))
        pointer += 2
    elif opcode == 6:
        operand = combo_map(operand)
        B = bdv(A,operand)
        pointer += 2
    elif opcode == 7:
        operand = combo_map(operand)
        C = cdv(A,operand)
        pointer += 2

print(outputs)