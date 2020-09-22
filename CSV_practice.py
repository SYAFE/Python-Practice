# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:47:10 2020

@author: usn00439
"""

# pandas 라이브러리 import
import pandas as pd

# csvdata라는 변수에 csv파일의 데이터 가져오기
csvdata = pd.read_csv('C:\\Users\\usn00439\\Desktop\\勉強用\\VBA\\0715_00001.csv', sep=',', header=8)

# csvdata의 첫행부터 n행까지 표시
print(csvdata.head(3))
print('\n')
# csvdata의 마지막행부터 n행까지 표시
print(csvdata.tail(3))
print('\n')
# csvdata의 데이터 프레임 칼럼 형식 표시
print(csvdata.dtypes)
print('\n')
# csvdata의 데이터 프레임 정보 표시
print(csvdata.info())
print('\n')

# csvdata 데이터의 특정 열 삭제하기
csvdata.drop(csvdata.columns[[4,5,6,7,8]], axis=1, inplace=True)

print(csvdata.head(3))
