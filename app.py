import streamlit as st
import random

st.title("🔮 異名診断テスト")

# ジャンル選択
genre = st.radio("まずは診断ジャンルを選んでください：", ["狂気", "ゆるふわ", "現実的", "ファンタジー"])

# 質問セット
questions = {
    "狂気": ["Q1. 夜眠れないとき、あなたは？", "Q2. 世界が崩壊したら？", "Q3. 異質な部分は？"],
    "ゆるふわ": ["Q1. 好きなおやつは？", "Q2. 休日は？", "Q3. 子供のころ好きだった遊びは？"],
    "現実的": ["Q1. 努力とは？", "Q2. 信じるのは？", "Q3. 勝利とは？"],
    "ファンタジー": ["Q1. あなたの魂の色は？", "Q2. 選ばれる力は？", "Q3. 旅の終わりに欲しいものは？"]
}

answers = []
st.subheader("質問に答えてください")
for q in questions[genre]:
    ans = st.radio(q, ["A", "B", "C", "D"], key=q)
    answers.append(ans)

# パーツ
parts = {
    "狂気": {"prefix": ["目を閉じても瞼の裏に走る", "無限回転する"], "middle": ["赤黒い", "歪曲した"], "core": ["骨のオルゴール", "千本足の母"]},
    "ゆるふわ": {"prefix": ["ふわふわの", "虹色の"], "middle": ["もこもこの", "甘やかな"], "core": ["わたあめ姫", "子羊"]},
    "現実的": {"prefix": ["無敗の", "鋼鉄の"], "middle": ["規律ある", "精鋭の"], "core": ["挑戦者", "執行官"]},
    "ファンタジー": {"prefix": ["終焉の", "雷哭の"], "middle": ["影纏う", "千年を超えし"], "core": ["第零魂", "門を通る者"]}
}

# 異名生成
if st.button("あなたの異名を診断！"):
    prefix = random.choice(parts[genre]["prefix"])
    core = random.choice(parts[genre]["core"])
    if random.random() < 0.7:
        name = prefix + core
    else:
        middle = random.choice(parts[genre]["middle"])
        name = prefix + middle + core
    st.success(f"✨ あなたの異名は…『{name}』")
