import streamlit as st
import random

# ===============================
# 回答カテゴリ仕分け
# ===============================
answer_categories = {
    # 狂気ジャンル
    "無限に続く階段": "noun",
    "燃え盛る檻": "noun",
    "血に濡れた書記": "noun",
    "虚ろな鏡": "noun",
    "壊す": "verb",
    "眠レ": "command",
    "還レ": "command",
    "叫ベ": "command",

    # ゆるふわジャンル
    "ひなたぼっこの縁側": "noun",
    "虹をかける子": "noun",
    "お菓子の夢": "noun",
    "雲のベッド": "noun",
    "笑う": "verb",
    "遊ぶ": "verb",
    "眠る": "verb",
    "歌う": "verb",

    # 現実的ジャンル
    "社会": "noun",
    "歴史": "noun",
    "科学": "noun",
    "経済": "noun",
    "戦う": "verb",
    "働く": "verb",
    "考える": "verb",
    "学ぶ": "verb",

    # ファンタジージャンル
    "古の剣": "noun",
    "失われた王国": "noun",
    "聖なる光": "noun",
    "漆黒の翼": "noun",
    "探す": "verb",
    "導く": "verb",
    "願う": "verb",
    "救う": "verb",
}

# ===============================
# 修飾語カテゴリ
# ===============================
modifier_categories = {
    "noun": ["を操る", "を抱く", "を纏う", "を司る", "を感じる"],
    "verb": ["ことを望む", "を繰り返す", "者", "ことを夢見る"],
    "command": ["に囚われし", "を残す", "に導かれた", "に抗う"]
}

# ===============================
# 異名用タイトル
# ===============================
titles = {
    "狂気": ["門を叩く者", "血に濡れた書記", "声なき王"],
    "ゆるふわ": ["虹をかける子", "森で眠る精霊", "お菓子の使者"],
    "現実的": ["社会を統べる者", "知識の探究者", "現実を歩む者"],
    "ファンタジー": ["選ばれし勇者", "失われし継承者", "闇に抗う者"]
}

# ===============================
# テンプレート（ジャンル×カテゴリ）
# ===============================
templates = {
    "noun": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{modifier}{answer}{title}"
    ],
    "verb": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{answer}{modifier}",
    ],
    "command": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{answer}{modifier}"
    ]
}

# ===============================
# ランダムでプレフィックス省略
# ===============================
def maybe_skip(text, prob=0.3):
    return "" if random.random() < prob else text

# ===============================
# 名前生成
# ===============================
def generate_name(genre, answers):
    core = random.choice(answers)
    category = answer_categories.get(core, "noun")
    modifier = random.choice(modifier_categories[category])

    prefix = maybe_skip(random.choice(
        ["終焉の", "零の", "奈落の", "反響する", "暁の", "永遠の"]
    ))

    title = random.choice(titles[genre])
    template = random.choice(templates[category])

    result = template.format(prefix=prefix, answer=core, modifier=modifier, title=title)
    return result.replace("  ", " ").replace("のの", "の").strip()

# ===============================
# Streamlit UI
# ===============================
st.title("異名診断メーカー")

if "stage" not in st.session_state:
    st.session_state.stage = "genre"
    st.session_state.genre = None
    st.session_state.answers = {}

# --- ジャンル選択 ---
if st.session_state.stage == "genre":
    st.subheader("ジャンルを選んでください")
    genre = st.radio("ジャンル", ["狂気", "ゆるふわ", "現実的", "ファンタジー"])
    if st.button("診断スタート"):
        st.session_state.genre = genre
        st.session_state.stage = "questions"
        st.session_state.answers = {}

# --- 質問パート ---
elif st.session_state.stage == "questions":
    st.subheader(f"ジャンル: {st.session_state.genre}")

    # 仮の質問（将来的にはプールからランダム出題もOK）
    questions = [
        ("あなたを最も表すものは？", ["無限に続く階段", "燃え盛る檻", "血に濡れた書記", "虚ろな鏡", "壊す", "眠レ", "還レ", "叫ベ"]),
    ]

    for i, (q, options) in enumerate(questions):
        answer = st.radio(q, options, key=f"q{i}")
        st.session_state.answers[i] = answer

    if st.button("診断結果を見る"):
        st.session_state.stage = "result"

# --- 結果表示 ---
elif st.session_state.stage == "result":
    genre = st.session_state.genre
    answers = list(st.session_state.answers.values())
    result = generate_name(genre, answers)

    st.success(f"あなたの異名は… {result}")

    if st.button("もう一度診断する"):
        st.session_state.stage = "genre"
