import random

# ===== テンプレート定義 =====
templates = {
    "狂気": [
        "{prefix}{answer}{modifier}の{title}",
        "{prefix}{modifier}{answer}を抱く{title}",
        "{prefix}{answer}に囚われし{title}",
        "{answer}{modifier}{title}",   # prefix省略型
        "{prefix}{answer}{title}"      # modifier省略型
    ],
    "ゆるふわ": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{modifier}{answer}と遊ぶ{title}",
        "{prefix}{answer}を愛する{title}",
        "{answer}{modifier}{title}",   # prefix省略型
        "{prefix}{answer}{title}"      # modifier省略型
    ],
    "現実的": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{modifier}{answer}を駆使する{title}",
        "{prefix}{answer}を極めし{title}",
        "{answer}{modifier}{title}",   # prefix省略型
        "{prefix}{answer}{title}"      # modifier省略型
    ],
    "ファンタジー": [
        "{prefix}{answer}{modifier}{title}",
        "{prefix}{modifier}{answer}を宿す{title}",
        "{prefix}{answer}に選ばれし{title}",
        "{answer}{modifier}{title}",   # prefix省略型
        "{prefix}{answer}{title}"      # modifier省略型
    ]
}

# ===== 短縮ルール（7:3の確率で要素を省略） =====
def maybe_skip(value, chance=0.3):
    if random.random() < chance:
        return ""
    return value

# ===== 異名生成関数 =====
def generate_name(genre, answers, modifiers, titles):
    core = random.choice(answers)
    modifier = random.choice(modifiers[genre])
    prefix = maybe_skip(random.choice(["終焉の", "零の", "奈落の", "反響する", "暁の", "永遠の"]))
    title = random.choice(titles[genre])

    template = random.choice(templates[genre])
    result = template.format(prefix=prefix, answer=core, modifier=modifier, title=title)

    # 不要なスペースや「のの」を削除
    result = result.replace("  ", " ").replace("のの", "の")
    return result.strip()
