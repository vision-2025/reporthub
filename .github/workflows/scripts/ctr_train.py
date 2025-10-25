import pandas as pd, json, datetime
from sklearn.linear_model import LinearRegression
import joblib, os

DATA = "logs/ctr_history.txt"
MODEL = "models/ctr_model.pkl"

if not os.path.exists(DATA):
    print("[ERROR] No CTR data"); exit()

df = pd.read_csv(DATA, sep=" ", names=["date","ctr"])
X = [[i] for i in range(len(df))]
y = df["ctr"]
model = LinearRegression().fit(X, y)
joblib.dump(model, MODEL)

report = {"updated": datetime.datetime.now().isoformat(), "coef": model.coef_[0], "score": model.score(X, y)}
with open("logs/ctr_train_report.json","w") as f: json.dump(report,f,indent=2)
print("[OK] CTR 모델 재학습 완료")
