# URL Phishing Detection System

## Problem Statement
Phishing attacks are one of the most common cyber threats where attackers create fake websites to steal sensitive information. This project builds a machine learning system to automatically detect phishing URLs by analyzing their characteristics.

## Dataset
The system uses a labeled dataset of URLs containing:
- **Legitimate URLs**: Real websites from trusted sources
- **Phishing URLs**: Known malicious URLs from phishing databases

Sample dataset is included in `dataset/urls.csv`

## Features Extracted
The system extracts the following features from each URL:

1. **URL Length**: Total number of characters
2. **Number of Dots**: Count of '.' in URL
3. **Has @ Symbol**: Presence of '@' (often used in phishing)
4. **Has Dash**: Presence of '-' in domain
5. **Has Double Slash**: '//' in path (suspicious redirects)
6. **Uses HTTPS**: Whether URL uses secure protocol
7. **Number of Subdomains**: Count of subdomains
8. **Suspicious Keywords**: Presence of words like 'secure', 'account', 'login'
9. **Has IP Address**: Whether URL uses IP instead of domain
10. **Digit Ratio**: Proportion of digits in URL

## Machine Learning Approach

### Models Used:
1. **Logistic Regression**: Simple, interpretable baseline model
2. **Random Forest**: Ensemble method for better accuracy
3. **Support Vector Machine (SVM)**: Non-linear classification

### Pipeline:
1. Data Loading → 2. Feature Extraction → 3. Train-Test Split → 4. Model Training → 5. Evaluation → 6. Prediction

## Project Structure
```
phishing-detection/
│
├── dataset/
│   └── urls.csv              # Sample dataset
│
├── feature_extraction.py      # Feature engineering functions
├── train_model.py            # Model training script
├── predict.py                # Prediction script
├── models/                   # Saved trained models
└── README.md                 # This file
```

## Installation

### Prerequisites:
```bash
pip install pandas numpy scikit-learn
```

## How to Run

### Step 1: Prepare Dataset
Ensure `dataset/urls.csv` exists with columns: `url,label`
- label: 1 for phishing, 0 for legitimate

### Step 2: Train Models
```bash
python train_model.py
```
This will:
- Extract features from URLs
- Train 3 ML models
- Display accuracy, precision, recall, F1-score
- Save models to `models/` directory

### Step 3: Make Predictions
```bash
python predict.py
```
Enter a URL to check if it's phishing or legitimate.

## Results
Expected performance on test set:
- **Logistic Regression**: ~85-90% accuracy
- **Random Forest**: ~90-95% accuracy
- **SVM**: ~88-93% accuracy

## Key Learnings
- Feature engineering is crucial for ML success
- Ensemble methods (Random Forest) often outperform single models
- URL patterns are strong indicators of phishing attempts

## Future Improvements
- Add more features (domain age, SSL certificate info)
- Try deep learning models
- Build web interface for real-time detection
- Integrate with browser extension

## References
- Phishing Database: PhishTank, OpenPhish
- Scikit-learn Documentation
- Feature Engineering for Cybersecurity
