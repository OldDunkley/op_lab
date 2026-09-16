#imports
import pandas as pd

#calc
def metrics_calculator(score):
    total = 0
    for i in range(0,len(score)):
        total = total + score[i]
    avg = total / (len(score))
    print(avg)

    if avg>95:
        print("Meets Expectations")
    else:
        print("Needs Improvement")

df = pd.read_csv('SELECT_score_FROM_UpworkGTNP.tasky_quality.csv')
scores = df['score']
metrics_calculator(scores)

