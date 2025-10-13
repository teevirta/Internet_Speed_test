import streamlit as st
import pandas as pd

# Loading data from CSV-file
def get_data():
    df = pd.read_csv('speed_test_data.csv')

    rows, columns = df.shape
    last_row = df.iloc[-1]

    download_mbps = last_row['download_mbps']
    upload_mbps = last_row['upload_mbps']
    ping_ms = last_row['ping_ms']
    server_name = last_row['server_name']
    server_location = last_row['server_location']
    isp = last_row['isp']
    timestamp = last_row['timestamp']

    # Download speed deviation
    download_speeds = df['download_mbps']
    mean_download_mbps = download_speeds.mean()
    download_deviation = round(number=download_mbps - mean_download_mbps, ndigits=1)

    # upload speed deviation
    upload_speeds = df['upload_mbps']
    mean_upload_mbps = upload_speeds.mean()
    upload_deviation = round(number=upload_mbps - mean_upload_mbps, ndigits=1)

    # ping deviation
    ping_speeds = df['ping_ms']
    mean_ping_ms = ping_speeds.mean()
    ping_deviation = round(number=ping_ms - mean_ping_ms, ndigits=1)

    return rows, download_mbps, upload_mbps, ping_ms, server_name, \
        server_location, isp, download_deviation, upload_deviation, \
        ping_deviation, timestamp


# Streamlit dashboard
def streamlit_webpage():
    rows, download_mbps, upload_mbps, ping_ms, server_name, server_location, \
        isp, download_deviation, upload_deviation, ping_deviation, timestamp \
              = get_data()
    st.set_page_config(layout="wide")
    st.title("🌍 Internet Speed Monitor")
    st.text("Track your internet performance over time")
    st.header("Latest Speed Test")

    col_download, col_upload, col_ping, col_runs, = st.columns(4)

    with col_download:
        st.text("⬇️ Download Speed")
        st.header(f"{download_mbps} Mbps")
        if download_deviation < 0:
            st.write(f" :red[↓ {download_deviation} vs avg]")
        else:
            st.write(f":green[↑ {download_deviation} vs avg]")

    with col_upload:
        st.text("⬆️ Upload Speed")
        st.header(f"{upload_mbps} Mbps")   
        if upload_deviation < 0:
            st.write(f" :red[↓ {upload_deviation} vs avg]")
        else:
            st.write(f":green[↑ {upload_deviation} vs avg]") 

    with col_ping:
        st.text("📊 Ping")
        st.header(f"{ping_ms} ms")
        if ping_deviation > 0:
            st.write(f" :red[↑ {ping_deviation} vs avg]")
        else:
            st.write(f":green[↓ {ping_deviation} vs avg]") 

    with col_runs:
        st.text("🏃‍♂️‍➡️ Test Runs")
        st.header(rows)

    st.write(f":gray[ISP: {isp}]")
    st.write(f":gray[Server: {server_name} ({server_location})]")
    st.write(f":gray[Last test: {timestamp}]")


streamlit_webpage()