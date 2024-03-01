import pandas as pd
import plotly.express as px
import streamlit as st

def readData(file):
    tmp = pd.read_csv(file)
    return tmp

def main():
    data = readData("./grdp_birth_2020.csv")
    # print( data.info() )
    # print( data )
    fig = px.scatter( data_frame = data,
                      x = "price_2020", y = "birth",
                      log_x=True,
                      color = "sido_nm",
                      color_discrete_sequence=px.colors.qualitative.Dark24,
                      hover_name="adm_nm", hover_data=["price_2020", "birth"],
                      labels ={"price_2020": "GRDP(백만원)",
                               "birth": "신생아 출산(명)",
                               "sido_nm": "시도명"})
    # 크기, 마진 설정
    fig.update_layout(
        width=800,
        height=600,
        margin_l=50,
        margin_r=20,
        margin_b=50,
        margin_t=20
        # 백그라운드 칼라 지정, margin 잘 보이게 하기위함
        # paper_bgcolor = "LightSteelBlue"
    )
    # fig.show()
    st.plotly_chart( fig, use_container_width=True)

if __name__ == "__main__":
    main()
