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
    "verb": ["する者", "し続ける者", "を求める者", "を司る者"],
    "command": ["に囚われし", "を残す", "に導かれし", "を宿す"]
}

# ===============================
# 命令形 → 抽象名詞化
# ===============================
command_map = {
    "眠レ": "眠りの衝動",
    "還レ": "還りの声",
    "叫ベ": "叫びの囁き"
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
# テンプレート（カテゴリごと）
# ===============================
templates = {
    "noun": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{modifier}{answer}{title}"
    ],
    "verb": [
        "{prefix}{answer}{modifier}",
        "{prefix}{answer}{modifier}{title}"
    ],
    "command": [
        "{prefix}{answer}{modifier}",
        "{prefix}{answer}{modifier}{title}"
    ]
}

# ===============================
# 質問プール
# ===============================
question_pool = {
    "狂気": [
        ("夜にあなたを支配するものは？", ["無限に続く階段", "燃え盛る檻", "虚ろな鏡", "血に濡れた書記"]),
        ("内側から湧き上がる衝動は？", ["壊す", "眠レ", "還レ", "叫ベ"]),
        ("あなたが見た最悪の夢は？", ["虚ろな鏡", "血に濡れた書記", "壊す", "叫ベ"]),
        ("終わりにあなたを導く声は？", ["眠レ", "還レ", "無限に続く階段", "燃え盛る檻"]),
        ("心を閉じ込めるものは？", ["燃え盛る檻", "虚ろな鏡", "血に濡れた書記", "無限に続く階段"]),
        ("抗えぬ衝動を一つ選ぶとしたら？", ["壊す", "眠レ", "叫ベ", "還レ"]),
    ],
    "ゆるふわ": [
        ("休日に過ごしたい場所は？", ["ひなたぼっこの縁側", "雲のベッド", "お菓子の夢", "虹をかける子"]),
        ("気分が明るくなる瞬間は？", ["笑う", "歌う", "遊ぶ", "眠る"]),
        ("あなたが守りたい日常は？", ["ひなたぼっこの縁側", "雲のベッド", "お菓子の夢", "虹をかける子"]),
        ("幸せを運んでくるものは？", ["虹をかける子", "お菓子の夢", "笑う", "歌う"]),
        ("誰かに分け与えたい気持ちは？", ["眠る", "遊ぶ", "ひなたぼっこの縁側", "お菓子の夢"]),
        ("心の中に一番近い存在は？", ["雲のベッド", "虹をかける子", "笑う", "遊ぶ"]),
    ],
    "現実的": [
        ("あなたの関心が最も強い分野は？", ["社会", "歴史", "科学", "経済"]),
        ("日常で最もよくする行動は？", ["働く", "学ぶ", "考える", "戦う"]),
        ("人生を支配する要素は？", ["経済", "社会", "科学", "歴史"]),
        ("あなたが誇るものは？", ["考える", "学ぶ", "働く", "戦う"]),
        ("現実の中で戦う相手は？", ["社会", "経済", "科学", "歴史"]),
        ("未来を切り開く力は？", ["学ぶ", "考える", "働く", "戦う"]),
    ],
    "ファンタジー": [
        ("あなたが手に取る武器は？", ["古の剣", "漆黒の翼", "聖なる光", "失われた王国"]),
        ("旅の目的は？", ["救う", "願う", "導く", "探す"]),
        ("あなたの魂を象徴するものは？", ["聖なる光", "漆黒の翼", "古の剣", "失われた王国"]),
        ("世界を覆うものは？", ["闇に抗う者", "失われた王国", "聖なる光", "漆黒の翼"]),
        ("仲間から託された想いは？", ["願う", "導く", "救う", "探す"]),
        ("あなたの行く末を決めるのは？", ["古の剣", "願う", "導く", "漆黒の翼"]),
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

    if category == "noun":
        answer_text = core
        modifier = random.choice(modifier_categories["noun"])

    elif category == "verb":
        base = core.rstrip("る") if core.endswith("る") else core
        answer_text = base
        modifier = random.choice(modifier_categories["verb"])

    elif category == "command":
        answer_text = command_map.get(core, core)
        modifier = random.choice(modifier_categories["command"])

    else:
        answer_text = core
        modifier = ""

    prefix = maybe_skip(random.choice(
        ["終焉の", "零の", "奈落の", "反響する", "暁の", "永遠の"]
    ))

    title = random.choice(titles[genre])
    template = random.choice(templates[category])

    result = template.format(
        prefix=prefix, answer=answer_text, modifier=modifier, title=title
    )
    return result.replace("  ", " ").replace("のの", "の").strip()

# ===============================
# Streamlit UI
# ===============================
st.title("異名診断メーカー")

if "stage" not in st.session_state:
    st.session_state.stage = "genre"
    st.session_state.genre = None
    st.session_state.questions = []
    st.session_state.answers = {}

# --- ジャンル選択 ---
if st.session_state.stage == "genre":
    st.subheader("ジャンルを選んでください")
    genre = st.radio("ジャンル", ["狂気", "ゆるふわ", "現実的", "ファンタジー"])
    if st.button("診断スタート"):
        st.session_state.genre = genre
        # 出題数はランダムで4か5問
        num_q = random.choice([4, 5])
        st.session_state.questions = random.sample(question_pool[genre], num_q)
        st.session_state.stage = "questions"
        st.session_state.answers = {}

# --- 質問パート ---
elif st.session_state.stage == "questions":
    st.subheader(f"ジャンル: {st.session_state.genre}")

    for i, (q, options) in enumerate(st.session_state.questions):
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
