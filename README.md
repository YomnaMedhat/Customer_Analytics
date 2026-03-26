# Telecom Churn Analytics Pipeline

##  Project Overview

This project implements a complete pipeline using Docker.
The pipeline processes telecom customer data to generate insights through ingestion, preprocessing, clustering, analytics, and visualization.

---

##  Docker Build & Run Commands

### 1. Build Docker Image

```bash
docker build -t telecom_analysis .
```

### 2. Run Container

```bash
docker run -it telecom_analysis
```

### 3. Run Pipeline (if not auto-run)

```bash
python ingest.py
python preprocess.py
python cluster.py
python analytics.py
python visualize.py
```

### 4. Run Summary Script

```bash
chmod +x summary.sh
./summary.sh
```

---

##  Execution Flow

1. **Data Ingestion (ingest.py)**

   * Accepts a dataset file path as a **command-line argument** (sys.argv[1]).
   * In this project, the dataset is first downloaded from Hugging Face.
   * `ingest.py` then loads the dataset from the given path and saves a copy as `data_raw.csv` for further processing.

2. **Preprocessing (preprocess.py)**
   
   * Handles missing values and duplicates
   * Encodes and scales features
   * Properly handles CustomerID as an identifier (excluded from encoding).
     
   * Implements **Tenure Binning**:
     * Newcomer
     * Standard
     * Loyal

3. **Manual PCA (analytics.py)**

   * Reduces **37 features --> 2 principal components** for dimensionality reduction and visualization.

4. **Clustering (cluster.py)**

   * Applies **K-Means Clustering**
   * Identifies 3 customer segments:

     * High-Value Customers
     * Budget Customers
     * Newcomers

5. **Visualization (`visualize.py`)**

   * Generates `.png` plots for clusters and PCA

6. **Summary (summary.sh)**

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

* clusters.csv
* pca_components.csv
* tenure_binned.csv
* summary.txt
* Visualization images (.png)

---

##  Sample Outputs

### Terminal Execution

<img width="1486" height="962" alt="image" src="https://github.com/user-attachments/assets/28265eab-d5fe-465a-9730-b5e6ece52d35" />

### CSV Output Example

# CLUSTRING

<img width="1012" height="840" alt="image" src="https://github.com/user-attachments/assets/eaaf88c0-a3d1-40ba-9f7c-1ff6eb31503f" />

# PROCESSING

<img width="1898" height="858" alt="image" src="https://github.com/user-attachments/assets/2d80f820-9428-4824-b3dc-e9142dedde0a" />


### Visualization

<img width="1050" height="701" alt="image" src="https://github.com/user-attachments/assets/899386f6-1ea7-4f36-b7ce-8d3f1c5c4f33" />

---

##  Requirements

* Docker installed
* Python 3.11-slim (inside container)

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
