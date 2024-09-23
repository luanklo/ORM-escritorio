from infra.Controllers.PessoaController import PessoaController
from infra.Controllers.AdvogadoController import AdvogadoController

repo = AdvogadoController()

# repo.insert("luan", "123.123.123-65", "12 1234 1234")
# repo.insert("pedro", "123.123.123-64", "12 1234 1233")
# repo.insert("jose", "123.123.123-63", "12 1234 1232")

adv = repo.select(id=4)
repo.update(adv, nome="teste")

for x in repo.select(): print(x)