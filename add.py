from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.PessoaController import PessoaController
from infra.Controllers.AdvogadoController import AdvogadoController

processo_controller = ProcessoController()
processo = processo_controller.select(numero="0016047-10.2024.5.16.0011")[0]

pessoa_controller = PessoaController()
pessoa1 = pessoa_controller.select(cpf_cnpj="037.911.233-78")
empresa1 = pessoa_controller.select(cpf_cnpj="44.860.817/0001-05")
empresa2 = pessoa_controller.select(cpf_cnpj="10.515.785/0001-99")
empresa3 = pessoa_controller.select(cpf_cnpj="598.390.409-44")

