# 国才笔译·备考台（PWA 壳）

把 `https://4m25wqkpa1s63.aiforce.cloud/app/app_17e5urnjjs3/` 工作台包装成移动端 PWA 应用，与「华为ICT备考工作台」同款形式：手机浏览器访问后「添加到主屏幕」，即可像原生 App 一样全屏打开。

## 结构

```
├── index.html              # 壳页面：全屏 iframe 嵌入目标工作台 + 加载层 + 离线提示
├── manifest.webmanifest    # PWA 清单（standalone / 图标 / 主题色）
├── sw.js                   # Service Worker（壳资源预缓存 + 网络优先）
├── icons/                  # PWA 图标（192/512/maskable/apple-touch-icon/favicon）
├── make_icons.py           # 图标生成脚本（Pillow）
└── .github/workflows/deploy.yml  # GitHub Pages 自动部署
```

## 部署

- 仓库：`haha666-star/guocai-prep-app`（main 分支）
- 线上地址：`https://haha666-star.github.io/guocai-prep-app/`
- push 后 Actions 自动部署到 Pages，约 1–2 分钟。

## 手机使用

1. 手机浏览器打开线上地址
2. Android Chrome / 微信内置浏览器：菜单 → 「添加到主屏幕」
3. iOS Safari：分享 → 「添加到主屏幕」
4. 主屏幕出现「国才笔译」图标，点击全屏打开工作台

## 验证清单

- [ ] GitHub Actions 绿色对勾
- [ ] 站点可访问，iframe 正常加载工作台
- [ ] manifest 与图标返回 200
- [ ] 手机「添加到主屏幕」出现应用图标
