from pathlib import Path
from typing import Optional

root = Path('/Users/columbina.hyposelenia/.openclaw/workspace/openclaw-summary-ver0.1')
(root / 'assets').mkdir(exist_ok=True)

pages = {
    '/': {
        'file': 'index.html',
        'title': 'OpenClaw 中文学习指南',
        'eyebrow': 'OpenClaw Summary',
        'hero_title': '一套更适合中文用户的 OpenClaw 学习路径',
        'hero_desc': '不是简单搬运文档，而是把 OpenClaw 从“看起来很强”整理成“真的能理解、能上手、能分享”的学习站。',
        'summary': '先理解，再上手，再深入。这个站点把 OpenClaw 拆成学习路径、核心概念、配置实践与常见问题。',
        'sections': [
            {'title': '你可以从这 4 个入口开始', 'type': 'cards', 'items': [
                ['我是新手，先看什么？', '先建立整体印象，再进入推荐学习路线。', '/getting-started/'],
                ['我想搞懂它的结构', '从架构、会话、网关、技能、工具、记忆开始。', '/concepts/'],
                ['我想尽快跑起来', '按步骤完成 requirements → install → config → gateway → first message。', '/setup/'],
                ['我只想知道它值不值得学', '它适合做私人助理、消息中台、自动化入口和开发协作界面。', '/use-cases/'],
            ]},
            {'title': '推荐学习路径', 'type': 'steps', 'items': [
                ['1. 先知道它是什么', '理解 OpenClaw 不是单一聊天框，而是一个带网关、会话、技能、工具与记忆层的系统。'],
                ['2. 建立系统心智模型', '优先读 architecture、session、gateway、skills、tools、memory。'],
                ['3. 完成一次最小成功', '按 setup 路线完成安装、配置、启动网关，并发出第一条消息。'],
                ['4. 再看进阶话题', '当你已经跑通后，再进入高级机制、最佳实践与 FAQ。'],
            ]},
            {'title': '核心模块', 'type': 'cards', 'items': [
                ['Getting Started', '给第一次接触 OpenClaw 的用户一条不迷路的路线。', '/getting-started/'],
                ['Core Concepts', '用关系图和结构化解释建立正确的系统理解。', '/concepts/'],
                ['Setup & Deployment', '把安装、配置、启动和首条消息拆成清晰步骤。', '/setup/'],
                ['Advanced Topics', '当你已经会用之后，继续理解策略、边界和设计思路。', '/advanced/'],
                ['FAQ', '快速定位常见问题，不用被日志和术语吓住。', '/faq/'],
            ]},
            {'title': '概念图预览', 'type': 'grid-note', 'items': [
                ['Gateway', '承接交互与服务入口'],
                ['Session', '承载上下文边界'],
                ['Skills', '决定如何做'],
                ['Tools', '决定能做什么'],
                ['Memory', '提供文件化连续性'],
                ['Dashboard', '帮助观察与操作系统'],
            ]},
            {'title': '继续深入', 'type': 'cards', 'items': [
                ['为什么 session 很关键？', '如果不理解上下文边界，就很容易误判行为。', '/advanced/session-model/'],
                ['为什么记忆设计不是越多越好？', '文件化连续性需要清晰层次与边界。', '/advanced/memory-design/'],
                ['为什么安全边界会影响体验？', '因为有些动作本来就应该留给人确认。', '/advanced/safety-boundaries/'],
                ['常见问题从哪里进？', '先看 setup / connectivity 两个 FAQ 入口。', '/faq/'],
            ]},
        ],
        'cta': [('开始学习', '/getting-started/'), ('查看配置路径', '/setup/')],
    },
}


def add_page(route, title, eyebrow, hero_title, hero_desc, summary, sections, cta=None):
    path = route.strip('/')
    file = 'index.html' if not path else f"{path}/index.html"
    pages[route] = {
        'file': file,
        'title': title,
        'eyebrow': eyebrow,
        'hero_title': hero_title,
        'hero_desc': hero_desc,
        'summary': summary,
        'sections': sections,
        'cta': cta or []
    }

# Wave 1
add_page('/getting-started/', 'Getting Started', 'Getting Started', '先别急着看一切，先按顺序理解 OpenClaw', '这一部分给新手一条低摩擦路线：先认识它，再知道怎么学，最后完成第一次成功。', '如果你是第一次接触 OpenClaw，先读这里会比直接冲文档轻松很多。', [
    {'title': '推荐起步顺序', 'type': 'steps', 'items': [
        ['先读 what is OpenClaw', '建立最基本的产品认知。'],
        ['再进入 concepts', '理解几个最核心的结构件。'],
        ['然后走 setup', '完成 requirements → install → configuration → gateway → first message。'],
    ]},
    {'title': '新手现在最需要知道的事', 'type': 'bullets', 'items': [
        'OpenClaw 更像一个可编排的助理系统，而不只是聊天界面。',
        '你不需要一开始就理解全部架构，但必须知道 session、gateway、skills、tools、memory 这几个词。',
        '第一次成功的目标不是“全懂”，而是“能启动、能互动、知道接下来去哪看”。',
    ]},
    {'title': '建议优先页面', 'type': 'cards', 'items': [
        ['什么是 OpenClaw', '最短路径理解它解决什么问题。', '/getting-started/what-is-openclaw/'],
        ['核心概念总览', '把系统拆成几个能看懂的模块。', '/concepts/'],
        ['安装与配置', '把最小可运行路径跑通。', '/setup/'],
    ]},
], [('什么是 OpenClaw', '/getting-started/what-is-openclaw/'), ('进入 Setup', '/setup/')])

add_page('/getting-started/what-is-openclaw/', '什么是 OpenClaw', 'Getting Started', 'OpenClaw 是一套可接入真实工具与渠道的 AI 助理系统', '它不是单纯在网页里和你聊天，而是让代理、会话、工具、技能、记忆和外部入口一起协作。', '先把它理解成“有结构、有边界、可操作”的助理平台，会比把它当成普通聊天机器人更接近真实。', [
    {'title': '一句话定义', 'type': 'bullets', 'items': ['OpenClaw 是一个让 AI 代理在真实消息渠道、工具系统与文件记忆上运行的助理框架。']},
    {'title': '它解决什么问题', 'type': 'bullets', 'items': [
        '让助理不只会回答，还能读取文件、调用工具、连接 Telegram / Discord / GitHub 等入口。',
        '把长期协作需要的“人格、规则、记忆、执行能力”放到可管理的结构里。',
        '让不同任务可以用不同 session、不同 skill、不同权限和不同工作流来处理。',
    ]},
    {'title': '它和普通聊天 UI 的区别', 'type': 'cards', 'items': [
        ['普通聊天 UI', '重点是对话本身，能力边界常常不透明。', None],
        ['OpenClaw', '重点是“对话 + 系统结构 + 工具执行 + 渠道接入 + 持续协作”。', None],
    ]},
    {'title': '下一步怎么读', 'type': 'cards', 'items': [
        ['想先理解结构', '去看 concepts 和 architecture。', '/concepts/'],
        ['想先跑起来', '直接进入 setup。', '/setup/'],
    ]},
], [('看架构', '/concepts/architecture/'), ('开始安装', '/setup/install/')])

add_page('/concepts/', '核心概念', 'Core Concepts', '先理解关系，再理解术语', 'OpenClaw 难的地方往往不是单个名词，而是这些部分是怎么一起工作的。', '这一页是概念系统入口，建议先看 architecture，再看 session / gateway / skills / tools / memory。', [
    {'title': '推荐阅读顺序', 'type': 'steps', 'items': [
        ['Architecture', '先知道系统里有哪些大部件。'],
        ['Session', '理解上下文与边界。'],
        ['Gateway', '理解运行与入口层。'],
        ['Skills / Tools', '理解“怎么做”与“能做什么”的分工。'],
        ['Memory', '理解连续性与文件边界。'],
    ]},
    {'title': '概念卡片', 'type': 'cards', 'items': [
        ['Architecture', '系统总览与消息/动作流转。', '/concepts/architecture/'],
        ['Session', '上下文容器与协作边界。', '/concepts/session/'],
        ['Gateway', '服务层、控制面与远程接入入口。', '/concepts/gateway/'],
        ['Skills', '指导行为、规范工具使用的说明层。', '/concepts/skills/'],
        ['Tools', '真正执行动作的能力接口。', '/concepts/tools/'],
        ['Memory', '把连续性写入文件，而不是幻想模型“记住一切”。', '/concepts/memory/'],
    ]},
], [('看架构总览', '/concepts/architecture/'), ('看 Session', '/concepts/session/')])

add_page('/concepts/architecture/', '系统架构', 'Core Concepts', 'OpenClaw 是由入口、会话、能力层和持久化层组成的系统', '最实用的理解方式不是背定义，而是看消息怎么进来、上下文怎么积累、工具怎么被调用、结果怎么回去。', '把架构看懂后，后面的 gateway、session、skills、tools、memory 就不再像零散术语。', [
    {'title': '主要构件', 'type': 'bullets', 'items': [
        'Gateway：承接运行、连接与服务入口。',
        'Session：承载当前上下文与边界。',
        'Agent instructions / persona：定义这个助理怎么说、怎么做。',
        'Skills：在特定任务里注入更细的行为规则。',
        'Tools：真正执行读文件、发请求、调用服务等动作。',
        'Memory files：提供跨会话连续性与长期记录。',
    ]},
    {'title': '一条典型流转', 'type': 'steps', 'items': [
        ['消息进入系统', '来自 Telegram、Discord、Dashboard 或其他入口。'],
        ['系统选择当前 session', '决定沿用哪些上下文与规则。'],
        ['模型结合 instructions / skills 规划动作', '判断是直接回答，还是需要读文件 / 调工具。'],
        ['调用 tools 执行', '读取、搜索、写入、查询、发送。'],
        ['把结果回传', '输出给当前用户或目标渠道。'],
    ]},
    {'title': '为什么它比名词列表更重要', 'type': 'bullets', 'items': [
        '因为很多问题本质上都是“结构关系没搞清”。',
        '比如权限、行为边界、记忆位置、远程连接、日志现象，最终都能回到架构层解释。',
    ]},
], [('看 Session', '/concepts/session/'), ('看 Gateway', '/concepts/gateway/')])

add_page('/concepts/session/', 'Session', 'Core Concepts', 'Session 是 OpenClaw 里最重要的上下文边界之一', '你可以把它理解成“某一段持续协作的工作容器”，里面会积累对话、工具使用痕迹、任务上下文和状态。', '很多“为什么它这样回答”“为什么上下文变多了”“为什么要开新线程”之类的问题，都和 session 有关。', [
    {'title': 'Session 是什么', 'type': 'bullets', 'items': [
        '它不是单纯的聊天窗口，而是一次持续协作的上下文单元。',
        '它决定模型当前能看到哪些历史信息，也影响后续动作和成本。',
    ]},
    {'title': '为什么 session 边界很重要', 'type': 'bullets', 'items': [
        '上下文越长，不代表越聪明；很多时候只会更重、更慢、更乱。',
        '产品讨论、代码实现、复杂诊断拆到不同 session，通常更稳定。',
        '不同人、不同渠道、不同任务也应有不同边界，避免信息串味。',
    ]},
    {'title': '常见误解', 'type': 'cards', 'items': [
        ['误解：开新 session 会“失忆”', '实际上重要内容应该写入文件记忆，而不是强行塞在上下文里。', None],
        ['误解：所有事都堆一个 session 最方便', '短期省事，长期通常更糟。', None],
    ]},
], [('看 Gateway', '/concepts/gateway/'), ('看 Memory', '/concepts/memory/')])

add_page('/concepts/gateway/', 'Gateway', 'Core Concepts', 'Gateway 是 OpenClaw 的运行与连接核心层', '如果把 OpenClaw 看成一个可工作的助理系统，那么 gateway 更像承载它对外服务、控制面与部分连接能力的基础设施。', '很多用户真正“操作 OpenClaw”的感觉，都是通过 gateway 体现出来的。', [
    {'title': 'Gateway 主要负责什么', 'type': 'bullets', 'items': [
        '提供系统服务入口。',
        '支撑 Dashboard / Control UI 等操作界面。',
        '承接部分远程访问、连接状态与服务健康检查。',
        '成为很多日志、连接问题和运行状态观察的中心。',
    ]},
    {'title': '为什么新手必须理解它', 'type': 'bullets', 'items': [
        '因为“装好了但为什么没跑起来”的问题，很多都落在 gateway 层。',
        '启动、状态、连接、token、远程访问、回退行为，都会和 gateway 直接相关。',
    ]},
    {'title': '你通常会在哪些场景遇到它', 'type': 'cards', 'items': [
        ['启动服务', '确认网关是否已正常运行。', '/setup/start-gateway/'],
        ['连接控制界面', '通过 dashboard / control UI 观察与操作。', '/faq/connectivity/'],
        ['排查 ws / http 行为', '理解某些连接链路为何会 fallback。', '/faq/'],
    ]},
], [('看 Setup', '/setup/'), ('查看启动网关', '/setup/start-gateway/')])

add_page('/concepts/skills/', 'Skills', 'Core Concepts', 'Skill 决定“在某类任务里，助理应该怎样做”', '它更像可按需加载的专业操作说明，而不是底层执行器。', '如果把 OpenClaw 比作一个团队，skill 更像 SOP、工作手册或岗位剧本。', [
    {'title': 'Skill 不是什么', 'type': 'bullets', 'items': [
        '它不是模型本身。',
        '它不是 tool，也不是直接执行命令的接口。',
        '它不是无限长的万能提示词堆。',
    ]},
    {'title': 'Skill 真正做的事', 'type': 'bullets', 'items': [
        '告诉助理什么时候该用哪套规则。',
        '约束输出方式、执行顺序和注意事项。',
        '把某类任务的专业做法封装成可复用行为。',
    ]},
    {'title': '和 Tool 的区别', 'type': 'cards', 'items': [
        ['Skill', '说明“怎么做更对”。', '/concepts/skills/'],
        ['Tool', '提供“实际能做什么”。', '/concepts/tools/'],
    ]},
], [('看 Tools', '/concepts/tools/'), ('看 Setup', '/setup/')])

add_page('/concepts/tools/', 'Tools', 'Core Concepts', 'Tool 是 OpenClaw 真正把动作落到系统上的能力接口', '读文件、写文件、搜网页、发消息、起子代理……这些都属于 tools 的范畴。', '没有 tool，再聪明的说明也只能停留在“会说但做不了”。', [
    {'title': 'Tool 的核心意义', 'type': 'bullets', 'items': [
        '把模型从“文本回答者”扩展成“可执行助理”。',
        '让系统可以访问文件、网络、服务和外部能力。',
        '把行动留痕并放在可观察、可约束的边界里。',
    ]},
    {'title': '为什么 tool 和普通函数思维不完全一样', 'type': 'bullets', 'items': [
        '因为工具调用常常伴随权限、审批、执行环境与风险控制。',
        '用户看到的不只是“有没有这个功能”，还包括“什么时候允许用、怎么用更安全”。',
    ]},
    {'title': '新手需要记住的区分', 'type': 'cards', 'items': [
        ['Model', '负责理解和规划。', None],
        ['Skill', '负责行为规则和任务套路。', '/concepts/skills/'],
        ['Tool', '负责真正执行。', '/concepts/tools/'],
    ]},
], [('看 Skills', '/concepts/skills/'), ('看 Memory', '/concepts/memory/')])

add_page('/concepts/memory/', 'Memory', 'Core Concepts', 'OpenClaw 的“记忆”更接近文件化连续性，而不是神秘的永久脑内记忆', '它强调把重要信息写进文件、分层保存，再在需要时检索。', '这比幻想模型天然长期记住一切更可靠，也更适合真实协作。', [
    {'title': '要先建立的正确直觉', 'type': 'bullets', 'items': [
        '会话上下文是短期的，会变长、会切换、也会被重置。',
        '真正值得保留的信息，应写入 memory/YYYY-MM-DD.md 或 MEMORY.md 之类的文件。',
        '记忆不是越多越好，而是越有结构越好。',
    ]},
    {'title': '为什么文件记忆很重要', 'type': 'bullets', 'items': [
        '它能跨 session 保持连续性。',
        '它更容易审计、编辑、纠正和清理。',
        '它天然支持安全边界：什么能长期保留，什么不该泄露。',
    ]},
    {'title': '常见边界', 'type': 'cards', 'items': [
        ['Daily memory', '适合记录最近发生的事与临时上下文。', None],
        ['Long-term memory', '适合保留稳定偏好、长期决策与重要背景。', None],
        ['不要做的事', '别把所有细枝末节都塞进去，最后只会变成垃圾堆。', None],
    ]},
], [('看 Setup', '/setup/'), ('看 Advanced: Memory Design', '/advanced/memory-design/')])

add_page('/setup/', 'Setup & Deployment', 'Setup', '把第一次安装和启动拆成一条可验证的路径', '新手最容易卡住的地方不是不会点按钮，而是不知道现在该验证什么、下一步去哪。', '这部分把 setup 按顺序拆开，每一页都强调“目标、动作、成功信号、常见问题”。', [
    {'title': '推荐顺序', 'type': 'steps', 'items': [
        ['Requirements', '先确认环境是否满足最低条件。'],
        ['Install', '完成安装并确认命令可用。'],
        ['Configuration', '配置必须项，别一上来全改。'],
        ['Start Gateway', '启动服务并检查健康状态。'],
        ['First Message', '完成第一条成功交互。'],
    ]},
    {'title': 'Setup 的核心原则', 'type': 'bullets', 'items': [
        '按顺序走，不要跳步。',
        '每一步都要看成功信号。',
        '遇到问题先判断是安装、配置、启动还是连接层。',
    ]},
], [('看 Requirements', '/setup/requirements/'), ('看 Install', '/setup/install/')])

add_page('/setup/requirements/', '环境要求', 'Setup', '先确认环境，再开始安装', '很多“安装失败”其实不是安装命令错了，而是系统、运行时、权限或依赖前提没满足。', '这一步的价值不是复杂，而是避免你后面浪费时间。', [
    {'title': '你至少要确认什么', 'type': 'bullets', 'items': [
        '操作系统与基本运行环境是否受支持。',
        'Node / 包管理器 / 终端权限是否正常。',
        '你是否能访问后续需要的模型/API/网络资源。',
        '如果要用 Dashboard、消息平台或外部集成，相关入口条件是否满足。',
    ]},
    {'title': '成功信号', 'type': 'bullets', 'items': [
        '运行环境版本明确。',
        '终端可正常执行基础命令。',
        '没有明显的权限或网络阻断前提。',
    ]},
], [('继续安装', '/setup/install/')])

add_page('/setup/install/', '安装', 'Setup', '安装阶段的目标只有一个：把 OpenClaw 正确装上，而不是顺手把所有高级玩法一起搞完', '先完成最小安装，再进入配置与启动，会比一口气全冲更稳。', '如果你已经习惯开发环境，也建议先按最小可运行路径验证。', [
    {'title': '安装时的建议节奏', 'type': 'steps', 'items': [
        ['执行安装', '按官方方式安装 OpenClaw。'],
        ['确认命令存在', '比如先看 help 或基础状态命令。'],
        ['不要过早扩展', '先别急着做高级配置、远程接入或复杂集成。'],
    ]},
    {'title': '常见坑', 'type': 'bullets', 'items': [
        '把安装问题和配置问题混在一起。',
        '命令装上了，但 PATH / shell 环境没刷新。',
        '一开始就同时处理多套外部集成，导致定位困难。',
    ]},
], [('看 Configuration', '/setup/configuration/'), ('看 Requirements', '/setup/requirements/')])

add_page('/setup/configuration/', '配置', 'Setup', '配置不是“把所有选项都填满”，而是先把最关键的行为开关对齐', '新手最常见的问题，是把配置想成一次性大工程。其实首轮只需要完成能支撑第一次成功的必要项。', '理解哪些是必须项、哪些可以后补，会让 setup 难度大幅下降。', [
    {'title': '首轮最关心的配置问题', 'type': 'bullets', 'items': [
        '默认模型与可用提供商是否设置好。',
        '网关相关配置是否能支撑本地启动与控制界面。',
        '需要的基础渠道或插件是否已最小化启用。',
        '工作目录、技能、记忆文件结构是否符合预期。',
    ]},
    {'title': '不要一上来就做的事', 'type': 'bullets', 'items': [
        '同时开启一堆还不会用的外部接入。',
        '在没验证基础链路前就做复杂远程访问配置。',
        '看到所有字段就想一次配置到“完美状态”。',
    ]},
    {'title': '成功信号', 'type': 'bullets', 'items': [
        '能解释当前最小配置为什么足够。',
        '知道下一步应该去启动 gateway，而不是继续盲改配置。',
    ]},
], [('启动 Gateway', '/setup/start-gateway/'), ('完成第一条消息', '/setup/first-message/')])

add_page('/setup/start-gateway/', '启动 Gateway', 'Setup', '启动网关的目标不是看到一串日志，而是确认系统已经进入健康可交互状态', '你需要知道“正常启动长什么样”，这样遇到异常时才不会被无意义日志吓到。', '很多体验好不好，取决于你是否会验证 gateway 状态。', [
    {'title': '你要验证的不是“有没有输出”', 'type': 'bullets', 'items': [
        '而是 gateway 是否成功启动。',
        '状态检查是否正常。',
        '控制界面 / 连接入口是否能工作。',
    ]},
    {'title': '健康启动的直觉', 'type': 'bullets', 'items': [
        '服务命令能正常启动。',
        '状态命令能给出清晰结果。',
        '如果有 dashboard / control UI，它应能连上当前运行中的 gateway。',
    ]},
    {'title': '遇到异常时优先判断哪一层', 'type': 'steps', 'items': [
        ['启动失败', '先看环境与配置。'],
        ['界面连不上', '优先看 gateway 与 token / 连接配置。'],
        ['日志有 warning', '先判断是否只是可容忍回退，而不是致命故障。'],
    ]},
], [('完成 First Message', '/setup/first-message/'), ('看 Troubleshooting', '/setup/troubleshooting/')])

add_page('/setup/first-message/', '第一条消息', 'Setup', '第一次成功不是“看懂全部”，而是完成一次真实可验证的交互', '只要你能在目标入口和 OpenClaw 正常互动，并确认背后的链路是通的，这次 setup 就算过了第一关。', '接下来再逐步补概念和高级能力，会轻松很多。', [
    {'title': '第一次成功应包含什么', 'type': 'bullets', 'items': [
        '你知道消息从哪里发出。',
        '你知道系统在哪里响应。',
        '你能判断这不是假象，而是真正完成了一次可用交互。',
    ]},
    {'title': '建议验证项', 'type': 'steps', 'items': [
        ['发出一条简单请求', '例如让系统回答一个基础问题。'],
        ['确认响应回来', '并确认不是卡在 gateway / UI / token 层。'],
        ['观察最小运行闭环', '知道这条消息经历了入口、session、模型、工具（如有）和返回。'],
    ]},
    {'title': '跑通后该去哪', 'type': 'cards', 'items': [
        ['补核心概念', '把刚才体验到的东西和 architecture / session / gateway 对上。', '/concepts/'],
        ['查看常见问题', '提前建立对 setup / connectivity 问题的判断。', '/faq/'],
        ['进入高级主题', '理解长期协作、记忆设计与安全边界。', '/advanced/'],
    ]},
], [('看 FAQ', '/faq/'), ('看 Advanced', '/advanced/')])

add_page('/setup/troubleshooting/', 'Setup Troubleshooting', 'Setup', '当 setup 卡住时，先判断你卡在第几层，而不是直接怀疑整个系统坏了', '排错的关键不是看更多日志，而是把问题缩到 requirements、install、configuration、gateway、first message 其中一层。', '这一页作为 Wave 1.5 过渡页，先帮助你建立最小排错路径，后续再扩成更完整的 troubleshooting 页面。', [
    {'title': '最小排查顺序', 'type': 'steps', 'items': [
        ['看 requirements', '先确认是不是环境前提没满足。'],
        ['看 install', '确认安装本身是否真的成功。'],
        ['看 configuration', '必要配置是否已经对齐。'],
        ['看 gateway', '服务是否健康运行。'],
        ['看 first message', '问题到底发生在入口、连接还是响应链路。'],
    ]},
    {'title': '排错时最常见的坏习惯', 'type': 'bullets', 'items': [
        '还没分层，就开始贴一大堆混杂日志。',
        '把安装、配置、连接问题统称成“OpenClaw 不工作”。',
        '没有先确认成功信号，就直接改一堆配置。',
    ]},
], [('看 Setup FAQ', '/faq/setup/'), ('回到 Setup 首页', '/setup/')])

# linked Wave 2 pages
add_page('/use-cases/', 'Use Cases', 'Use Cases', 'OpenClaw 真正有趣的地方，在于它不是只能“聊”', '它可以作为私人助理、消息中台、自动化入口、文件协作层和开发辅助系统。', '这一部分用场景而不是术语来帮助你理解它为什么有价值。', [
    {'title': '场景入口', 'type': 'cards', 'items': [
        ['Personal Assistant', '日程、提醒、信息整理与生活协作。', '/use-cases/personal-assistant/'],
        ['Messaging Platforms', '把助理放进 Telegram、Discord 等消息环境。', '/use-cases/messaging-platforms/'],
    ]},
], [('看私人助理', '/use-cases/personal-assistant/')])
add_page('/use-cases/personal-assistant/', '私人助理场景', 'Use Cases', '把 OpenClaw 当成私人助理时，重点不是“会聊天”，而是“会协作”', '它的价值在于可以结合渠道、工具、记忆与规则，把长期支持做得更稳定。', '这也是很多人第一次真正感觉 OpenClaw 和普通聊天产品不一样的地方。', [
    {'title': '典型能力', 'type': 'bullets', 'items': [
        '在聊天渠道里直接沟通。', '读取和整理本地文件。', '连接日历、邮件、提醒、笔记等真实工具。', '通过记忆文件保持长期偏好和协作连续性。'
    ]},
], [('回到 Use Cases', '/use-cases/')])
add_page('/use-cases/messaging-platforms/', '消息平台场景', 'Use Cases', 'Telegram、Discord、Signal 这类入口让 OpenClaw 从“本地工具”变成“能随手叫到的助理”', '消息平台不是装饰，而是很多真实使用场景的主入口。', '理解这类接入的意义，也有助于理解 gateway、session 和远程可达性。', [
    {'title': '为什么消息平台很关键', 'type': 'bullets', 'items': [
        '它让助理进入用户原本就在使用的环境。', '它天然支持多轮协作与低摩擦触达。', '它会把权限、边界、群聊行为这些问题带到真实世界。'
    ]},
], [('回到 Use Cases', '/use-cases/')])
add_page('/advanced/', 'Advanced Topics', 'Advanced', '当你已经能用 OpenClaw，下一步就该理解为什么有些设计必须这么做', '高级主题不是为了炫技，而是帮助你做出更稳、更清晰、更省成本的使用与架构决策。', '如果你已经跑通过第一次成功，这部分会开始变得非常有价值。', [
    {'title': '推荐先读', 'type': 'cards', 'items': [
        ['Session Model', '为什么上下文边界会影响质量、成本与稳定性。', '/advanced/session-model/'],
        ['Memory Design', '为什么记忆需要分层与治理。', '/advanced/memory-design/'],
        ['Safety Boundaries', '为什么有些动作必须确认。', '/advanced/safety-boundaries/'],
        ['Best Practices', '把经验沉淀成日常可执行规则。', '/advanced/best-practices/'],
    ]},
], [('看 Session Model', '/advanced/session-model/')])
add_page('/advanced/session-model/', 'Session Model', 'Advanced', 'Session 设计会直接影响体验、成本和可维护性', '如果你把所有事都堆在一个超长会话里，通常只会越来越慢、越来越糊。', '理解 session model，本质上是在理解“如何给协作切边界”。', [
    {'title': '为什么重要', 'type': 'bullets', 'items': ['影响上下文质量与 token 成本。', '影响任务拆分与长期协作稳定性。', '影响不同人、不同渠道、不同工作流是否会互相污染。']},
], [('看 Memory Design', '/advanced/memory-design/')])
add_page('/advanced/memory-design/', 'Memory Design', 'Advanced', '记忆设计不是让系统记更多，而是让重要信息以合适的层次留下来', '好的记忆设计会让协作越来越顺；糟糕的记忆设计会让系统越来越臃肿、越来越危险。', '这页关注的是“写什么、写到哪、什么时候读、什么时候清”。', [
    {'title': '核心原则', 'type': 'bullets', 'items': ['把稳定偏好和长期决策沉淀到长期记忆。', '把临时上下文记录到日记式记忆。', '不要把敏感或无关信息无差别长期保留。']},
], [('看 Safety Boundaries', '/advanced/safety-boundaries/')])
add_page('/advanced/safety-boundaries/', 'Safety Boundaries', 'Advanced', '一个真的能做事的助理，必须同时有能力边界与审批边界', '否则它越强，就越容易在错误的场景里做出错误动作。', '安全边界不是妨碍体验，而是在保护真实世界里的用户。', [
    {'title': '常见边界类型', 'type': 'bullets', 'items': ['外发动作需要确认。', '高风险命令需要审批。', '群聊与私聊的隐私边界不同。', '记忆、文件与工具访问都应该有范围。']},
], [('看 Best Practices', '/advanced/best-practices/')])
add_page('/advanced/best-practices/', 'Best Practices', 'Advanced', '真正让 OpenClaw 好用的，常常不是某个神奇功能，而是一组稳定的小习惯', '例如把不同任务拆 session、把重要信息写文件、不要被 benign log 噪音吓到、逐步扩展配置。', '这页是把实践经验浓缩成行动建议。', [
    {'title': '建议', 'type': 'bullets', 'items': ['先跑通最小成功，再扩展。', '先理解结构，再追高级玩法。', '把重要连续性写文件。', '把复杂任务拆开处理。']},
], [('看 FAQ', '/faq/')])
add_page('/faq/', 'FAQ', 'FAQ', '先别慌，很多“看起来像故障”的东西其实是常见现象', 'FAQ 的作用不是替代完整文档，而是帮你快速判断：这是不是已知常见问题、该先看哪一层。', '对新手来说，FAQ 能显著降低被术语和日志吓退的概率。', [
    {'title': '优先入口', 'type': 'cards', 'items': [
        ['Setup FAQ', '安装、配置、启动、首条消息相关问题。', '/faq/setup/'],
        ['Connectivity FAQ', '连接、token、访问与控制界面相关问题。', '/faq/connectivity/'],
    ]},
], [('看 Setup FAQ', '/faq/setup/')])
add_page('/faq/setup/', 'FAQ · Setup', 'FAQ', '很多 setup 问题本质上不是“系统坏了”，而是顺序错了、前提没确认或成功信号没看懂', '先按层判断 requirements / install / configuration / gateway / first message，通常会快很多。', '别把所有问题都打成“安装失败”四个字，那样最难排。', [
    {'title': '优先排查顺序', 'type': 'steps', 'items': [
        ['Requirements', '环境前提是否满足？'], ['Install', '命令和安装是否真的成功？'], ['Configuration', '必要配置是否对齐？'], ['Gateway', '服务是否健康启动？'], ['First Message', '问题是在入口层还是运行层？']
    ]},
], [('看 Connectivity FAQ', '/faq/connectivity/')])
add_page('/faq/connectivity/', 'FAQ · Connectivity', 'FAQ', '连不上，不一定是“整个系统坏了”', '很多连接问题其实集中在 gateway 状态、访问入口、token 不一致、控制界面缓存或远程可达性配置。', '只要分层判断，通常很快能把问题缩小。', [
    {'title': '优先怀疑什么', 'type': 'bullets', 'items': ['Gateway 是否真的在运行。', '当前 UI / 控制面拿到的 token 是否正确。', '是不是旧页面缓存了过期状态。', '远程访问路径是否与当前配置一致。']},
], [('回到 FAQ', '/faq/')])

nav = [
    ('首页', '/'), ('入门', '/getting-started/'), ('概念', '/concepts/'), ('配置', '/setup/'), ('场景', '/use-cases/'), ('进阶', '/advanced/'), ('FAQ', '/faq/'),
]

style = """
:root {
  --bg: #08111f;
  --panel: rgba(14, 25, 46, 0.82);
  --text: #ecf3ff;
  --muted: #9db0d1;
  --line: rgba(157, 176, 209, 0.18);
  --accent: #78d7ff;
  --accent-2: #8c7bff;
  --shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
  --radius: 24px;
  --radius-sm: 18px;
  --content: 1180px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; color: var(--text); background: radial-gradient(circle at top, rgba(120, 215, 255, 0.14), transparent 35%), radial-gradient(circle at 85% 15%, rgba(140, 123, 255, 0.16), transparent 28%), linear-gradient(180deg, #07101d 0%, #091526 100%); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.65; }
a { color: inherit; text-decoration: none; }
.shell { width: min(calc(100% - 32px), var(--content)); margin: 0 auto; }
.topbar { position: sticky; top: 0; z-index: 20; backdrop-filter: blur(18px); background: rgba(8, 17, 31, 0.72); border-bottom: 1px solid var(--line); }
.topbar-inner { display:flex; align-items:center; justify-content:space-between; gap:20px; padding: 16px 0; }
.brand { font-weight: 700; letter-spacing: .02em; }
.nav { display:flex; gap: 10px; flex-wrap: wrap; }
.nav a { padding: 10px 14px; border-radius: 999px; color: var(--muted); border: 1px solid transparent; }
.nav a.active, .nav a:hover { color: var(--text); border-color: var(--line); background: rgba(255,255,255,.03); }
.hero { padding: 56px 0 24px; }
.eyebrow { display:inline-flex; align-items:center; gap:8px; padding: 8px 12px; border-radius:999px; border:1px solid var(--line); color: var(--accent); font-size: 14px; background: rgba(120,215,255,.06); }
.hero-grid { display:grid; grid-template-columns: 1.35fr .85fr; gap: 24px; margin-top: 18px; }
.panel { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); }
.hero-copy { padding: 34px; }
.hero-copy h1 { font-size: clamp(34px, 5vw, 56px); line-height: 1.08; margin: 0 0 18px; }
.hero-copy p { margin: 0; color: var(--muted); font-size: 18px; }
.hero-side { padding: 24px; display:flex; flex-direction:column; gap: 16px; }
.kpi { padding: 18px; border-radius: var(--radius-sm); background: rgba(255,255,255,.03); border:1px solid var(--line); }
.kpi strong { display:block; font-size: 28px; margin-bottom: 6px; }
.cta-row { display:flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.btn { display:inline-flex; align-items:center; justify-content:center; gap:8px; padding: 12px 18px; border-radius: 999px; border:1px solid var(--line); }
.btn.primary { background: linear-gradient(135deg, var(--accent), #9ae6ff); color: #08111f; border-color: transparent; font-weight: 700; }
.section { padding: 18px 0; }
.section-head { margin-bottom: 14px; }
.section-head h2 { margin: 0 0 8px; font-size: clamp(24px, 4vw, 34px); }
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
@media (max-width: 900px) { .hero-grid, .cards, .grid-note { grid-template-columns: 1fr; } .topbar-inner { flex-direction: column; align-items:flex-start; } }
"""
(root / 'assets' / 'styles.css').write_text(style)
(root / 'assets' / 'app.js').write_text("const currentPath = window.location.pathname.replace(/index\\.html$/, '/');document.querySelectorAll('[data-nav]').forEach((link)=>{const href=link.getAttribute('href');const abs=new URL(href, window.location.href).pathname.replace(/index\\.html$/, '/');if(abs===currentPath||(abs!=='/'&&currentPath.startsWith(abs))){link.classList.add('active');}});")


def prefix_for(file_path: str) -> str:
    if file_path == 'index.html':
        return './'
    depth = len(Path(file_path).parts) - 1
    return '../' * depth


def to_href(prefix: str, link: Optional[str]) -> Optional[str]:
    if link is None:
        return None
    if link == '/':
        return prefix
    return prefix + link.lstrip('/')

for route, page in pages.items():
    file_path = root / page['file']
    file_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = prefix_for(page['file'])
    nav_html = ''.join(f"<a data-nav href='{to_href(prefix, href)}'>{label}</a>" for label, href in nav)
    section_html = []
    for section in page['sections']:
        body = ''
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
        elif section['type'] == 'grid-note':
            body = "<div class='grid-note'>" + ''.join(f"<article class='note'><h3>{title}</h3><p>{desc}</p></article>" for title, desc in section['items']) + "</div>"
        section_html.append(f"<section class='section'><div class='section-head'><h2>{section['title']}</h2></div>{body}</section>")

    ctas = ''.join(
        f"<a class='btn {'primary' if i == 0 else ''}' href='{to_href(prefix, link)}'>{label}</a>"
        for i, (label, link) in enumerate(page['cta'])
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
          <div class='cta-row'>{ctas}</div>
        </div>
        <aside class='panel hero-side'>
          <div class='kpi'><strong>Wave 1</strong><span>当前优先覆盖理解 → 配置 → 首次成功闭环。</span></div>
          <div class='kpi'><strong>多页面</strong><span>每个重要主题都有独立 URL，便于分享与扩展。</span></div>
          <div class='kpi'><strong>分层阅读</strong><span>所有页面都遵循“短答案 → 解释 → 下一步”的节奏。</span></div>
        </aside>
      </div>
      <div class='pathline'>{page['summary']}</div>
    </section>
    {''.join(section_html)}
  </main>
  <footer class='footer'>
    <div class='shell footer-box'>
      <strong>openclaw-summary v0.1</strong>
      <div>面向中文用户的 OpenClaw 学习站。当前优先完成 Wave 1 骨架，后续继续补齐 Wave 2 / Wave 3 页面与内容深度。</div>
    </div>
  </footer>
  <script src='{prefix}assets/app.js'></script>
</body>
</html>
"""
    file_path.write_text(html)

readme = """# openclaw-summary-ver0.1

一个面向中文用户的 OpenClaw 学习站原型。

## 当前状态
- 已根据 `ROADMAP.md` 与 `PHASE1_CONTENT_MATRIX.md` 落地 Wave 1 多页面静态骨架
- 已补齐首页、Getting Started、Core Concepts、Setup，以及基础的 Use Cases / Advanced / FAQ 入口页
- 当前实现为可直接本地打开的静态站点，便于快速迭代页面结构与文案

## 已实现页面
- `/`
- `/getting-started`
- `/getting-started/what-is-openclaw`
- `/concepts`
- `/concepts/architecture`
- `/concepts/session`
- `/concepts/gateway`
- `/concepts/skills`
- `/concepts/tools`
- `/concepts/memory`
- `/setup`
- `/setup/requirements`
- `/setup/install`
- `/setup/configuration`
- `/setup/start-gateway`
- `/setup/first-message`

并补充了基础入口页：
- `/use-cases`
- `/use-cases/personal-assistant`
- `/use-cases/messaging-platforms`
- `/advanced`
- `/advanced/session-model`
- `/advanced/memory-design`
- `/advanced/safety-boundaries`
- `/advanced/best-practices`
- `/faq`
- `/faq/setup`
- `/faq/connectivity`

## 本地预览
直接打开 `index.html`，或在仓库目录启动一个静态文件服务器。
"""
(root / 'README.md').write_text(readme)
