from infra.Controllers.AdvogadoController import AdvogadoController
from infra.Controllers.AudienciaController import AudienciaController
from infra.Controllers.MotivoController import MotivoController
from infra.Controllers.ParteController import ParteController
from infra.Controllers.PessoaController import PessoaController
from infra.Controllers.ProcessoController import ProcessoController

advogadoC = AdvogadoController()
audienciaC = AudienciaController()
motivoC = MotivoController()
parteC = ParteController()
pessoaC = PessoaController()
processoC = ProcessoController()

#processoC.insert("111", "111", "vara1", "calsse1", "link1")
processo1 = processoC.select(numero="111")[0]
motivo1 = motivoC.select(id=1)[0]
motivo2 = motivoC.select(id=2)[0]
motivo3 = motivoC.select(id=3)[0]

#pessoaC.insert("pessoa1", "cpf1")
#pessoaC.insert("pessoa2", "cpf2")

pessoa1 = pessoaC.select(id=1)[0]
pessoa2 = pessoaC.select(id=2)[0]

#advogadoC.insert("adv1", "abo2")
#advogadoC.insert("adv2", "abo1")

adv1 = advogadoC.select(1)[0]
adv2 = advogadoC.select(2)[0]

parte1 = parteC.select(1)[0]
parte2 = parteC.select(2)[0]

#parte1.addAdvogado(adv1)
#parte2.addAdvogado(adv2)