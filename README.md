# Kaggle_dataset_Supercar_0to60_time_prediction.


## To do section:

- ✅ set up architecture and file system. (DONE)
- ✅ choose which kaggle dataset we want? (DONE): Final pick "Elite_Sports_Cars_in_Data.csv".
- ✅ Mockup gui: done
- ✅ exploration on new dataset (5000 ....)
- ✅ Preprocessing on new dataset (already done)
- ✅ documenattion. 
- 

-
-  Numerical features:

    - year (discounter or decay varible because older cars will have reduced horsepower)
    - initial horsepower
    - weight.
    - torque
    - torque to weight 
    - power to weight 

- Binary features

    - transmission 
        - DCT
        - Automatic
    
    - Drivetrain 
        - AWD
        - RWD


- 


- need to make a fast api for the react app,
- need to trian and set up model. 
- exploration
0- set up either google workspace 

 



## system architecture:

```
supercar-0to60-prediction/



├── Frontend/
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
- engine size have a direct to complex relationship, some big engins give off fast 0-60 some small engines have higher 0-60.


## Proprocessing Notes

## Training Milestones:

- used a 3 hidden layer architecture , 64 -> 64 -> 32 most common in for regression problems, also called funnel pattern




## Training Notes

Exploritory data analysis

- correlation for each feature was checked, we expected 

 - Originally trained on the kaggle dataset, on 'year', 'car age','Horsepower', 'Mileage', 'Engine_Size', 'Weight', 'Torque' and 'top speed'. This gave a very high error (~2.6 seconds)
 - we analyzed all features and dicovered the following:
    - car age and year were reducndant (same infromation different representation) -> only kept year
    - mileage had minimal impact on acceleration.
    - top speed correlated with HP and Weight
    - solution: all features except year were removed. After the clean up, the feature set was reduced to Horsepower, Torque, Weight, Engine_Size and Year. the MAE reduced to ~2.4
 - Observed Oscillation and Hyperparamter Tuning
    
    - (val_loss jumping from 4.8 -> 5.5 -> 4.9 -> 5.3) this menat that the leanring rate must have been too high.
    - solution: we reduced learning rate gradually from      0.001 and landing finally to 0.00005 which almost eliminated the oscillation.
    - experimentation with layer configuration:
        - we experimented with different layers setups,
        - 32 -> 16 -> 1  (caused underfitting)
        - 64 -> 32 -> 1  (MAE : 2.2)
        - 64 -> 32 -> 32  (MAE : 2.0)
        - 128 -> 128 -> 64 -> 1  (caused Overfitting)
        - final choice:  64 -> 32 -> 32  (MAE : 2.0), resulting in sufficienct capacity without overfitting, added dropout for regulerization (meaing it would penlize the model if it started becoming too complex.)
    - experimentation with batch sizes
        - we further experimented with different batch sizes to find improvements.
        - batch size = 32 "too noisy"
        - batch size = 64 "baseline"
        - batch size = 128 "best stability"
- Feature Engineering:

    - through research we observed that ratios have a huge impact on the 0-60 acceleration times in the real world. 
    - result: engineered power to weight and torque to weight ratios
    - 
- Optimzer Experimentation 

    - Tested different optimzers to find possible efficiency
    - Adam :                 MAE = ~2.0s (baseline)
    - SGD :                  MAE = ~2.5s worse than baseline
    - SGD ( momentum= 0.9 ): MAE = ~1.4s (better!)
    - result: finalized the optimizer to SGD momentum= 0.9

- Milestone check: 
    - with all improvements to this point, MAE dropped to ~1.26 big improvement from baseline.

- Addiing Categorical Features:

    - through research we foudn that transmission and drivetrain as well as other features have a big impact on the 0-60 acceleration time.
    - Changes: used one-hot encoding to add:
        - DCT vs Auto transmission (effecting shift speed)
        - AWD vs RWD (effecting traction and launch)
        - added the following features to binary features:
            - Transmission_DCT
            - Transmission_Auto  
            - Drivetrain_AWD
            - Drivetrain_RWD

    - Results:
        - MAE experinced to change stuck at ~1.26 
    - observed issues:
        - scaling on the entire feature set, why is this an issue? one-hot encoded features are either 1 or 0 and should notbe scaled or normalized. 
        - solution: splitting the training set to numerical and binary, scaling numerical and concatinating with the binary fixed observed issue HOWEVER, did not result in any changes to MAE. 


- Milstone and sanity check:
    - at this point we went over the data and did correlation checking to see if we find any issues which would explain the high MAE, 
    - correlation check showed that the features had a very low correlation: 
        -  Horsepower:      -0.0113
        -  Weight:          +0.0040
        -  Power_Weight:    -0.0124
        -  Engine_Size:     +0.0211
    - Issue observed: All correlations were nearing zero. Through manual inspection a discrepancy was observed within the dataset, different brands of cars had scrambled models, ie ferrari with a 911 gt3rs model. This meant that other cells of the table were also scrambled, 
    - Solution:
        - We fixed the dataset with real values from veriufied sources. resulting in our new updated kaggle dataset: "5000_car_dataset_TRANSMISSION_FIXED_FINAL.csv"
    - Result:
        - Training the model again with the updated dataset resulted in strong correlations:
            - Horsepower:       -0.6023
            - Weight:           +0.6614
            - Power_Weight:     -0.7663
            - Torque_Weight:    -0.7513
            - Engine_Size:      -0.0011
            - Transmission_DCT: -0.6011
        - MAE dropped from ~1.26 to 0.28 huge improvement!!
        
    
- Investigating Engine Size low correlation:

    - getting rid of engine size did not chnage MAE.
    - We observed that Enginesize was redundant and the relationship was already being captured by power to weight and torque to weight, same results with or without engine size.(confirmed through research)


- Val-MAE explosions:
    -  val-mae would explode through some runs:
        - 0.36 -> 3.36 -> 19.88 

    - solution: the large gradient caused huge weight update resulting the model to spiral out of control. By introducing gradient clipping through clipnorm 1.0 this issue was resolved. Running the model 10+ times showed no instability or explosion. resulting in consistent MAE: ~0.27-0.30 (current and best results.)

- Testing with random seeds:
    - upto this point t o work with the same split we used seed set at 42 which would allow to see the real change different configuratiosn would give us. 
    - now we experimented with different seeds which did not show any huge changes.
    - 

- saving model:

    - the model was saved using joblid for making predictions later using the trained model and connecting it to the fastapi.










        


    
















- 