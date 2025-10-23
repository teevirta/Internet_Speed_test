# 🌐 Internet Speed Test Dashboard

A Python-based project to **measure**, **store**, and **visualize** your internet speed over time.  
It includes a **command-line speed test collector** and an **interactive Streamlit dashboard** for data visualization.

---

## 📦 Features

✅ Run manual speed tests using the `speedtest` library  
✅ Save results (download, upload, ping, ISP, server) into a CSV file  
✅ Visualize trends over time with an interactive dashboard  
✅ Compare your latest test against averages  
✅ Filter results by time range (24h, 3 days, 1 week, 2 weeks, 1 month, all time)  
✅ Export full test history as CSV  

---

## 🧠 Project Structure

```
📁 Internet-Speed-Test/
│
├── speed_test_collector.py     # Script to perform speed tests and store results
├── speed_test_dashboard.py     # Streamlit dashboard for data visualization
├── speed_test_data.csv         # Data file storing test results
└── README.md                   # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/teevirta/internet-speed-test.git
cd internet-speed-test
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:
```bash
pip install speedtest-cli pandas streamlit plotly
```

---

## 🚀 Usage

### 🧪 Run a speed test
This runs a test and saves the result to `speed_test_data.csv`.

```bash
python speed_test_collector.py
```

Example output:
```
Download: 150.23 Mbps
Upload: 32.15 Mbps
Latency: 18.3 ms
Results saved to speed_test_data.csv
```

---

### 📊 Launch the dashboard

After collecting some data, start the Streamlit dashboard:

```bash
streamlit run speed_test_dashboard.py
```

Open the provided link (usually http://localhost:8501) in your browser to explore:
- Latest test summary  
- Download/Upload trends  
- Ping latency chart  
- Performance statistics (best, worst, average, std)  
- Full test history table with download option  

---

## 📈 Example Visualization

https://teevirta-internet-speed-test-speed-test-dashboard-nicnsa.streamlit.app/
https://teevirta-internet-speed-test-speed-test-dashboard-nicnsa.streamlit.app/


---

## 🧰 Dependencies

- Python 3.8+
- [speedtest-cli](https://pypi.org/project/speedtest-cli/)
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)
- [streamlit](https://streamlit.io/)

---

## 🧾 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

## 👨‍💻 Author

**Teemu Virta**  
💻 [GitHub](https://github.com/teevirta)  
📧 teemu.virta@icloud.com

---

## ⭐ Contribute

Pull requests and issues are welcome!  
If you like this project, please ⭐ it to support development 🙌
