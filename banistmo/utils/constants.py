file_location = "../data/default_dataset.csv"

columns_to_categorical = ["SEX", 
                          "EDUCATION", 
                          "MARRIAGE", 
                          "default"]


test_size = 0.20

rename_SEX = {"1": "hombre",
              "2": "mujer"}

rename_EDUCATION = {"0": "otros",
                    "1": "bachiller",
                    "2": "universitario",
                    "3": "secundaria",
                    "4": "otros",
                    "5": "otros",
                    "6": "otros"}

rename_MARRIAGE = {"0": "otros", 
                   "1": "casado",
                   "2": "soltero",
                   "3": "otros"}

rename_default = {"0": "no paga",
                  "1": "paga"}

gbm_param_grid = {'classifier__learning_rate': np.array([0.01,0.001]),
                  'classifier__n_estimators': np.array([100,200,300,400]),
                  'classifier__subsample': np.array([0.7,0.8,0.9]),
                  'classifier__max_depth': np.array([10,11,12,13,14,15,16,17]),
                  'classifier__lambda': np.array([1]),
                  'classifier__gamma': np.array([0])}