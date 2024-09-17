from infra.Controllers.PessoaController import PessoaController

#repo = AtorRepository()
#repo.inser("algum filme", "comedia", 2101)
#repo.delete("algum filme")
#repo.update("Forest Gump", 2000)
#data = repo.select()
#for x in data: print(x)

# repo2 = FilmeRepository()
# data2 = repo2.select()
# print(data2)

repo = PessoaController()
data = repo.select()
for x in data: print(x)