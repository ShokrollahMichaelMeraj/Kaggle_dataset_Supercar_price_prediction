# Kaggle_dataset_Supercar_0to60_time_prediction.


## To do section:

- ✅ set up architecture and file system. (DONE)
- ✅ choose which kaggle dataset we want? (DONE): Final pick "Elite_Sports_Cars_in_Data.csv".
- ✅ Mockup gui: done
- ❌ new exploration -> ....
-
- new features:

    - year (discounter or decay varible because older cars will have reduced horsepower)
    - initial horsepower
    - millage
    - engine size
    - top speed,
    - weight.
    - torque

- need to make a fast api for the react app,
- need to trian and set up model. 
- exploration
0- set up either google workspace 

 



## system architecture:

```
supercar-0to60-prediction/
│
│
│
│
│
│
│

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
python3 -m venv venv # initializes virtual enviornment
source venv/bin/activate # activate virtual envionment 
pip install -r requirements.txt #install requiremnets
deactivate # to deactivate venv (virtual environment)

For windows it is:
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1 # for powershell
venv\Scripts\activate.bat # for command prompt
pip install -r requirements.txt
deactivate

```



### CheckPoints:


## Exploration Notes:
- the dataset is clean. 
- there is a strong inverse relation ship between torque and 0-60
- there is a strong inverse relation ship between Horsepower and 0-60 
- seems to not matter too much, in cell [64] we see the graph.
- top speed has more of a complex relationship and we have to take everything else into acocunt
- weight has a dirct relationship. but  is effect by other factors. 
- engine size have a direct to complex relationship, some big engins give off fast 0-60 some small engines
have higher 0-60.
