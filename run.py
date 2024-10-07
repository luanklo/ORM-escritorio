from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.MotivoController import MotivoController

processo_controller = ProcessoController()
motivo_controller = MotivoController()

# 1. Definindo os Motivos (se ainda não existem no banco)
# motivo1 = motivo_controller.insert(nome="Motivo 1")
# motivo2 = motivo_controller.insert(nome="Motivo 2")
# motivo3 = motivo_controller.insert(nome="Motivo 3")



# 2. Criando o Processo
processo = processo_controller.select(numero="0016047-10.2024.5.16.0011")
print(processo)

