from itertools import combinations

#calculate_match_score(userA, userB)
def calculate_match_score(userA: dict, userB: dict) -> int:
    score = 0
    
    # ① 기질 일치도 (기질 동일시 +20점)
    if userA["labels"][0] == userB["labels"][0]:
        score += 20

    # ② 에니어그램 궁합 점수
    score += enneagram_compatibility_score(userA["labels"][1], userB["labels"][1])

    # ③ 날개 궁합 점수
    score += wing_bonus(userA["labels"][5], userB["labels"][5])

    # ④ 발달 수준
    if userA["labels"][2] == userB["labels"][2]:
        score += 10  # 동일 발달 수준
    else:
        score += 5   # 상보적 수준

    # ⑤ 본능
    if userA["labels"][3] == userB["labels"][3]:
        score += 5   # 동일 본능
    else:
        score += 10  # 상보 본능

    return score

# 에니어그램 궁합 점수
def enneagram_compatibility_score(typeA: str, typeB: str) -> int:
    typesA = [int(t) for t in typeA.split(",")]
    typesB = [int(t) for t in typeB.split(",")]

    max_score = 0
    for a in typesA:
        for b in typesB:
            s = abs(a + b)
            if a == b:
                max_score = max(max_score, 15)
            elif s == 10:
                max_score = max(max_score, 30)
            elif s == 9 or s == 11:
                max_score = max(max_score, 20)
            else:
                max_score = max(max_score, 10)
    return max_score

# 날개 궁합 점수
def wing_bonus(wingA: str, wingB: str) -> int:
    try:
        a = int(wingA[0])
        b = int(wingB[0])
        if abs(a + b - 10) <= 1:
            return 10
        else:
            return 5
    except:
        return 0

# 모든 유저 쌍 중 최고 매칭 찾기
def find_best_matches(user_profiles: list[dict], top_n: int = 5):
    matches = []
    for u1, u2 in combinations(user_profiles, 2):
        score = calculate_match_score(u1, u2)
        matches.append({
            "pair": (u1["user_id"], u2["user_id"]),
            "score": score
        })
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches[:top_n]