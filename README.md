# DNA-Kmer-Classifier

Dataset Used:
UCI Molecular Biology (Promoter Gene Sequences)

Source:
UCI Machine Learning Repository

Dataset contains 106 DNA promoter/non-promoter sequences.

# Structure Of this Repo. - 
DNA-Kmer-Classifier/

│
├── data/

│   ├── promoters.data

│   └── promoter_sequences_clean.csv

│

├── notebooks/

│   └── 01_dataset_exploration.ipynb

│

├── src/
│   └── kmer_features.py
│
├── models/ (YET TO ADD)
│   ├── random_forest_model.pkl
│   └── kmer_vectorizer.pkl
│
├── results/
│   ├── model_comparison.csv
│   └── kmer_importance.csv
│
├── README.md
└── requirements.txt
