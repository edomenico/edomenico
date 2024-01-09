# import pandas as pd
# from datetime import datetime,timedelta
# import plotly.graph_objects as go
# import streamlit as st
#
# area=['Área 1', 'Área 2']
# area_1= ['SBJR','SBES','SBME','SBCP','SBRJ','SBCB','SBVT','SBPS','SBGL','SBNT','SBMS','SBAC','SBJE','SBPB','SBAR','SBMO','SBRF','SBJP','SBSG','SBFZ','SBSL','SBTE','SBJU','SBKG','SBFN','SBPL','SBPJ']
# area_2= ['SBRD','SBVH','SBJI','SBRB','SBCY','SBPV','SBCZ','SBTT','SBIZ','SBCI','SBMA','SBCJ','SBHT','SBTB','SBOI','SBBE','SBMQ','SBSN','SBSO','SBSI','SBAT','SBIH','SBTF','SBUA','SBEG','SBBV','SSKW']
# start_date=datetime.today()-timedelta(days=365)
# end_date=datetime.today()
#
# def consulta_dado_grafico(estacao,datainicio,datafim):
#
#     hhhh=kkkk
#
#
# barra_lateral=st.sidebar.empty()
# area_seleciona=st.sidebar.selectbox("Seleciona a área:",area)
# if area_seleciona=='Área 1':
#     areasel=area_1
# else:
#     areasel = area_2
# estacao_seleciona=st.sidebar.selectbox("Seleciona o Aeródromo",areasel)

#st.title('Dados Estatísticos')



if from_data < to_data:
    st.sidebar.error('Data de ínicio maior do que data final')
else:
    df = consulta_dado_grafico(areasel, estacao_seleciona, to_data, from_data, area_seleciona)
    if carregar_dados:
        st.subheader('Dados')
        dados = st.dataframe(df)
        stock_select = st.sidebar.selectbox
    figura=graficos(to_data,from_data)
    grafico_line = st.plotly_chart(figura)

if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
     #   sys.argv = ["streamlit", "run", sys.argv[0]]
       # sys.exit(stcli.main())
