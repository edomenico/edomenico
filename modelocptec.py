import streamlit as st
import pandas as pd
import plotly.express as px
import colorcet as cc
from streamlit import runtime
import sys
from streamlit.web import cli as stcli

def main():



    import pandas as pd
    #@st.cache_data
    def get_siglas():
        df = pd.read_csv('sigla.csv')
        df = df.rename(columns={'Sigla': 'tempo'})
        df = df.set_index('tempo')
        return df

    #@st.cache_data
    def get_coord():
        df = pd.read_csv('https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv')
        est = pd.read_csv('https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/estados.csv')
        est = est.set_index('codigo_uf')
        df = df.join(est, 'codigo_uf', rsuffix='_est')
        df['id'] = df['nome'] + '-' + df['uf']
        df['color'] = (cc.glasbey * 23)[:len(df)]
        return df

    def get_previsao(lat,lon):
        siglas = get_siglas()
        df = pd.DataFrame()
        #for i in id.index:
            #lat = id.at[i, 'latitude']
            #long = id.at[i, 'longitude']
        dfi = pd.concat([pd.read_xml(
            f'http://servicos.cptec.inpe.br/XML/cidade/7dias/{lat}/{lon}/previsaoLatLon.xml', encoding='cp1252'),
                            pd.read_xml(f'http://servicos.cptec.inpe.br/XML/cidade/{lat}/{lon}/estendidaLatLon.xml',
                                        encoding='cp1252')
                            ])
            #dfi['cidade'] = id.at[i, 'nome']
        df = pd.concat([df, dfi])
        df = df.join(siglas, 'tempo')
        df = df.dropna(subset=['dia'])
        df = df.drop(columns=['tempo', 'uf', 'atualizacao', 'nome'])
        return df

    def make_fig(prev):
        fig = px.line(prev, 'dia', ['maxima', 'minima'],
                      hover_data=['iuv', 'Descrição'])
        fig.update_yaxes(title="Temperatura")
        return fig

    area_1 = ['SBJR', 'SBMI', 'SBES', 'SBME', 'SBFS', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
              'SBAC',
              'SBJE',
              'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SNRU', 'SBFN',
              'SBPL',
              'SBPJ']
    area_2 = ['SBRD', 'SBVH', 'SBJI', 'SSKW', 'SBRB', 'SWEI', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SWGN', 'SBMA',
              'SBCJ', 'SBHT',
              'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SWPI', 'SBMY', 'SBTF', 'SBUY',
              'SBUA', 'SBEG',
              'SBBV']
    st.set_page_config(layout="wide")
    st.title("Modelo CPTEC em teste :sun_behind_rain_cloud:")
    with st.sidebar:
        with st.container(border=True):
            with st.container(border=True):
                selarea = st.radio("Escolha a área", ["Área 1", "Área 2"], horizontal=True)

                # col1, col2 = st.columns(2)
                if selarea == "Área 1":
                    # with col1:
                    # st.header('Área 1')
                    nomedaestacao = st.radio("Área 1", area_1)
                    noarea = 1

                else:
                    # st.header('Área 2')
                    nomedaestacao = st.radio("Área 2", area_2)
                    noarea = 2

            st.markdown(
                """


                e-mail → edomenico813@gmail.com


                """
            )


    file = "estacaomodelos.csv"
    data = pd.read_csv(file, sep=',')

    # Select Country

    country_data = data.loc[data.loc[:, "estacao"] == nomedaestacao, :]

    #df = pd.read_csv("estacaomodelos.csv")

    #df1=df[df['estacao'] ==nomedaestacao]
    #lat=float(df1['lat'])
    #lon = float(df1['lon'])
    print(country_data.loc[:,"lat"])
    lat = float(country_data.loc[:,"lat"])
    lon = float(country_data.loc[:,"lon"])

#    st.set_page_config(layout='wide')
    #st.title('Previsão do tempo e Localização')
    #df = get_coord()
    cols = st.columns(2)
    #cidades = cols[0].multiselect('Cidades', df['id'])
    #dados = df[df['id'].isin(cidades)]
    #if not dados.empty:
       # cols[1].dataframe(dados[['nome', 'nome_est', 'regiao', 'ddd', 'latitude', 'longitude']], hide_index=True,
        #                  width=500)
    prev = get_previsao(lat,lon)
    with st.container():
        #col1, col2 = st.columns((5, 5))

            #min_max2(df)
            #plotly_chart(make_fig(prev))
        cols[0].plotly_chart(make_fig(prev))
    #cols[0].write('dados: CPTEC/INPE')
    #plotly_chart(make_fig(prev))
    st.write('dados: CPTEC/INPE - Estação: ',nomedaestacao)
#    cols[1].map(dados.reset_index(tacao), zoom=3, color='color')

st.set_page_config(
        page_title="Tabuleiro - CMA-GL",
        page_icon="✅",
        layout="wide",
    )
#st.session_state
main()
