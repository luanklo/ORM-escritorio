from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.MotivoController import MotivoController
from infra.Controllers.ParteController import ParteController
from infra.Controllers.AudienciaController import AudienciaController
from infra.Models.LuanParte import LuanParte
from datetime import datetime, timedelta


ant = {1,2,3,4}
agr = set()
agr.add(22)

print('sairam = ', ant - agr)
print('novos = ',  agr - ant)