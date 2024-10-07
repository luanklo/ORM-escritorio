from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

from infra.Controllers.ProcessoController import ProcessoController
from infra.Controllers.PessoaController import PessoaController
from infra.Controllers.ParteController import ParteController
from infra.Controllers.AdvogadoController import AdvogadoController

processo_controller = ProcessoController()
pessoa_controller = PessoaController()
parte_controller = ParteController()
advogado_controller = AdvogadoController()

drive = webdriver.Chrome()
drive.get("https://pje.trt16.jus.br/primeirograu/authenticateSSO.seam"); input()

def cadastroProcesso(numero):
    drive.get("https://pje.trt16.jus.br/primeirograu/Painel/painel_usuario/advogado.seam")
    drive.find_element(By.ID, "leftAdvPnl_header_label").click()
    element = drive.find_element(By.ID, "consultaProcessoAdvogadoForm:numeroProcessoDecoration:numeroProcesso")
    sleep(0.5)

    element.get_attribute('value')
    drive.execute_script(f"arguments[0].value = '{numero}';", element)
    
    drive.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)
    sleep(0.5)
    drive.find_element(By.ID, "consultaProcessoAdvogadoForm:searchButon").click()
    sleep(0.5)

    link = drive.find_element(By.XPATH, "//a[span[contains(text(), '0016047-10.2024.5.16.0011')]]").get_attribute('onclick')
    link = link[link.find("https"):link.find("')")]
    drive.get(link); sleep(1)

    drive.find_element(By.XPATH, "//span[@class = 'texto-numero-processo']//button").click(); sleep(1)

    vara = drive.find_element(By.XPATH, "//div[@aria-label = 'Dados do processo']//dd[1]").text
    classe, numero = drive.find_element(By.XPATH, "//div[@aria-label = 'Dados do processo']//dd[2]").text.split()
    valor = drive.find_element(By.XPATH, "//div[@aria-label = 'Dados do processo']//dd[5]").text.split()[1]

    print(numero)

    processo = processo_controller.select(numero=numero)
    if processo: processo = processo[0]
    else:
        processo = processo_controller.insert(
            numero=numero,
            valor=valor.replace('.', '').replace(',', '.'),
            vara=vara,
            classe=classe,
            link=link
        )
    
    partes = drive.find_elements(By.XPATH, "//div[@id= 'processo-partes']")
    for parte in partes:
        polo = parte.find_element(By.CLASS_NAME, "polo-header").text.split()[1]

        pessoas = parte.find_elements(By.TAG_NAME, "ul")[::2]
        for pessoa in pessoas:
            nome = pessoa.find_element(By.TAG_NAME, "pje-nome-parte").text
            pessoa_dados = [x.text for x in pessoa.find_elements(By.CLASS_NAME, "ng-star-inserted")[:2]]
            cpf_cnpj = pessoa_dados[0].split()[1] if pessoa_dados[0] != "" else pessoa_dados[1].split()[1]

            Pessoa = pessoa_controller.select(nome=nome,cpf_cnpj=cpf_cnpj)
            if Pessoa: Pessoa = Pessoa[0]            
            else: Pessoa = pessoa_controller.insert(nome=nome, cpf_cnpj=cpf_cnpj)

            tipo = pessoa.find_element(By.TAG_NAME, "li").text[:-1]

            parte = parte_controller.select(pessoa_id=Pessoa.id, processo_id=processo.id)
            if parte: parte = parte[0]
            else:
                parte = parte_controller.insert(
                    tipo=tipo,
                    polo=polo,
                    processo_id=processo.id,
                    pessoa_id=Pessoa.id
                )


            for adv in pessoa.find_elements(By.CLASS_NAME, "partes-representante"):
                nome, cpf, aob = adv.text.split("\n")[:3]
                nome = nome[:nome.find(" (ADVOGADO)")]
                aob = aob.split()[1][:-1]
                
                advogado = advogado_controller.select(aob=aob)
                if advogado: advogado = advogado[0]
                else:
                    advogado = advogado_controller.insert(
                        nome=nome,
                        aob=aob
                    )
                
                parte.addAdvogado(advogado)

cadastroProcesso("0016047-10.2024.5.16.0011")