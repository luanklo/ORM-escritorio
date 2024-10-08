from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.MotivoController import MotivoController
from infra.Controllers.ParteController import ParteController

processo_controller = ProcessoController()
motivo_controller = MotivoController()
parte_controller = ParteController()

# 1. Definindo os Motivos (se ainda não existem no banco)
# motivo1 = motivo_controller.insert(nome="Motivo 1")
# motivo2 = motivo_controller.insert(nome="Motivo 2")
# motivo3 = motivo_controller.insert(nome="Motivo 3")



# 2. Criando o Processo
parte = parte_controller.select()
print(parte.advogados)