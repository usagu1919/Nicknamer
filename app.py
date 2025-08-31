import streamlit as st
import random

st.title("🔮 異名診断テスト")

# ジャンル選択
genre = st.radio("まずは診断ジャンルを選んでください：", ["狂気", "ゆるふわ", "現実的", "ファンタジー"])

# 質問セット（ジャンルごとに変わる）
questions = {
    "狂気": [
        "Q1. 夜眠れないとき、あなたは何を考える？",
        "Q2. 世界が崩壊したらまず探すものは？",
        "Q3. 自分の中で最も異質だと思う部分は？"
    ],
    "ゆるふわ": [
        "Q1. 好きなおやつは？",
        "Q2. 休日はどう過ごす？",
        "Q3. 子供のころ一番好きだった遊びは？"
    ],
    "現実的": [
        "Q1. あなたにとって努力とは？",
        "Q2. 信じるのは数字か感情か？",
        "Q3. 勝利とはどういう状態？"
    ],
    "ファンタジー": [
        "Q1. あなたの魂は何色？",
        "Q2. 選ばれるならどの力？",
        "Q3. 旅の終わりに欲しいものは？"
    ]
}

answers = []
st.subheader("質問に答えてください")
for q in questions[genre]:
    ans = st.radio(q, ["A", "B", "C", "D"], key=q)
    answers.append(ans)

# パーツ
parts = {
    "狂気": {
        "prefix": ["目を閉じても瞼の裏に走る", "無限回転する", "全ての赤ん坊が叫ぶ"],
        "middle": ["赤黒い", "歪曲した", "崩壊する"],
        "core": ["千本足の母", "骨のオルゴール", "無窮の吐息"]
    },
    "ゆるふわ": {
        "prefix": ["ふわふわの", "虹色の", "おやつを守る"],
        "middle": ["もこもこの", "甘やかな"],
        "core": ["子羊", "わたあめ姫", "夢の妖精"]
    },
    "現実的": {
        "prefix": ["無敗の", "鋼鉄の", "孤高の"],
        "middle": ["精鋭の", "規律ある"],
        "core": ["挑戦者", "執行官", "剣士"]
    },
    "ファンタジー": {
        "prefix": ["終焉の", "雷哭の", "深淵の"],
        "middle": ["千年を超えし", "影纏う"],
        "core": ["第零魂", "白翼", "門を通る者"]
    }
}

# 名前生成
if st.button("あなたの異名を診断！"):
    prefix = random.choice(parts[genre]["prefix"])
    core = random.choice(parts[genre]["core"])

    if random.random() < 0.7:
        name = prefix + core
    else:
        middle = random.choice(parts[genre]["middle"])
        name = prefix + middle + core

    st.success(f"✨ あなたの異名は…『{name}』")

