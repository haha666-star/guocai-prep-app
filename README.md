# 国才笔译·备考台（PWA 应用本体）

把「国才笔译·备考台」工作台作为独立 PWA 应用部署到 GitHub Pages，与「华为ICT备考工作台」同款形式：手机浏览器访问后「添加到主屏幕」，即可像原生 App 一样全屏使用。**不再依赖 aiforce 运行时**，因此界面无「豆包工作生成」水印。

## 结构

```
├── index.html      # 应用本体（单文件：数据/题库/刷题/模考/错题本等全部逻辑）
├── manifest.json   # PWA 清单（standalone / 图标 / 主题色）
├── sw.js           # Service Worker（网络优先 + 运行时缓存，v2）
├── icon-192.png    # PWA 图标 192
├── icon-512.png    # PWA 图标 512
└── .github/workflows/deploy.yml  # GitHub Pages 自动部署
```

## 部署

- 仓库：`haha666-star/guocai-prep-app`（main 分支）
- 线上地址：`https://haha666-star.github.io/guocai-prep-app/`
- push 后 Actions 自动部署到 Pages，约 1–2 分钟。

## v2.1 变更（2026-09-17）

1. **刷题回顾**：每组题目刷完后，结果页下方新增「本次作答回顾」，逐题展示题干、四个选项（正确答案绿色、错选红色）、你的作答结果与解析，方便纠错。
2. **去除 aiforce 运行时**：应用本体直接部署，右下角「豆包工作生成」水印与下载菜单不再出现。

## 手机使用

1. 手机浏览器打开线上地址
2. Android Chrome：菜单 → 「添加到主屏幕」
3. iOS Safari：分享 → 「添加到主屏幕」
4. 若此前安装过旧版（iframe 壳），需先在浏览器设置中清除该站点缓存再重新打开。

## 验证清单

- [ ] GitHub Actions 绿色对勾
- [ ] 站点可访问，无「豆包工作生成」水印
- [ ] 刷题完成后出现「本次作答回顾」列表
- [ ] manifest 与图标返回 200
- [ ] 手机「添加到主屏幕」出现应用图标
