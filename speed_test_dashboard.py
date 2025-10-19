import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('speed_test_data.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Time Range filter
def timerange_filter(dataframe, choice):
    latest = dataframe['timestamp'].max()

    if choice == "Last 24 hours":
        start = latest - pd.Timedelta(days=1)
    elif choice == "Last 3 days":
        start = latest - pd.Timedelta(days=3)
    elif choice == "Last week":
        start = latest - pd.Timedelta(weeks=1)
    elif choice == "Last 2 weeks":
        start = latest - pd.Timedelta(weeks=2)
    elif choice == "Last month":
        start = latest - pd.DateOffset(months=1)
    else:
        return dataframe

    return dataframe[dataframe['timestamp'] >= start]


# Latest Speed test
def latest_speed_test(df):
    col_download, col_upload, col_ping, col_runs, = st.columns(4)

    with col_download:
        st.text("⬇️ Download Speed") 
        st.subheader(f"{df.iloc[-1]['download_mbps']} Mbps")

        download_mean = df['download_mbps'].mean()
        download_deviation = round(df.iloc[-1]['download_mbps'] - download_mean, 1)

        if download_deviation < 0:
            st.write(f" :red[↓ {download_deviation} vs avg]")
        else:
            st.write(f":green[↑ {download_deviation} vs avg]")

    with col_upload:
        st.text("⬆️ Upload Speed")
        st.subheader(f"{df.iloc[-1]['upload_mbps']} Mbps")

        upload_mean = df['upload_mbps'].mean()
        upload_deviation = round(number=df.iloc[-1]['upload_mbps'] - upload_mean, ndigits=1)

        if upload_deviation < 0:
            st.write(f" :red[↓ {upload_deviation} vs avg]")
        else:
            st.write(f":green[↑ {upload_deviation} vs avg]") 

    with col_ping:
        st.text("📊 Ping")
        st.subheader(f"{df.iloc[-1]['ping_ms']} ms")

        ping_mean = df['ping_ms'].mean()
        ping_deviation = round(number=df.iloc[-1]['ping_ms'] - ping_mean, ndigits=1)

        if ping_deviation > 0:
            st.write(f" :red[↑ {ping_deviation} vs avg]")
        else:
            st.write(f":green[↓ {ping_deviation} vs avg]") 

    with col_runs:
        st.text("🏃‍♂️‍➡️ Test Runs")
        rows, columns = df.shape
        st.subheader(rows)

    st.write(f":gray[ISP: {df.iloc[-1]['isp']}]")
    st.write(f":gray[Server: {df.iloc[-1]['server_name']} ({df.iloc[-1]['server_location']})]")
    st.write(f":gray[Last test: {df.iloc[-1]['timestamp']}]")


# Chart 1 : Download/Upload Speeds
def download_upload_chart(df):
    df_speeds = df.melt(id_vars='timestamp', 
                        value_vars=['download_mbps', 'upload_mbps'], 
                        var_name='Type', 
                        value_name='Speed (Mbps)')

    df_speeds['Type'] = df_speeds['Type'].replace({'download_mbps': 'Download',
                                                'upload_mbps': 'Upload'})
    chart_speeds = px.line(df_speeds, 
                        x='timestamp', 
                        y='Speed (Mbps)', 
                        color='Type', 
                        labels={'timestamp': 'Time', 
                                'Speed (Mbps)': 'Speed (Mbps)',
                                'Type': ''}, 
                            markers=True, 
                            range_y=(0,df['download_mbps'].max()+10),
                            color_discrete_map={'Download': 'green',
                                                'Upload': 'blue'})

    for trace in chart_speeds.data:
        if trace.name == 'Download':
            trace.update(fill='tozeroy', fillcolor='rgba(0, 128, 0, 0.1)')
        elif trace.name == 'Upload':
            trace.update(fill='tozeroy', fillcolor='rgba(0, 0, 255, 0.05)')

    chart_speeds.update_layout(
        hovermode='x unified',
        hoverlabel=dict(bgcolor='white', bordercolor='rgba(0,0,0,0.25)'))
    chart_speeds.update_xaxes(hoverformat="%b %d, %Y, %H:%M")  

    chart_speeds.update_traces(
        hovertemplate=" %{fullData.name} : %{y:.2f}<extra></extra> Mbps")
    
    st.plotly_chart(chart_speeds)


# Chart 2 : Ping latency
def ping_chart(df):
    chart_ping = px.line(df, 
                        x='timestamp', 
                        y='ping_ms', 
                        labels={'timestamp': 'Time', 
                                'ping_ms': 'Ping (ms)'}, 
                            markers=True, 
                            range_y=(0,df['ping_ms'].max()+1),
                            color_discrete_sequence=['orange'])

    mean_ping = df['ping_ms'].mean()
    chart_ping.add_hline(y=mean_ping, 
                        line_dash="dash", 
                        line_color="orange",
                        annotation_text=f"Avg Ping: {mean_ping:.1f} ms",
                        annotation_position="top")

    for trace in chart_ping.data:
        if trace.name == '':
            trace.update(fill='tozeroy', fillcolor='rgba(255, 165, 0, 0.2)')

    chart_ping.update_layout(
        hovermode='x unified',
        hoverlabel=dict(bgcolor='white', bordercolor='rgba(0,0,0,0.25)'))
    chart_ping.update_xaxes(hoverformat="%b %d, %Y, %H:%M")  

    chart_ping.update_traces(
        hovertemplate=" %{fullData.name} : %{y:.2f} ms")

    st.plotly_chart(chart_ping)


#Performance Statistics
def performance_statistics(df):
    st.subheader('Performance Statistics')

    col_download_stat, col_upload_stat, col_ping_stat = st.columns(3)

    with col_download_stat:
        st.subheader('⬇️ Download')
        st.write('Best')
        st.subheader(f'{df['download_mbps'].max()} Mbps')
        st.write('Worst')
        st.subheader(f'{df['download_mbps'].min()} Mbps')
        st.write('Average')
        st.subheader(f'{round(df['download_mbps'].mean(), 2)} Mbps')
        st.write('Std Dev')
        st.subheader(f'{round(df['download_mbps'].std(), 2)} Mbps')        


    with col_upload_stat:
        st.subheader('⬆️ Upload')
        st.write('Best')
        st.subheader(f'{df['upload_mbps'].max()} Mbps')
        st.write('Worst')
        st.subheader(f'{df['upload_mbps'].min()} Mbps')
        st.write('Average')
        st.subheader(f'{round(df['upload_mbps'].mean(), 2)} Mbps')
        st.write('Std Dev')
        st.subheader(f'{round(df['upload_mbps'].std(), 2)} Mbps')   

    with col_ping_stat:
        st.subheader('📊 Ping')
        st.write('Best')
        st.subheader(f'{df['ping_ms'].min()} ms')
        st.write('Worst')
        st.subheader(f'{df['ping_ms'].max()} ms')
        st.write('Average')
        st.subheader(f'{round(df['ping_ms'].mean(), 2)} ms')
        st.write('Std Dev')
        st.subheader(f'{round(df['ping_ms'].std(), 2)} ms') 


#Speed Test History table
def history_table():
    st.subheader("Speed Test History")
    st.dataframe(pd.read_csv('speed_test_data.csv'))

    with open("speed_test_data.csv", "r") as file:
        st.download_button(
            label="Download Data as CSV",
            data=file,
            file_name="speed_test_data.csv",
            mime="text/csv",)


def main():
    st.set_page_config(layout="wide")
    st.sidebar.subheader("⚙️ Settings")
    selection = st.sidebar.selectbox("Time Range", ("Last 24 hours",
                                                    "Last 3 days", 
                                                    "Last week",
                                                    "Last 2 weeks",
                                                    "Last month",
                                                    "All time"),
                                                    index=3)                                                    

    st.title("🌍 Internet Speed Monitor")
    st.text("Track your internet performance over time")
    st.header("Latest Speed Test")
    df_view = timerange_filter(df, selection)
    latest_speed_test(df)
    st.divider()

    st.subheader("Speed Trends")
    download_upload_chart(df_view)
    st.subheader("Ping Latency")
    ping_chart(df_view)
    st.divider()

    performance_statistics(df)
    st.divider()

    history_table()


main()


