## 과제 1
'''
Input
하나 이상의 아이템
--sorted 플래그 인자 (옵션)
Output
아이템이 한 개만 입력된 경우: 아이템 그대로 출력
아이템이 두 개 입력된 경우: 아이템을 and로 연결
아이템이 세 개 이상 입력된 경우: 아이템을 콤마(,)로 연결하되 마지막 아이템은 and로 연결
--sorted 플래그가 주어진 경우: 아이템을 알파벳 순으로 정렬하여 출력
제약
동일한 아이템이 두 개 이상 입력된 경우 중복을 제거하여 한 번만 출력
'''

import argparse

def get_args():

    # 파라미터 값 받아오기
    parser = argparse.ArgumentParser()
    parser.add_argument("item",nargs = "+", help="item value")
    parser.add_argument("--sorted",action="store_true" ,help="ifsorted")
    #print(parser.parse_args())
    return  parser.parse_args()

def main():
    #print("?")
    param = get_args()
    remove_dupli = []
    

    sort_flag = param.sorted

    if sort_flag is True:
        
        result_sorted = sorted(param.item)
        #print("정렬되었다 : ",result_sorted)
    else:
        
        result_sorted = param.item
        #print("정렬 필요없어")
    
    # 중복제거
    for value in result_sorted:
        
        if value not in remove_dupli:
            remove_dupli.append(value)
        
    # 받아온 갯수만큼 진행하고 갯수가 2 이면 and 만
    # 3개 이상이면 , 분이고 마지막엔 and 로 종료
    value_count = len(remove_dupli)

    #print("value_count ",value_count)
    cnt = 1
    for value in remove_dupli:
        #print(cnt)
        if cnt == 1:
            final_value = value
        elif value_count > 1 and cnt != value_count and value_count !=2:
            final_value = final_value +", "+ value
            
        elif cnt == value_count:
            final_value = final_value+ " and "+value
            
        cnt += 1

    print(final_value)

if __name__ == "__main__":
    main()


