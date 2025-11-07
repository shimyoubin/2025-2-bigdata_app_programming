import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'


def get_covid_data_df(file_path):
    kor_df = pd.read_csv(file_path)
    kor_df['date'] = pd.to_datetime(kor_df['date'])
    kor_index_df = kor_df.set_index('date')
    return kor_index_df


kor_data_df = get_covid_data_df('../ch05/data/covid-kor.csv')
hi_data_df = get_covid_data_df('hi_covid_data.csv')

kor_data_index = kor_data_df.index
hi_data_index = hi_data_df.index
data_index = kor_data_index.union(hi_data_index)

##################################################################
# 인구비율 구하기
kor_data_pop = kor_data_df.loc['2021-01-01', 'population']
hi_data_pop = hi_data_df.loc['2021-01-01', 'population']

rate = round(kor_data_pop / hi_data_pop,2)



covid_df = pd.DataFrame(
    {
        '대한민국': kor_data_df['total_cases'],
        '하와이 (인구 보정)': hi_data_df['total_cases'] * rate
    }, index = data_index)

covid_df.plot.line()
plt.show()