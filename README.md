
# 🔐 AI-Based URL Phishing Detection System

**Machine Learning | Cybersecurity | Python | URL Analysis**

## 📌 Project Overview

This project implements a Machine Learning-based system to detect phishing and malicious URLs by analyzing their structural and lexical characteristics.

The system extracts relevant URL-based features and uses Machine Learning classification algorithms to distinguish between phishing and legitimate URLs.

## 🎯 Problem Statement

Phishing attacks are one of the most common cybersecurity threats, where attackers create fraudulent URLs and websites to trick users into revealing sensitive information.

This project aims to develop an automated phishing detection system that analyzes URL characteristics and classifies suspicious links using Machine Learning techniques.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Algorithms:** Logistic Regression, Random Forest, Support Vector Machine (SVM)
- **Development Environment:** Jupyter Notebook

## 📊 Dataset

The project uses a labeled URL dataset containing two categories:

- **Legitimate URLs:** URLs associated with genuine websites.
- **Phishing URLs:** URLs identified as potentially malicious.

### Classification Labels

- `1` – Phishing
- `0` – Legitimate

**Dataset File:** `dataset/urls.csv`

## 🔍 Feature Extraction

The system analyzes URL characteristics to identify suspicious patterns.

The following features are extracted:

| No. | Feature | Description |
|---|---|---|
| 1 | URL Length | Total number of characters in the URL |
| 2 | Number of Dots | Counts dots present in the URL |
| 3 | @ Symbol | Checks for the presence of @ |
| 4 | Dash | Identifies hyphens in the domain |
| 5 | Double Slash | Checks for double-slash patterns |
| 6 | HTTPS | Identifies whether the URL uses HTTPS |
| 7 | Subdomains | Counts the number of subdomains |
| 8 | Suspicious Keywords | Detects keywords such as login, secure and account |
| 9 | IP Address | Checks whether an IP address is used instead of a domain |
| 10 | Digit Ratio | Calculates the proportion of numerical characters |

## 🤖 Machine Learning Algorithms

### 1. Logistic Regression

- Used as a baseline classification algorithm.
- Predicts phishing and legitimate URLs using extracted features.

### 2. Random Forest

- Uses an ensemble of decision trees.
- Helps identify complex relationships between URL features.

### 3. Support Vector Machine (SVM)

- Performs classification by identifying decision boundaries between URL categories.

## ⚙️ Project Workflow

1. Dataset Collection
2. Data Preprocessing
3. URL Feature Extraction
4. Feature Preparation
5. Train-Test Splitting
6. Machine Learning Model Training
7. Model Evaluation
8. URL Classification

## 📁 Project Structure

```text
url-phishing-detection-ml/
│
├── dataset/
│   └── urls.csv
│
├── models/
│   └── trained models
│
├── feature_extraction.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
```

## 💻 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Unnati-coder25/url-phishing-detection-ml.git
```

### Step 2: Navigate to the Project Directory

```bash
cd url-phishing-detection-ml
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

### Step 1: Prepare the Dataset

Ensure the dataset is available in the appropriate directory with the required URL and label columns.

### Step 2: Train the Machine Learning Models

```bash
python train_model.py
```

This step performs data preprocessing, feature extraction, model training and evaluation.

### Step 3: Make Predictions

```bash
python predict.py
```

Enter a URL to check whether it is classified as phishing or legitimate.

## 📈 Model Evaluation

The models are evaluated using standard classification metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Evaluation graphs and classification reports can be included in the `results/` directory.

## 🔮 Future Enhancements

- Integration with real-time phishing URL detection.
- Improved URL and domain-based feature extraction.
- Development of a Flask-based web application.
- Integration with external threat intelligence sources.
- Exploration of advanced Machine Learning and Deep Learning techniques.
- Browser extension for suspicious URL detection.

## 📚 References

- [PhishTank](https://phishtank.org/)
- [OpenPhish](https://openphish.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

## 👩‍💻 Author

**Unnati Pandit**



- [GitHub Profile](https://github.com/Unnati-coder25)

---

*Exploring the intersection of Artificial Intelligence, Machine Learning and Cybersecurity.*
