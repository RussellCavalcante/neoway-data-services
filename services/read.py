import pandas as pd
import os
from services.process import ProcessingService

class read:
    def readarquive(*args, **kwargs):
        target = os.path.join(os.path.dirname(__file__), '../processing_folder/')
        arquivos = os.listdir(target)

        for arquivo in arquivos:
            newarquivo = open(target+arquivo, 'r') 
            linhas = newarquivo.readlines()

            for  i , linha in enumerate(linhas):
                
                cpf = linha[0:18]  
                PRIVATE = linha[19] 
                INCOMPLETO = linha[31]
                DATE_LAST_BUY = linha[43:57]
                AVERAGE_TICKET = linha[65:77]
                TICKET_LAST_BUY = linha[87:100]
                MOST_FREQUENT_STORE = linha[111:130]
                STORE_LAST_BUY = linha[131:149]
                
                caracteres_indesejados = ".-/"

                for caractere in caracteres_indesejados:
                    cpf = cpf.replace(caractere, "")
                    MOST_FREQUENT_STORE = MOST_FREQUENT_STORE.replace(caractere, "")
                    STORE_LAST_BUY = STORE_LAST_BUY.replace(caractere, "")

                caracteres_indesejados = ","

                for caractere in caracteres_indesejados:
                    AVERAGE_TICKET = AVERAGE_TICKET.replace(caractere, ".")
                    TICKET_LAST_BUY = TICKET_LAST_BUY.replace(caractere, ".")
                
        
                
                print(i , 'linhas percorridas')
                if i != 0:
                    ProcessingService.create_processment(cpf, PRIVATE, INCOMPLETO, DATE_LAST_BUY, AVERAGE_TICKET, TICKET_LAST_BUY, MOST_FREQUENT_STORE, STORE_LAST_BUY)
            
        print('Importação de arquivos concluida com sucesso!')
                
                

            

            