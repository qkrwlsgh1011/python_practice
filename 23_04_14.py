import random
dinner_lst = ["갈매기", "순찌", "매운갈비찜", "삼겹의 난", "닭살부부", "치킨"]
dinner_dict ={"갈매기" : 0, "순찌" : 0, "매운갈비찜": 0, "삼겹의 난": 0, "닭살부부": 0, "치킨": 0}
for _ in range(20):
    tmp = random.choice(dinner_lst)
    if tmp == "갈매기":
        dinner_dict["갈매기"] += 1
    elif tmp == "순찌":
        dinner_dict["순찌"] += 1
    elif tmp == "매운갈비찜":
        dinner_dict["매운갈비찜"] += 1
    elif tmp == "삼겹의 난":
        dinner_dict["삼겹의 난"] += 1
    elif tmp == "닭살부부":
        dinner_dict["닭살부부"] += 1
    elif tmp == "치킨":
        dinner_dict["치킨"] += 1
dinner_dict_sort = sorted(dinner_dict.items(), key = lambda x : -x[1])
print(dinner_dict_sort)