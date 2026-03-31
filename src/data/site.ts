export type ModuleKey = 'getting-started' | 'concepts' | 'setup' | 'faq' | 'use-cases' | 'advanced';

export type Difficulty = '入门' | '基础' | '进阶';
export type CompletionLevel = 'full' | 'standard' | 'transitional';
export type PageType = 'overview' | 'detail';

export type NavItem = {
  title: string;
  description: string;
  href: string;
};

export type TopicSection = {
  title: string;
  body: string[];
};

export type Topic = {
  slug: string;
  module: ModuleKey;
  title: string;
  navTitle?: string;
  summary: string;
  purpose: string;
  whyItMatters: string;
  audience: string;
  difficulty: Difficulty;
  readingTime: string;
  tags: string[];
  prerequisites?: string[];
  related?: string[];
  next?: string;
  completion: CompletionLevel;
  group?: string;
  quickAnswer: string;
  misunderstandings?: string[];
  sections: TopicSection[];
};

export type ModuleSection = {
  title: string;
  description: string;
  topics: string[];
};

export type ModuleDef = {
  key: ModuleKey;
  title: string;
  shortTitle: string;
  tagline: string;
  description: string;
  accent: string;
  tone: string;
  routeLabel: string;
  startHere: string;
  explorerLabel: string;
  pageTypeLabel: string;
  moduleMode: string;
  overviewSummary: string;
  quickPathTitle: string;
  quickPaths: NavItem[];
  bridge: NavItem[];
  sections: ModuleSection[];
};

const t = (
  module: ModuleKey,
  slug: string,
  title: string,
  summary: string,
  purpose: string,
  whyItMatters: string,
  audience: string,
  difficulty: Difficulty,
  readingTime: string,
  tags: string[],
  quickAnswer: string,
  sections: TopicSection[],
  extras: Partial<Omit<Topic, 'module' | 'slug' | 'title' | 'summary' | 'purpose' | 'whyItMatters' | 'audience' | 'difficulty' | 'readingTime' | 'tags' | 'quickAnswer' | 'sections'>> = {}
): Topic => ({
  module,
  slug,
  title,
  summary,
  purpose,
  whyItMatters,
  audience,
  difficulty,
  readingTime,
  tags,
  quickAnswer,
  sections,
  completion: 'standard',
  ...extras
});

export const modules: ModuleDef[] = [
  {
    key: 'getting-started',
    title: '入门引导',
    shortTitle: 'Getting Started',
    tagline: '先给新手一条能走通的学习入口，而不是一张吓人的目录。',
    description: '把第一次接触 OpenClaw 的用户从“这是什么”带到“我知道接下来要看什么”。',
    accent: 'var(--accent-green)',
    tone: 'rgba(93,214,179,.18)',
    routeLabel: '适合第一次接触 OpenClaw 的用户',
    startHere: '先看「什么是 OpenClaw」→ 再看「如何学习」→ 再进入 Setup 最小成功路径。',
    explorerLabel: '新手路径',
    pageTypeLabel: 'Onboarding Hub',
    moduleMode: '按路径、按时间、按结果带你起步。',
    overviewSummary: '这里不是知识堆料区，而是新手路径面板：告诉你该先建立什么预期、哪些内容能暂时跳过、怎样最快进入第一次成功。',
    quickPathTitle: '如果你只有 10 分钟',
    quickPaths: [
      { title: '5 分钟搞懂 OpenClaw', description: '先建立正确预期，再决定要不要继续投入。', href: '/getting-started/what-is-openclaw' },
      { title: '直接看推荐学习路径', description: '知道第一轮该读什么、不该急着读什么。', href: '/getting-started/how-to-learn' }
    ],
    bridge: [
      { title: '接着去 Concepts', description: '当你想把“会用”升级为“会理解”。', href: '/concepts' },
      { title: '接着去 Setup', description: '当你已经准备好开始部署。', href: '/setup' }
    ],
    sections: [
      { title: '第一轮必看', description: '先建立方向感。', topics: ['what-is-openclaw', 'how-to-learn', 'first-roadmap'] }
    ]
  },
  {
    key: 'concepts',
    title: '核心概念',
    shortTitle: 'Concepts',
    tagline: '重点不是背定义，而是看清关系、边界和协作方式。',
    description: '通过关系分组解释 agent、session、gateway、skills、tools、memory 等核心机制。',
    accent: 'var(--accent-blue)',
    tone: 'rgba(106,183,255,.16)',
    routeLabel: '适合想建立系统心智模型的用户',
    startHere: '先看「整体架构」，再沿着 运行上下文 / 能力系统 / 接入表面 三条枝干继续。',
    explorerLabel: '概念地图',
    pageTypeLabel: 'Relation Hub',
    moduleMode: '按关系分组浏览，不再是纯平列表。',
    overviewSummary: '这个模块强调“概念与概念之间怎么连起来”。你可以顺着整体架构读，也可以按运行上下文、接入层、能力系统三条线横向理解。',
    quickPathTitle: '如果你只看一页',
    quickPaths: [
      { title: '先看整体架构', description: '它是 Concepts 模块最关键的总入口。', href: '/concepts/architecture' },
      { title: '从 Session 开始补心智模型', description: '很多理解偏差都从 session 开始。', href: '/concepts/session' }
    ],
    bridge: [
      { title: '去 Setup', description: '理解结构后，最自然的下一步就是把系统跑起来。', href: '/setup' },
      { title: '去 FAQ', description: '如果你已经卡住，先排错往往比继续读更值。', href: '/faq' }
    ],
    sections: [
      { title: '全局与运行上下文', description: '先理解系统怎么组织一次交互。', topics: ['architecture', 'agent', 'session', 'subagents', 'heartbeat-cron'] },
      { title: '接入与运行层', description: '理解入口、连接与控制面。', topics: ['gateway', 'node', 'dashboard', 'acp'] },
      { title: '能力与持久化层', description: '理解 skills、tools、memory 如何协同。', topics: ['skills', 'tools', 'memory'] }
    ]
  },
  {
    key: 'setup',
    title: '配置与部署',
    shortTitle: 'Setup',
    tagline: '把安装过程做成任务流：每一步都知道成功信号是什么。',
    description: '按准备、安装、配置、启动、验证、排错的顺序带你走通 OpenClaw。',
    accent: 'var(--accent-orange)',
    tone: 'rgba(255,179,107,.16)',
    routeLabel: '适合想尽快跑通 OpenClaw 的用户',
    startHere: '先确认 requirements，再 install → configuration → start gateway → first message。',
    explorerLabel: '部署流程',
    pageTypeLabel: 'Task-flow Hub',
    moduleMode: '更像任务看板，不像说明书。',
    overviewSummary: 'Setup 的核心不是把命令堆给你，而是让你知道每一步在验证什么、卡住时要退回哪一层、什么时候算第一次成功。',
    quickPathTitle: '如果你只想走最短路线',
    quickPaths: [
      { title: 'Requirements → Install', description: '先把最低前提与安装闭环跑通。', href: '/setup/install' },
      { title: 'Gateway → First Message', description: '把系统从“装上了”推进到“真的活了”。', href: '/setup/start-gateway' }
    ],
    bridge: [
      { title: '去 FAQ', description: '如果启动、连接或验证阶段卡住，先走排错入口。', href: '/faq' },
      { title: '去 Concepts', description: '如果你想知道为什么这些配置会影响行为。', href: '/concepts' }
    ],
    sections: [
      { title: '准备与安装', description: '先完成最低前提与基础安装。', topics: ['requirements', 'install'] },
      { title: '配置与启动', description: '再处理启动链路与验证点。', topics: ['configuration', 'start-gateway', 'first-message'] },
      { title: '卡住时回退', description: '当你需要快速定位问题层。', topics: ['troubleshooting'] }
    ]
  },
  {
    key: 'faq',
    title: '常见问题',
    shortTitle: 'FAQ',
    tagline: '别再翻全站目录了，先按症状 triage。',
    description: '把 setup、connectivity、files、skills、行为边界等问题整理成更像诊断台的入口。',
    accent: 'var(--accent-pink)',
    tone: 'rgba(255,142,203,.16)',
    routeLabel: '适合遇到阻塞、想先判断问题性质的用户',
    startHere: '先判断自己卡在安装、连接、文件/记忆，还是行为边界。',
    explorerLabel: '问题分诊',
    pageTypeLabel: 'Triage Hub',
    moduleMode: '按症状和处理优先级组织内容。',
    overviewSummary: 'FAQ 的目标不是“问题大全”，而是把你快速带到正确层级：先判断是致命阻断、可接受现象、还是认知偏差，再决定要回 Setup、Concepts 还是继续深挖。',
    quickPathTitle: '如果你只想先判断是不是异常',
    quickPaths: [
      { title: '先看 Setup FAQ', description: '安装、启动、第一条消息问题最常见。', href: '/faq/setup' },
      { title: '先看连接问题', description: 'token、remote、pairing、gateway 相关问题。', href: '/faq/connectivity' }
    ],
    bridge: [
      { title: '回到 Setup', description: '定位问题层之后，回对应步骤重新验证。', href: '/setup' },
      { title: '去 Concepts', description: '如果根因其实是对系统结构理解不足。', href: '/concepts' }
    ],
    sections: [
      { title: '先按阻塞阶段看', description: '最常见的起步与连接问题。', topics: ['setup', 'connectivity', 'ws-http-fallback'] },
      { title: '再按系统层看', description: '文件、记忆、能力与边界类问题。', topics: ['files-and-memory', 'skills-and-tools', 'security-and-behavior'] }
    ]
  },
  {
    key: 'use-cases',
    title: '实际场景',
    shortTitle: 'Use Cases',
    tagline: '从“我要解决什么事”切入，比先啃概念更容易感到价值。',
    description: '展示个人助理、消息平台、GitHub、Google Workspace、提醒与远程访问等场景。',
    accent: 'var(--accent-purple)',
    tone: 'rgba(167,139,250,.16)',
    routeLabel: '适合按目标或结果理解产品的人',
    startHere: '先挑一个最贴近你的目标场景，再回 Concepts 或 Setup 补结构。',
    explorerLabel: '价值地图',
    pageTypeLabel: 'Scenario Hub',
    moduleMode: '按目标探索，不按术语探索。',
    overviewSummary: 'Use Cases 用场景把 OpenClaw 的价值拉近：你不一定先懂全部架构，也能先知道它在日常工作、消息平台、GitHub 或远程访问里能怎么帮忙。',
    quickPathTitle: '如果你想先看价值',
    quickPaths: [
      { title: '个人助理场景', description: '最贴近日常使用感，也最容易建立直觉。', href: '/use-cases/personal-assistant' },
      { title: 'GitHub 工作流', description: '适合工程向用户快速看到生产力价值。', href: '/use-cases/github-workflow' }
    ],
    bridge: [
      { title: '回 Concepts', description: '看完场景后，回去补系统理解。', href: '/concepts' },
      { title: '回 Setup', description: '如果你已经被说服，下一步就是把它跑起来。', href: '/setup' }
    ],
    sections: [
      { title: '日常个人工作流', description: '从个人助理到提醒与自动化。', topics: ['personal-assistant', 'notes-reminders', 'google-workspace', 'heartbeat-automation'] },
      { title: '多表面与工程协作', description: '从消息平台到代码协作。', topics: ['messaging-platforms', 'github-workflow', 'remote-access'] }
    ]
  },
  {
    key: 'advanced',
    title: '进阶主题',
    shortTitle: 'Advanced',
    tagline: '已经能用起来以后，再去理解为什么这样设计、怎样更稳地运行。',
    description: '围绕 session、memory、safety、skills、subagents、logs 等主题做更深入的解释。',
    accent: 'var(--accent-cyan)',
    tone: 'rgba(109,226,255,.16)',
    routeLabel: '适合已经过了第一轮入门的用户',
    startHere: '先看 session model、memory design、best practices，再按需要深入。',
    explorerLabel: '进阶深挖',
    pageTypeLabel: 'Depth Hub',
    moduleMode: '按机制、方法论、调试三个层面组织。',
    overviewSummary: 'Advanced 不是“看起来更难”的杂项区，而是帮助你把经验升级为方法：为什么 session 会影响协作、memory 怎样设计更稳、logs 该怎么读、subagent 又该怎么用。',
    quickPathTitle: '如果你只想先补一个进阶点',
    quickPaths: [
      { title: '先补 Session Model', description: '很多后续高级能力都建立在这里。', href: '/advanced/session-model' },
      { title: '先看 Best Practices', description: '先收敛常见误用，再逐步深入机制。', href: '/advanced/best-practices' }
    ],
    bridge: [
      { title: '回 Concepts', description: '如果发现基础概念还没完全扎稳，先回去补底层关系。', href: '/concepts' },
      { title: '回 FAQ', description: '如果你的深挖目标其实是在排错。', href: '/faq' }
    ],
    sections: [
      { title: '核心机制', description: '更深地理解运行模型。', topics: ['session-model', 'memory-design', 'safety-boundaries'] },
      { title: '高级实践', description: '把机制转化成设计与协作方法。', topics: ['best-practices', 'skill-design', 'subagent-workflows', 'debugging-logs'] }
    ]
  }
];

export const topics: Topic[] = [
  t('getting-started', 'what-is-openclaw', '什么是 OpenClaw', '一个面向真实工具、文件、设备与工作流的个人 AI 助手系统，而不只是聊天窗口。', '帮第一次接触的人迅速建立正确预期。', '如果一开始把 OpenClaw 理解成普通聊天 UI，后面很多概念都会显得奇怪。', '绝对新手', '入门', '5 分钟', ['入门', '定义', '定位'], 'OpenClaw 不是“会聊天的页面”，而是一套可以接入工具、文件、网关、设备与自动化流程的 AI 助手系统。', [
    { title: '它解决什么问题', body: ['它把模型能力与真实工具、文件和设备操作连接起来，让 AI 助手不止会说，还能做。', '因此它更像一个可扩展的助手运行环境，而不是单一对话界面。'] },
    { title: '为什么和普通聊天产品不同', body: ['OpenClaw 强调 session、skills、tools、memory、gateway、nodes 这些系统层能力。', '这些能力共同决定它如何理解上下文、调用能力、保持连续性，以及接入不同表面。'] },
    { title: '第一轮应该怎么理解它', body: ['先把它理解为“一个可在多种表面上工作的 AI 助手系统”。', '先建立用途和结构感，再逐步看 Concepts 与 Setup。'] }
  ], { related: ['getting-started/how-to-learn', 'concepts/architecture'], next: 'getting-started/how-to-learn', completion: 'full', group: '第一轮必看', misunderstandings: ['它不是纯网页聊天产品。', '它不是只靠模型回答问题的单点体验。', '第一轮学习不需要把全部架构都吃透。'] }),
  t('getting-started', 'how-to-learn', '如何学习 OpenClaw', '按你的目标选路径：快速跑通、先懂结构、先看场景，三条路都成立。', '把“该从哪里开始”变成可选择的路径，而不是让用户自己猜。', 'v0.2 的核心就是把学习路径做成界面能力。', '新手 / 回访用户', '入门', '6 分钟', ['学习路径', '路线', '入门'], '如果你想快点成功，就先走 Setup；如果你想少走弯路，就先看 Concepts；如果你想判断值不值得投入，就先看 Use Cases。', [
    { title: '按目标选路线', body: ['想尽快用起来：先走 Setup 的最短路径。', '想搞懂结构：先看 Architecture，再补 session / gateway / skills。', '想判断价值：先看首页的目标入口与场景模块。'] },
    { title: '第一轮不要追求全覆盖', body: ['OpenClaw 主题很多，但不是每一页都需要第一天读完。', '先抓住定义、整体架构、最短部署链路与常见问题入口即可。'] }
  ], { related: ['getting-started/what-is-openclaw', 'setup/install', 'concepts/architecture'], next: 'getting-started/first-roadmap', completion: 'full', group: '第一轮必看' }),
  t('getting-started', 'first-roadmap', '第一轮路线图', '把“从零到第一次成功”切成几步，让新手知道每一段的目标和停点。', '给第一次使用 OpenClaw 的人一个现实可执行的第一轮路线。', '它能降低“是不是非得把全部都搞懂才能开始”的心理门槛。', '新手', '入门', '6 分钟', ['路线图', '第一轮', '起步'], '第一轮的目标不是全懂，而是建立定义、结构感、最小成功链路和基本自救能力。', [
    { title: '建议顺序', body: ['先看什么是 OpenClaw → 如何学习 → 整体架构。', '然后进入 Setup 的 requirements / install / configuration / gateway / first message。'] },
    { title: '什么时候算第一轮完成', body: ['你能解释 OpenClaw 大致是什么。', '你能跑通最小成功路径。', '你卡住时知道先去 FAQ 的哪一类。'] }
  ], { related: ['getting-started/how-to-learn', 'setup/install', 'faq/setup'], next: 'concepts/architecture', completion: 'full', group: '第一轮必看' }),

  t('concepts', 'architecture', '整体架构', 'OpenClaw 的核心价值不在单个组件，而在它们如何协同完成一次真实助手交互。', '先给用户一张全局图，再进入细分概念。', '这是 Concepts 模块最关键的总入口。', '所有认真学习的用户', '基础', '8 分钟', ['架构', '系统图', '概览'], '你可以把 OpenClaw 看成：用户从某个表面进入 → gateway / session 组织上下文 → agent 在 skills 指导下决定行为 → tools 执行动作 → memory / files 提供连续性。', [
    { title: '主要构件', body: ['session 负责承接一段连续上下文。', 'skills 负责提供任务型行为规则与工具使用方式。', 'tools 负责实际执行外部动作。', 'memory / files 负责让连续性落到可持久化层。'] },
    { title: '为什么关系比定义更重要', body: ['单独解释每个术语不难，难的是理解它们如何共同影响体验与操作结果。', '所以 v0.2 不再只给列表，而是强调关系、先后顺序与下一步。'] }
  ], { related: ['concepts/session', 'concepts/gateway', 'concepts/skills', 'setup/install'], next: 'concepts/agent', completion: 'full', group: '全局与运行上下文', misunderstandings: ['gateway 不是全部产品，只是核心服务层之一。', 'skills 和 tools 不是一回事。', 'session 不是“聊天记录”的简单别名。'] }),
  t('concepts', 'agent', 'Agent 是什么', 'Agent 不是一个神秘人格，而是带着规则、目标与工具边界工作的执行主体。', '帮助用户理解 agent 在一次任务中的职责。', '很多对“AI 助手到底是谁在干活”的困惑都发生在这里。', '入门后用户', '基础', '6 分钟', ['agent', '行为主体'], '把 agent 理解成“在一套规则和能力边界里完成任务的执行者”会更准确。', [
    { title: '它和模型的关系', body: ['模型提供推理与生成能力。', 'agent 则是被包装成一个可执行任务角色的行为主体。'] },
    { title: '为什么要强调边界', body: ['agent 不是想做什么就做什么，它会受到 skills、tools、权限与安全规则的共同约束。'] }
  ], { related: ['concepts/session', 'concepts/skills'], next: 'concepts/session', completion: 'standard', group: '全局与运行上下文' }),
  t('concepts', 'session', 'Session 是什么', 'Session 是 OpenClaw 中承接连续上下文与行为历史的基本运行单元。', '解释为什么 session 不是普通“聊天窗口”。', '很多行为边界、上下文积累和子代理协作都跟 session 密切相关。', '入门后准备深入的人', '基础', '7 分钟', ['session', '上下文', '运行模型'], 'Session 决定一段交互如何积累上下文、持有任务状态，并与工具调用和记忆策略发生关系。', [
    { title: '为什么不是普通聊天窗口', body: ['聊天窗口只是展示层，session 则更接近运行中的工作上下文容器。', '这也是为什么同样一句话，在不同 session 里可能意味着完全不同的动作。'] },
    { title: '它影响什么', body: ['影响上下文连续性、工具使用历史、任务状态，以及多步骤任务如何延续。'] }
  ], { related: ['concepts/architecture', 'advanced/session-model'], next: 'concepts/gateway', completion: 'full', group: '全局与运行上下文' }),
  t('concepts', 'gateway', 'Gateway 的角色', 'Gateway 是用户最常操作到的服务层：状态、连接、接入表面、远程访问都常在这里汇合。', '帮助用户把 operational layer 和概念层连接起来。', '很多 setup、remote access 和 dashboard 体验都围绕 gateway 展开。', '实操用户', '基础', '7 分钟', ['gateway', '服务层', '连接'], '如果你把 OpenClaw 当成一套运行中的助手系统，gateway 就是它最核心的运行与接入枢纽之一。', [
    { title: '它通常处理什么', body: ['状态管理、接入层协作、对 dashboard / control UI 的支撑，以及远程连接相关能力。'] },
    { title: '为什么它常出现在排错里', body: ['因为很多“连不上”“状态不对”“控制台有异常”的问题，最终都会落到 gateway 这一层。'] }
  ], { related: ['setup/start-gateway', 'faq/connectivity'], next: 'concepts/node', completion: 'full', group: '接入与运行层' }),
  t('concepts', 'node', 'Node 的作用', 'Node 让 OpenClaw 不只运行在单一入口，而是能扩展到不同设备与接入环境。', '解释为什么会有 companion app、远程节点与接入差异。', '很多 pairing、public URL 与 remote 访问问题都与 node 视角相关。', '准备做跨设备接入的用户', '基础', '6 分钟', ['node', '设备', '接入'], 'Node 可以理解为接入 OpenClaw 生态的设备或运行节点，它决定了某些表面如何接进来。', [
    { title: '它带来的价值', body: ['让用户不必只在一台机器或一种表面上使用 OpenClaw。', '也让本地、远程、移动端等接入路径成为可能。'] },
    { title: '为什么要先分清层次', body: ['node 问题和 gateway 问题经常一起出现，但并不总是同一层。', '先分清本地是否正常，再看节点接入是否异常。'] }
  ], { related: ['faq/connectivity', 'use-cases/remote-access'], next: 'concepts/skills', completion: 'standard', group: '接入与运行层' }),
  t('concepts', 'skills', 'Skills 的角色', 'Skills 像任务型行为说明书：告诉 agent 该怎样做、何时用工具、怎样保持风格与边界。', '帮助用户区分“模型能力”和“任务行为约束”。', '不理解 skills，就很难真正理解 OpenClaw 为什么能表现出稳定的任务风格。', '想深入行为机制的用户', '基础', '7 分钟', ['skills', '行为规则'], 'Skills 不是工具本身，而是把任务目标、步骤偏好、工具用法和边界感打包成可复用行为规范。', [
    { title: '它和 tools 的区别', body: ['tools 负责执行动作。', 'skills 负责告诉 agent 在什么情况下调用哪些 tools，以及调用时的策略。'] },
    { title: '为什么它很重要', body: ['它让助手不只是“临场发挥”，而是能表现出更稳定、更可控的任务能力。'] }
  ], { related: ['concepts/tools', 'advanced/skill-design'], next: 'concepts/tools', completion: 'full', group: '能力与持久化层' }),
  t('concepts', 'tools', 'Tools 的角色', 'Tools 是 OpenClaw 对外部世界动手的接口：文件、命令、网页、设备、服务都靠它们真正执行。', '帮助用户理解“会做事”是怎么落地的。', '如果不理解 tools，用户很容易把可执行系统误会成纯文本系统。', '所有实操用户', '基础', '7 分钟', ['tools', '执行', '能力'], 'Tools 让 agent 不只是说，而是能真正读文件、运行命令、调用网页、接设备、处理外部资源。', [
    { title: '它负责什么', body: ['把抽象决策变成可执行动作。', '承担真正的读写、调用、搜索、生成等操作。'] },
    { title: '为什么要和 skills 一起看', body: ['因为“能做什么”和“该怎么做”是两件事。', '理解 tools 与 skills 的配合，才能理解行为稳定性。'] }
  ], { related: ['concepts/skills', 'faq/skills-and-tools'], next: 'concepts/memory', completion: 'full', group: '能力与持久化层' }),
  t('concepts', 'memory', 'Memory 的角色', 'Memory 让助手的连续性不只停留在当前窗口，而能跨会话、跨任务保留真正值得留下的信息。', '帮助用户理解短期上下文和长期记忆的区别。', '很多“为什么它记得/不记得”的问题都来自这里。', '所有会长期使用的人', '基础', '7 分钟', ['memory', '连续性', '持久化'], 'Memory 不是所有内容都无脑保存，而是把值得保留的长期信息结构化沉淀下来。', [
    { title: '和 session 的区别', body: ['session 更像当前运行上下文。', 'memory 则更像跨 session 的长期连续性。'] },
    { title: '为什么要谨慎设计', body: ['记得太多会噪，记得太少会断。', '好的 memory 设计在于选择性保留真正有复用价值的信息。'] }
  ], { related: ['advanced/memory-design', 'faq/files-and-memory'], next: 'concepts/dashboard', completion: 'full', group: '能力与持久化层' }),
  t('concepts', 'dashboard', 'Dashboard 的角色', 'Dashboard 是用户观察系统状态、进入控制面和理解当前运行情况的重要窗口。', '帮助用户把“系统在发生什么”可视化。', '它让 OpenClaw 不只是黑盒，尤其在 setup 和排错阶段非常重要。', '实操用户', '基础', '5 分钟', ['dashboard', '控制面'], 'Dashboard 的价值在于让你看到系统是否活着、哪些表面连上了、哪里可能需要干预。', [
    { title: '适合用它看什么', body: ['服务状态、连接情况、某些运行层信号，以及进入控制面时的全局感。'] },
    { title: '它不替代什么', body: ['它不是全部真相。', '更深层的问题仍可能需要日志、FAQ 与概念理解配合判断。'] }
  ], { related: ['setup/start-gateway', 'advanced/debugging-logs'], next: 'concepts/heartbeat-cron', completion: 'standard', group: '接入与运行层' }),
  t('concepts', 'heartbeat-cron', 'Heartbeat 与 Cron', 'Heartbeat 更像温和的周期性关心，Cron 更像精确、孤立、定时的任务触发。', '帮助用户理解两种自动化方式该怎么选。', '很多“为什么不用一个东西全包”会卡在这里。', '准备做自动化的人', '基础', '6 分钟', ['heartbeat', 'cron', '自动化'], 'Heartbeat 适合批量、可漂移、带会话感的周期检查；Cron 适合精确时间、隔离执行、独立任务投递。', [
    { title: '什么时候选 heartbeat', body: ['想顺手检查邮件、日历、天气等可批处理事项。', '希望任务依赖会话上下文且时间可略微漂移。'] },
    { title: '什么时候选 cron', body: ['需要精确时点。', '需要独立任务，不想污染当前对话上下文。'] }
  ], { related: ['use-cases/heartbeat-automation', 'advanced/best-practices'], next: 'concepts/subagents', completion: 'standard', group: '全局与运行上下文' }),
  t('concepts', 'subagents', 'Subagents 的作用', 'Subagent 适合把复杂任务拆成隔离的执行过程，让主线程更干净、上下文更稳。', '帮助用户理解为什么要把实现工作交给单独进程。', '这是 OpenClaw 在复杂协作和长任务上的重要能力。', '进阶用户 / 工程用户', '进阶', '6 分钟', ['subagents', '隔离协作'], 'Subagent 不是多开聊天，而是为了隔离上下文、并行或聚焦完成某个明确子任务。', [
    { title: '它解决什么', body: ['避免主线程被大段实现细节、日志和中间状态污染。', '让复杂工作流拆成更可控的独立执行单元。'] },
    { title: '什么时候值得用', body: ['任务复杂、时间较长、需要独立实现或并行探索时。'] }
  ], { related: ['advanced/subagent-workflows', 'advanced/best-practices'], next: 'concepts/acp', completion: 'standard', group: '全局与运行上下文' }),
  t('concepts', 'acp', 'ACP 是什么', 'ACP 可以理解为让能力与接口更可组合、可接入的一层协议化/标准化思路。', '给用户一个足够实用的理解入口，而不是把协议细节一下子全倒出来。', '它常出现在更进阶的能力接入讨论里。', '中高级用户', '进阶', '5 分钟', ['acp', '协议', '扩展'], '第一轮理解 ACP，不必死记细节；先知道它属于“让能力更容易被接入和复用”的规范化思路即可。', [
    { title: '为什么你现在可能还不急着看它', body: ['如果你还在第一轮入门，ACP 不是最先影响上手体验的东西。', '但当你开始关心扩展性、协议化接入时，它就会出现。'] },
    { title: '怎样把它放进全局图里', body: ['把它放在“接入与扩展能力的规范层”来理解，会比把它当孤立名词更有帮助。'] }
  ], { related: ['concepts/tools', 'advanced/best-practices'], completion: 'standard', group: '接入与运行层' }),

  t('setup', 'requirements', '开始前需要准备什么', '在安装前先确认环境、权限与关键前提，能少掉很多无意义折返。', '让用户先看最低门槛，而不是出错后才补票。', 'requirements 页的作用就是减少后面那些本可避免的 setup friction。', '准备部署的新手', '入门', '5 分钟', ['requirements', '准备'], 'requirements 的价值不是“看起来很基础”，而是帮你提前清掉最常见的前提条件坑。', [
    { title: '最低前提', body: ['先确认系统环境、基础命令、网络与权限是否满足官方路径。', '先把最关键前提确认掉，再开始安装。'] },
    { title: '为什么先看它更省时间', body: ['很多安装失败不是安装步骤本身的问题，而是前提不满足。'] }
  ], { related: ['setup/install', 'faq/setup'], next: 'setup/install', completion: 'full', group: '准备与安装' }),
  t('setup', 'install', '安装 OpenClaw', '先把系统装起来，但要用“最小成功路径”思维，而不是一开始追求全功能。', '让用户按顺序完成最小安装闭环。', '很多挫败感不是安装失败，而是用户一开始就试图同时解决太多事。', '想尽快跑起来的用户', '基础', '8 分钟', ['setup', 'install', '最短路径'], '先满足 prerequisites，再按官方路径完成安装，之后立刻验证 gateway 和 first message，而不是先优化所有高级配置。', [
    { title: '推荐顺序', body: ['requirements → install → configuration → start gateway → first message。', '每一步都要有“成功信号”，这样出问题时才知道卡在哪里。'] },
    { title: '什么叫最小成功', body: ['能启动核心服务、能看到状态正常、能完成第一条成功交互。', '只要这条链路通了，后面的扩展和排错都会容易很多。'] }
  ], { related: ['setup/requirements', 'setup/configuration', 'faq/setup'], next: 'setup/configuration', completion: 'full', group: '准备与安装', misunderstandings: ['安装完成不等于已经可用。', '第一轮不需要把远程接入、所有插件、所有平台都一次打通。'] }),
  t('setup', 'configuration', '配置层该先配什么', '先配影响“能不能跑”的关键项，再配影响“跑得多舒服”的增强项。', '避免配置阶段信息过载。', '很多用户会在配置海里失去优先级判断。', '实操新手', '基础', '8 分钟', ['config', 'setup', '优先级'], '优先处理与启动、连接、基本行为直接相关的配置；其他舒适度和扩展性项可以第二轮再补。', [
    { title: '配置优先级', body: ['先看哪些配置影响基本运行。', '再看哪些配置影响接入表面、远程访问或扩展能力。'] },
    { title: '配置阶段怎么降低风险', body: ['一次只改少数关键项。', '改完就验证，不要累计太多变量再一起出问题。'] }
  ], { related: ['setup/install', 'setup/start-gateway'], next: 'setup/start-gateway', completion: 'full', group: '配置与启动' }),
  t('setup', 'start-gateway', '启动并验证 Gateway', '不要只“启动命令”，还要知道健康启动长什么样。', '把 setup 页面从说明文变成带 checkpoint 的任务流。', '用户最需要的是“我现在到底算不算启动成功了”。', '实操用户', '基础', '6 分钟', ['gateway', '验证', 'checkpoint'], '启动 gateway 后，关键不是“命令跑了”，而是状态正常、访问路径通、后续交互能继续。', [
    { title: '成功信号', body: ['服务状态健康。', '对应界面或连接入口可访问。', '后续 first message 能顺利完成。'] },
    { title: '如果不健康怎么办', body: ['先确认基础启动链路，再区分是本地服务层、接入层还是授权层问题。'] }
  ], { related: ['concepts/gateway', 'faq/connectivity'], next: 'setup/first-message', completion: 'full', group: '配置与启动' }),
  t('setup', 'first-message', '完成第一条成功消息', '第一条成功消息是“系统真的活了”的关键验证点。', '把安装完成转化为可感知的首次成功。', '这一步最能建立信心，也最容易暴露残留问题。', '实操用户', '基础', '5 分钟', ['setup', 'first success'], '当你能稳定完成一条成功交互时，说明最小闭环已经建立；之后再扩展场景和高级能力。', [
    { title: '要验证的不是“会回复”这么简单', body: ['你要确认路径是否正确、上下文是否正常、表面接入是否如预期工作。'] },
    { title: '第一次成功之后做什么', body: ['先回顾当前链路。', '再决定要继续补概念、扩展场景，还是处理剩余小问题。'] }
  ], { related: ['setup/start-gateway', 'faq/setup'], next: 'setup/troubleshooting', completion: 'full', group: '配置与启动' }),
  t('setup', 'troubleshooting', 'Setup 卡住时怎么回退', '当安装链路中途出问题时，最重要的是先退回到正确的检查点，而不是盲试所有命令。', '把 setup 排错做成回退流程。', '这能显著降低“越修越乱”的情况。', '被 setup 卡住的人', '基础', '6 分钟', ['troubleshooting', 'setup', '回退'], '排错最有价值的动作，是先确认你卡在 requirements、install、configuration、gateway 还是 first message。', [
    { title: '先判断层级', body: ['要求不满足 → 回 requirements。', '安装命令异常 → 回 install。', '启动或访问异常 → 看 gateway / connectivity。'] },
    { title: '别把现象混在一起', body: ['缺文件、token mismatch、ws fallback、启动失败，严重性和处理方式都不同。'] }
  ], { related: ['faq/setup', 'faq/connectivity'], next: 'faq/setup', completion: 'full', group: '卡住时回退' }),

  t('faq', 'setup', 'Setup 常见问题', '当安装、启动、第一条消息阶段出现阻塞时，先按症状判断问题落在哪一层。', '提供 setup 阶段的 FAQ triage 入口。', 'FAQ 的价值在于快速缩小范围，而不是把所有错误一股脑丢给用户。', '配置阶段被卡住的人', '入门', '6 分钟', ['faq', 'setup', '排错'], '先判断你是卡在 prerequisites、install、configuration、gateway status，还是 first message。不同症状对应完全不同的排查路径。', [
    { title: '先按阶段判断', body: ['安装前卡住：看 requirements。', '启动后卡住：看 gateway / connectivity。', '能启动但行为不对：看 configuration、skills、session 理解是否偏了。'] },
    { title: '什么问题值得先冷静', body: ['一些日志噪音或 fallback 现象未必是致命故障。', '先区分功能阻断、性能小问题和正常可接受现象。'] }
  ], { related: ['setup/install', 'setup/start-gateway'], next: 'faq/connectivity', completion: 'full', group: '先按阻塞阶段看', misunderstandings: ['不是所有报错都代表系统坏了。', '缺文件、fallback、token 问题的处理优先级并不相同。'] }),
  t('faq', 'connectivity', '连接问题怎么判断', 'token、pairing、gateway remote、public URL 等问题，看起来像一类，其实层次不同。', '帮用户先判断连接问题属于哪一层。', 'FAQ 不只是给答案，更要帮用户少走错路。', '遇到远程 / 接入异常的用户', '基础', '7 分钟', ['faq', 'connectivity', 'gateway'], '先分清本地是否正常、gateway 是否正常、授权/token 是否正常，再看 remote / pairing / publicUrl 这类外层问题。', [
    { title: '先看哪一层', body: ['本地正常但远程不通，和本地就起不来，是两种完全不同的问题。', 'token mismatch、pairing required、publicUrl 配置错误，也不能混为一谈。'] },
    { title: '建议排查顺序', body: ['先确认 gateway 健康。', '再确认本地访问。', '最后才看 remote / token / pairing。'] }
  ], { related: ['concepts/gateway', 'setup/start-gateway'], next: 'faq/ws-http-fallback', completion: 'full', group: '先按阻塞阶段看' }),
  t('faq', 'files-and-memory', '文件与 Memory 问题', '缺文件、记忆没命中、文件读写异常，看起来都像“它忘了”，其实可能完全不是一层问题。', '帮助用户先区分文件问题和长期记忆问题。', '这类问题很常见，也很容易被误判。', '开始长期使用的用户', '基础', '6 分钟', ['faq', 'files', 'memory'], '先分清是文件根本不存在、路径不对、权限不对，还是 memory 本来就不该记住这件事。', [
    { title: '文件问题的典型特征', body: ['通常表现为找不到、读不到、写不进去，或者路径搞错。'] },
    { title: 'memory 问题的典型特征', body: ['通常表现为用户以为它该记住，但系统其实没有长期存储那个信息。'] }
  ], { related: ['concepts/memory', 'advanced/memory-design'], next: 'faq/skills-and-tools', completion: 'full', group: '再按系统层看' }),
  t('faq', 'ws-http-fallback', 'WS / HTTP fallback 是什么情况', 'ws-stream 500 之后回退到 HTTP，往往意味着传输链路有兼容或实现问题，但不一定表示系统彻底坏了。', '帮助用户判断 fallback 现象的严重性。', '这类现象很容易制造误报式焦虑。', '正在看日志或调试性能的人', '基础', '5 分钟', ['faq', 'ws', 'http', 'fallback'], '先判断功能是否仍可用；如果系统自动回退且核心功能正常，它更像持续性小摩擦，而不一定是致命故障。', [
    { title: '为什么它容易吓人', body: ['因为日志里有 500，又涉及 ws/http 切换，看起来像核心链路坏了。'] },
    { title: '怎样判断优先级', body: ['如果系统仍可正常工作，就先把它归为性能/兼容性问题。', '只有在功能明显受阻时，才把它升级为高优先级故障。'] }
  ], { related: ['faq/connectivity', 'advanced/debugging-logs'], completion: 'full', group: '先按阻塞阶段看' }),
  t('faq', 'skills-and-tools', 'Skills / Tools 问题怎么分', '当行为不符合预期时，先分清是“没有能力”还是“能力用错了方式”。', '帮助用户把工具层和行为规则层拆开。', '很多“它为什么不这么做”其实并不是同一个根因。', '开始自定义能力的用户', '基础', '6 分钟', ['faq', 'skills', 'tools'], 'Tools 更像“能做什么”，skills 更像“应该怎样做”；问题判断时不能混成一团。', [
    { title: '更像 tools 问题的情况', body: ['某个动作根本执行不了。', '外部接口、命令、权限或调用路径本身异常。'] },
    { title: '更像 skills 问题的情况', body: ['助手有能力，但做法不稳、顺序不对、边界不清。'] }
  ], { related: ['concepts/skills', 'concepts/tools'], completion: 'standard', group: '再按系统层看' }),
  t('faq', 'security-and-behavior', '安全与行为边界问题', '当你怀疑助手“越界”或“不够听话”时，真正要看的是权限、规则、上下文与安全策略如何共同作用。', '帮助用户更成熟地判断行为边界问题。', '这类问题往往带有情绪，但更需要结构化理解。', '进阶用户 / 管理者', '进阶', '6 分钟', ['faq', 'security', 'behavior'], '行为边界不是单点开关，而是由系统提示、skills、工具权限、审批策略和会话上下文共同决定。', [
    { title: '为什么不能只怪模型', body: ['因为很多“越界”或“没做成”，其实跟规则设计和权限结构更相关。'] },
    { title: '先看哪几类因素', body: ['技能规则、工具权限、审批要求、当前 session 目标，以及是否存在安全红线。'] }
  ], { related: ['advanced/safety-boundaries', 'concepts/agent'], completion: 'standard', group: '再按系统层看' }),

  t('use-cases', 'personal-assistant', '个人助理场景', '这是最贴近日常直觉的入口：日程、记录、提醒、查询、整理，都能让人迅速感受到 OpenClaw 的“会做事”。', '用最接近日常生活的场景解释产品价值。', '它通常是最容易让人“哦，原来是这种东西”的页面。', '所有新用户', '入门', '5 分钟', ['use case', 'assistant'], '把 OpenClaw 当成能接触文件、日历、提醒、消息与工作流的个人助理，会比把它当成聊天机器人更接近现实。', [
    { title: '为什么这个场景最容易理解', body: ['因为它贴近日常任务，用户很容易把功能映射到自己生活。'] },
    { title: '看完后适合去哪里', body: ['如果你被价值打动，去 Setup。', '如果你想知道为什么它能这么做，去 Concepts。'] }
  ], { related: ['use-cases/notes-reminders', 'setup/install'], completion: 'standard', group: '日常个人工作流' }),
  t('use-cases', 'messaging-platforms', '消息平台场景', 'OpenClaw 可以接在不同消息表面上工作，这让“助手”变成可触达的存在，而不是只能困在一个网页里。', '解释多表面使用价值。', '它能帮助用户理解 why gateway / node / remote matter。', '想在聊天表面使用 OpenClaw 的用户', '基础', '5 分钟', ['messaging', 'surface'], '消息平台场景的关键不是换皮，而是让助手真正进入你已经在用的沟通入口。', [
    { title: '它体现了什么价值', body: ['减少切换成本。', '让助手进入现有工作与生活表面。'] },
    { title: '背后最相关的概念', body: ['gateway、node、session 与接入配置。'] }
  ], { related: ['concepts/gateway', 'use-cases/remote-access'], completion: 'standard', group: '多表面与工程协作' }),
  t('use-cases', 'github-workflow', 'GitHub 工作流', '从 issue、PR、review 到实现子进程协作，OpenClaw 在工程工作流里能显著减少重复跳转与信息切换。', '把产品价值放进工程协作语境里。', '这通常是技术用户最容易被说服的场景之一。', '工程用户', '基础', '6 分钟', ['github', 'workflow'], 'GitHub 场景最能体现 OpenClaw 不是只会回答，而是能围绕真实工具链做事。', [
    { title: '典型价值点', body: ['查看 issue / PR 状态。', '启动独立实现进程。', '回收结果、继续 review 与修正。'] },
    { title: '为什么它适合展示 subagents', body: ['因为实现任务天然适合隔离执行，并把主线程保持在管理与决策层。'] }
  ], { related: ['concepts/subagents', 'advanced/subagent-workflows'], completion: 'standard', group: '多表面与工程协作' }),
  t('use-cases', 'notes-reminders', 'Notes / Reminders 场景', '当助手能写笔记、管提醒时，它就开始接近日常“外脑”而不是一次性对话。', '帮助用户理解轻办公与生活组织类价值。', '这是最自然的日常持续使用入口之一。', '日常效率用户', '基础', '5 分钟', ['notes', 'reminders'], '记录和提醒类场景，最能让用户感受到长期连续性的价值。', [
    { title: '它为什么有代表性', body: ['任务简单、频率高、反馈快，很适合建立使用习惯。'] },
    { title: '相关能力', body: ['tools、memory、heartbeat 与日常表面接入。'] }
  ], { related: ['use-cases/personal-assistant', 'use-cases/heartbeat-automation'], completion: 'standard', group: '日常个人工作流' }),
  t('use-cases', 'google-workspace', 'Google Workspace 场景', '当助手能接 Gmail、Calendar、Drive、Docs 时，它就能进入大量真实工作流。', '解释与生产力套件协作的价值。', '这是“接入真实世界工具”的强力示范。', '办公用户', '基础', '5 分钟', ['google', 'workspace'], 'Google Workspace 场景体现的是：助手不只在聊天里回答，还能在常用工作系统里真正落地。', [
    { title: '典型收益', body: ['少做重复点击。', '把零散信息整理成行动。'] },
    { title: '先补什么概念更有帮助', body: ['tools、session、memory 和权限边界。'] }
  ], { related: ['concepts/tools', 'advanced/safety-boundaries'], completion: 'standard', group: '日常个人工作流' }),
  t('use-cases', 'heartbeat-automation', 'Heartbeat 自动化场景', 'Heartbeat 适合那些不必分秒精确、但又希望助手定期顺手看一眼的事情。', '把 heartbeat 的概念落到实际体验。', '这能帮助用户理解“主动但不过度打扰”的自动化风格。', '想做轻周期自动化的人', '基础', '5 分钟', ['heartbeat', 'automation'], 'Heartbeat 最适合把多个轻量周期检查打包在一起，而不是把所有定时任务都变成 cron。', [
    { title: '适合的任务类型', body: ['邮件 / 日历 / 天气 / 项目状态等可批量检查项。'] },
    { title: '为什么它像“关心”而不是“命令”', body: ['因为它更允许上下文感、批量感和时间轻微漂移。'] }
  ], { related: ['concepts/heartbeat-cron', 'use-cases/personal-assistant'], completion: 'standard', group: '日常个人工作流' }),
  t('use-cases', 'remote-access', '远程访问场景', '当助手不只活在本机，而能跨设备、跨网络可达时，它的实用性会发生质变。', '帮助用户理解 remote access 的真实价值与复杂度。', '也是理解 gateway / node / connectivity 的绝佳现实案例。', '需要跨设备使用的人', '基础', '5 分钟', ['remote', 'access'], '远程访问的价值很大，但它也更容易暴露 token、pairing、public URL、网络层等问题。', [
    { title: '为什么值得看', body: ['它直接关系到 OpenClaw 是否能融入真实生活，而不是只能在某台机器前使用。'] },
    { title: '看完后该补什么', body: ['补 gateway、node 和 connectivity FAQ，会更容易真正落地。'] }
  ], { related: ['concepts/node', 'faq/connectivity'], completion: 'standard', group: '多表面与工程协作' }),

  t('advanced', 'session-model', 'Session Model', '很多高级行为、协作方式与稳定性理解，最终都要回到 session 是怎样组织上下文与任务状态的。', '把 session 从基础概念升级为设计与操作视角。', '这是很多进阶话题的底层支点。', '已经完成第一轮入门的用户', '进阶', '7 分钟', ['session', 'model'], '把 session 当成运行中的任务上下文容器，而不是聊天记录，会让很多复杂行为一下子变得合理。', [
    { title: '为什么它是高级主题的底层支点', body: ['因为子代理、连续工具调用、审批、记忆边界等高级能力都和 session 组织方式有关。'] },
    { title: '从“会用”到“会设计”', body: ['理解 session model 后，你更容易规划怎样拆任务、怎样保持线程干净、怎样减少上下文污染。'] }
  ], { related: ['concepts/session', 'advanced/subagent-workflows'], completion: 'standard', group: '核心机制' }),
  t('advanced', 'memory-design', 'Memory Design', '好的 memory 设计不是尽量多记，而是让长期信息更干净、更可复用、更少干扰。', '把 memory 从概念层推进到设计层。', '长期使用体验的质量，在很大程度上取决于这里。', '长期使用者 / 设计者', '进阶', '7 分钟', ['memory', 'design'], 'Memory design 的关键是选择什么值得留下、保存在哪里、怎样避免长期噪音压垮后续体验。', [
    { title: '为什么“全记住”不是答案', body: ['因为无差别记忆会带来噪音、风险和理解偏差。'] },
    { title: '怎样判断值得保留的内容', body: ['看是否跨任务复用、是否长期稳定、是否对未来判断有持续帮助。'] }
  ], { related: ['concepts/memory', 'faq/files-and-memory'], completion: 'standard', group: '核心机制' }),
  t('advanced', 'safety-boundaries', 'Safety Boundaries', '安全边界不是让助手变“胆小”，而是确保它在真实工具世界里仍然可控。', '帮助用户用系统视角理解安全约束。', '当工具和外部动作越来越真实时，这一页的重要性会迅速上升。', '进阶用户 / 管理者', '进阶', '6 分钟', ['safety', 'boundaries'], '安全边界的核心不是阻止一切，而是在权限、审批、策略与行为规则之间取得可靠平衡。', [
    { title: '为什么它和传统聊天产品不同', body: ['因为 OpenClaw 不是只输出文字，它还会接触文件、命令、设备与外部系统。'] },
    { title: '边界感来自哪里', body: ['来自系统规则、skills、工具权限、审批流程，以及用户明确的意图约束。'] }
  ], { related: ['faq/security-and-behavior', 'concepts/agent'], completion: 'standard', group: '核心机制' }),
  t('advanced', 'best-practices', 'Best Practices', '当你已经知道它能做什么，下一步就是学会怎样更稳、更省上下文、更少反复。', '把零散经验收敛成方法论。', '它能帮用户避免很多常见误用。', '所有进阶用户', '进阶', '6 分钟', ['best practices'], '最佳实践通常围绕三件事：保持上下文干净、分层处理复杂任务、以及把工具使用和审批习惯做得可预测。', [
    { title: '最常见的三个方向', body: ['先规划路径再执行。', '复杂任务拆给 subagent。', '高风险动作保留审批与复核。'] },
    { title: '为什么这比继续堆技巧更值', body: ['方法论能在新场景里复用，而不是只对一个技巧有效。'] }
  ], { related: ['advanced/subagent-workflows', 'concepts/heartbeat-cron'], completion: 'standard', group: '高级实践' }),
  t('advanced', 'skill-design', 'Skill Design', '设计 skill 的关键不是把说明写得越多越好，而是让行为边界、工具策略和任务目标足够清楚。', '帮助用户理解如何写出更稳的 skill。', '这页对自定义能力的人很重要，但可以比核心 backbone 稍晚完善。', '准备自定义 skills 的用户', '进阶', '6 分钟', ['skill design'], '好的 skill 设计应该同时回答：目标是什么、怎么做、什么时候用工具、哪些边界不能跨。', [
    { title: '为什么“更长的规则”不一定更好', body: ['规则过长可能让核心意图被淹没，增加执行时的歧义。'] },
    { title: '设计时先抓什么', body: ['任务目标、步骤偏好、工具策略、安全边界。'] }
  ], { related: ['concepts/skills', 'advanced/best-practices'], completion: 'transitional', group: '高级实践' }),
  t('advanced', 'subagent-workflows', 'Subagent Workflows', '当任务复杂度上升时，subagent 工作流能把主线程从“卷入实现”拉回“管理与汇总”。', '把 subagent 从概念转化为工作流实践。', '这页非常适合工程与复杂项目用户。', '工程用户 / 复杂任务用户', '进阶', '6 分钟', ['subagent', 'workflow'], 'Subagent workflow 的核心收益是：隔离实现细节、减少主线程污染、让任务拆分与回收更清晰。', [
    { title: '最典型的用法', body: ['实现子任务、并行探索、长任务隔离、日志与中间状态托管。'] },
    { title: '它不适合什么', body: ['过度拆分简单任务。', '把本可直接完成的轻任务复杂化。'] }
  ], { related: ['concepts/subagents', 'use-cases/github-workflow'], completion: 'transitional', group: '高级实践' }),
  t('advanced', 'debugging-logs', 'Debugging Logs', '日志不是拿来把人吓住的，而是帮助你区分致命错误、兼容性摩擦和正常噪音。', '帮助用户建立更成熟的日志阅读方式。', '很多 setup / fallback / ws / token 问题都需要这层心态。', '愿意自己排错的用户', '进阶', '6 分钟', ['logs', 'debugging'], '看日志时先分级：功能阻断、持续摩擦、普通噪音。只要先分级，排错就不会被吓跑。', [
    { title: '先看什么', body: ['先看是否影响核心功能。', '再看错误是否稳定复现。', '最后再考虑是否属于实现兼容性问题。'] },
    { title: '为什么先分级很重要', body: ['因为不是所有红字都值得最高优先级。', '过度反应反而会浪费精力。'] }
  ], { related: ['faq/ws-http-fallback', 'faq/setup'], completion: 'transitional', group: '高级实践' })
];

export const topicMap = Object.fromEntries(topics.map((topic) => [`${topic.module}/${topic.slug}`, topic]));

export function getModule(key: ModuleKey) {
  return modules.find((module) => module.key === key)!;
}

export function getTopicsByModule(module: ModuleKey) {
  return topics.filter((topic) => topic.module === module);
}

export function getTopic(path: string) {
  return topicMap[path] as Topic | undefined;
}

export function getModuleSections(module: ModuleKey) {
  return getModule(module).sections.map((section) => ({
    ...section,
    items: section.topics.map((slug) => getTopic(`${module}/${slug}`)).filter(Boolean) as Topic[]
  }));
}

export function getModuleTopicOrder(module: ModuleKey) {
  return getModule(module).sections.flatMap((section) => section.topics);
}

export function getTopicSiblings(module: ModuleKey, slug: string) {
  const order = getModuleTopicOrder(module);
  const index = order.indexOf(slug);
  return {
    prev: index > 0 ? getTopic(`${module}/${order[index - 1]}`) : undefined,
    next: index >= 0 && index < order.length - 1 ? getTopic(`${module}/${order[index + 1]}`) : undefined
  };
}

export function getExplorerTree() {
  return modules.map((module) => ({
    key: module.key,
    title: module.title,
    href: `/${module.key}`,
    children: getModuleSections(module.key).flatMap((section) => section.items.map((item) => ({
      title: item.navTitle || item.title,
      href: `/${item.module}/${item.slug}`,
      group: section.title
    })))
  }));
}

export const homeRoutes = {
  stage: [
    { title: '我是新手，先建立起点', description: '先看定义、学习路径，再进入 Setup。', href: '/getting-started' },
    { title: '我想建立心智模型', description: '先看 Architecture，再按关系深入 Concepts。', href: '/concepts' },
    { title: '我想尽快部署成功', description: '直接走 Setup 的最短成功路径。', href: '/setup' },
    { title: '我已经卡住了', description: '进入 FAQ 按症状 triage。', href: '/faq' }
  ],
  goal: [
    { title: '我想先搞懂 OpenClaw', description: '从定义和整体架构开始。', href: '/getting-started/what-is-openclaw' },
    { title: '我想尽快跑起来', description: '从 install → config → gateway → first message。', href: '/setup/install' },
    { title: '我想看实际用途', description: '从 Use Cases 先建立价值感。', href: '/use-cases' },
    { title: '我想排查常见问题', description: '按 setup / connectivity / files / behavior 切入。', href: '/faq' }
  ]
};

export const learningPath = [
  {
    step: '01',
    title: '先知道它是什么',
    outcome: '建立产品定位与合理预期',
    time: '5–10 分钟',
    pages: [
      { title: '什么是 OpenClaw', href: '/getting-started/what-is-openclaw' },
      { title: '如何学习 OpenClaw', href: '/getting-started/how-to-learn' }
    ]
  },
  {
    step: '02',
    title: '建立整体结构感',
    outcome: '知道 gateway / session / skills / tools / memory 的关系',
    time: '10–15 分钟',
    pages: [
      { title: '整体架构', href: '/concepts/architecture' },
      { title: 'Session 是什么', href: '/concepts/session' },
      { title: 'Gateway 的角色', href: '/concepts/gateway' }
    ]
  },
  {
    step: '03',
    title: '走通最小成功路径',
    outcome: '完成安装、配置、启动与第一条成功消息',
    time: '15–30 分钟',
    pages: [
      { title: 'Install', href: '/setup/install' },
      { title: 'Configuration', href: '/setup/configuration' },
      { title: 'Start Gateway', href: '/setup/start-gateway' },
      { title: 'First Message', href: '/setup/first-message' }
    ]
  },
  {
    step: '04',
    title: '学会快速自救',
    outcome: '遇到常见阻塞时知道先按哪一层判断',
    time: '5–10 分钟',
    pages: [
      { title: 'Setup FAQ', href: '/faq/setup' },
      { title: '连接问题怎么判断', href: '/faq/connectivity' }
    ]
  }
];

export const shareableLinks = [
  { title: '什么是 OpenClaw', reason: '最适合第一次转给别人看的解释页。', href: '/getting-started/what-is-openclaw' },
  { title: '整体架构', reason: '适合想快速建立系统图的人。', href: '/concepts/architecture' },
  { title: '安装 OpenClaw', reason: '适合实操用户直接开始。', href: '/setup/install' },
  { title: 'Setup 常见问题', reason: '适合已经卡住的人快速判断问题范围。', href: '/faq/setup' }
];
