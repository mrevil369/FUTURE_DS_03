# 🎓 College Event Feedback Analysis

This project analyzes feedback collected from participants in college events, helping organizers understand what worked well and what can be improved. It processes feedback data using sentiment analysis, generates visual summaries like word clouds and charts, and provides actionable insights.

---

## 🔍 Overview

The **College Event Feedback Analysis** tool allows you to:

* Clean and process raw feedback data (CSV/Excel)
* Perform sentiment analysis (positive, negative, neutral)
* Generate word clouds from comments
* Create visualizations (bar graphs, pie charts)
* Summarize results in a report

---

## 🧰 Built With

* **Python 3.x**
* `pandas` – for data manipulation
* `matplotlib` / `seaborn` – for data visualization
* `nltk` or `TextBlob` – for natural language processing and sentiment analysis
* `wordcloud` – to create word clouds
* `openpyxl` – for Excel file support

---

## 📁 Example Use Cases

* End-of-semester event surveys
* Guest lectures, workshops, and hackathon feedback
* Club event and festival analysis
* Anonymous suggestion collection

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed. Then install the required libraries:

```bash
pip install pandas matplotlib seaborn nltk wordcloud openpyxl textblob
```

You may also need to download NLTK data (if using NLTK):

```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
```

---

### Step 1: Prepare Your Feedback Data

Your data should be in a CSV or Excel file with at least one column containing text feedback (e.g., “Comments”).

**Sample Format:**

| Name  | Event Name    | Comments                              |
| ----- | ------------- | ------------------------------------- |
| Aditi | Career Fair   | It was informative and well-organized |
| Ravi  | Tech Workshop | Too long, and hard to follow          |

---

### Step 2: Run the Analysis

```bash
python College Event Feedback Analysis.py
```

You will be prompted to provide:

* The path to the feedback file
* The name of the column containing textual feedback

---

## 📊 Outputs

After processing, the script will generate:

* **Sentiment Summary**: % Positive / Neutral / Negative
* **Word Cloud Image**: `wordcloud.png`
* **Sentiment Chart**: Bar or pie chart (`sentiment_chart.png`)
* **Keyword Frequency**: Table or CSV export (optional)
* **Summary Report**: Console or file-based (optional)

---

## 📌 Project Structure

```
College-Event-Feedback-Analysis/
├── College Event Feedback Analysis.py
├── sample_feedback.csv
├── wordcloud.png
├── sentiment_chart.png
├── README.md
└── requirements.txt
```

---

## ✨ Future Enhancements

* Add interactive dashboard (using Streamlit or Dash)
* Real-time feedback submission and analysis
* Support for multilingual feedback
* Integration with Google Forms or Microsoft Forms

---
