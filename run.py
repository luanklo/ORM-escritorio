from infra.Controllers.PessoaController import PessoaController
from infra.Controllers.AdvogadoController import AdvogadoController

repo = AdvogadoController()

adv = repo.select(id=4)
repo.update(adv, nome="teste")

for x in repo.select(): print(x)