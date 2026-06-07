from analytics.dataprep.data_loader import load_data
from analytics.dataprep.data_cleaning import clean_dataframe
from analytics.eda import quick_eda

from analytics.neural_network.nn_model import SimpleNN
from analytics.neural_network.nn_train import train_nn
from analytics.neural_network.nn_evaluate import evaluate_nn

# 1. Load
df = load_data("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/housing.csv")

# 2. Clean
df = clean_dataframe(df)

# 3. EDA
quick_eda(df)

# 4. Prepare data
target = "price"
X = df.drop(columns=[target])
y = df[target]

input_dim = X.shape[1]

# 5. Build model
model = SimpleNN(input_dim=input_dim, hidden_dim=64, output_dim=1)

# 6. Train
model = train_nn(model, X, y, epochs=100, lr=0.001)

# 7. Evaluate (using same data for simplicity)
metrics = evaluate_nn(model, X, y)
print(metrics)
