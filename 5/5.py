from string import ascii_uppercase


with open('5.txt') as file:
    strings, instrucoes = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))


stacks = {int(digito):[] for digito in strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(strings[-1]) if char != " "]


def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")



def carregaStacks():
    for string in strings[:-1]:
        stack_numero = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_numero].insert(0, string[index])
            stack_numero += 1


def esvaziaStacks():
    for stack_numero in stacks:
        stacks[stack_numero].clear()


def getStackEnds():
    resposta = ""
    for stack in stacks:
        resposta += stacks[stack][-1]
    return resposta


carregaStacks()
for instrucao in instrucoes:
    instrucao =instrucao.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instrucao = [int(i) for i in instrucao]

    crates = instrucao[0]
    from_stack = instrucao[1]
    to_stack = instrucao[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

print("resposta 1: ", getStackEnds())


# === PART 2 ===
esvaziaStacks()
carregaStacks()
for instrucao in instrucoes:
    instrucao = instrucao.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instrucao = [int(i) for i in instrucao]

    crates = instrucao[0]
    from_stack = instrucao[1]
    to_stack = instrucao[2]

    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack] = stacks[from_stack][:-crates]

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)

print("resposta 2: ", getStackEnds())