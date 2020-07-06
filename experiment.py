from methods.svm import SVM
from preparers import ticker_svm
from core.functions import forecast
from core.simulation import simulate_trades_continuous

from loaders.alphavantage import get_ticker_data
from utils.viz import plot_time_series, plot_balance, plot_balance_vs_price

# Step 1: Data Loading
data_df = get_ticker_data('AMZN', interval='daily')
# Step 2: Data Preparation
x_features, y_features = ticker_svm(raw_data=data_df)
ground_truth, start_t = y_features.to_numpy(), 5
# Step 3: Forecasting
predictions = forecast(method=SVM(), data=(x_features, y_features), start_t=start_t, look_back=14)
# Step 4: Simulation
balances = simulate_trades_continuous(predictions=predictions, ground_truth=ground_truth, slowed=False, verbose=False)
# Step 5: Visualization
plot_time_series(ts_1=predictions, ts_label_1='SVM', ts_2=ground_truth, ts_label_2='Close', title='SVM predictions vs. ground truth')
plot_balance(data=balances)
plot_balance_vs_price(balances=balances, price=ground_truth[1:], title='balance vs. price')