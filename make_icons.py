# -*- coding: utf-8 -*-
"""生成「国才笔译·备考台」PWA 图标：192 / 512 / maskable / apple-touch-icon(180) / favicon.svg"""
import math
from PIL import Image, ImageDraw

OUT = r"C:\Users\34598\Doubao\chats\2026-09-15\new-chat-1\guocai-prep-app\public\icons"
import os
os.makedirs(OUT, exist_ok=True)

# 配色
C_TOP = (16, 42, 87)      # 深蓝
C_BOT = (23, 120, 168)    # 青蓝
C_GOLD = (255, 200, 87)   # 金色钢笔
C_PAPER = (250, 252, 255) # 纸白

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def draw_icon(size, content_scale=1.0, rounded_bg=True):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # 渐变背景（垂直）
    for y in range(size):
        t = y / (size - 1)
        d.line([(0, y), (size, y)], fill=lerp(C_TOP, C_BOT, t))

    # 可选圆角遮罩（PWA 背景本身系统裁切，这里保留整幅渐变 + 轻微径向高光）
    # 顶部径向高光
    hl = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hl)
    hd.ellipse([-size * 0.25, -size * 0.35, size * 1.25, size * 0.35], fill=(255, 255, 255, 36))
    img = Image.alpha_composite(img, hl)
    d = ImageDraw.Draw(img)  # 重新绑定到合成后的图像

    # 内容画布居中缩放
    cx = cy = size / 2
    s = size * 0.62 * content_scale  # 内容整体宽度基准

    # ---- 书本（两页）----
    book_w = s * 0.92
    book_h = s * 0.78
    page_half = book_w / 2 - book_w * 0.10  # 单页宽度（含间隙）
    top = cy - book_h / 2
    bottom = cy + book_h / 2
    gap = book_w * 0.055
    # 左页
    d.polygon([
        (cx - gap / 2 - page_half, top),
        (cx - gap / 2, top + book_h * 0.04),
        (cx - gap / 2, bottom),
        (cx - gap / 2 - page_half, bottom - book_h * 0.02),
    ], fill=C_PAPER)
    # 右页
    d.polygon([
        (cx + gap / 2, top + book_h * 0.04),
        (cx + gap / 2 + page_half, top),
        (cx + gap / 2 + page_half, bottom - book_h * 0.02),
        (cx + gap / 2, bottom),
    ], fill=(228, 236, 248))
    # 书页中缝线
    d.line([(cx, top + book_h * 0.05), (cx, bottom)], fill=(180, 198, 222), width=max(1, int(size * 0.008)))
    # 左页文字线
    lx0 = cx - gap / 2 - page_half
    for i in range(4):
        yy = top + book_h * (0.24 + i * 0.16)
        d.line([(lx0 + book_w * 0.10, yy), (cx - gap / 2 - book_w * 0.10, yy)],
               fill=(170, 190, 215), width=max(1, int(size * 0.007)))
    # 右页文字线（短一点）
    rx1 = cx + gap / 2 + page_half
    for i in range(4):
        yy = top + book_h * (0.24 + i * 0.16)
        d.line([(cx + gap / 2 + book_w * 0.10, yy), (rx1 - book_w * 0.10, yy)],
               fill=(170, 190, 215), width=max(1, int(size * 0.007)))

    # ---- 金色钢笔斜放（左下 → 右上）----
    pen_len = s * 1.18
    ang = math.radians(48)
    dx, dy = math.cos(ang), -math.sin(ang)
    px0, py0 = cx - s * 0.78, cy + s * 0.52   # 笔尾
    px1, py1 = cx + s * 0.55, cy - s * 0.45   # 笔尖
    pen_w = s * 0.11
    # 笔身（粗矩形沿方向）
    nx, ny = -dy, dx
    p1 = (px0 + nx * pen_w / 2, py0 + ny * pen_w / 2)
    p2 = (px0 - nx * pen_w / 2, py0 - ny * pen_w / 2)
    p3 = (px1 - nx * pen_w / 2, py1 - ny * pen_w / 2)
    p4 = (px1 + nx * pen_w / 2, py1 + ny * pen_w / 2)
    d.polygon([p1, p2, p3, p4], fill=C_GOLD)
    # 笔尖（三角）
    tip = s * 0.16
    t1 = (px1 + nx * pen_w * 0.32, py1 + ny * pen_w * 0.32)
    t2 = (px1 - nx * pen_w * 0.32, py1 - ny * pen_w * 0.32)
    t3 = (px1 + dx * tip, py1 + dy * tip)
    d.polygon([t1, t2, t3], fill=(255, 226, 145))
    # 笔尾圆点
    r = pen_w * 0.55
    d.ellipse([px0 - r, py0 - r, px0 + r, py0 + r], fill=(255, 226, 145))

    return img

for size, name in [(512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png")]:
    draw_icon(size).save(os.path.join(OUT, name))
    print("saved", name)

# maskable：内容缩小到安全区（约 66%）
draw_icon(512, content_scale=0.72).save(os.path.join(OUT, "icon-maskable-512.png"))
print("saved icon-maskable-512.png")

# favicon.svg（简单 SVG 同款图形）
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#102A57"/><stop offset="1" stop-color="#1778A8"/>
</linearGradient></defs>
<rect width="64" height="64" fill="url(#g)"/>
<g transform="translate(32 34)">
<polygon points="-16,-9 -2,-7 -2,11 -16,10" fill="#FAFCFF"/>
<polygon points="2,-7 16,-9 16,10 2,11" fill="#E4ECF8"/>
<rect x="-1" y="-7" width="2" height="18" fill="#B4C6DE"/>
<g stroke="#AABED7" stroke-width="1.2" stroke-linecap="round">
<line x1="-13" y1="-2" x2="-5" y2="-2"/><line x1="-13" y1="1" x2="-5" y2="1"/><line x1="-13" y1="4" x2="-8" y2="4"/>
<line x1="5" y1="-2" x2="13" y2="-2"/><line x1="5" y1="1" x2="13" y2="1"/><line x1="5" y1="4" x2="10" y2="4"/>
</g>
<polygon points="-14,6 -1,5 -1,11 -14,10" fill="#B4C6DE" opacity="0"/>
</g>
<g transform="rotate(48 32 30)" stroke="#FFC857" stroke-width="3.2" stroke-linecap="round">
<line x1="20" y1="46" x2="44" y2="16"/>
<path d="M44 16 l7 2 -4 -7 z" fill="#FFE291" stroke="none"/>
<circle cx="20" cy="46" r="3.2" fill="#FFE291" stroke="none"/>
</g>
</svg>'''
with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(svg)
print("saved favicon.svg")
print("DONE")
