# openclaw-summary-ver0.1

一个面向中文用户的 OpenClaw 学习站原型。

## 当前状态
- 已根据 `ROADMAP.md` 与 `PHASE1_CONTENT_MATRIX.md` 开发完整首版多页面静态站点
- 已覆盖首页、Getting Started、Core Concepts、Setup、Use Cases、Advanced、FAQ 七大模块
- 所有 roadmap 页面均已生成独立 URL，可直接本地打开或通过 GitHub Pages 访问

## 本地预览
直接打开 `index.html`，或在仓库目录启动静态文件服务器：

```bash
python3 -m http.server 8000
```

然后访问：`http://localhost:8000`

## 站点规模
- 总页面数：48
- 模块：Home / Getting Started / Concepts / Setup / Use Cases / Advanced / FAQ
- 形式：纯静态多页面站点，便于继续升级到框架化实现
