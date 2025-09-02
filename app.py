import streamlit as st
import random

st.title("異名診断メーカー")

# ===== 修飾語リスト =====
modifiers = {
    "狂気": ["を吐き出す", "を刻む", "を呪う", "を孕む", "に取り憑かれた", "を抱く", "を纏う", "を見下ろす"],
    "ゆるふわ": ["を包む", "と踊る", "に寄り添う", "を愛する", "に微笑む", "を散らす", "を香らせる", "と歌う"],
    "現実的": ["を操る", "を極めた", "を統べる", "を駆使する", "を支配する", "を制御する", "を分析する", "を突破する"],
    "ファンタジー": ["を宿す", "を継ぐ", "を纏いし", "を超越せし", "を解き放つ", "を背負う", "に選ばれし", "を召喚する"]
}

# ===== 質問プール =====
questions = {
    "狂気": [
        ("あなたの夢に繰り返し現れるものは？", ["燃え盛る檻", "無限に続く階段", "溶ける時計", "歪んだ鏡"]),
        ("世界の音がすべて一つに溶けたとき、あなたは何を聞いた？", ["血の鼓動", "無音", "囁き声", "金属音"]),
        ("闇に浮かぶ一つの瞳。その色は？", ["深紅", "蒼白", "金色", "真っ黒"]),
        ("禁じられた書物を開いたとき最初に見た言葉は？", ["断絶", "再生", "螺旋", "解体"]),
        ("最期に残す言葉を刻めるとしたら？", ["壊セ", "眠レ", "笑エ", "還レ"]),
        ("あなたの肉体に刻まれている紋様は？", ["裂けた口", "螺旋の印", "千の目", "黒い翼"]),
        ("崩壊する世界であなたが守るものは？", ["誰もいない椅子", "割れた人形", "名前のない墓", "叫ぶ影"])
    ],
    "ゆるふわ": [
        ("あなたが一番落ち着く場所は？", ["ひなたぼっこの縁側", "ふわふわの草原", "絵本の図書館", "虹色のカフェ"]),
        ("あなたを一言で表すと？", ["もふもふ", "ほわほわ", "きらきら", "ゆらゆら"]),
        ("小さな魔法が使えるなら何をする？", ["花を咲かせる", "動物と話す", "空に絵を描く", "お菓子を出す"]),
        ("空から降ってきてほしいものは？", ["花びら", "星屑", "シャボン玉", "綿あめ"]),
        ("あなたの隣にいつもいるものは？", ["小鳥", "ぬいぐるみ", "妖精", "優しい風"]),
        ("好きな音は？", ["鈴の音", "波の音", "風の音", "子守唄"]),
        ("眠りにつく前に見る景色は？", ["満月", "お花畑", "暖炉の火", "雲の上"])
    ],
    "現実的": [
        ("あなたが最も誇れるスキルは？", ["計算力", "記憶力", "分析力", "交渉力"]),
        ("日々を支える最大の道具は？", ["パソコン", "手帳", "ペン", "時計"]),
        ("人生のモットーは？", ["効率", "努力", "挑戦", "安定"]),
        ("最も頼りになるものは？", ["知識", "経験", "人脈", "体力"]),
        ("未来を切り開く鍵は？", ["情報", "金", "信頼", "技術"]),
        ("勝負の瞬間、あなたが頼るものは？", ["論理", "直感", "準備", "運"]),
        ("壁を前にしたときのあなたの選択は？", ["壊す", "回り込む", "登る", "諦めない"])
    ],
    "ファンタジー": [
        ("あなたが生まれたのはどの地？", ["天空の城", "深淵の洞窟", "古代の森", "砂漠の遺跡"]),
        ("あなたに宿る力は？", ["炎", "氷", "雷", "影"]),
        ("契約した存在は？", ["龍", "精霊", "魔王", "古代の神"]),
        ("あなたの武器は？", ["剣", "杖", "弓", "槍"]),
        ("背負っている運命は？", ["滅亡", "再生", "永遠", "選ばれし者"]),
        ("旅の目的は？", ["復讐", "探索", "解放", "守護"]),
        ("あなたの名が語られる場所は？", ["伝説の書", "神殿の壁画", "吟遊詩人の歌", "夢の中"])
    ]
}

# ===== 称号リスト =====
titles = {
    "狂気": ["千本足の母", "門を叩く者", "声なき王", "血に濡れた書記"],
    "ゆるふわ": ["もふもふの守護者", "お昼寝の女王", "お菓子職人の妖精", "虹をかける子"],
    "現実的": ["理論の支配者", "現実の設計者", "計画の番人", "社会を統べる者"],
    "ファンタジー": ["竜を継ぐ者", "永遠の旅人", "天空の使者", "封印を解く者"]
}

# ===== セッション管理 =====
if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "genre" not in st.session_state:
    st.session_state.genre = None
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ===== スタート画面 =====
if st.session_state.stage == "start":
    genre = st.selectbox("ジャンルを選んでください", ["狂気", "ゆるふわ", "現実的", "ファンタジー"])
    if st.button("診断スタート"):
        st.session_state.genre = genre
        st.session_state.selected_questions = random.sample(
            questions[genre], k=random.randint(4, 5)
        )
        st.session_state.stage = "questions"
        st.rerun()

# ===== 質問画面 =====
elif st.session_state.stage == "questions":
    st.write(f"ジャンル: {st.session_state.genre}")
    for idx, (q, options) in enumerate(st.session_state.selected_questions):
        st.session_state.answers[idx] = st.radio(
            q, options, key=f"q{idx}"
        )
    if st.button("診断結果を見る"):
        st.session_state.stage = "result"
        st.rerun()

# ===== 結果画面 =====
elif st.session_state.stage == "result":
    genre = st.session_state.genre
    answers = list(st.session_state.answers.values())
    core = random.choice(answers)
    modifier = random.choice(modifiers[genre])
    prefix = random.choice(["終焉の", "零の", "奈落の", "反響する", "暁の", "永遠の"])
    title = random.choice(titles[genre])

    result = f"**{prefix}{core}{modifier}{title}**"
    st.success(f"あなたの異名は… {result}")

    if st.button("もう一度診断する"):
        st.session_state.stage = "start"
        st.session_state.answers = {}
        st.rerun()
