import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import sys
#from streamlit import cli as stcli
from streamlit.web import cli as stcli
import streamlit
def main():
    import numpy as np  # np mean, np random
    import pandas as pd  # read csv, df manipulation
    import plotly.express as px  # interactive charts
    import plotly.graph_objects as go
    import streamlit as st  #
    from datetime import datetime, timedelta
    from plotly.subplots import make_subplots
    st.set_page_config(
        page_title="Real-Time Data Science Dashboard",
        page_icon="✅",
        layout="wide",
    )

    # read csv from a github repo
    #dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


    # read csv from a URL
    # @st.experimental_memo
    # def get_data() -> pd.DataFrame:
    #     return pd.read_csv(dataset_url)

    st.cache(allow_output_mutation=True)
    df = pd.read_csv('metar_trat_teste1.csv')
    x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in df.datahora]
    df['data_hora'] = x
    df['period'] = df['data_hora'].dt.hour
    df.drop(columns=["metar", "speci", "gust"], inplace=True)
    df.sort_values(by=['data_hora'], inplace=True)
    df = df.reset_index(drop=True)
    # dashboard title

    st.title("Dados Estatísticos")
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # top-level filters
    job_filter = st.selectbox("Selecione o aeródromo", pd.unique(df["estacao"]))

    # creating a single-element container
    placeholder = st.empty()

    # dataframe filter
    df = df[df["estacao"] == job_filter]

    # near real-time / live feed simulation
    for seconds in range(200):
        df["wspd_new"] = df["wspd"]
        df["wdir_new"] = df["wdir"]
        df["dryt_new"] = df["dryt"]

        # creating KPIs
        avg_wspd = np.mean(df["wspd_new"])
        avg_dryt = np.mean(df["dryt_new"])

        # count_married = int(
        #     df[(df["marital"] == "married")]["marital"].count()
        #     + np.random.choice(range(1, 30))
        # )

        avg_wdir = np.mean(df["wdir_new"])

        with placeholder.container():
            # create three columns
            kpi1, kpi2, kpi3 = st.columns(3)

            # fill in those three columns with respective metrics or KPIs
            kpi1.metric(
                label="Int vento(kt) ⏳",
                value=round(avg_wspd),
                delta=round(avg_wspd) - 10,
            )

            kpi2.metric(
                label="Temperatura(°C) 💍",
                value=round(avg_dryt),
                delta=round(avg_dryt) - 10,
            )

            kpi3.metric(
                label="Direção do vento ＄",
                value=round(avg_wdir),
                delta=round(avg_wdir) - 10,
            )

            # create two columns for charts
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("### Gráfico 1")

                fig = go.Figure(go.Histogram2dContour(
                    x=df["period"],
                    y=df["altn1"],
                    colorscale='Jet',
                    contours=dict(
                        showlabels=True,
                        labelfont=dict(
                            family='Raleway',
                            color='white'
                        )
                    ),
                    hoverlabel=dict(
                        bgcolor='white',
                        bordercolor='black',
                        font=dict(
                            family='Raleway',
                            color='black'
                        )
                    )

                ))
                fig.update_xaxes(title_text="hora")
                fig.update_yaxes(title_text="altura nuvens baixas(ft)")
                


                st.write(fig)

            with fig_col2:
                st.markdown("### Gráfico 2")
                fig2 = px.histogram(data_frame=df, x="dryt")

                st.write(fig2)

            st.markdown("### Dados metar descodificado")
            st.dataframe(df)
            time.sleep(1)
if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
