from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.MotivoController import MotivoController

processo_controller = ProcessoController()
motivo_controller = MotivoController()

# 1. Definindo os Motivos (se ainda não existem no banco)
# motivo1 = motivo_controller.insert(nome="Motivo 1")
# motivo2 = motivo_controller.insert(nome="Motivo 2")
# motivo3 = motivo_controller.insert(nome="Motivo 3")

pesq = motivo_controller.select(nome="Motivo 1")
for x in pesq: print(x)


# 2. Criando o Processo
# novo_processo = Processo(
#     numero="123456",
#     valor=1500.0,
#     vara="2ª Vara",
#     classe="Classe B",
#     link="http://exemplo.com/processo/123456",
#     profissao="Advogado"
# )