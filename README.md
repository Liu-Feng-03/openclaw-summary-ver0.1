# openclaw-summary-ver0.1 / v0.2 rebuild in progress

一个面向中文用户的 OpenClaw 学习站项目。

## 当前状态
- v0.1：静态多页面 HTML 版本已完成并上线
- v0.2：已开始 Astro 架构重建
- 当前重点：先重建产品体验系统，再继续迁移剩余页面

## 这次已经落下的 v0.2 架构
- Astro 静态项目骨架
- 共享 layout / nav / breadcrumb / metadata 系统
- 可展开 topic card / accordion 模式
- 首页：改为 routing / confidence-building 页面
- 模块页：改为 expandable knowledge hub
- 详情页：改为 self-contained reading page
- 优先模块已接入：Getting Started / Concepts / Setup / FAQ
- 一批代表性详情页已接入共享数据模型

## 关键目录
```text
src/
  components/
  data/
  layouts/
  pages/
  styles/
```

## 本地运行
先安装依赖：

```bash
npm install
```

开发模式：

```bash
npm run dev
```

构建静态站：

```bash
npm run build
```

## 设计/实施文档
- `ROADMAP.md`
- `PHASE1_CONTENT_MATRIX.md`
- `V0.2_REDESIGN_BRIEF.md`
- `DESIGN_TO_BUILD_WORKFLOW.md`
- `V0.2_ISSUE_LIST_AND_PRIORITIES.md`
- `V0.2_WIREFRAMES.md`
- `V0.2_IMPLEMENTATION_BRIEF.md`
- `V0.2_NAVIGATION_SYSTEM.md`
- `V0.2_VISUAL_SYSTEM_REFINEMENT.md`
- `V0.2_COMPONENT_SPEC.md`
- `V0.2_PAGE_COMPLETION_PLAN.md`
- `V0.2_REVIEW_CHECKLIST.md`
- `IMPLEMENTATION_PLAN_V0.2.md`

## 说明
- 仓库里原有 v0.1 静态 HTML 仍保留，方便对照。
- v0.2 不再沿用旧的重复 hero / KPI sidebar 模式。
- 后续迁移应继续围绕共享架构与数据模型推进，而不是回到逐页硬编码。
