from data_loader import load_data
from data_cleaning import clean_dataframe
from eda import quick_eda
from classification import train_classifier
from evaluation import evaluate_classification

df = load_data("/home/sudhir/OneDrive/prof/sw/data-analytics/titanic.csv")
df = clean_dataframe(df)
quick_eda(df)

model, splits = train_classifier(df, target="Survived")
metrics = evaluate_classification(model, splits["X_test"], splits["y_test"])
print(metrics)
