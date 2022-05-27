alunos = ["Pablo", "Joao", "Maria", "Jose"]

#trocar Maria por Julia
alunos[2] = "Julia"

#adicionar novo na lista .append
alunos.append("Roberto")
alunos.append("Joao")

print(alunos)

#quantas pessoas tem com mesmo nome
print(alunos.count("Joao"))

#mostrar quantos tem na lista
print(len(alunos))

#mostrar em ordem alfabetica
print(sorted(alunos))