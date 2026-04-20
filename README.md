# Telecom Churn Analytics Pipeline

##  Project Overview

This project implements a complete pipeline using Docker.
The pipeline processes telecom customer data to generate insights through ingestion, preprocessing, clustering, analytics, and visualization.

---

##  Docker Build & Run Commands

### Option A — Build Locally

**1. Build Docker Image**
```bash
docker build -t telecom_analysis .
```

**2. Run Container**
```bash
docker run -it --name my_container telecom_analysis
```

### Option B — Pull from Docker Hub

**1. Pull Image**
```bash
docker pull yomna124/telecom_analysis:latest
```

**2. Run Container**
```bash
docker run -it --name my_container yomna124/telecom_analysis:latest
```

🔗 Docker Hub Link: https://hub.docker.com/r/yomna124/telecom_analysis

🔗 GitHub Repository: https://github.com/yomna124/Customer_Analytics

---

### 3. Run the Pipeline (inside the container)

Only one command is needed — each script automatically calls the next:
```bash
python ingest.py telco_customer_churn.csv
```

### 4. Run Summary Script (inside the container)

```bash
bash summary.sh
```

### 5. Exit the container

```bash
exit
```

---

##  Execution Flow

1. **Data Ingestion (`ingest.py`)**

   * Accepts a dataset file path as a **command-line argument** (sys.argv[1]).
   * In this project, the dataset is first downloaded from Hugging Face.
   * `ingest.py` then loads the dataset from the given path and saves a copy as `data_raw.csv` for further processing.

2. **Preprocessing (`preprocess.py`)**
   
   * Handles missing values and duplicates
   * Encodes and scales features
   * Properly handles CustomerID as an identifier (excluded from encoding).
     
   * Implements **Tenure Binning**:
     * Newcomer
     * Standard
     * Loyal

3. **Analytics (`analytics.py`)**

   * Generates three textual insights from the preprocessed data:
     * Average Monthly Charge
     * Average Tenure in Months
     * Average Churn Score

4. **Clustering (`cluster.py`)**

   * Applies **K-Means Clustering**
   * Identifies 3 customer segments:

     * High-Value Customers
     * Budget Customers
     * Newcomers

5. **Visualization (`visualize.py`)**

   * Generates `.png` plots for clusters and PCA

6. **Summary (`summary.sh`)**

   * Copies `.csv`, `.txt`, `.png` to host
   * Stops and removes container
   *  Generated reports include:
      *  Processed CSV files with clusters and PCA results
      *  Text summaries for insights
      *  Visualization images (.png)

---

##  Output Files

Saved in:

```
customer-analytics/results/
```

### Generated Files:

* `data_preprocessed.csv` — cleaned, encoded, scaled, and PCA-reduced dataset
* `data_clustered.csv` — preprocessed data with cluster labels added
* `clusters.txt` — number of samples per K-Means cluster
* `insight1.txt` — average monthly charge
* `insight2.txt` — average tenure in months
* `insight3.txt` — average churn score
* `summary_plot.png` — visualizations (histogram, heatmap, PCA scatter)

##  Sample Outputs

### Terminal Execution

<img width="1486" height="962" alt="image" src="https://github.com/user-attachments/assets/28265eab-d5fe-465a-9730-b5e6ece52d35" />

### CSV Output Example

### CLUSTRING

<img width="1012" height="840" alt="image" src="https://github.com/user-attachments/assets/eaaf88c0-a3d1-40ba-9f7c-1ff6eb31503f" />

### PROCESSING

<img width="1898" height="858" alt="image" src="https://github.com/user-attachments/assets/2d80f820-9428-4824-b3dc-e9142dedde0a" />


### Visualization

<img width="1200" height="800" alt="summary_plot" src="https://github.com/user-attachments/assets/f561a781-6057-4c0e-974e-a86da2262862" />

---

##  Requirements

* Docker installed
* Python 3.11-slim

Libraries used:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* Datasets

---

## 👥 Team Members

* Yomna Medhat Saad
* Rania Ossama Hassan
