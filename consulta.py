import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation

import sys

import os
from datetime import datetime, timedelta, date
from datetime import datetime, timezone

from streamlit import runtime

from streamlit.web import cli as stcli
import streamlit  as st
global estacao,df
#from csv2pdf import convert
#from io import BytesIO

#from fpdf import FPDF


def main():
    def gerar_pdf_tabela(dataframe: pd.DataFrame) -> bytes:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Relatório de Tabela", ln=True)
        pdf.set_font("Helvetica", "B", 10)

        col_w = pdf.epw / len(dataframe.columns)
        row_h = 8

        for col in dataframe.columns:
            pdf.cell(col_w, row_h, str(col), border=1)
        pdf.ln(row_h)

        pdf.set_font("Helvetica", "", 10)
        for _, row in dataframe.iterrows():
            for val in row:
                pdf.cell(col_w, row_h, str(val), border=1)
            pdf.ln(row_h)

        buf = BytesIO()
        pdf.output(buf)
        return buf.getvalue()
    def consulta(tipo,datai,horai,dataf,horaf,area):

        import datetime
        import time
        import requests
        import pandas as pd
        import json
        from datetime import datetime, timedelta, date
        from bs4 import BeautifulSoup
        estacaoasw=[]
        arquivo = []
       
        f = open("metarteste.csv", "w")
        
        
        data_hora1 = datetime.combine(datai, horai)
        data_hora2 = datetime.combine(dataf, horaf)
        diferenca = data_hora2 - data_hora1
        intervalo=int(str(diferenca).split(":")[0])
        horainicialint=int(str(horai).split(":")[0])
        horafinalint = int(str(horaf).split(":")[0])

        if area==1:
            estacaoaws = []
            estacaoaws.append('SBJR%2C')
            estacaoaws.append('SBJR%2C')
            estacaoaws.append('SBMI%2C')
            estacaoaws.append('SBES%2C')
            estacaoaws.append('SBME%2C')
            estacaoaws.append('SBFS%2C')
            estacaoaws.append('SBCP%2C')
            estacaoaws.append('SBRJ%2C')
            estacaoaws.append('SBCB%2C')
            estacaoaws.append('SBVT%2C')
            estacaoaws.append('SBPS%2C')
            estacaoaws.append('SBGL%2C')

            estacaoaws.append('SBNT%2C')
            estacaoaws.append('SBMS%2C')
            estacaoaws.append('SBAC%2C')
            estacaoaws.append('SBJE%2C')
            estacaoaws.append('SBPB%2C')
            estacaoaws.append('SBAR%2C')
            estacaoaws.append('SBMO%2C')
            estacaoaws.append('SBRF%2C')
            estacaoaws.append('SBJP%2C')
            estacaoaws.append('SBSG%2C')
            estacaoaws.append('SBFZ%2C')
            estacaoaws.append('SBSL%2C')

            estacaoaws.append('SBTE%2C')
            estacaoaws.append('SBJU%2C')
            estacaoaws.append('SBKG%2C')
            estacaoaws.append('SNRU%2C')
            estacaoaws.append('SBFN%2C')
            estacaoaws.append('SBPL%2C')
            estacaoaws.append('SBPJ%2C')




            # estacaoaws.append('SBAC%2CSBAR%2CSBCB%2CSBCP%2CSBES')
            # estacaoaws.append('SBFS%2CSBFN%2CSBFZ%2CSBGL%2CSBJE%2CSBJP')
            # estacaoaws.append('SBJU%2CSBKG%2CSBME%2CSBMI%2CSBMO%2CSBMS')
            # estacaoaws.append('SBRJ%2CSBPB%2CSBPJ')
            # estacaoaws.append('SBPL%2CSBPS%2CSBRF')
            # estacaoaws.append('SBNT%2CSBSL%2CSBSG')
            # estacaoaws.append('SBTE%2CSBVT%2CSNRU')
        elif area==2:
            estacaoaws = []
            estacaoaws.append('SBRD%2C')
            estacaoaws.append('SBRD%2C')
            estacaoaws.append('SBVH%2C')
            estacaoaws.append('SBJI%2C')
            estacaoaws.append('SSKW%2C')
            estacaoaws.append('SBRB%2C')
            estacaoaws.append('SWEI%2C')
            estacaoaws.append('SBCY%2C')
            estacaoaws.append('SBPV%2C')
            estacaoaws.append('SBCZ%2C')
            estacaoaws.append('SBTT%2C')
            estacaoaws.append('SBIZ%2C')

            estacaoaws.append('SWGN%2C')
            estacaoaws.append('SBMA%2C')
            estacaoaws.append('SBCJ%2C')
            estacaoaws.append('SBHT%2C')
            estacaoaws.append('SBTB%2C')
            estacaoaws.append('SBOI%2C')
            estacaoaws.append('SBBE%2C')
            estacaoaws.append('SBRF%2C')
            estacaoaws.append('SBMQ%2C')
            estacaoaws.append('SBSN%2C')
            estacaoaws.append('SBSO%2C')
            estacaoaws.append('SBSI%2C')

            estacaoaws.append('SBAT%2C')
            estacaoaws.append('SBIH%2C')
            estacaoaws.append('SWPI%2C')
            estacaoaws.append('SBMY%2C')
            estacaoaws.append('SBTF%2C')
            estacaoaws.append('SBUY%2C')
            estacaoaws.append('SBUA%2C')
            estacaoaws.append('SBEG%2C')
            estacaoaws.append('SBBV%2C')
        elif area == 3:
            estacaoaws = []
            estacaoaws.append('SBBV,'+estacao+'%2C')



            # estacaoaws.append('SBRD%2CSBVH%2CSWEI%2CSBUY%2CSBJI%2CSBRB')
            # estacaoaws.append('SSKW%2CSBCY%2CSBPV%2CSBCZ%2CSBTT%2CSBIZ')
            # estacaoaws.append('SWGN%2CSBMA%2CSBCJ%2CSBHT%2CSBTB%2CSBOI')
            # estacaoaws.append('SWPI%2CSBBE%2CSBMQ%2CSBSN%2CSBSO')
            # estacaoaws.append('SBSI%2CSBAT%2CSBIH%2CSBMY%2CSBTF%2CSBUA')
            # estacaoaws.append('SBEG%2CSBBV')
        for k in range(0, len(estacaoaws)):

            for j in range(0, intervalo + 1, 1):

                #datainic = datahini + timedelta(days=j)
                anoi = str(datai)[0:4]
                mesi = str(datai)[5:7]
                diai = str(datai)[8:10]
                #horaii = str(int(horai[0:2])+int(j))
                horaii = str(horainicialint+j)
                datainicio = diai + '/' + mesi + '/' + anoi
                anof = str(datai)[0:4]
                mesf = str(datai)[5:7]
                diaf = str(datai)[8:10]
                #horaff = str(int(horai[0:2])+int(j))


                # url = 'https://redemet.decea.gov.br//api/consulta_automatica/index.php?local=sbbr,sbgl,sbsp&msni=2023041900&data_fim=2023041923&saida_html=SIM'g=metar&data_i

                if tipo=="TAF":
                    url = 'https://api-redemet.decea.mil.br/mensagens/taf/' + estacaoaws[k] + '?api_key=bIV369CxQg0Zc8x0RoQPx75pXCfrBZqGZr1nfi2T' + '&msg=taf&data_ini=' + anoi + mesi + diai + horaii+'&data_fim=' + anof + mesf + diaf + horaii+'&saida_html=SIMhoraii&page_tam=200'
                else:
                    url = 'https://api-redemet.decea.mil.br/mensagens/metar/' + estacaoaws[k] + '?api_key=bIV369CxQg0Zc8x0RoQPx75pXCfrBZqGZr1nfi2T' + '&msg=metar&data_ini=' + anoi + mesi + diai + horaii + '&data_fim=' + anof + mesf + diaf + horaii + '&saida_html=SIMhoraii&page_tam=200'

                print('cheguei 1')
                print(url)
                res = requests.get(url)
                soup = BeautifulSoup(res.content, "lxml")
                s = soup.select('html')[0].text.strip('jQuery1720724027235122559_1542743885014(').strip(')')
                s = s.replace('null', '"placeholder"')
                s = s.replace('- ', ',')
                s = s.replace('\/', '/')
                p = s.split('"mens":')
                print('cheguei 2')
                print(p)

                for i in range(1, len(p), 1):
                    if p[i].find('METAR') > -1:
                        b = 'METAR'
                    else:
                        b = 'SPECI'
                    if p[i].find('SB') > -1:
                        a = p[i][p[i].find('SB'):p[i].find(
                            'SB') + 4]  # or p[i].find('SSKW') > -1 or mensagem1[i].find('SWPI') > -1 or mensagem1[i].find('SWEI') > -1:
                    elif p[i].find('SSKW') > -1:
                        a = 'SSKW'
                    elif p[i].find('SWPI') > -1:
                        a = 'SWPI'
                    elif p[i].find('SWEI') > -1:
                        a = 'SWEI'
                    elif p[i].find('SNRU') > -1:
                        a = 'SNRU'

                    #montalinha = str(i) + ',' + a + ',' + b + ',' + datainicio + ',' + p[i][0:p[i].find('=') + 1]
                    montalinha = p[i][0:p[i].find('=') + 1]
                    arquivo.append(montalinha)
                    montalinha = montalinha.replace('"', '')
                    f.write("\n" + montalinha)
        f.close()
        return arquivo




    clicou=False
    st.set_page_config(layout="wide")
    while True:
        with st.sidebar:
            with st.container(border=True):
                # end_date = datetime.today()
                # start_date = datetime.today()
                tipo = st.radio("Escolha a mensagem",["Metar", "TAF"], horizontal=True)
                # diain = st.date_input('Dia Inicial:', start_date)
                # diafi = st.date_input('Dia Final:', end_date)
                hoje_zulu = datetime.now(timezone.utc).date()
                agora_zulu = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)

                col1, col2 = st.columns(2)

                with col1:
                    datai = st.date_input("Data Inicial", value=hoje_zulu,format="DD/MM/YYYY")
                    dataf = st.date_input("Data Final", value=hoje_zulu, format="DD/MM/YYYY")

                with col2:
                    horai = st.time_input("Hora Inicial",value=agora_zulu,step=3600)
                    horaf = st.time_input("Hora Final", value=agora_zulu, step=3600)

                #col3, col4 = st.columns(2)

                #with col3:
                    #area1 = st.checkbox("Área_1",value=True)
                area = st.radio("Escolha a área", ["Área 1", "Área 2","Estação"], horizontal=True)

                #with col4:
                #    area2 = st.checkbox("Área_2")
                if area =='Área 1':
                    area=1
                if area =='Área 2':
                    area=2
                if area == 'Estação':
                    estacao = (st.text_input('Escolha a estação:')).upper()
                    #estacao="SBGR"+estacao
                    area=3

                col5, col6 = st.columns(2)
                with col5:
                    if st.button("Consultar", use_container_width=True):
                        pdf=consulta(tipo, datai, horai, dataf, horaf, area)
                        clicou=True


                with col6   :
                    if st.button("Salvar pdf", use_container_width=True):
                        st.write("Em implementação")
                        #pdf_bytes = gerar_pdf_tabela(df)

                       # st.download_button(
                        #    label="Baixar tabela em PDF",
                        #    data=pdf_bytes,
                       #     file_name="tabela.pdf",
                       #     mime="application/pdf",
                      #  )






        break

    if tipo=="Metar" or tipo=="TAF":


        if clicou:
            df = pd.read_csv("metarteste.csv")
            df.to_csv("arquivo_limpo.csv", index=False)
            df = pd.read_csv("arquivo_limpo.csv")



            #st.dataframe(df, use_container_width=True, height=1000,hide_index=True)
            df.index = [""] * len(df)
            df.columns = [""] * len(df.columns)
            st.markdown(
                    """
                    <style>
                    [data-testid="stTable"] table {
                        white-space: nowrap;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
            if tipo=="Metar":

                st.dataframe(df,height=300)
            else:
                st.dataframe(df, use_container_width=True,row_height=80)
            
           # st.table(df, width="stretch")
            html = df.to_html(index=False)
            #convert("arquivo_limpo.csv", "relatorio.pdf", orientation="L", delimiter=";")
            #clicou=False

            #pdf_bytes = gerar_pdf_tabela(df)

            #st.download_button(
             #   label="Baixar tabela em PDF",
             #   data=pdf_bytes,
              #  file_name="tabela.pdf",
               # mime="application/pdf",
           # )

st.set_page_config(
        page_title="Consulta Redemet",
        page_icon="✅",
        layout="wide",
    )
#st.session_state
main()
