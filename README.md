🧬 Gene Expression Analysis under Oxidative Stress
📌 Overview

This project analyzes gene expression data from RNA-seq experiments to study how normal and tumor pancreatic cells respond to oxidative stress.

The goal is to identify differentially expressed genes, explore biological patterns, and build a simple machine learning model capable of classifying cell types based on gene expression profiles.

🧪 Dataset
Source: GEO DataSets (GSE196284)
Organism: Human
Samples: 4 (2 normal, 2 tumor)
Conditions:
Normal pancreatic cells (HPNE)
Tumor pancreatic cells (PANC1)
With and without oxidative stress (H2O2)
🔬 Methodology
1. Exploratory Data Analysis (EDA)
Data loading and inspection
Quality checks (missing values, duplicates, distribution)
Visualization (histograms, boxplots, correlation heatmaps)
2. Preprocessing
CPM normalization (Counts Per Million)
Log2 transformation
Gene annotation
3. Differential Expression Analysis
Calculation of log2 Fold Change
Statistical testing (p-values)
Identification of significantly regulated genes

📊 Visualizations:

Volcano plot
Heatmap of top genes
4. Biological Insight

An additional analysis explored the effect of oxidative stress within each cell type.

Results suggest that normal cells exhibit stronger transcriptional changes under oxidative stress, while tumor cells show a more moderate response, potentially reflecting altered regulatory mechanisms.

5. Machine Learning

A classification model was built to predict cell type (normal vs tumor) from gene expression data.

Steps:

Feature selection using top differentially expressed genes
Data scaling
Model training using Logistic Regression

⚠️ Note:
Due to the extremely small dataset (4 samples), the model is evaluated on the training data and shows overfitting. This implementation is intended for demonstration purposes only.

🧠 Key Learnings
High-dimensional biological data requires careful feature selection
Small datasets can lead to overfitting in machine learning models
Combining biological knowledge with data science improves interpretation of results
End-to-end workflows require both analysis and structured pipelines
🛠️ Tech Stack
Python
Pandas, NumPy
Seaborn, Matplotlib
Scikit-learn
Jupyter Notebooks
Git & GitHub
🚀 Future Work
Refactor code into a structured pipeline
Deploy model using FastAPI
Containerize with Docker
Deploy to cloud (Render or Railway)
📂 Project Structure
gene-expression-analysis/
│
├── data/
├── notebooks/
├── results/
├── README.md
🔗 Repository

👉 https://github.com/FedericaUntermann/gene-expression-analysis

📬 Contact

If you're interested in this project or would like to collaborate, feel free to connect!