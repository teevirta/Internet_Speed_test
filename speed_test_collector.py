import speedtest
import pandas as pd
import os


def speed_test():
    servers = []

    st = speedtest.Speedtest()
    print("Starting speed test...")
    print("This may take 30-60 seconds...")
    st.get_servers(servers)

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    st.download()

    print("Testing upload speed...")
    st.upload()

    results_dict = st.results.dict()

    print()
    timestamp = results_dict['timestamp']
    timestamp_date = results_dict['timestamp'][:10]
    timestamp_time = results_dict['timestamp'][11:19]
    timestamp = f"{timestamp_date} {timestamp_time}"
    print('Timestamp:', timestamp)


    download = round(number=results_dict['download'] / 1000000, ndigits=2)
    print('Download:', download, 'Mbps')
    upload = round(number=results_dict['upload'] / 1000000, ndigits=2)
    print('Upload:', upload, 'Mbps')
    ping = results_dict['ping']
    print('Latency:', ping, 'ms')
    server_name = results_dict['server']['sponsor']
    print('Server name:', server_name)
    server_location = f"{results_dict['server']['name']}, {results_dict['server']['country']}"
    print('Server location:', server_location)
    isp = results_dict['client']['isp']
    print('Isp:', isp)

    return {'timestamp': [timestamp], 'download_mbps': [download], 'upload_mbps': [upload], 
            'ping_ms': [ping], 'server_name': [server_name], 'server_location': [server_location], 
            'isp': [isp]}


def save_to_csv(data):
    df = pd.DataFrame(data)
    print(df)
    if os.path.isfile('speed_test_data.csv'):
        df_csv = pd.read_csv('speed_test_data.csv')
        print(df_csv)
        # df_csv = pd.concat([df_csv, df], ignore_index=True)
        df.to_csv('speed_test_data.csv', mode='a', header=not os.path.isfile('speed_test_data.csv'), index=False)
    else:
        df.to_csv('speed_test_data.csv', mode='w', header=not os.path.isfile('speed_test_data.csv'), index=False)


if __name__ == "__main__":
    print()
    data = speed_test()
    print()
    save_to_csv(data)

    print("Results saved to speed_test_data.csv")
