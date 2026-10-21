import pickle
import numpy as np
import pandas as pd


with open('car.pkl', 'rb') as f:
    saved = pickle.load(f)
model = saved['model']
columns = saved['columns']

def ask(text):
    """숫자가 들어올 때까지 다시 물어보는 함수"""
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("숫자만 입력해 주세요.")

while True:
    print("\n=== 자동차 연비 예측 ===")
    cylinders    = ask("실린더 수 (예: 4): ")
    displacement = ask("배기량 (예: 150): ")
    horsepower   = ask("마력 (예: 100): ")
    weight       = ask("무게 (예: 2500): ")
    acceleration = ask("가속력 (예: 15): ")
    model_year   = ask("연식 두 자리 (예: 80): ")

    while True:
        origin = input("출신 (1=미국, 2=유럽, 3=일본): ").strip()
        if origin in ("1", "2", "3"):
            break
        print("1, 2, 3 중에서 입력해 주세요.")

    new = pd.DataFrame([[cylinders, displacement, horsepower, weight,
                         acceleration, model_year,
                         1.0 if origin == "2" else 0.0,
                         1.0 if origin == "3" else 0.0]], columns=columns)

    mpg = float(np.exp(model.predict(new))[0])
    print(f"\n예상 연비: {mpg:.1f} mpg (약 {mpg*0.425:.1f} km/L)")

    again = input("\n다른 차도 해볼까요? (y/n): ").strip().lower()
    if again != "y":
        print("종료합니다.")
        break