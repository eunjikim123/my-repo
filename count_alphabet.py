#과제2
'''
Input:
임의의 문자열
Top N
Output:
개수 순서대로 Top N개의 알파벳 글자와 개수를 출력
제약:
대소문자를 구별하지 않음
알파벳 이외의 문자는 무시
개수가 동일한 알파벳은 알파벳 순으로 정렬
'''
import argparse
import re
from collections import Counter


def get_args():
    # 파라미터 값 받아오기
    parser = argparse.ArgumentParser()
    parser.add_argument("item", help="alphabet")
    parser.add_argument("slice", help="topN")
    
    #print(parser.parse_args())
    return  parser.parse_args()
 
 
def main():
    param = get_args()
    item = param.item
    top_num = int(param.slice)
    
    # 받은값 전부 소문자로 만들기
    # 그담 영어랑 빈칸 다 지워버리기

    item = item.lower()
    value_clean = re.sub('[^a-zA-Z]','',item).strip()
    
    
    # 알파벳 갯수 가져오기
    count_result = Counter(value_clean)

    #count_result = sorted(count_result.items(), key=lambda x: x[1], reverse=True)
    
    # 가져와서 내림차순 하고 같은 값이면 알파벳 순으로 하귀

    count_result = sorted(count_result.items(), key= lambda x: (-x[1], x[0]))
    #print(count_result)
    count_result = count_result[:top_num]
    
    # 값 뽑아내기~
    for i,j in count_result:
        print(i,j)


  

 
 
if __name__ == "__main__":
    main()