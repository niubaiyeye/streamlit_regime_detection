import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

######
file_path = 'Data\\'
list = ['000016.SH', '000300.SH', '000852.SH', '000905.SH']
######
def upload_data(file):
    file_address = os.path.join(file_path + file + '.csv')
    df = pd.read_csv(file_address)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['CLOSE','superTrend','volRank','atrRank','volvPctRank', 'vmPctRank', 'DailyVolRank'])
    return df

def draw_pic(file):
    df = upload_data(file)
    # ax1
    fig, ax1 = plt.subplots(figsize=(15, 8))
    ax1.set_ylabel('Rank', color='black')
    ax1.tick_params('y', colors='black')
    ax1.set_xlabel('date')
    p1 = ax1.bar(df['date'], df['volRank'], color=('orange', 0.5), label='volRank')
    p2 = ax1.bar(df['date'], df['atrRank'], color=('purple', 0.5), bottom=df['volRank'], label='atrRank')
    p3 = ax1.bar(df['date'], df['volvPctRank'], color=('sienna', 0.5), bottom=df['volRank'] + df['atrRank'],
                 label='volvPctRank')
    p4 = ax1.bar(df['date'], df['vmPctRank'], color=('cornflowerblue', 0.5),
                 bottom=df['volRank'] + df['atrRank'] + df['volvPctRank'], label='vmPctRank')
    p5 = ax1.bar(df['date'], df['DailyVolRank'], color=('teal', 0.5),
                 bottom=df['volRank'] + df['atrRank'] + df['volvPctRank'] + df['vmPctRank'], label='DailyVolRank')
    ymax = (df['volRank'] + df['atrRank'] + df['volvPctRank'] + df['vmPctRank'] + df['DailyVolRank']).max() * 1.5
    ax1.set_ylim(0, ymax)
    ax1.grid(axis='y', linestyle='-', color='gray', alpha=0.3)

    # ax2
    ax2 = ax1.twinx()
    ax2.plot(df['date'], df['CLOSE'], color='red', label='CLOSE', linewidth=2.5)
    ax2.plot(df['date'], df['superTrend'], color='forestgreen', label='superTrend', linestyle='--', linewidth=2.5)
    ax2.set_ylabel('Index', color='black')
    ax2.tick_params('y', colors='black')

    # 添加图例
    bar, labels1 = [p1, p2, p3, p4, p5], ['volRank', 'atrRank', 'volvPctRank', 'vmPctRank', 'DailyVolRank']
    line, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(bar + line, labels1 + labels2, loc='upper left')

    # 调整布局
    plt.tight_layout()
    return(fig)



def page50():
    st.title("SS50_VolChart")
    fig = draw_pic('000016.SH')
    st.pyplot(fig)
def page300():
    st.title("HS300_VolChart")
    fig = draw_pic('000300.SH')
    st.pyplot(fig)

def page500():
    st.title("CSI500_VolChart")
    fig = draw_pic('000852.SH')
    st.pyplot(fig)

def page1000():
    st.title("CSI1000_VolChart")
    fig = draw_pic('000905.SH')
    st.pyplot(fig)

def page000016():
    st.title("000016.SH")
    df = upload_data('000016.SH')
    st.dataframe(df)

def page000300():
    st.title("000300.SH")
    df = upload_data('000300.SH')
    st.dataframe(df)

def page000852():
    st.title("000852.SH")
    df = upload_data('000852.SH')
    st.dataframe(df)


def page000905():
    st.title("000905.SH")
    df = upload_data('000905.SH')
    st.dataframe(df)


st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ("SS50_VolChart", "HS300_VolChart", "CSI500_VolChart", "CSI1000_VolChart", "000016 SH", "000300 SH", "000852 SH", "000905 SH"))

# 根据选择显示相应的页面
if selection == "SS50_VolChart":
    page50()
if selection == "HS300_VolChart":
    page300()
if selection == "CSI500_VolChart":
    page500()
if selection == "CSI1000_VolChart":
    page1000()
if selection == "000016 SH":
    page000016()
if selection == "000300 SH":
    page000300()
if selection == "000852 SH":
    page000852()
if selection == "000905 SH":
    page000905()


