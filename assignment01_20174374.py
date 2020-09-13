# -*- coding: utf-8 -*-
"""Assignment01_20174374.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TDtMLSIIQngzunk1mR2ZMFTI9yd9w71l

# 인공지능과 보안기술
## 과제 01 - 조합
### 20174374 정여민
"""

# Combination - 조합, 가능한 모든 수를 보이게.
# arr : 주어진 리스트
# k : nCr 에서 r. 몇 개를 선택할 것인가?
def Comb(arr, k):
  # 리스트 내의 중복 제거
  arr = trim(arr)
 
  # 리스트 길이만큼 반복 <= nCr에서 n
  for i in range(len(arr)):
      if k == 1:
        yield [arr[i]]
      else : 
        for a in Comb(arr[i+1:], k-1):
          yield [arr[i]] + a

# 리스트 내의 중복을 제거하는 함수
def trim(arr):
  num = []

  for i in arr:
    if i not in num:
      num.append(i)

  return num

# 조합의 결과를 출력하는 함수
# nCr에서 r을 0~n까지 수행
def print_Comb(arr):
  for i in range(len(arr)):
    for a in Comb(arr,i):
      print(a)
  return

# 숫자 받아오기. 각 항목의 구분은 띄어쓰기로 해주세요. ex) 1 1 2 입력 => [1, 1, 2] 저장됨
print("숫자를 입력하시오 : ") 
number = list(map(int, input().split()))
print("현재 리스트 : " , number)

print_Comb(number)