import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Set up the Chrome driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    def redemet_baixa(escolha, ar, datahini, datahfim,estacao1):
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
        # Create the driver with the options
        browser = webdriver.Chrome(options=chrome_options)
    
        # Load the page with Selenium
        #browser.get(url)
    
        # Wait up to 10 seconds for the page to load
        # Wait for the page to finish loading all JavaScript
        wait = WebDriverWait(driver, 10)


        
        from datetime import datetime, timedelta
        import datetime
        import time
        if escolha == 1:
            from urllib.request import Request, urlopen
            #import lxml
            import pandas as pd
            import pandas as pd
            import time
            from datetime import datetime, timedelta
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from selenium.webdriver.support.select import Select

            # datai = "01/06/2020 00:00"
            # dataf = "02/06/2020 23:00"
            datahi = datetime.strftime(datahini, '%d/%m/%Y %H:%M')
            datahf = datetime.strftime(datahfim, '%d/%m/%Y %H:%M')
            tempo = datahfim - datahini

            if datahi == datahf:
                intervalo = 0
            else:
                intervalo = int((str(tempo)[0:2]))
            mes = datahini.month
            # nome = "SBSC,SBAR,SBBH,SBBR,SBBV,SBCB,SBCG,SBCP,SBCT,SBCY,SBEN,SBES,SBFL,SBFN,SBFS,SBFZ,SBGL,SBGO,SBGR,SBIL,SBJF,SBJP,SBLB,SBME,SBMM,SBMO,SBMQ,SBNF,SBNT,SBPA,SBPJ,SBPV,SBRB,SBRF,SBRJ,SBSL,SBSP,SBST,SBSV,SBTE,SBMN,SBBE,SBVT,SBSG"
            nome = estacao1
            for i in range(intervalo + 1):
                # abre o Firefox
                #browser = webdriver.Firefox(executable_path='geckodriver.exe')
                # browser=webbrowser.open('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet', new=2)
                # browser = webdriver.Chrome(executable_path='chrome.EXE')
                # chama a página da redemet para consulta

                # browser.get('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet')
                browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')
                browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')
                # browser.get('https://www.redemet.aer.mil.br/old/?i=produtos&p=consulta-de-mensagens-opmet')
                # if (datahi.day + i)==31:
                datacori = datahini + timedelta(days=i)
                    # datacori=datahf
                datacoris = datetime.strftime(datacori, '%d/%m/%Y %H:%M')


                datacori = datetime.strftime(datacori, '%d/%m/%Y %H:%M')
                datacorf=  datahfim + timedelta(hours=23)
                datacorfs = datetime.strftime(datacorf, '%d/%m/%Y %H:%M')
                datacorfs =datacorfs[0:10] + ' 23:00'

                # espera 5s
                time.sleep(5)
                # tira a checkbox para mensagem recente
                browser.find_element_by_id("consulta_recente").click()

                # preenche o nome das estações para consulta
                element = browser.find_element_by_id("msg_localidade")
                element.send_keys(nome)

                # preenche a data inicial e final

                element = browser.find_element_by_id("consulta_data_ini").clear()
                element = browser.find_element_by_id("consulta_data_ini").click()
                element = browser.find_element_by_id("consulta_data_ini").send_keys(datacoris)
                element = browser.find_element_by_id("consulta_data_fim").clear()
                element = browser.find_element_by_id("consulta_data_fim").click()
                element = browser.find_element_by_id("consulta_data_fim").send_keys(datacorfs)

                # envia a consulta
                botao = browser.find_element_by_id("consulta_localidade")
                time.sleep(20)
                botao.click()

                # espera 10s
                time.sleep(20)

                ## coloca todo o resultado numa página
                # select_fr = Select(browser.find_element_by_name("msg_resultado_length"))
                # select_fr.select_by_index(3)

                table = browser.find_element_by_id('msg_resultado')

                # df = pd.read_html(str(table))
                # print(table)
                table_html = table.get_attribute('outerHTML')
                # print(df[0])

                # print(table)
                if i == 0:
                    df = pd.read_html(str(table_html))
                    df = df[0]
                else:
                    df2 = pd.read_html(str(table_html))
                    df2 = df2[0]

                    df = df.append(df2, ignore_index=True)
                    print(df)

                # print(df.loc[(df["Localidade"] == 'SBSC')])
                df.to_csv("metar.csv", header=True)
                browser.quit()
            print(df)
            # df = df.drop(columns=['Unnamed: 0'])
            df.to_csv("metar.csv", header=True)
            # df.to_csv('example.csv')
if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
