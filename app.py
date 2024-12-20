"""Arquivo principal do Streamlit."""

import streamlit as st
from streamlit import runtime
import sys
from streamlit.web import cli as stcli

from datetime import datetime, timedelta, date



import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

import criar_cursos
import criar_cursos2
from home import home
import listar_cursos
def main():
    st.set_page_config(page_title="Confecção de TAF", page_icon="🏫", layout="wide")

    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.sidebar.title("Páginas")
        st.sidebar.write(f'Bem Vindo *{st.session_state["name"]}*')

        paginas = st.sidebar.selectbox("Selecione uma página", ("Home", "Lista de TAF", "Criar TAF", "Ajuda") )
        with st.sidebar:
            with st.container(border=True):
                on = st.toggle('Gerenciar dados')

                if on == True:
                    selarea = st.radio("Escolha a área", ["Área 1", "Área 2"], horizontal=True)
                    if selarea == 'Área 1':
                        estarea = [' ','SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT',
                                   'SBMS',
                                   'SBAC', 'SBJE', 'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL',
                                   'SBTE',
                                   'SBJU', 'SBKG', 'SBFN', 'SBPL', 'SBPJ']
                    else:
                        estarea = [' ','SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI',
                                   'SBMA',
                                   'SBCJ', 'SBHT', 'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT',
                                   'SBIH', 'SBMY', 'SBTF',
                                   'SBUA', 'SBEG', 'SBBV', 'SSKW', 'SWEI', 'SWPI']
                else:
                    estarea = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
                               'SBAC', 'SBJE', 'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE',
                               'SBJU', 'SBKG', 'SBFN', 'SBPL', 'SBPJ']
                on1 = st.toggle('Data hora de inicio da validade')

                if on1 == True:
                    selvalidade = st.radio("Escolha a validade", ["Atual", "Definir"], horizontal=True)
                    if selvalidade == 'Atual':
                        datavalidade = datetime.utcnow()
                        dia = datavalidade.day
                        if dia < 10:
                            diastr = '0' + str(dia)
                        else:
                            diastr = str(dia)

                        hora = datavalidade.hour
                        mes = datavalidade.month
                        minuto = datavalidade.minute
                        if hora > 17 and hora <= 22:
                            horainicio = '00'
                            diainicioaux = dia + 1
                            if diainicioaux < 10:
                                dianicio = '0' + str(diainicioaux)
                            else:
                                dianicio = str(diainicioaux)
                        elif hora > 22:# or hora < 29:
                            horainicio = '06'
                            diainicioaux = dia + 1
                            if diainicioaux < 10:
                                dianicio = '0' + str(diainicioaux)
                            else:
                                dianicio = str(diainicioaux)
                        elif hora > 5 and hora < 11:
                            horainicio = '12'
                            diainicioaux = dia
                            if diainicioaux < 10:
                                dianicio = '0' + str(diainicioaux)
                            else:
                                dianicio = str(diainicioaux)
                        else:
                            horainicio = '18'
                            diainicioaux = dia
                            if diainicioaux < 10:
                                dianicio = '0' + str(diainicioaux)
                            else:
                                dianicio = str(diainicioaux)
                        if hora < 10:
                            horastring = '0' + str(hora)
                        else:
                            horastring = str(hora)
                        if minuto < 10:
                            minstring = '0' + str(minuto)
                        else:
                            minstring = str(minuto)

                        dataenvio = dianicio + horastring + minstring + 'Z'




        if paginas == "Home":
             home()
        elif paginas == "Criar TAF":
                 criar_cursos2.form_curso(estarea,horainicio,dataenvio,dianicio,' ')
        elif paginas == "Lista de TAF":
            listar_cursos.listar()
        else:
            st.write("Ainda Estou desenvolvendo")




    elif st.session_state["authentication_status"] is False:
        st.error("Usuário/Senha is inválido")
    elif st.session_state["authentication_status"] is None:
        st.warning("Por Favor, utilize seu usuário e senha!")
if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())