# Kaggle_dataset_Supercar_price_prediction.


## To do section:

- set up architecture and file system. 
- choose direction:
-   do we want an interactive app? pros and cons
-   do we want to just keep it a notebook? pros and cons
- choose which kaggle dataset we want, 




## system architecture:

```
supercar-price-prediction/
│
├── data/
│   ├── raw/                # Original Kaggle CSVs (never modify these)
│   ├── processed/          # Cleaned data ready for training
│   └── external/           # Optional: other datasets merged in
│
├── notebooks/
│   ├── 01_exploration.ipynb        # EDA (exploratory data analysis)
│   ├── 02_preprocessing.ipynb      # Data cleaning & feature engineering
│   ├── 03_training.ipynb           # Model training experiments
│   └── 04_evaluation.ipynb         # Model evaluation & visualizations
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py       # Functions to clean and prepare data
│   ├── feature_engineering.py      # Add custom derived features
│   ├── model_training.py           # Code to train & evaluate model
│   ├── model_utils.py              # Save/load model functions
│   └── visualization.py            # Plotting helpers
│
├── models/
│   └── supercar_price_model.pkl    # Saved trained model
│
├── app/
│   └── app.py                      # Streamlit or Flask app (UI)
│
├── reports/
│   ├── figures/                    # Graphs and plots
│   └── model_summary.txt           # Performance summary
│
├── requirements.txt                # List of dependencies
├── README.md                       # Project description
└── main.py                         # Entry point if you want to run 


```


"""
Explanation of Each Folder
    Folder	Purpose
    data/	Holds all datasets — separate raw vs processed to avoid overwriting originals.
    notebooks/	Step-by-step experimentation and documentation (good for your report).
    src/	Reusable code modules so you don’t repeat logic in notebooks.
    models/	Where you save trained .pkl or .joblib model files.
    app/	Optional frontend (Streamlit or Flask).
    reports/	Graphs, figures, and summaries for your presentation.
    requirements.txt	Keeps track of packages to install.
    main.py	One-click script to train or run the model (optional for automation).
"""




# virtual environment set up

### what i did for initial set up
```
python3 -m venv venv    # set up virtual environment

source venv/bin/activate # activate

pip3 install pandas numpy scikit-learn matplotlib seaborn xgboost streamlit joblib  # install dependencies 

pip3 freeze > requirements.txt # save packages what you just installed into into requirement.txt

deactivate # to deactivate venv (virtual environment)

```

### what you need to do

```
python3 -m venv venv # initialize virtual enviornment
source venv/bin/activate # activate virtual envionment 
pip install -r requirements.txt #install requiremnets
deactivate # to deactivate venv (virtual environment)


```

