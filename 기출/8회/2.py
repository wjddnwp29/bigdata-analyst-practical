# 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("https://raw.githubusercontent.com/lovedlim/inf/refs/heads/main/p4/8_2/churn_train.csv")
test = pd.read_csv("https://raw.githubusercontent.com/lovedlim/inf/refs/heads/main/p4/8_2/churn_test.csv")

print(train.shape,test.shape)

target = train.pop("TotalCharges")