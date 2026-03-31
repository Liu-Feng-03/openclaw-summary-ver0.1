from pathlib import Path
from typing import Optional

root = Path('/Users/columbina.hyposelenia/.openclaw/workspace/openclaw-summary-ver0.1')
(root / 'assets').mkdir(exist_ok=True)

NAV = [
    ('首页', '/'),
    ('入门', '/getting-started/'),
    ('概念', '/concepts/'),
    ('配置', '/setup/'),
    ('场景', '/use-cases/'),
    ('进阶', '/advanced/'),
    ('FAQ', '/faq/'),
]

PAGES = {}


def add_page(route: str, title: str, eyebrow: str, hero_title: str, hero_desc: str, summary: str,
             sections: list, cta: Optional[list] = None):
    path = route.strip('/')
    file = 'index.html' if not path else f'{path}/index.html'
    PAGES[route] = {
        'file': file,
        'title': title,
        'eyebrow': eyebrow,
        'hero_title': hero_title,
        'hero_desc': hero_desc,
        'summary': summary,
        'sections': sections,
        'cta': cta or [],
    }


def bullets(title, *items):
    return {'title': title, 'type': 'bullets', 'items': list(items)}


def steps(title, *items):
    return {'title': title, 'type': 'steps', 'items': list(items)}


def cards(title, *items):
    return {'title': title, 'type': 'cards', 'items': list(items)}


def notes(title, *items):
    return {'title': title, 'type': 'grid-note', 'items': list(items)}


# Home
add_page('/', 'OpenClaw 中文学习指南', 'OpenClaw Summary', '一套更适合中文用户的 OpenClaw 学习站',
         '从是什么、怎么学、如何部署，到进阶机制、场景应用与疑难排查，直接按路线读就行。',
         '这不是文档镜像，而是一个可分享、可跳读、可循序渐进的中文学习产品。', [
    cards('你可以从这 5 个入口开始',
          ['我是新手，先看什么？', '先建立整体印象，再进入推荐学习路线。', '/getting-started/'],
          ['我想搞懂它的结构', '从 architecture、session、gateway、skills、tools、memory 开始。', '/concepts/'],
          ['我想尽快跑起来', '沿着 setup 路线完成 requirements → install → config → gateway → first message。', '/setup/'],
          ['我想知道能拿它做什么', '直接从 use cases 进入，按目标看场景。', '/use-cases/'],
          ['我已经会一点，想看进阶', '去 advanced 和 FAQ。', '/advanced/']),
    steps('推荐学习路径',
          ['先知道它是什么', '理解它是助理系统，不是单纯聊天框。'],
          ['再建立系统心智模型', '看架构、会话、网关、技能、工具、记忆之间的关系。'],
          ['再完成最小成功', '装好、配好、启动、发出第一条消息。'],
          ['最后再看进阶与排错', '这样不会被术语和日志压垮。']),
    cards('模块入口',
          ['Getting Started', '新手路线与阅读建议。', '/getting-started/'],
          ['Core Concepts', '系统结构、核心概念与关系图。', '/concepts/'],
          ['Setup & Deployment', '环境准备、安装、配置、启动、首条消息。', '/setup/'],
          ['Use Cases', '私人助理、消息平台、GitHub、Google Workspace 等场景。', '/use-cases/'],
          ['Advanced Topics', '会话模型、记忆设计、技能设计、安全边界等。', '/advanced/'],
          ['FAQ', '连接、文件、技能工具、安全与行为问题。', '/faq/']),
    notes('概念图预览',
          ['Gateway', '承接服务、状态与访问入口'],
          ['Session', '定义上下文边界'],
          ['Skills', '说明该怎么做'],
          ['Tools', '说明能做什么'],
          ['Memory', '提供文件化连续性'],
          ['Subagents / ACP', '负责拆分复杂工作与开发工作流']),
    cards('继续深入',
          ['先理解 architecture', '很多问题最后都能回到结构关系。', '/concepts/architecture/'],
          ['去看 setup path', '跑通一次最小闭环最重要。', '/setup/'],
          ['去看 advanced', '理解为什么 session、memory、safety 这么关键。', '/advanced/'],
          ['去看 FAQ', '遇到现象先判断，不要先恐慌。', '/faq/']),
], [('开始学习', '/getting-started/'), ('快速配置', '/setup/')])

# Getting started
add_page('/getting-started/', 'Getting Started', 'Getting Started', '给第一次接触 OpenClaw 的用户一条低摩擦路线',
         '先知道什么该先看，什么可以后看，再开始会轻松很多。',
         '本模块负责建立新手阅读顺序，而不是一口气塞满全部细节。', [
    steps('推荐起步顺序',
          ['先读 what is OpenClaw', '建立最基本认知。'],
          ['再读 concepts', '建立结构理解。'],
          ['然后走 setup', '完成第一次成功。'],
          ['最后进入 use cases / advanced / FAQ', '按目标与问题继续深入。']),
    bullets('新手最需要先知道的事',
            'OpenClaw 更像可编排的助理系统，而不只是聊天界面。',
            '你不需要立刻看懂全部架构，但需要先认识 session、gateway、skills、tools、memory 这些关键词。',
            '第一次成功的目标不是“全懂”，而是“能跑起来、能互动、知道下一步”。'),
    cards('建议优先页面',
          ['什么是 OpenClaw', '最短路径理解它解决什么问题。', '/getting-started/what-is-openclaw/'],
          ['如何学习', '按目标选择阅读路线。', '/getting-started/how-to-learn/'],
          ['首轮路线图', '从零到第一次成功应该怎么走。', '/getting-started/first-roadmap/'])
], [('什么是 OpenClaw', '/getting-started/what-is-openclaw/'), ('如何学习', '/getting-started/how-to-learn/')])

add_page('/getting-started/what-is-openclaw/', '什么是 OpenClaw', 'Getting Started', 'OpenClaw 是一套可接入真实工具与渠道的 AI 助理系统',
         '它不是单纯在网页里和你聊天，而是让代理、会话、技能、工具、记忆与外部入口一起协作。',
         '先把它理解成“有结构、有边界、可操作”的助理平台，会比把它当成普通聊天机器人更接近真实。', [
    bullets('一句话定义', 'OpenClaw 是一个让 AI 代理在真实消息渠道、工具系统和文件记忆上运行的助理框架。'),
    bullets('它解决什么问题',
            '让助理不只会回答，还能读文件、调工具、连接 Telegram / Discord / GitHub 等入口。',
            '把长期协作需要的人格、规则、记忆和执行能力放到可管理的结构里。',
            '让不同任务可以用不同 session、skill、权限和工作流来处理。'),
    cards('它和普通聊天 UI 的区别',
          ['普通聊天 UI', '重点是对话本身，能力边界常常不透明。', None],
          ['OpenClaw', '重点是“对话 + 系统结构 + 工具执行 + 渠道接入 + 持续协作”。', None]),
    cards('下一步建议',
          ['先看 concepts', '建立系统结构直觉。', '/concepts/'],
          ['想直接上手就去 setup', '尽快完成一次可验证的成功。', '/setup/'])
], [('看概念', '/concepts/'), ('去配置', '/setup/')])

add_page('/getting-started/how-to-learn/', '如何学习 OpenClaw', 'Getting Started', '学习 OpenClaw 的关键不是看得多，而是看得有顺序',
         '不同人进入 OpenClaw 的目标不同：有人想先装起来，有人想先懂架构，有人只关心场景价值。',
         '这页帮你按目标选路线，而不是被完整 sitemap 吓退。', [
    cards('按目标选路线',
          ['我只想先装起来', '先看 setup，再回 concepts 补理解。', '/setup/'],
          ['我想先建立系统心智模型', '优先 concepts，尤其是 architecture / session / gateway。', '/concepts/'],
          ['我想知道值不值得学', '直接看 use cases 和首页。', '/use-cases/'],
          ['我已经在用了，想更稳', '直接进入 advanced 和 FAQ。', '/advanced/']),
    bullets('学习建议',
            '先抓住关系，再记名词。',
            '先跑通最小成功，再补全部细节。',
            '遇到不懂的日志先查 FAQ，不要立刻脑补成严重故障。'),
], [('看首轮路线图', '/getting-started/first-roadmap/'), ('看概念', '/concepts/')])

add_page('/getting-started/first-roadmap/', '从零到第一次成功', 'Getting Started', '第一次成功的目标不是“精通”，而是“闭环”',
         '你只需要知道最小成功长什么样：安装完成、配置必要项、网关健康、能发出并收到第一条消息。',
         '只要闭环形成，你后面再补概念和高级话题都会轻松很多。', [
    steps('首轮建议路线',
          ['准备环境', '先确认 requirements。'],
          ['完成安装', '先别同时搞复杂集成。'],
          ['配置必要项', '只配支撑第一次成功的最小集合。'],
          ['启动 gateway', '确认系统健康启动。'],
          ['发出第一条消息', '完成第一次可验证交互。']),
    bullets('新手最容易混淆的点',
            '把安装问题、配置问题和连接问题混成一团。',
            '以为第一次必须全懂架构。',
            '看到 warning 就以为整个系统坏了。'),
], [('开始 Setup', '/setup/'), ('看 FAQ', '/faq/')])

# Concepts overview and pages
add_page('/concepts/', '核心概念', 'Core Concepts', '先理解关系，再理解术语',
         'OpenClaw 难的地方往往不是单个名词，而是这些部分是怎么一起工作的。',
         '这一页是概念系统入口，建议先看 architecture，再看 session / gateway / skills / tools / memory。', [
    steps('推荐阅读顺序',
          ['Architecture', '先知道系统里有哪些大部件。'],
          ['Session', '理解上下文与边界。'],
          ['Gateway', '理解运行与入口层。'],
          ['Skills / Tools', '理解“怎么做”和“能做什么”的分工。'],
          ['Memory', '理解连续性与文件边界。']),
    cards('核心概念卡片',
          ['Architecture', '系统总览与消息/动作流转。', '/concepts/architecture/'],
          ['Agent', 'OpenClaw 中“助理本身”到底是什么。', '/concepts/agent/'],
          ['Session', '上下文容器与协作边界。', '/concepts/session/'],
          ['Gateway', '服务层、控制面与连接入口。', '/concepts/gateway/'],
          ['Node', '设备连接与节点模型。', '/concepts/node/'],
          ['Skills', '指导行为的说明层。', '/concepts/skills/'],
          ['Tools', '真正执行动作的能力接口。', '/concepts/tools/'],
          ['Memory', '文件化连续性。', '/concepts/memory/'],
          ['Dashboard', '观察与操作系统的界面层。', '/concepts/dashboard/'],
          ['Heartbeat / Cron', '周期检查与定时任务。', '/concepts/heartbeat-cron/'],
          ['Subagents', '复杂任务拆分机制。', '/concepts/subagents/'],
          ['ACP', '开发/编码类 harness 工作流。', '/concepts/acp/'])
], [('看架构', '/concepts/architecture/'), ('看 Session', '/concepts/session/')])

concept_pages = [
    ('/concepts/architecture/', '系统架构', 'OpenClaw 是由入口、会话、能力层和持久化层组成的系统',
     '最实用的理解方式不是背定义，而是看消息怎么进来、上下文怎么积累、工具怎么被调用、结果怎么回去。',
     '把架构看懂后，后面的 gateway、session、skills、tools、memory 就不再像零散术语。', [
         bullets('主要构件', 'Gateway：承接运行、连接与服务入口。', 'Session：承载当前上下文与边界。', 'Skills：在特定任务里注入行为规则。', 'Tools：真正执行读文件、发请求、调用服务等动作。', 'Memory files：提供跨会话连续性与长期记录。'),
         steps('一条典型流转', ['消息进入系统', '来自 Dashboard、Telegram、Discord 或其他入口。'], ['系统选择当前 session', '决定沿用哪些历史与规则。'], ['模型结合 instructions / skills 规划动作', '判断是直接回答还是调用工具。'], ['调用 tools 执行', '读取、搜索、写入、发送。'], ['把结果回传', '输出给当前用户或目标渠道。']),
         bullets('为什么它最重要', '很多问题本质上都是“结构关系没搞清”。', '权限、记忆位置、连接、日志现象，最终都能回到架构层解释。')]),
    ('/concepts/agent/', 'Agent', '在 OpenClaw 里，agent 不是抽象 buzzword，而是具体承担角色、规则和能力边界的助理单元',
     '它会结合系统指令、人格、工具能力、技能和记忆去做事。',
     '理解 agent 的关键，是把它看成“有身份、有工作边界、有执行接口”的助理。', [
         bullets('需要先理解的点', 'Agent 不是纯模型本体。', 'Agent 也不是单独一个 skill 或 tool。', '它是“指令 + 能力 + 行为规则 + 记忆 + 渠道上下文”的组合体。'),
         cards('相关概念', ['Skills', '告诉 agent 在某类任务里该怎么做。', '/concepts/skills/'], ['Tools', '让 agent 真正执行动作。', '/concepts/tools/'], ['Session', '让 agent 在当前工作上下文里持续协作。', '/concepts/session/'])]),
    ('/concepts/session/', 'Session', 'Session 是 OpenClaw 里最重要的上下文边界之一',
     '你可以把它理解成“某一段持续协作的工作容器”，里面会积累对话、工具使用痕迹、任务上下文和状态。',
     '很多“为什么它这样回答”“为什么上下文变多了”“为什么要开新线程”之类的问题，都和 session 有关。', [
         bullets('Session 是什么', '它不是单纯的聊天窗口，而是一次持续协作的上下文单元。', '它决定模型当前能看到哪些历史信息，也影响后续动作和成本。'),
         bullets('为什么边界很重要', '上下文越长，不代表越聪明；很多时候只会更重、更慢、更乱。', '产品讨论、代码实现、复杂诊断拆到不同 session，通常更稳定。', '不同人、不同渠道、不同任务也应有不同边界，避免信息串味。'),
         cards('常见误解', ['误解：开新 session 会“失忆”', '真正重要内容应该写入文件记忆，而不是塞在上下文里。', None], ['误解：所有事堆一个 session 最方便', '短期省事，长期通常更糟。', None])]),
    ('/concepts/gateway/', 'Gateway', 'Gateway 是 OpenClaw 的运行与连接核心层',
     '如果把 OpenClaw 看成可工作的助理系统，那么 gateway 更像承载它对外服务、控制面与连接能力的基础设施。',
     '很多用户真正“操作 OpenClaw”的感觉，都是通过 gateway 体现出来的。', [
         bullets('Gateway 主要负责什么', '提供系统服务入口。', '支撑 Dashboard / Control UI。', '承接部分远程访问、连接状态与服务健康检查。', '成为很多日志、连接问题和运行状态观察的中心。'),
         bullets('为什么新手必须理解它', '“装好了但为什么没跑起来”的问题，很多都落在 gateway 层。', '启动、状态、token、远程访问、回退行为，都会和 gateway 直接相关。'),
         cards('你通常会在哪里遇到它', ['启动服务', '确认网关是否已正常运行。', '/setup/start-gateway/'], ['连接控制界面', '通过 dashboard / control UI 观察与操作。', '/faq/connectivity/'], ['排查 ws / http 行为', '理解某些链路为何会 fallback。', '/faq/ws-http-fallback/'])]),
    ('/concepts/node/', 'Node', 'Node 帮你理解 OpenClaw 如何跨设备、跨入口连接现实世界',
     '如果 gateway 更偏服务核心，那么 node 更接近“某个设备或接入点是怎么接入系统”的直觉。',
     '理解 node 会帮助你看懂本地、远程、配对和设备连接相关问题。', [
         bullets('需要知道的直觉', 'Node 往往代表某个设备侧的接入与连接身份。', '本地直连和远程连接在感受上相似，但背后链路不同。', '很多配对、授权、可达性问题都会落到 node 相关配置上。'),
         cards('继续阅读', ['远程访问', '从场景角度理解多设备与远程接入。', '/use-cases/remote-access/'], ['连接 FAQ', '排查 token、访问与可达性问题。', '/faq/connectivity/'])]),
    ('/concepts/skills/', 'Skills', 'Skill 决定“在某类任务里，助理应该怎样做”',
     '它更像可按需加载的专业操作说明，而不是底层执行器。',
     '如果把 OpenClaw 比作一个团队，skill 更像 SOP、工作手册或岗位剧本。', [
         bullets('Skill 不是什么', '它不是模型本身。', '它不是 tool，也不是直接执行命令的接口。', '它不是无限长的万能提示词堆。'),
         bullets('Skill 真正做的事', '告诉助理什么时候该用哪套规则。', '约束输出方式、执行顺序和注意事项。', '把某类任务的专业做法封装成可复用行为。'),
         cards('和 Tool 的区别', ['Skill', '说明“怎么做更对”。', '/concepts/skills/'], ['Tool', '提供“实际能做什么”。', '/concepts/tools/'])]),
    ('/concepts/tools/', 'Tools', 'Tool 是 OpenClaw 真正把动作落到系统上的能力接口',
     '读文件、写文件、搜网页、发消息、起子代理……这些都属于 tools 的范畴。',
     '没有 tool，再聪明的说明也只能停留在“会说但做不了”。', [
         bullets('Tool 的核心意义', '把模型从“文本回答者”扩展成“可执行助理”。', '让系统可以访问文件、网络、服务和外部能力。', '把行动留痕并放在可观察、可约束的边界里。'),
         bullets('为什么它不只是“函数调用”', '工具调用常常伴随权限、审批、执行环境与风险控制。', '用户看到的不只是“有没有这个功能”，还包括“什么时候允许用、怎么用更安全”。'),
         cards('新手需要记住的区分', ['Model', '负责理解和规划。', None], ['Skill', '负责行为规则和任务套路。', '/concepts/skills/'], ['Tool', '负责真正执行。', '/concepts/tools/'])]),
    ('/concepts/memory/', 'Memory', 'OpenClaw 的“记忆”更接近文件化连续性，而不是神秘的永久脑内记忆',
     '它强调把重要信息写进文件、分层保存，再在需要时检索。',
     '这比幻想模型天然长期记住一切更可靠，也更适合真实协作。', [
         bullets('要先建立的直觉', '会话上下文是短期的，会变长、会切换、也会被重置。', '真正值得保留的信息，应写入 memory/YYYY-MM-DD.md 或 MEMORY.md 一类文件。', '记忆不是越多越好，而是越有结构越好。'),
         bullets('为什么文件记忆很重要', '它能跨 session 保持连续性。', '它更容易审计、编辑、纠正和清理。', '它天然支持安全边界。'),
         cards('继续阅读', ['Memory Design', '从进阶视角看“写什么、写到哪、何时读”。', '/advanced/memory-design/'], ['FAQ: Files and Memory', '理解缺文件、ENOENT、记忆边界等常见问题。', '/faq/files-and-memory/'])]),
    ('/concepts/dashboard/', 'Dashboard / Control UI', 'Dashboard 是观察和操作 OpenClaw 的控制面',
     '它不是系统本体，但能让你更方便地查看状态、切换界面、验证连接与操作会话。',
     '理解 dashboard 的定位，有助于区分“界面层问题”和“系统层问题”。', [
         bullets('它的作用', '观察状态。', '进入控制界面。', '辅助验证 gateway、token、连接情况。'),
         cards('相关页面', ['Gateway', '很多 dashboard 问题最后都回到 gateway。', '/concepts/gateway/'], ['Connectivity FAQ', '控制界面、token 和连接问题优先从这里排。', '/faq/connectivity/'])]),
    ('/concepts/heartbeat-cron/', 'Heartbeat 与 Cron', 'Heartbeat 和 cron 都能做“周期性工作”，但适用场景不同',
     '一个更偏“定期顺手检查”，一个更偏“按时间点精确执行”。',
     '理解两者差异，能帮你设计更省 token、更稳定的自动化方式。', [
         bullets('Heartbeat 更适合', '把多项检查批量合并。', '需要依赖最近上下文的轻量周期工作。', '时间允许略有漂移的任务。'),
         bullets('Cron 更适合', '精确时间触发。', '独立线程处理。', '一次性提醒或严格调度任务。'),
         cards('场景页', ['Heartbeat Automation', '从使用角度看周期性帮助。', '/use-cases/heartbeat-automation/'], ['Best Practices', '看如何降低无效 API 消耗。', '/advanced/best-practices/'])]),
    ('/concepts/subagents/', 'Subagents', 'Subagent 的价值在于把复杂任务拆开，不让一个 session 扛下整个世界',
     '它特别适合长任务、复杂诊断、分工协作和减少主线程上下文膨胀。',
     '你可以把它理解成“给任务开分身”，但边界更清晰、目标更明确。', [
         bullets('什么时候该用', '任务复杂、耗时长。', '需要独立上下文。', '需要把主线程保持清爽。', '需要并行探索或拆分执行。'),
         cards('继续阅读', ['Subagent Workflows', '进阶视角看拆分策略。', '/advanced/subagent-workflows/'], ['Session Model', '理解为什么要切边界。', '/advanced/session-model/'])]),
    ('/concepts/acp/', 'ACP', 'ACP 更适合代码、代理式开发和特定 harness 场景',
     '如果普通会话更像通用助理协作，那么 ACP 更像接入专门的编码/工具化工作流。',
     '它通常出现在“让 codex / claude code / cursor 类环境接手开发”的上下文里。', [
         bullets('要点', 'ACP 不是普通子代理的简单别名。', '它适合线程绑定、持久化、开发流。', '它帮助把复杂编码工作隔离到更合适的执行环境中。'),
         cards('继续阅读', ['GitHub Workflow', '看开发协作类场景。', '/use-cases/github-workflow/'], ['Subagent Workflows', '看任务拆分与开发流。', '/advanced/subagent-workflows/'])]),
]

for route, title, hero_title, hero_desc, summary, sections in concept_pages:
    add_page(route, title, 'Core Concepts', hero_title, hero_desc, summary, sections,
             [('', '/concepts/')])
PAGES['/concepts/architecture/']['cta'] = [('看 Session', '/concepts/session/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/agent/']['cta'] = [('看 Skills', '/concepts/skills/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/session/']['cta'] = [('看 Gateway', '/concepts/gateway/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/gateway/']['cta'] = [('看 Setup', '/setup/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/node/']['cta'] = [('看 Remote Access', '/use-cases/remote-access/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/skills/']['cta'] = [('看 Tools', '/concepts/tools/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/tools/']['cta'] = [('看 Skills', '/concepts/skills/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/memory/']['cta'] = [('看 Memory Design', '/advanced/memory-design/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/dashboard/']['cta'] = [('看 Connectivity FAQ', '/faq/connectivity/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/heartbeat-cron/']['cta'] = [('看 Heartbeat Automation', '/use-cases/heartbeat-automation/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/subagents/']['cta'] = [('看 Subagent Workflows', '/advanced/subagent-workflows/'), ('回到 Concepts', '/concepts/')]
PAGES['/concepts/acp/']['cta'] = [('看 GitHub Workflow', '/use-cases/github-workflow/'), ('回到 Concepts', '/concepts/')]

# Setup
add_page('/setup/', 'Setup & Deployment', 'Setup', '把第一次安装和启动拆成一条可验证的路径',
         '新手最容易卡住的地方不是不会点按钮，而是不知道现在该验证什么、下一步去哪。',
         '这部分把 setup 按顺序拆开，每一页都强调目标、动作、成功信号和常见问题。', [
    steps('推荐顺序', ['Requirements', '先确认环境是否满足最低条件。'], ['Install', '完成安装并确认命令可用。'], ['Configuration', '配置必须项，别一上来全改。'], ['Start Gateway', '启动服务并检查健康状态。'], ['First Message', '完成第一条成功交互。']),
    bullets('Setup 的核心原则', '按顺序走，不要跳步。', '每一步都要看成功信号。', '遇到问题先判断是环境、安装、配置、启动还是连接层。'),
    cards('继续往下', ['Requirements', '先确认前提。', '/setup/requirements/'], ['Install', '把 OpenClaw 装上。', '/setup/install/'], ['Troubleshooting', '卡住时先缩层级。', '/setup/troubleshooting/'])
], [('看 Requirements', '/setup/requirements/'), ('看 Install', '/setup/install/')])

setup_pages = [
    ('/setup/requirements/', '环境要求', '先确认环境，再开始安装', '很多“安装失败”其实不是安装命令错了，而是系统、运行时、权限或依赖前提没满足。', '这一步的价值不是复杂，而是避免后面浪费时间。', [
        bullets('至少要确认什么', '操作系统与基础运行环境是否受支持。', 'Node / 包管理器 / 终端权限是否正常。', '是否能访问后续需要的模型/API/网络资源。', '如果要用 Dashboard、消息平台或外部集成，相关前提是否满足。'),
        bullets('成功信号', '运行环境版本明确。', '终端可正常执行基础命令。', '没有明显的权限或网络阻断前提。')], [('继续安装', '/setup/install/'), ('回到 Setup', '/setup/')]),
    ('/setup/install/', '安装', '安装阶段的目标只有一个：把 OpenClaw 正确装上', '先完成最小安装，再进入配置与启动，会比一口气把所有高级玩法一起搞完更稳。', '如果你已经习惯开发环境，也建议先按最小可运行路径验证。', [
        steps('安装建议节奏', ['执行安装', '按官方方式安装。'], ['确认命令存在', '先看 help 或状态命令。'], ['不要过早扩展', '先别急着做复杂远程接入或多集成。']),
        bullets('常见坑', '把安装问题和配置问题混在一起。', '命令装上了，但 PATH / shell 环境没刷新。', '一开始就同时处理多套外部集成，导致定位困难。')], [('看 Configuration', '/setup/configuration/'), ('回到 Setup', '/setup/')]),
    ('/setup/configuration/', '配置', '配置不是“把所有选项都填满”，而是先把最关键的行为开关对齐', '新手最常见的问题，是把配置想成一次性大工程。其实首轮只需要完成能支撑第一次成功的必要项。', '理解哪些是必须项、哪些可以后补，会让 setup 难度大幅下降。', [
        bullets('首轮最关心什么', '默认模型与可用提供商是否设置好。', '网关相关配置是否足以支撑本地启动与控制界面。', '必要渠道或插件是否已最小化启用。', '工作目录、技能、记忆结构是否符合预期。'),
        bullets('不要一上来就做的事', '同时开启一堆还不会用的外部接入。', '在没验证基础链路前就做复杂远程访问配置。', '看到所有字段就想一次配置到完美状态。'),
        bullets('成功信号', '能解释当前最小配置为什么足够。', '知道下一步应该去启动 gateway，而不是继续盲改配置。')], [('启动 Gateway', '/setup/start-gateway/'), ('回到 Setup', '/setup/')]),
    ('/setup/start-gateway/', '启动 Gateway', '启动网关的目标不是看到一串日志，而是确认系统已经进入健康可交互状态', '你需要知道“正常启动长什么样”，这样遇到异常时才不会被无意义日志吓到。', '很多体验好不好，取决于你是否会验证 gateway 状态。', [
        bullets('你要验证的不是“有没有输出”', '而是 gateway 是否成功启动。', '状态检查是否正常。', '控制界面 / 连接入口是否能工作。'),
        bullets('健康启动的直觉', '服务命令能正常启动。', '状态命令能给出清晰结果。', 'Dashboard / Control UI 应能连上当前运行中的 gateway。'),
        steps('遇到异常时先判断哪一层', ['启动失败', '先看环境与配置。'], ['界面连不上', '优先看 gateway 与 token / 连接配置。'], ['日志有 warning', '先判断是否只是可容忍回退，而不是致命故障。'])], [('完成 First Message', '/setup/first-message/'), ('看 Troubleshooting', '/setup/troubleshooting/')]),
    ('/setup/first-message/', '第一条消息', '第一次成功不是“看懂全部”，而是完成一次真实可验证的交互', '只要你能在目标入口和 OpenClaw 正常互动，并确认背后的链路是通的，这次 setup 就算过了第一关。', '接下来再逐步补概念和高级能力，会轻松很多。', [
        bullets('第一次成功应包含什么', '你知道消息从哪里发出。', '你知道系统在哪里响应。', '你能判断这不是假象，而是真正完成了一次可用交互。'),
        steps('建议验证项', ['发出一条简单请求', '例如让系统回答一个基础问题。'], ['确认响应回来', '并确认不是卡在 gateway / UI / token 层。'], ['观察最小运行闭环', '知道消息经历了入口、session、模型与返回。']),
        cards('跑通后该去哪', ['补核心概念', '把刚才体验到的东西和 architecture / session / gateway 对上。', '/concepts/'], ['查看常见问题', '提前建立对 setup / connectivity 问题的判断。', '/faq/'], ['进入高级主题', '理解长期协作、记忆设计与安全边界。', '/advanced/'])], [('看 FAQ', '/faq/'), ('看 Advanced', '/advanced/')]),
    ('/setup/troubleshooting/', 'Setup Troubleshooting', '当 setup 卡住时，先判断你卡在第几层，而不是先怀疑整个系统坏了', '排错的关键不是看更多日志，而是把问题缩到 requirements、install、configuration、gateway、first message 其中一层。', '这一页提供最小排错路径，让你先收缩范围，再看细节。', [
        steps('最小排查顺序', ['看 requirements', '先确认是不是环境前提没满足。'], ['看 install', '确认安装本身是否真的成功。'], ['看 configuration', '必要配置是否已经对齐。'], ['看 gateway', '服务是否健康运行。'], ['看 first message', '问题到底发生在入口、连接还是响应链路。']),
        bullets('排错时最常见的坏习惯', '还没分层，就开始贴一大堆混杂日志。', '把安装、配置、连接问题统称成“OpenClaw 不工作”。', '没有先确认成功信号，就直接改一堆配置。')], [('看 Setup FAQ', '/faq/setup/'), ('回到 Setup', '/setup/')]),
]
for route, title, hero_title, hero_desc, summary, sections, ctas in setup_pages:
    add_page(route, title, 'Setup', hero_title, hero_desc, summary, sections, ctas)

# Use cases
add_page('/use-cases/', 'Use Cases', 'Use Cases', 'OpenClaw 真正有趣的地方，在于它不是只能“聊”',
         '它可以作为私人助理、消息中台、自动化入口、文件协作层和开发辅助系统。',
         '这一部分用场景而不是术语来帮助你理解它为什么有价值。', [
    cards('按场景浏览',
          ['Personal Assistant', '日程、提醒、信息整理与生活协作。', '/use-cases/personal-assistant/'],
          ['Messaging Platforms', '把助理放进 Telegram、Discord 等消息环境。', '/use-cases/messaging-platforms/'],
          ['GitHub Workflow', '开发协作、issue、PR、review、CI。', '/use-cases/github-workflow/'],
          ['Notes & Reminders', '日常信息管理与任务跟进。', '/use-cases/notes-reminders/'],
          ['Google Workspace', 'Gmail、Calendar、Docs、Drive 协作。', '/use-cases/google-workspace/'],
          ['Heartbeat Automation', '周期检查与主动提醒。', '/use-cases/heartbeat-automation/'],
          ['Remote Access', '多设备与远程接入。', '/use-cases/remote-access/'])
], [('看私人助理', '/use-cases/personal-assistant/'), ('看消息平台', '/use-cases/messaging-platforms/')])

use_case_pages = [
    ('/use-cases/personal-assistant/', '私人助理场景', '把 OpenClaw 当成私人助理时，重点不是“会聊天”，而是“会协作”', '它的价值在于可以结合渠道、工具、记忆与规则，把长期支持做得更稳定。', '这也是很多人第一次真正感觉 OpenClaw 和普通聊天产品不一样的地方。', [
        bullets('典型能力', '在聊天渠道里直接沟通。', '读取和整理本地文件。', '连接日历、邮件、提醒、笔记等真实工具。', '通过记忆文件保持长期偏好和协作连续性。')], [('回到 Use Cases', '/use-cases/'), ('看 Notes & Reminders', '/use-cases/notes-reminders/')]),
    ('/use-cases/messaging-platforms/', '消息平台场景', 'Telegram、Discord、Signal 这类入口让 OpenClaw 从“本地工具”变成“能随手叫到的助理”', '消息平台不是装饰，而是很多真实使用场景的主入口。', '理解这类接入的意义，也有助于理解 gateway、session 和远程可达性。', [
        bullets('为什么消息平台很关键', '它让助理进入用户原本就在使用的环境。', '它天然支持多轮协作与低摩擦触达。', '它会把权限、边界、群聊行为这些问题带到真实世界。')], [('回到 Use Cases', '/use-cases/'), ('看 Remote Access', '/use-cases/remote-access/')]),
    ('/use-cases/github-workflow/', 'GitHub 工作流', 'OpenClaw 在 GitHub 场景里最有价值的地方，是把“看 issue、做修改、提 PR、看 CI”串成可协作流程', '它并不是替代开发者，而是把许多重复性的查询、检查和执行动作组织得更顺手。', '对于技术用户来说，这是最容易感受到“助理真的在干活”的场景之一。', [
        bullets('典型工作流', '看 issue / PR / CI 状态。', '让代理做代码实现与修复。', '拆分子任务给 subagent / ACP。', '在本地工作区和 GitHub 之间形成闭环。'),
        cards('相关概念', ['ACP', '开发类 harness 场景。', '/concepts/acp/'], ['Subagents', '复杂任务拆分。', '/concepts/subagents/'])], [('回到 Use Cases', '/use-cases/'), ('看 ACP', '/concepts/acp/')]),
    ('/use-cases/notes-reminders/', '笔记与提醒', '当 OpenClaw 接到 notes / reminders 类工具后，它就从“会说”变成“会帮你记和跟”', '这类场景特别适合生活管理、轻量项目跟进和个人助理日常。', '价值不在复杂，而在低摩擦长期可用。', [
        bullets('适合的事', '快速记下想法。', '维护待办。', '完成提醒。', '把对话中出现的重要事项沉淀下来。')], [('回到 Use Cases', '/use-cases/'), ('看 Personal Assistant', '/use-cases/personal-assistant/')]),
    ('/use-cases/google-workspace/', 'Google Workspace', 'Google Workspace 场景让 OpenClaw 进入真正的生产力协作层', '邮件、日历、文档、Drive 这些入口一旦接起来，助理就能帮你处理更接近真实工作的任务。', '它最适合那些已经有明确办公流程的用户。', [
        bullets('你通常会拿它做什么', '查 Gmail。', '创建或查看 Calendar。', '处理 Docs / Sheets / Drive 相关操作。', '把对话里的事务转成具体执行。')], [('回到 Use Cases', '/use-cases/'), ('看 Setup', '/setup/')]),
    ('/use-cases/heartbeat-automation/', 'Heartbeat 自动化', 'Heartbeat 的魅力不在“自动”两个字本身，而在它能像贴身秘书一样定期顺手看一眼', '它适合邮箱、日历、天气、通知、项目状态等“值得偶尔看看，但不需要精确秒级调度”的任务。', '用得好，它会很贴心；用不好，它会变成 API 烧钱机器。', [
        bullets('适合的检查', '邮箱有没有重要新邮件。', '接下来 24-48h 的日程。', '项目状态或提醒事项。', '天气等轻量情境信息。'),
        bullets('要注意', '少量批量检查比高频单点检查更划算。', '没事就安静，不要为了“主动”而主动。')], [('回到 Use Cases', '/use-cases/'), ('看 Heartbeat / Cron', '/concepts/heartbeat-cron/')]),
    ('/use-cases/remote-access/', '远程访问与多设备', 'Remote access 场景决定了 OpenClaw 是否只是“家里那台机器上的小玩具”，还是“你随时能叫到的助理”', '一旦涉及多设备和远程访问，连接模型、gateway、token、pairing、public URL 这些问题就会变得重要。', '这也是很多人第一次真正碰到 node / pairing / remote 配置的场景。', [
        bullets('这类场景常见问题', '本地能连，远程不能连。', '控制界面缓存旧 token。', '配对过期或 public URL 配错。', '多设备链路理解不清。')], [('回到 Use Cases', '/use-cases/'), ('看 Connectivity FAQ', '/faq/connectivity/')]),
]
for route, title, hero_title, hero_desc, summary, sections, ctas in use_case_pages:
    add_page(route, title, 'Use Cases', hero_title, hero_desc, summary, sections, ctas)

# Advanced
add_page('/advanced/', 'Advanced Topics', 'Advanced', '当你已经能用 OpenClaw，下一步就该理解为什么有些设计必须这么做',
         '高级主题不是为了炫技，而是帮助你做出更稳、更清晰、更省成本的使用与架构决策。',
         '如果你已经跑通过第一次成功，这部分会开始变得非常有价值。', [
    cards('推荐先读',
          ['Session Model', '为什么上下文边界会影响质量、成本与稳定性。', '/advanced/session-model/'],
          ['Memory Design', '为什么记忆需要分层与治理。', '/advanced/memory-design/'],
          ['Skill Design', '什么时候需要把经验固化成 skill。', '/advanced/skill-design/'],
          ['Subagent Workflows', '复杂任务如何拆开做。', '/advanced/subagent-workflows/'],
          ['Safety Boundaries', '为什么有些动作必须确认。', '/advanced/safety-boundaries/'],
          ['Debugging Logs', '怎么读日志而不被 benign 噪音带偏。', '/advanced/debugging-logs/'],
          ['Best Practices', '把经验沉淀成日常规则。', '/advanced/best-practices/'])
], [('看 Session Model', '/advanced/session-model/'), ('看 Best Practices', '/advanced/best-practices/')])

advanced_pages = [
    ('/advanced/session-model/', 'Session Model', 'Session 设计会直接影响体验、成本和可维护性', '如果你把所有事都堆在一个超长会话里，通常只会越来越慢、越来越糊。', '理解 session model，本质上是在理解“如何给协作切边界”。', [
        bullets('为什么重要', '影响上下文质量与 token 成本。', '影响任务拆分与长期协作稳定性。', '影响不同人、不同渠道、不同工作流是否会互相污染。')], [('看 Memory Design', '/advanced/memory-design/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/memory-design/', 'Memory Design', '记忆设计不是让系统记更多，而是让重要信息以合适的层次留下来', '好的记忆设计会让协作越来越顺；糟糕的记忆设计会让系统越来越臃肿、越来越危险。', '这页关注的是“写什么、写到哪、什么时候读、什么时候清”。', [
        bullets('核心原则', '把稳定偏好和长期决策沉淀到长期记忆。', '把临时上下文记录到日记式记忆。', '不要把敏感或无关信息无差别长期保留。')], [('看 Skill Design', '/advanced/skill-design/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/skill-design/', 'Skill Design', '当某类任务一再重复，而且你已经知道“怎么做更对”时，就该考虑把它固化成 skill', 'Skill design 的价值不在写得长，而在把经验沉淀成可复用行为。', '好的 skill 会让执行更稳定；糟糕的 skill 只会制造又长又乱的提示负担。', [
        bullets('什么时候值得设计 skill', '任务高频重复。', '有明确流程与注意事项。', '需要统一输出格式或风险控制。', '需要把专业经验沉淀下来。'),
        bullets('常见坏味道', '把所有知识都塞进一个巨型万能 skill。', '没有边界，没有触发条件。', '写得像文档抄录，而不是执行指引。')], [('看 Subagent Workflows', '/advanced/subagent-workflows/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/subagent-workflows/', 'Subagent Workflows', '复杂任务最好拆开做，而不是让主线程一口吞下全部上下文', '分任务、分线程、分上下文，是提升稳定性和降低 token 浪费的关键手段之一。', '这也是产品讨论、编码实现、复杂排错经常需要分开的原因。', [
        bullets('适合拆出去的任务', '长时间编码。', '复杂日志诊断。', '并行探索方案。', '批量处理或观察任务。'),
        bullets('为什么有效', '主线程更干净。', '不同任务不会互相污染。', '更容易复盘和控制成本。')], [('看 Safety Boundaries', '/advanced/safety-boundaries/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/safety-boundaries/', 'Safety Boundaries', '一个真的能做事的助理，必须同时有能力边界与审批边界', '否则它越强，就越容易在错误的场景里做出错误动作。', '安全边界不是妨碍体验，而是在保护真实世界里的用户。', [
        bullets('常见边界类型', '外发动作需要确认。', '高风险命令需要审批。', '群聊与私聊的隐私边界不同。', '记忆、文件与工具访问都应该有范围。')], [('看 Debugging Logs', '/advanced/debugging-logs/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/debugging-logs/', 'Debugging Logs', '读日志的目标不是看到更多文本，而是更快分辨“严重故障”和“可容忍噪音”', '很多新手被日志吓到，不是因为问题真的大，而是因为缺少一套分层判断方法。', '这一页帮助你建立“先分类、再定位、再决定是否需要处理”的直觉。', [
        bullets('先判断什么', '这是 error、warning 还是 benign noise？', '它影响功能，还是只是回退/降级？', '它落在哪一层：环境、配置、gateway、连接、工具、UI？'),
        cards('相关 FAQ', ['WS / HTTP fallback', '理解为什么 fallback 不等于系统坏了。', '/faq/ws-http-fallback/'], ['Files & Memory', '理解缺文件或 ENOENT 类现象。', '/faq/files-and-memory/'])], [('看 Best Practices', '/advanced/best-practices/'), ('回到 Advanced', '/advanced/')]),
    ('/advanced/best-practices/', 'Best Practices', '真正让 OpenClaw 好用的，常常不是某个神奇功能，而是一组稳定的小习惯', '例如把不同任务拆 session、把重要信息写文件、不要被 benign log 噪音吓到、逐步扩展配置。', '这页是把实践经验浓缩成行动建议。', [
        bullets('建议', '先跑通最小成功，再扩展。', '先理解结构，再追高级玩法。', '把重要连续性写文件。', '把复杂任务拆开处理。', '不要把所有问题都堆进一个上下文里。')], [('看 FAQ', '/faq/'), ('回到 Advanced', '/advanced/')]),
]
for route, title, hero_title, hero_desc, summary, sections, ctas in advanced_pages:
    add_page(route, title, 'Advanced', hero_title, hero_desc, summary, sections, ctas)

# FAQ
add_page('/faq/', 'FAQ', 'FAQ', '先别慌，很多“看起来像故障”的东西其实是常见现象',
         'FAQ 的作用不是替代完整文档，而是帮你快速判断：这是不是已知常见问题、该先看哪一层。',
         '对新手来说，FAQ 能显著降低被术语和日志吓退的概率。', [
    cards('优先入口',
          ['Setup FAQ', '安装、配置、启动、首条消息相关问题。', '/faq/setup/'],
          ['Connectivity FAQ', '连接、token、访问与控制界面相关问题。', '/faq/connectivity/'],
          ['WS / HTTP Fallback', '理解回退现象，不要误判。', '/faq/ws-http-fallback/'],
          ['Files & Memory', '理解缺文件、ENOENT 与记忆边界。', '/faq/files-and-memory/'],
          ['Skills & Tools', '为什么它有时不按你想的方式工作。', '/faq/skills-and-tools/'],
          ['Security & Behavior', '为什么会要求审批、为什么群聊会克制发言。', '/faq/security-and-behavior/'])
], [('看 Setup FAQ', '/faq/setup/'), ('看 Connectivity FAQ', '/faq/connectivity/')])

faq_pages = [
    ('/faq/setup/', 'FAQ · Setup', '很多 setup 问题本质上不是“系统坏了”，而是顺序错了、前提没确认或成功信号没看懂', '先按层判断 requirements / install / configuration / gateway / first message，通常会快很多。', '别把所有问题都打成“安装失败”四个字，那样最难排。', [
        steps('优先排查顺序', ['Requirements', '环境前提是否满足？'], ['Install', '命令和安装是否真的成功？'], ['Configuration', '必要配置是否对齐？'], ['Gateway', '服务是否健康启动？'], ['First Message', '问题是在入口层还是运行层？'])], [('看 Connectivity FAQ', '/faq/connectivity/'), ('回到 FAQ', '/faq/')]),
    ('/faq/connectivity/', 'FAQ · Connectivity', '连不上，不一定是“整个系统坏了”', '很多连接问题其实集中在 gateway 状态、访问入口、token 不一致、控制界面缓存或远程可达性配置。', '只要分层判断，通常很快能把问题缩小。', [
        bullets('优先怀疑什么', 'Gateway 是否真的在运行。', '当前 UI / 控制面拿到的 token 是否正确。', '是不是旧页面缓存了过期状态。', '远程访问路径是否与当前配置一致。')], [('看 WS / HTTP Fallback', '/faq/ws-http-fallback/'), ('回到 FAQ', '/faq/')]),
    ('/faq/ws-http-fallback/', 'FAQ · WS / HTTP Fallback', '看到 ws-stream 出错再 fallback 到 HTTP，并不自动等于“系统已经坏了”', '很多时候这代表某条 WebSocket 传输链路没有成功建立，但系统仍可退回 HTTP 继续工作。', '它可能带来性能或流量上的小浪费，但要先判断是否影响核心功能。', [
        bullets('你应该先判断什么', '功能是否仍正常可用。', '这是网关整体故障，还是某条传输链路兼容问题。', '有没有明显的持续错误影响实际使用。'),
        bullets('为什么容易被误判', '因为 500 / fallback 这些词看起来很吓人。', '但现实里回退机制本来就是为了“出问题也先保持可用”。')], [('看 Debugging Logs', '/advanced/debugging-logs/'), ('回到 FAQ', '/faq/')]),
    ('/faq/files-and-memory/', 'FAQ · Files & Memory', '缺文件、ENOENT、记忆相关日志，不一定说明系统异常', '有些文件本来就是“按约定可存在，但也可能暂时不存在”的状态。', '关键不是看到 ENOENT 就紧张，而是判断它是否真的影响你的工作流。', [
        bullets('常见情况', '某些 memory 文件还没创建。', '系统按约定尝试读取，但文件尚不存在。', '这会产生日志噪音，但不一定影响核心功能。'),
        bullets('你该做什么', '先判断它是不是预期文件。', '再判断是否真的导致功能失败。', '如果只是噪音，可以后续再优化，而不是立刻当成阻断。')], [('看 Memory', '/concepts/memory/'), ('回到 FAQ', '/faq/')]),
    ('/faq/skills-and-tools/', 'FAQ · Skills & Tools', '很多“它为什么不那样做”的困惑，本质上都来自 skills 和 tools 的分工没搞清', '有时不是系统不会，而是当前没有正确 skill；有时不是规则不对，而是根本没有可执行的 tool。', '先分清“它该怎么做”和“它能做什么”，很多困惑就会消失。', [
        bullets('常见困惑', '为什么它知道但做不了？', '为什么它用了奇怪的步骤？', '为什么某个能力有时有、有时没有？'),
        cards('先去补哪里', ['Skills', '理解行为规则层。', '/concepts/skills/'], ['Tools', '理解执行能力层。', '/concepts/tools/'])], [('看 Skills', '/concepts/skills/'), ('回到 FAQ', '/faq/')]),
    ('/faq/security-and-behavior/', 'FAQ · Security & Behavior', '如果一个助理真的能做事，它就不可能完全没有边界', '审批、确认、群聊克制、隐私边界，这些看起来像“限制”，其实是它变得可长期信任的前提。', '你不该把这些行为理解成笨，而应该理解成边界设计。', [
        bullets('常见现象', '为什么有些动作要确认。', '为什么群聊里不会逢消息必回。', '为什么不会随便泄露私人信息。', '为什么不会默认去做高风险外发动作。')], [('看 Safety Boundaries', '/advanced/safety-boundaries/'), ('回到 FAQ', '/faq/')]),
]
for route, title, hero_title, hero_desc, summary, sections, ctas in faq_pages:
    add_page(route, title, 'FAQ', hero_title, hero_desc, summary, sections, ctas)

STYLE = """
:root {
  --bg: #08111f;
  --bg-2: #0b1426;
  --panel: rgba(14, 25, 46, 0.82);
  --panel-2: rgba(18, 31, 57, 0.92);
  --text: #ecf3ff;
  --muted: #9db0d1;
  --line: rgba(157, 176, 209, 0.18);
  --accent: #78d7ff;
  --accent-2: #8c7bff;
  --accent-3: #52f0c5;
  --shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
  --radius: 24px;
  --radius-sm: 18px;
  --content: 1180px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--text);
  background:
    radial-gradient(circle at top, rgba(120, 215, 255, 0.14), transparent 35%),
    radial-gradient(circle at 85% 15%, rgba(140, 123, 255, 0.16), transparent 28%),
    linear-gradient(180deg, #07101d 0%, #091526 100%);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  line-height: 1.68;
}
a { color: inherit; text-decoration: none; }
.shell { width: min(calc(100% - 32px), var(--content)); margin: 0 auto; }
.topbar { position: sticky; top: 0; z-index: 20; backdrop-filter: blur(18px); background: rgba(8, 17, 31, 0.72); border-bottom: 1px solid var(--line); }
.topbar-inner { display:flex; align-items:center; justify-content:space-between; gap:20px; padding: 16px 0; }
.brand { font-weight: 800; letter-spacing: .02em; }
.nav { display:flex; gap: 10px; flex-wrap: wrap; }
.nav a { padding: 10px 14px; border-radius: 999px; color: var(--muted); border: 1px solid transparent; }
.nav a.active, .nav a:hover { color: var(--text); border-color: var(--line); background: rgba(255,255,255,.03); }
.hero { padding: 56px 0 26px; }
.eyebrow { display:inline-flex; align-items:center; gap:8px; padding: 8px 12px; border-radius:999px; border:1px solid var(--line); color: var(--accent); font-size: 14px; background: rgba(120,215,255,.06); }
.hero-grid { display:grid; grid-template-columns: 1.3fr .7fr; gap: 24px; margin-top: 18px; }
.panel { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
.hero-copy { padding: 34px; }
.hero-copy h1 { font-size: clamp(34px, 5vw, 56px); line-height: 1.08; margin: 0 0 18px; }
.hero-copy p { margin: 0; color: var(--muted); font-size: 18px; }
.hero-side { padding: 24px; display:flex; flex-direction:column; gap: 16px; }
.kpi { padding: 18px; border-radius: var(--radius-sm); background: rgba(255,255,255,.03); border:1px solid var(--line); }
.kpi strong { display:block; font-size: 28px; margin-bottom: 6px; }
.cta-row { display:flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding: 12px 18px; border-radius: 999px; border:1px solid var(--line); min-height: 46px; }
.btn.primary { background: linear-gradient(135deg, var(--accent), #9ae6ff); color: #08111f; border-color: transparent; font-weight: 700; }
.section { padding: 18px 0; }
.section-head { margin-bottom: 14px; }
.section-head h2 { margin: 0 0 8px; font-size: clamp(24px, 4vw, 34px); }
.section-head p { margin: 0; color: var(--muted); }
.cards, .grid-note { display:grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
.card, .note { padding: 22px; border-radius: var(--radius-sm); background: var(--panel); border:1px solid var(--line); box-shadow: var(--shadow); }
.card h3, .note h3 { margin: 0 0 10px; font-size: 20px; }
.card p, .note p { margin:0; color: var(--muted); }
.card .jump { display:inline-flex; margin-top: 16px; color: var(--accent); font-weight: 600; }
.steps { display:grid; gap: 14px; }
.step { display:grid; grid-template-columns: 40px 1fr; gap: 14px; padding: 20px; border-radius: var(--radius-sm); background: var(--panel); border:1px solid var(--line); }
.step-index { width: 40px; height: 40px; border-radius: 50%; display:grid; place-items:center; background: linear-gradient(135deg, var(--accent-2), var(--accent)); font-weight: 800; color:#fff; }
.step h3 { margin:0 0 6px; font-size: 18px; }
.step p, .bullet-list li, .pathline, .footer { color: var(--muted); }
.bullet-list { margin: 0; padding: 24px 24px 24px 44px; background: var(--panel); border-radius: var(--radius-sm); border:1px solid var(--line); }
.bullet-list li + li { margin-top: 10px; }
.footer { padding: 42px 0 60px; }
.footer-box { padding: 22px; border-radius: var(--radius-sm); border:1px solid var(--line); background: rgba(255,255,255,.03); }
.pathline { font-size: 14px; margin-top: 8px; }
.badges { display:flex; flex-wrap:wrap; gap: 10px; margin-top: 16px; }
.badge { display:inline-flex; align-items:center; gap:8px; padding: 8px 12px; border-radius:999px; border:1px solid var(--line); color: var(--muted); background: rgba(255,255,255,.03); }
@media (max-width: 900px) {
  .hero-grid, .cards, .grid-note { grid-template-columns: 1fr; }
  .topbar-inner { flex-direction: column; align-items:flex-start; }
}
"""

APP_JS = """
const currentPath = window.location.pathname.replace(/index\\.html$/, '/');
document.querySelectorAll('[data-nav]').forEach((link) => {
  const href = link.getAttribute('href');
  const abs = new URL(href, window.location.href).pathname.replace(/index\\.html$/, '/');
  if (abs === currentPath || (abs !== '/' && currentPath.startsWith(abs))) link.classList.add('active');
});
"""


def prefix_for(file_path: str) -> str:
    return './' if file_path == 'index.html' else '../' * (len(Path(file_path).parts) - 1)


def to_href(prefix: str, link: Optional[str]) -> Optional[str]:
    if link is None:
        return None
    return prefix if link == '/' else prefix + link.lstrip('/')


def render_section(section: dict, prefix: str) -> str:
    title_html = f"<div class='section-head'><h2>{section['title']}</h2></div>"
    if section['type'] == 'cards':
        items = []
        for title, desc, link in section['items']:
            jump = f"<a class='jump' href='{to_href(prefix, link)}'>查看页面 →</a>" if link else ''
            items.append(f"<article class='card'><h3>{title}</h3><p>{desc}</p>{jump}</article>")
        body = f"<div class='cards'>{''.join(items)}</div>"
    elif section['type'] == 'steps':
        items = []
        for idx, (title, desc) in enumerate(section['items'], start=1):
            items.append(f"<article class='step'><div class='step-index'>{idx}</div><div><h3>{title}</h3><p>{desc}</p></div></article>")
        body = f"<div class='steps'>{''.join(items)}</div>"
    elif section['type'] == 'bullets':
        body = "<ul class='bullet-list'>" + ''.join(f"<li>{item}</li>" for item in section['items']) + "</ul>"
    else:
        body = "<div class='grid-note'>" + ''.join(f"<article class='note'><h3>{a}</h3><p>{b}</p></article>" for a, b in section['items']) + "</div>"
    return f"<section class='section'>{title_html}{body}</section>"


def write_site():
    (root / 'assets' / 'styles.css').write_text(STYLE)
    (root / 'assets' / 'app.js').write_text(APP_JS)

    for route, page in PAGES.items():
        file_path = root / page['file']
        file_path.parent.mkdir(parents=True, exist_ok=True)
        prefix = prefix_for(page['file'])
        nav_html = ''.join(f"<a data-nav href='{to_href(prefix, href)}'>{label}</a>" for label, href in NAV)
        section_html = ''.join(render_section(section, prefix) for section in page['sections'])
        ctas = ''.join(
            f"<a class='btn {'primary' if i == 0 else ''}' href='{to_href(prefix, link)}'>{label}</a>"
            for i, (label, link) in enumerate(page['cta']) if label
        )
        html = f"""<!doctype html>
<html lang='zh-CN'>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0' />
  <title>{page['title']} · openclaw-summary</title>
  <meta name='description' content='{page['hero_desc']}' />
  <link rel='stylesheet' href='{prefix}assets/styles.css' />
</head>
<body>
  <header class='topbar'>
    <div class='shell topbar-inner'>
      <a class='brand' href='{to_href(prefix, '/')}'>OpenClaw 中文学习指南</a>
      <nav class='nav'>{nav_html}</nav>
    </div>
  </header>
  <main class='shell'>
    <section class='hero'>
      <span class='eyebrow'>{page['eyebrow']}</span>
      <div class='hero-grid'>
        <div class='panel hero-copy'>
          <h1>{page['hero_title']}</h1>
          <p>{page['hero_desc']}</p>
          <div class='badges'>
            <span class='badge'>中文学习站</span>
            <span class='badge'>可分享 URL</span>
            <span class='badge'>从入门到进阶</span>
          </div>
          <div class='cta-row'>{ctas}</div>
        </div>
        <aside class='panel hero-side'>
          <div class='kpi'><strong>{len(PAGES)}</strong><span>已覆盖 roadmap 中首页、入门、概念、配置、场景、进阶、FAQ 全部模块。</span></div>
          <div class='kpi'><strong>多页面</strong><span>每个重要主题都有独立 URL，方便分享与后续扩写。</span></div>
          <div class='kpi'><strong>分层阅读</strong><span>页面都遵循“短答案 → 解释 → 下一步”的学习节奏。</span></div>
        </aside>
      </div>
      <div class='pathline'>{page['summary']}</div>
    </section>
    {section_html}
  </main>
  <footer class='footer'>
    <div class='shell footer-box'>
      <strong>openclaw-summary v0.1</strong>
      <div>面向中文用户的 OpenClaw 学习站。已覆盖 roadmap 规划的主要页面骨架与首版内容层。</div>
    </div>
  </footer>
  <script src='{prefix}assets/app.js'></script>
</body>
</html>
"""
        file_path.write_text(html)

    readme = f"""# openclaw-summary-ver0.1

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
- 总页面数：{len(PAGES)}
- 模块：Home / Getting Started / Concepts / Setup / Use Cases / Advanced / FAQ
- 形式：纯静态多页面站点，便于继续升级到框架化实现
"""
    (root / 'README.md').write_text(readme)

    urls = []
    base = 'https://liu-feng-03.github.io/openclaw-summary-ver0.1'
    for route, page in sorted(PAGES.items()):
        if route == '/':
            urls.append(base + '/')
        else:
            urls.append(base + route)
    (root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    (root / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + base + '/sitemap.xml\n')
    (root / '404.html').write_text((root / 'index.html').read_text())


if __name__ == '__main__':
    write_site()
