
with open("7.txt") as file:
    comandos = file.readlines()

dirs = {"/casa":0}
caminho = "/casa"


for comando in comandos:

    if comando[0] == "$":

        if comando[2:4] == "ls":
            pass
 
        elif comando[2:4] == "cd":

            if comando[5:6] == "/":
                caminho = "/casa"

            elif comando[5:7] == "..":
                caminho = caminho[0:caminho.rfind("/")]

            else:
                dir_name = comando[5:]             
                caminho = caminho + "/" + dir_name       
                dirs.update({caminho:0})              

    

    elif comando[0:3] == "dir":
        pass

    else:
        size = int(comando[:comando.find(" ")])    

        dir = caminho
        for i in range(caminho.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]


total = 0


limite = 30000000 - (70000000 - dirs["/casa"])
valid_dirs = []


for dir in dirs:
    
    # ==== PART 1 ====
    if dirs[dir] < 100000:
        total += dirs[dir]
    
    # ==== PART 2 ====
    if limite <= dirs[dir]:
        valid_dirs.append(dirs[dir])

menor = min(valid_dirs)

print("Answer to part 1: ", total)
print("Answer to part 2: ", menor)