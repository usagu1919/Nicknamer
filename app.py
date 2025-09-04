import streamlit as st
import random

# テンプレート候補
templates = [
    "{keyword}を纏う{role}",
    "{keyword}に導かれし{role}",
    "{keyword}を抱く{role}",
    "{keyword}に選ばれし{role}",
    "{keyword}の{role}"
]

roles = {
    "威圧的": ["王", "覇者", "破壊者"],
    "神秘的": ["導きの者", "観測者", "異邦人"],
    "可愛い": ["夢見る者", "小さき勇者", "微笑む者"],
    "狂気的": ["声なき者", "血に濡れし者", "狂笑する者"]
}

st.title("対話式・異名ジェネレーター")

# ステップ1: 雰囲気
mood = st.selectbox("どんな雰囲気を纏いたいですか？", ["威圧的", "神秘的", "可愛い", "狂気的"])

# ステップ2: 役割
role_choice = st.selectbox("役割や立場は？", roles[mood])

# ステップ3: キーワード
keyword = st.text_input("必ず入れたい言葉やイメージは？（例：闇／星／花／鎖）")

# ステップ4: 対象
target = st.selectbox("誰に向けた異名ですか？", ["敵に", "仲間に", "観客に", "自分自身に"])

# 生成ボタン
if st.button("異名を生成"):
    if not keyword:
        st.warning("キーワードを入力してください")
    else:
        template = random.choice(templates)
        epithet = template.format(keyword=keyword, role=role_choice)
        st.success(f"あなたにふさわしい異名は… {epithet}")
