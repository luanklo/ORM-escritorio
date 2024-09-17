from infra.Controllers.PessoaController import PessoaController



repo = PessoaController()

# repo.insert("luan", "123.123.123-65", "12 1234 1234")
# repo.insert("pedro", "123.123.123-64", "12 1234 1233")
# repo.insert("jose", "123.123.123-63", "12 1234 1232")

data = repo.select(nome="luan")
for x in data: print(x)