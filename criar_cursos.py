"""Página de Criação de Cursos."""
global data12,data24,dataval
#global horamudab[],bdirgmb[],bvelgmb[],visgmb[],tpgmb[], qn1gmb[],aln1gmb[num], qn2gmb[],aln2gmb[num], qn3gmb[],aln3gmb[num]
def form_curso(estarea,horainicio,dataenvio,diainicio,estacao):


    def validadetaf(horainicio,diainicio):

        diainti=int(diainicio)
        diaintf= diainti+1

        if diainti <10:
            diainiciali='0'+str(diainti)
        else:
            diainiciali = diainicio

        if diaintf < 10:
            diainicialf = '0' + str(diainti)
        else:
            diainicialf = str(diaintf)



        if horainicio=='00':
            dtavali12=diainiciali+horainicio+'/'+diainiciali+'12'
            dtavali24=diainiciali+horainicio+'/'+ diainiciali+'24'
        elif horainicio=='06':
            dtavali12 = diainiciali + horainicio + '/' + diainiciali + '18'
            dtavali24 = diainiciali + horainicio + '/' + diainicialf + '06'
        elif horainicio=='12':
            dtavali12 = diainiciali + horainicio + '/' + diainiciali + '24'
            dtavali24 = diainiciali + horainicio + '/' + diainicialf + '12'
        elif horainicio=='18':
            dtavali12 = diainiciali + horainicio + '/' + diainicialf + '06'
            dtavali24 = diainiciali + horainicio + '/' + diainicialf + '18'
        return dtavali12,dtavali24

    def home(horainicio, diainicio,estacao):
        global data12, data24,dataval,estaux
        #import streamlit as st
        data12, data24 = validadetaf(horainicio, diainicio)
        if estacao=='SBRJ':
            dataval=data12
        else :
            dataval = data24


    def becmg(ventodir,visibi,tp,qn,anv,num):
        import pandas as pd
        import streamlit as st


        col11, col12, col13, col14, col15, col16 = st.columns(6)
        # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
        with col11:
            bdirgmb = st.selectbox('Direção do Vento', ventodir)
            bvelgmb = st.text_input('Int. do Vento', max_chars=2)
        with col12:
            visgmb = st.selectbox('Visibilidade', visibi)
            tpgmb = st.selectbox('Tempo Presente', tp)

        with col13:
            qn1gmb = st.selectbox('Quant.de nuvens1', qn)
            aln1gmb = st.selectbox('Altura das nuvens1', anv)
        with col14:
            qn2gmb = st.selectbox('Quant.de nuvens2', qn)
            aln2gmb = st.selectbox('Altura das nuvens2', anv)
        with col15:
            qn3gmb = st.selectbox('Quant.de nuvens3', qn)
            aln3gmb = st.selectbox('Altura das nuvens3', anv)
        with col16:
            qn4gmb= st.selectbox('Quant.de nuvens4', qn)
            aln4gmb = st.selectbox('Altura das nuvens4', anv)
    def becmg1(ventodir,visibi,tp,qn,anv,num):
        import pandas as pd
        import streamlit as st

        hormudab1 = st.text_input('Hora1 Mudança', max_chars=9)
        col11, col12, col13, col14, col15, col16 = st.columns(6)
        # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
        with col11:
            bdirgmb1 = st.selectbox('Direção do Vento1', ventodir)
            bvelgmb1 = st.text_input('Int. do Vento1', max_chars=2)
        with col12:
            visgmb1 = st.selectbox('Visibilidade1', visibi)
            tpgmb1 = st.selectbox('Tempo Presente1', tp)

        with col13:
            qn1gmb1 = st.selectbox('Quant.de nuvens11', qn)
            aln1gmb1 = st.selectbox('Altura das nuvens11', anv)
        with col14:
            qn2gmb1 = st.selectbox('Quant.de nuvens21', qn)
            aln2gmb1 = st.selectbox('Altura das nuvens21', anv)
        with col15:
            qn3gmb1 = st.selectbox('Quant.de nuvens31', qn)
            aln3gmb1 = st.selectbox('Altura das nuvens31', anv)
        with col16:
            qn4gmb1= st.selectbox('Quant.de nuvens41', qn)
            aln4gmb1 = st.selectbox('Altura das nuvens41', anv)

    import pandas as pd
    import streamlit as st
    #estacao=" "
    #dataval=' '
    """Função de Formulário de Criação de TAF."""
    st.header("Criação de TAF")
    ventodir=[' ','360', '010', '020', '030', '040', '050', '060', '070',
                                                '080', '090', '100', '110', '120', '130', '140', '150', '160', '170',
                                                '180', '190','200', '210', '220', '230', '240', '250', '260', '270',
                                                '280', '290', '300', '310', '320', '330', '340', '350', '360']
    visibi=[' ', 'CAVOK','9999','9000','8000','7000','6000','5000','4900','4800','4700','4600','4500','4400','4300','4200','4100','4000',
            '3900','3800','3700','3600','3500','3400','3300','3200','3100','3000','2900','2800','2700','2600','2500','2400','2300','2200','2100','2000',
            '1900','1800','1700','1600','1500','1400','1300','1200','1100','1000','0950','0900','0850','0800','0750','0700','0650','0600','0550','0500',
            '0450','0400','0350','0300','0250','0200','0150','0100','0050','0040','0030','0020','0010','0009','0008','0007','0006','0005','0004',
            '0003','0002','0001','VV001']
    tp=[' ','BR', 'HZ', '-RA', 'RA', '+RA','TS' ,'TSRA', '-TSRA', '+TSRA','FU', 'SHRA', '-SHRA', '+SHRA','VCSH','VCTS',
            'DZ','-DZ','+DZ','RABR']
    qn=[' ','NSC','FEW', 'SCT', 'BKN', 'OVC', 'VV']
    anv=[' ','001','002', '003', '004', '005', '006', '007', '008', '009','010', '011', '012', '013','014','015',
        '016','017','018','019','020','021', '022', '023','024','025','026','027','028','029','030','031', '032', '033','034','035','036','037','038','039',
        '040','041', '042', '043','044','045','046','047','048','049','050']
    with st.container(border=True):
        st.markdown("## :gear: Corpo Principal")

        with st.form("form_taf"):
            col01,col02,col03,col04=st.columns(4)
            with col01:
                estacao = st.selectbox('Código ICAO: ', estarea,on_change=home(horainicio,diainicio,estacao),args=('selectbox',))
                #data12, data24 = validadetaf(horainicio, diainicio)
                if estacao=='SBRJ':
                    dataval=data12
                else:
                    dataval = data24
            with col02:
                dataconf = st.date_input('Data de confecção:')
            with col03:
                horaconf = st.time_input('Hora de confecção:')
            with col04:
                validade = st.text_input('Data validade',dataval)




           # submit = st.form_submit_button("Criação")


        #with st.form("form-cp"):
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10= st.columns(10)
            with col1:
                dircp=st.selectbox('Direção do Vento',ventodir)
            with col2:
                velcp=st.text_input('Int. do Vento',max_chars=2)
            with col3:
                viscp=st.selectbox('Visibilidade',visibi)

            with col4:
                tpcp = st.selectbox('Tempo Presente', tp)
            with col5:
                qn1=st.selectbox('Quant.de nuvens1', qn)
                aln1=st.selectbox('Altura das nuvens1', anv)
            with col6:
                qn2=st.selectbox('Quant.de nuvens2', qn)
                aln2= st.selectbox('Altura das nuvens2',anv)
            with col7:
                qn3 = st.selectbox('Quant.de nuvens3' ,qn)
                aln3= st.selectbox('Altura das nuvens3',anv)
            with col8:
                qn4 = st.selectbox('Quant.de nuvens4', qn)
                aln4 = st.selectbox('Altura das nuvens4', anv)
            with col9:
                txcp= st.text_input('Temp máxima: ')
                txhr=st.text_input('Hora max: ')
            with col10:
                tncp= st.text_input('Temp mínima: ')
                tnhr = st.text_input('Hora min: ')


            submit = st.form_submit_button("Criação TAF")

            if submit:
                novo_taf = {
                    "Estação": estacao,
                    "Data confecção": dataconf,
                    "Hora confecção": horaconf,
                    "Validade": validade,
                    "dircp": dircp,
                    "velcp": velcp,
                    "viscp": viscp,
                    "tpcp": tpcp,
                    "qn1" : qn1,
                    "aln1": aln1,
                    "qn2": qn2,
                    "aln2": aln2,
                    "qn3": qn3,
                    "aln3": aln3,
                    "qn4": qn4,
                    "aln4": aln4,
                    "txcp": txcp,
                    "txhr": txhr,
                    "tncp": tncp,
                    "tnhr": tnhr

                    # "Nome do Professor": professor_curso,
                }

                try:
                    df = pd.read_csv("data/taf.csv")
                except FileNotFoundError:
                    df = pd.DataFrame(
                        columns=[
                            "Estação",
                            "Data confecção",
                            "Hora confecção",
                            "Validade",
                            "dircp",
                            "velcp",
                            "viscp",
                            "tpcp",
                            "qn1",
                            "aln1",
                            "qn2",
                            "aln2",
                            "qn3",
                            "aln3",
                            "qn4",
                            "aln4",
                            "txcp",
                            "txhr",
                            "tncp",
                            "tnhr"
                            # "Nome do Professor",
                        ]
                    )
                df = pd.concat([df, pd.DataFrame([novo_taf])], ignore_index=True)

                df.to_csv("data/taf.csv", index=False)
                st.success("TAF criado com sucesso!")
    on = st.toggle("Grupo de Mudanças")
    if on:
        with st.container(border=True):
            st.markdown("## :gear: Grupo de Mudanças")
            options = ["BECMG", "FM", "PROB30", "PROB40", "TEMPO", "PROB30 TEMPO", "PROB40 TEMPO"]
            selection = st.segmented_control("Mudanças", options, selection_mode="single")

           #if selection:
            if selection=="BECMG":
                with st.form("form_becmgtaf"):


                    # hormuda=st.text_input('Hora Mudança',max_chars=9)
                    # col11, col12, col13, col14, col15, col16 = st.columns(6)
                    # # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
                    # with col11:
                    #     bdirgm = st.selectbox('Direção do Vento', ventodir)
                    #     bvelgm = st.text_input('Int. do Vento', max_chars=2)
                    # with col12:
                    #     visgm = st.selectbox('Visibilidade', visibi)
                    #     tpgm = st.selectbox('Tempo Presente', tp)
                    #
                    # with col13:
                    #     qn1gm = st.selectbox('Quant.de nuvens1', qn)
                    #     aln1gm = st.selectbox('Altura das nuvens1', anv)
                    # with col14:
                    #     qn2gm = st.selectbox('Quant.de nuvens2', qn)
                    #     aln2gm = st.selectbox('Altura das nuvens2', anv)
                    # with col15:
                    #     qn3gm = st.selectbox('Quant.de nuvens3', qn)
                    #     aln3gm = st.selectbox('Altura das nuvens3', anv)
                    # with col16:
                    #     qn4gm = st.selectbox('Quant.de nuvens4', qn)
                    #     aln4gm = st.selectbox('Altura das nuvens4', anv)
                    becmg(ventodir,visibi,tp,qn,anv,0)

                    submit1 = st.form_submit_button("GRUPO BECMG")

                    if submit1:
                        becmg1(ventodir, visibi, tp, qn, anv,1)


            elif selection=='TEMPO':
                with st.form("form_becmgtaf"):
                    hormuda = st.text_input('Hora Mudança', max_chars=9)
                    col11, col12, col13, col14, col15, col16 = st.columns(6)
                    # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
                    with col11:
                        dirgm = st.selectbox('Direção do Vento', ventodir)
                        velgm = st.text_input('Int. do Vento', max_chars=2)
                    with col12:
                        visgm = st.selectbox('Visibilidade', visibi)
                        tpgm = st.selectbox('Tempo Presente', tp)

                    with col13:
                        qn1gm = st.selectbox('Quant.de nuvens1', qn)
                        aln1gm = st.selectbox('Altura das nuvens1', anv)
                    with col14:
                        qn2gm = st.selectbox('Quant.de nuvens2', qn)
                        aln2gm = st.selectbox('Altura das nuvens2', anv)
                    with col15:
                        qn3gm = st.selectbox('Quant.de nuvens3', qn)
                        aln3gm = st.selectbox('Altura das nuvens3', anv)
                    with col16:
                        qn4gm = st.selectbox('Quant.de nuvens4', qn)
                        aln4gm = st.selectbox('Altura das nuvens4', anv)

                    submit1 = st.form_submit_button("GRUPO TEMPO")










