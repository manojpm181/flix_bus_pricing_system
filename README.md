# 🚀 Flix Pricing Optimization System

A **production-style data pipeline + analytics dashboard** that detects pricing inefficiencies using clustering and delivers actionable insights through an interactive UI.

---

## 📌 Project Overview

The **Flix Pricing Optimization System** analyzes large-scale pricing data (~800K+ records) to:

* Identify **overpriced and underpriced items**
* Generate **recommended prices**
* Segment data using **clustering (unsupervised ML)**
* Provide **business insights via dashboards and reports**

---

## 🎯 Key Features

### 🔍 Data Processing Pipeline

* Handles large datasets efficiently (800K+ rows)
* Data cleaning and preprocessing
* Feature engineering for pricing insights

### 🧠 Machine Learning

* Clustering-based segmentation (K-Means)
* Price deviation detection
* Intelligent price recommendations

### 📊 Reporting System

* Excel report with:

  * Summary sheet
  * Flagged cases (High / Low pricing)
  * Sample dataset
* Optimized for performance (avoids heavy Excel crashes)

### 🌐 Interactive Dashboard (Streamlit)

* KPI Cards (High / Low / Optimal pricing)
* Pie chart (price distribution)
* Scatter plot (price vs recommended)
* Cluster visualization
* Sidebar filters
* Data preview table

---

## 🏗️ Project Structure

```
flix_pricing_system/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── clustering.py
│   ├── pricing.py
│
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   └── results.xlsx
│   └──sample_data.csv
│   └──summary.csv
│   └──flagged_cases.csv
├── docs/
│   └── automation_plan.md
│
├── main.py
└── requirements.txt 
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/manojpm181/flix_bus_pricing_system.git
cd flix_bus_pricing_system
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Step 1: Run Data Pipeline

```
python main.py
```

✅ Generates:

* `outputs/full_data.csv`
* `outputs/results.xlsx`

---

### 🔹 Step 2: Launch Dashboard

```
streamlit run app/streamlit_app.py
```

🌐 Open in browser:

```
http://localhost:8501
```
https://manojpm181-flix-pricing-system-appstreamlit-app-kanoej.streamlit.app/
---

## 📊 Dashboard Preview

### Features:

* 📌 KPI Metrics (High / Low / Optimal)
* 📊 Price Distribution (Pie Chart)
* 📈 Price vs Recommended Scatter Plot
* 🧠 Cluster Analysis
* 🔍 Dynamic Filters
* 📋 Data Table

---

## 🧠 Technical Stack

| Layer         | Technology            |
| ------------- | --------------------- |
| Language      | Python                |
| Data          | Pandas, NumPy         |
| ML            | Scikit-learn (KMeans) |
| Visualization | Plotly                |
| Dashboard     | Streamlit             |
| Reporting     | OpenPyXL              |

---

## ⚡ Performance Optimizations

* Avoids Excel overload by limiting rows
* Stores full dataset in CSV format
* Uses caching (`@st.cache_data`) for fast UI
* Reduces memory-heavy formatting operations

---

## 🚨 Challenges Solved

### ❌ Large Dataset Handling

✔ Optimized processing for 800K+ rows

### ❌ Excel Memory Crash

✔ Limited export + CSV separation

### ❌ Disk Space Issues

✔ Redirected temp storage & reduced file size

### ❌ Slow UI Rendering

✔ Sampling + caching used

---

## 💡 Business Impact

* Identifies **revenue leakage**
* Improves **pricing strategy**
* Enables **data-driven decisions**
* Scales to real-world datasets

---

## 📈 Future Enhancements

* 🔮 AI-based dynamic pricing (real-time)
* 📡 API integration
* ☁️ Cloud deployment (AWS / GCP)
* 📊 Advanced analytics (forecasting)
* 🔐 Role-based dashboard access

---

## 👨‍💻 Author

**Manoj PM**
B.E. CSE
manojpoojari1511@gmail.com

---
## Results
<img width="615" height="586" alt="image" src="https://github.com/user-attachments/assets/fc292a3d-4d43-4675-ae36-abc5d431f0f1" />
<img width="1915" height="690" alt="Screenshot 2026-03-17 175533" src="https://github.com/user-attachments/assets/99dd05fa-3fdd-4a53-8036-7ba6a5f74060" />
<img width="1497" height="621" alt="Screenshot 2026-03-17 175547" src="https://github.com/user-attachments/assets/ed3cf953-144a-403a-ad60-8dea7ed7c030" />
<img width="1480" height="558" alt="Screenshot 2026-03-17 175603" src="https://github.com/user-attachments/assets/f8341544-06bf-43fb-873f-e26e7dbf4581" />
<img width="1434" height="562" alt="Screenshot 2026-03-17 175619" src="https://github.com/user-attachments/assets/aadc30e1-d34b-4552-b682-d181aaabc7e1" />
<img width="1482" height="583" alt="Screenshot 2026-03-17 175629" src="https://github.com/user-attachments/assets/8f88966e-9ff8-4165-bff6-143570c7142c" />
<img width="1472" height="530" alt="Screenshot 2026-03-17 175635" src="https://github.com/user-attachments/assets/e5c3076f-a86a-4e7e-b47b-07371b7b7da7" />
<img width="1519" height="549" alt="Screenshot 2026-03-17 175642" src="https://github.com/user-attachments/assets/56a3bad7-be18-4f9c-b195-1dac7dafda60" />
<img width="1569" height="812" alt="Screenshot 2026-03-17 175702" src="https://github.com/user-attachments/assets/487b2ea0-d773-432a-9ba8-1bd59fed6640" />


---
## 🏁 Conclusion

This project demonstrates:

* End-to-end data pipeline design
* Machine learning integration
* Scalable data handling
* Interactive data visualization


⭐ If you found this useful, give it a star!



