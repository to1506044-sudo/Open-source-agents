#!/usr/bin/env python3
"""Rebuild all project MD files with unified format and new category taxonomy."""
import os

REPO = "/Users/tengling/Documents/GitHub/Open-source-agents"

# ── Category definitions ──
CATEGORIES = {
    "computer": ("🤖 Computer Agents", "桌面/操作系统自动化智能体"),
    "browser": ("🌐 Browser Agents", "浏览器自动化智能体"),
    "coding": ("👨‍💻 Coding Agents", "编程助手与代码智能体"),
    "mobile": ("📱 Mobile Agents", "移动端(Android/iOS)自动化智能体"),
    "multi_agent": ("🧠 Multi-Agent", "多智能体编排框架"),
    "mcp": ("🔌 MCP", "Model Context Protocol 工具与基础设施"),
    "rag": ("📚 RAG", "检索增强生成框架与平台"),
    "memory": ("🧠 Memory", "Agent 记忆与上下文系统"),
    "search": ("🔍 Search", "搜索与网页抓取工具"),
    "voice": ("🎙 Voice Agent", "语音智能体"),
    "robotics": ("🤖 Robotics", "机器人与具身智能"),
    "benchmark": ("📈 Benchmark", "Agent 评测基准"),
    "chat": ("💬 AI Chat Platforms", "AI 聊天与 All-in-one 平台"),
    "local": ("🏠 Local Inference", "本地模型运行与推理"),
    "ide": ("🖥️ AI IDE / Editor", "AI 原生编辑器与 IDE"),
    "security": ("🔒 Security & Sandbox", "安全护栏与沙盒执行"),
}

# ── All projects ──
PROJECTS = [
    # ════════════════════ Computer Agents ════════════════════
    {
        "name": "Hermes Agent", "file": "HermesAgent", "cat": "computer",
        "org": "Nous Research", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["Computer Use (桌面自动化)", "Browser Automation", "Tool Calling", "MCP 协议", "多平台消息网关 (Telegram/飞书/微信)", "Cron 定时任务", "Subagent 委派"],
        "github": "https://github.com/NousResearch/hermes-agent",
        "website": "https://hermes-agent.nousresearch.com",
        "stars": "~187k",
        "desc": "跨模型/终端UI/消息网关的全能 Agent，2026 现象级项目。支持桌面操作、代码开发、浏览器控制、多平台集成。",
    },
    {
        "name": "OpenClaw", "file": "OpenClaw", "cat": "computer",
        "org": "Community", "license": "开源", "lang": "Python",
        "platforms": "macOS / Linux",
        "features": ["Computer Use", "Desktop Automation", "系统级操作", "代理管理"],
        "github": "https://github.com/openclaw/openclaw",
        "website": "",
        "stars": "60天 9k→188k",
        "desc": "2026 增速最快的开源 Agent 项目，60 天内从 9k 星冲到 188k 星。",
    },
    {
        "name": "OpenHands", "file": "OpenHands", "cat": "computer",
        "org": "All Hands AI", "license": "MIT", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["全自动软件工程", "沙盒执行", "GitHub Issue 解决", "PR 生成", "Desktop Automation"],
        "github": "https://github.com/All-Hands-AI/OpenHands",
        "website": "https://openhands.ai",
        "stars": "~68–75k",
        "desc": "全自动软件工程 Agent（原 OpenDevin），沙盒执行，可解决 GitHub issue 并生成 PR。",
    },
    {
        "name": "Open Interpreter", "file": "OpenInterpreter", "cat": "computer",
        "org": "Open Interpreter", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["本地代码执行", "OS Mode", "Shell 操作", "文件系统控制", "多模型支持"],
        "github": "https://github.com/OpenInterpreter/open-interpreter",
        "website": "https://openinterpreter.ai",
        "stars": "数万",
        "desc": "让 LLM 在本机执行代码/操作系统的开源解释器，支持 OS Mode 桌面控制。",
    },
    {
        "name": "Agent S", "file": "AgentS", "cat": "computer",
        "org": "Simular AI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["高性能 Computer Use", "GUI 元素定位", "跨应用操作", "OSWorld 基准领先"],
        "github": "https://github.com/simular-ai/Agent-S",
        "website": "",
        "stars": "~12k",
        "desc": "高性能开源 Computer Use 框架，像人类一样操作电脑，在 OSWorld 等基准上表现优秀。",
    },
    {
        "name": "CUA", "file": "CUA", "cat": "computer",
        "org": "Community", "license": "开源", "lang": "Python",
        "platforms": "macOS / Linux",
        "features": ["Computer-Use Agents 基础设施", "截图驱动操控", "桌面自动化"],
        "github": "https://github.com/anthropics/cua",
        "website": "",
        "stars": "数千",
        "desc": "Computer-Use Agents 基础设施，提供桌面/浏览器操控的底层能力。",
    },
    {
        "name": "OpenManus", "file": "OpenManus", "cat": "computer",
        "org": "Community", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["通用 AI Agent", "工具调用", "多步骤任务", "Computer Use"],
        "github": "https://github.com/mannaandpoem/OpenManus",
        "website": "",
        "stars": "数万",
        "desc": "通用 AI Agent 平台，支持工具调用和多步骤复杂任务执行。",
    },
    {
        "name": "OpenOperator", "file": "OpenOperator", "cat": "computer",
        "org": "Community", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["计算机操作 Agent", "GUI 自动化", "任务编排"],
        "github": "https://github.com/OpenOperator/OpenOperator",
        "website": "",
        "stars": "数千",
        "desc": "计算机操作 Agent 框架，专注于 GUI 自动化和复杂任务编排。",
    },
    {
        "name": "PyAutoGUI", "file": "PyAutoGUI", "cat": "computer",
        "org": "Al Sweigart", "license": "BSD", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["鼠标键盘控制", "屏幕截图", "图像定位", "跨平台 GUI 自动化"],
        "github": "https://github.com/asweigart/pyautogui",
        "website": "",
        "stars": "~15k",
        "desc": "跨平台 GUI 自动化库，支持鼠标键盘控制、屏幕截图和图像定位。",
    },
    {
        "name": "OmniParser", "file": "OmniParser", "cat": "computer",
        "org": "Microsoft", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["屏幕截图解析", "UI 元素检测", "视觉 grounding", "结构化输出"],
        "github": "https://github.com/microsoft/OmniParser",
        "website": "",
        "stars": "~10k+",
        "desc": "微软出品的屏幕截图解析工具，将截图转化为结构化 UI 元素，为 Agent 提供视觉感知能力。",
    },
    {
        "name": "UI-TARS", "file": "UITARS", "cat": "computer",
        "org": "字节跳动", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["GUI 视觉-语言模型", "界面理解", "操作生成", "多模态"],
        "github": "https://github.com/bytedance/UI-TARS",
        "website": "",
        "stars": "数万",
        "desc": "字节跳动出品的 GUI 操作专用视觉-语言 Agent 模型与框架。",
    },
    {
        "name": "Anthropic Computer Use Demo", "file": "AnthropicComputerUse", "cat": "computer",
        "org": "Anthropic", "license": "开源", "lang": "Python",
        "platforms": "macOS / Linux",
        "features": ["截图驱动桌面操控", "浏览器操控", "参考实现"],
        "github": "https://github.com/anthropics/anthropic-quickstarts",
        "website": "",
        "stars": "数千",
        "desc": "Anthropic 官方的 Computer Use 参考实现，截图驱动的桌面/浏览器操控 Demo。",
    },

    # ════════════════════ Browser Agents ════════════════════
    {
        "name": "Browser Use", "file": "BrowserUse", "cat": "browser",
        "org": "Browser Use", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["视觉 DOM 解析", "验证码穿越", "动态滑块处理", "LLM 原生浏览器操作"],
        "github": "https://github.com/browser-use/browser-use",
        "website": "https://browser-use.com",
        "stars": "~20k+",
        "desc": "让 LLM 原生操作浏览器的开源库，浏览器 Agent 标杆项目。",
    },
    {
        "name": "Skyvern", "file": "Skyvern", "cat": "browser",
        "org": "Skyvern", "license": "AGPL-3.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["CV 视觉定位", "浏览器自动化", "表单填写", "反检测"],
        "github": "https://github.com/Skyvern-AI/skyvern",
        "website": "https://skyvern.com",
        "stars": "数万",
        "desc": "基于计算机视觉的浏览器自动化 Agent，擅长复杂网页交互。",
    },
    {
        "name": "Stagehand", "file": "Stagehand", "cat": "browser",
        "org": "Browserbase", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["AI 原生浏览器自动化", "act/extract/navigate 原语", "Playwright 集成"],
        "github": "https://github.com/browserbase/stagehand",
        "website": "https://stagehand.dev",
        "stars": "数万",
        "desc": "AI 原生的浏览器自动化框架，提供 act/extract/navigate 高级原语。",
    },

    # ════════════════════ Coding Agents ════════════════════
    {
        "name": "OpenCode", "file": "OpenCode", "cat": "coding",
        "org": "SST", "license": "MIT", "lang": "Go / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端原生编码 Agent", "75+ 模型供应商", "Claude Code 开源替代", "多模型切换"],
        "github": "https://github.com/sst/opencode",
        "website": "",
        "stars": "~172–180k",
        "desc": "目前最受欢迎的终端原生开源编码 Agent，支持 75+ 模型供应商，Claude Code 的开源替代。",
    },
    {
        "name": "Claude Code", "file": "ClaudeCode", "cat": "coding",
        "org": "Anthropic", "license": "源码可见/非开源", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端编码 Agent", "代码理解与生成", "工具调用", "MCP 支持"],
        "github": "https://github.com/anthropics/claude-code",
        "website": "https://anthropic.com",
        "stars": "~135k",
        "desc": "Anthropic 官方终端编码 Agent，仓库用于 issue/文档，核心闭源。",
    },
    {
        "name": "Gemini CLI", "file": "GeminiCLI", "cat": "coding",
        "org": "Google", "license": "Apache-2.0", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端 Agent", "内置搜索", "Shell 执行", "MCP 协议", "Gemini 模型"],
        "github": "https://github.com/google-gemini/gemini-cli",
        "website": "https://gemini.google.com",
        "stars": "~105k",
        "desc": "Google 官方开源终端 Agent，内置搜索、Shell、MCP 支持。",
    },
    {
        "name": "OpenAI Codex CLI", "file": "CodexCLI", "cat": "coding",
        "org": "OpenAI", "license": "Apache-2.0", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端编码 Agent", "代码生成", "沙盒执行", "多模型支持"],
        "github": "https://github.com/openai/codex",
        "website": "https://openai.com",
        "stars": "~90–95k",
        "desc": "OpenAI 官方开源终端编码 Agent。",
    },
    {
        "name": "Cline", "file": "Cline", "cat": "coding",
        "org": "Cline", "license": "Apache-2.0", "lang": "TypeScript",
        "platforms": "VS Code / JetBrains",
        "features": ["IDE 智能体插件", "人工审批每步操作", "独立 CLI/SDK", "多模型"],
        "github": "https://github.com/cline/cline",
        "website": "https://cline.bot",
        "stars": "~58–63k",
        "desc": "VS Code/JetBrains 智能体插件，人工审批每一步操作，现支持独立 CLI/SDK。",
    },
    {
        "name": "Aider", "file": "Aider", "cat": "coding",
        "org": "Aider", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["Git 原生结对编程", "自动 commit", "多模型支持", "终端交互"],
        "github": "https://github.com/paul-gauthier/aider",
        "website": "https://aider.chat",
        "stars": "~41–47k",
        "desc": "Git 原生终端结对编程工具，每次修改自动 commit。",
    },
    {
        "name": "Kilo Code", "file": "KiloCode", "cat": "coding",
        "org": "Kilo Code", "license": "MIT", "lang": "TypeScript",
        "platforms": "VS Code / JetBrains / CLI",
        "features": ["Cline+Roo Code 融合", "500+ 模型路由", "并行 Agent", "多 IDE"],
        "github": "https://github.com/kilocode/kilo-code",
        "website": "",
        "stars": "快速增长中",
        "desc": "Cline + Roo Code 融合平台，500+ 模型路由、并行 Agent。",
    },
    {
        "name": "Roo Code", "file": "RooCode", "cat": "coding",
        "org": "Roo Code", "license": "Apache-2.0", "lang": "TypeScript",
        "platforms": "VS Code / JetBrains",
        "features": ["多角色模式", "Cline 分支", "已归档 (2026-05)"],
        "github": "https://github.com/RooVetGit/Roo-Code",
        "website": "",
        "stars": "~22–24k",
        "desc": "Cline 分支，多角色模式，官方已于 2026 年 5 月归档停止维护，建议迁移。",
    },
    {
        "name": "Continue", "file": "Continue", "cat": "coding",
        "org": "Continue", "license": "Apache-2.0", "lang": "TypeScript",
        "platforms": "VS Code / JetBrains",
        "features": ["IDE 原生助手", "双端支持", "代码补全", "聊天交互"],
        "github": "https://github.com/continuedev/continue",
        "website": "https://continue.dev",
        "stars": "~26–31k",
        "desc": "VS Code + JetBrains 双端支持的 IDE 原生助手。",
    },
    {
        "name": "Tabby", "file": "Tabby", "cat": "coding",
        "org": "TabbyML", "license": "Apache-2.0", "lang": "Rust / Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["自托管代码补全", "GitHub Copilot 替代", "本地推理", "多模型"],
        "github": "https://github.com/TabbyML/tabby",
        "website": "https://tabby.tabbyml.com",
        "stars": "~33k",
        "desc": "自托管的 GitHub Copilot 开源替代，专注代码补全。",
    },
    {
        "name": "Goose", "file": "Goose", "cat": "coding",
        "org": "Block / Linux Foundation", "license": "Apache-2.0", "lang": "Rust / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["通用自动化 Agent", "编码 + 脚本 + 科研", "MCP 支持", "Linux 基金会"],
        "github": "https://github.com/block/goose",
        "website": "https://block.github.io/goose",
        "stars": "~32k",
        "desc": "通用自动化 Agent，编码之外还支持脚本/科研任务，已转入 Linux Foundation。",
    },
    {
        "name": "Crush", "file": "Crush", "cat": "coding",
        "org": "Charm", "license": "FSL (2年后转MIT)", "lang": "Go",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端编码 Agent", "Charm 生态集成", "TUI 界面"],
        "github": "https://github.com/charmbracelet/crush",
        "website": "",
        "stars": "增长中",
        "desc": "Charm 团队出品的终端编码 Agent，与 Charm 生态深度集成。",
    },
    {
        "name": "Qwen Code", "file": "QwenCode", "cat": "coding",
        "org": "阿里通义千问", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["终端编码 Agent", "Qwen 模型", "中文优化", "代码生成"],
        "github": "https://github.com/QwenLM/QwenCode",
        "website": "",
        "stars": "增长中",
        "desc": "阿里通义千问团队开源终端编码 Agent。",
    },
    {
        "name": "Pi", "file": "Pi", "cat": "coding",
        "org": "Community", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["懒加载技能系统", "轻量编码 harness", "插件化"],
        "github": "https://github.com/pi-hoc/pi",
        "website": "",
        "stars": "增长中",
        "desc": "懒加载技能系统的轻量编码 harness。",
    },
    {
        "name": "SWE-agent", "file": "SWEagent", "cat": "coding",
        "org": "Princeton NLP", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["自动解决 GitHub Issue", "学术界代表性", "沙盒执行", "PR 生成"],
        "github": "https://github.com/princeton-nlp/SWE-agent",
        "website": "https://swe-agent.com",
        "stars": "数万",
        "desc": "普林斯顿大学出品，学术界代表性的自动解决 GitHub issue 的 Agent。",
    },
    {
        "name": "Sweep", "file": "Sweep", "cat": "coding",
        "org": "Sweep AI", "license": "开源", "lang": "Python",
        "platforms": "GitHub",
        "features": ["Issue 自动转 PR", "代码搜索", "重构"],
        "github": "https://github.com/sweepai/sweep",
        "website": "https://sweep.dev",
        "stars": "数千~数万",
        "desc": "把 GitHub issue 自动转成 PR。",
    },
    {
        "name": "GPT Engineer", "file": "GPTEngineer", "cat": "coding",
        "org": "GPT Engineer", "license": "Apache-2.0 / MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["一句话生成项目", "脚手架生成", "全栈应用"],
        "github": "https://github.com/gpt-engineer-org/gpt-engineer",
        "website": "https://gptengineer.com",
        "stars": "数万",
        "desc": "一句话生成完整项目脚手架。",
    },
    {
        "name": "Devika", "file": "Devika", "cat": "coding",
        "org": "Devika AI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["开源版 Devin", "自主软件工程", "浏览器搜索", "代码生成"],
        "github": "https://github.com/DevikaAI/devika",
        "website": "",
        "stars": "数万",
        "desc": "开源版 Devin，自主软件工程师 Agent。",
    },
    {
        "name": "bolt.diy", "file": "BoltDIY", "cat": "coding",
        "org": "StackBlitz", "license": "MIT", "lang": "TypeScript",
        "platforms": "浏览器",
        "features": ["浏览器内全栈应用生成", "实时预览", "WebContainer"],
        "github": "https://github.com/stackblitz-labs/bolt.diy",
        "website": "https://bolt.new",
        "stars": "~19k",
        "desc": "bolt.new 社区版，浏览器内全栈应用生成与编辑。",
    },
    {
        "name": "Plandex", "file": "Plandex", "cat": "coding",
        "org": "Plandex", "license": "开源(核心)", "lang": "Go / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["超大上下文 (100万+ token)", "终端编码 Agent", "文件分支", "多步骤规划"],
        "github": "https://github.com/plandex-ai/plandex",
        "website": "",
        "stars": "数千~数万",
        "desc": "面向超大上下文（100万+ token）的终端编码 Agent。",
    },
    {
        "name": "Nanocoder", "file": "Nanocoder", "cat": "coding",
        "org": "Nano Collective", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["默认本地推理", "Ollama/LM Studio 支持", "隐私优先"],
        "github": "https://github.com/nano-code/nanocoder",
        "website": "",
        "stars": "~2k+",
        "desc": "Nano Collective 出品，默认本地推理（Ollama/LM Studio）的终端编码 Agent。",
    },
    {
        "name": "Forge", "file": "Forge", "cat": "coding",
        "org": "Community", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["供应商无关", "终端编码 Agent", "多模型切换"],
        "github": "https://github.com/Forge-Open-Source/forge",
        "website": "",
        "stars": "增长中",
        "desc": "供应商无关的终端编码 Agent。",
    },
    {
        "name": "Trae Agent", "file": "TraeAgent", "cat": "coding",
        "org": "字节跳动", "license": "开源", "lang": "TypeScript",
        "platforms": "VS Code",
        "features": ["IDE 编码 Agent", "2026年2月 Trending 第一", "多模型支持"],
        "github": "https://github.com/anthropics/trae-agent",
        "website": "",
        "stars": "~25k",
        "desc": "字节跳动出品，2026 年 2 月 GitHub Trending 第一。",
    },
    {
        "name": "Cursor Agent", "file": "CursorAgent", "cat": "coding",
        "org": "Anysphere", "license": "专有", "lang": "TypeScript",
        "platforms": "macOS / Windows",
        "features": ["AI IDE 编码助手", "多模型切换", "Tab 补全", "Agent 模式"],
        "github": "",
        "website": "https://cursor.com",
        "stars": "专有产品",
        "desc": "Cursor IDE 内置的 AI 编程助手，支持 Agent 模式、代码补全、多模型切换。",
    },
    {
        "name": "ECC", "file": "ECC", "cat": "coding",
        "org": "Community", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["Agent Harness 性能优化", "Claude Code/Codex/Cursor 加速", "2026 增速最快之一"],
        "github": "https://github.com/anthropics/ecc",
        "website": "",
        "stars": "~210k",
        "desc": "Claude Code/Codex/Cursor 等的性能优化系统，2026 增速最快项目之一。",
    },

    # ════════════════════ Mobile Agents ════════════════════
    # (placeholder - no projects yet)

    # ════════════════════ Multi-Agent ════════════════════
    {
        "name": "LangGraph", "file": "LangGraph", "cat": "multi_agent",
        "org": "LangChain", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["有向图状态化工作流", "LangChain 官方", "生产级方案", "Human-in-the-loop"],
        "github": "https://github.com/langchain-ai/langgraph",
        "website": "https://langchain.com",
        "stars": "数万",
        "desc": "基于有向图的状态化 Agent 工作流，LangChain 官方生产级方案。",
    },
    {
        "name": "LangChain", "file": "LangChain", "cat": "multi_agent",
        "org": "LangChain", "license": "MIT", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["LLM 应用开发框架", "最大生态", "Tool Use", "Chain 编排"],
        "github": "https://github.com/langchain-ai/langchain",
        "website": "https://langchain.com",
        "stars": "数十万",
        "desc": "最早、生态最大的 LLM 应用开发框架。",
    },
    {
        "name": "CrewAI", "file": "CrewAI", "cat": "multi_agent",
        "org": "CrewAI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["角色扮演式多智能体协作", "上手最快", "任务委派", "流程编排"],
        "github": "https://github.com/crewAIInc/crewAI",
        "website": "https://crewai.com",
        "stars": "~31k",
        "desc": "角色扮演式多智能体协作框架，上手最快。",
    },
    {
        "name": "AutoGen", "file": "AutoGen", "cat": "multi_agent",
        "org": "Microsoft Research", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["对话式多智能体", "微软研究院出品", "代码执行", "人机协作"],
        "github": "https://github.com/microsoft/autogen",
        "website": "https://microsoft.github.io/autogen",
        "stars": "~42k",
        "desc": "对话式多智能体框架，微软研究院出品。",
    },
    {
        "name": "MetaGPT", "file": "MetaGPT", "cat": "multi_agent",
        "org": "DeepWisdom", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["软件公司模拟器", "PM/架构师/工程师/QA 多角色", "自动生成代码"],
        "github": "https://github.com/geekan/MetaGPT",
        "website": "",
        "stars": "数万",
        "desc": "软件公司模拟器：PM/架构师/工程师/QA 多角色自动生成代码。",
    },
    {
        "name": "AutoGPT", "file": "AutoGPT", "cat": "multi_agent",
        "org": "Significant Gravitas", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["全自动通用 Agent", "最早出圈", "自我反思", "工具调用"],
        "github": "https://github.com/Significant-Gravitas/AutoGPT",
        "website": "https://agpt.co",
        "stars": "数十万(历史最高峰)",
        "desc": "最早出圈的全自动通用 Agent 项目。",
    },
    {
        "name": "BabyAGI", "file": "BabyAGI", "cat": "multi_agent",
        "org": "Yohei Nakajima", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["任务驱动自主 Agent", "任务创建/优先/执行循环", "轻量级"],
        "github": "https://github.com/yoheinakajima/babyagi",
        "website": "",
        "stars": "数万",
        "desc": "任务驱动的自主 Agent 雏形项目。",
    },
    {
        "name": "SuperAGI", "file": "SuperAGI", "cat": "multi_agent",
        "org": "SuperAGI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["带 GUI 的多智能体基础设施", "工具市场", "Agent 管理"],
        "github": "https://github.com/TransformerOptimus/SuperAGI",
        "website": "",
        "stars": "数万",
        "desc": "带 GUI 的多智能体基础设施平台。",
    },
    {
        "name": "AgentGPT", "file": "AgentGPT", "cat": "multi_agent",
        "org": "Reworkd", "license": "开源", "lang": "TypeScript",
        "platforms": "浏览器",
        "features": ["浏览器端零代码", "自主 Agent", "任务定义"],
        "github": "https://github.com/reworkd/AgentGPT",
        "website": "",
        "stars": "数万",
        "desc": "浏览器端零代码自主 Agent。",
    },
    {
        "name": "XAgent", "file": "XAgent", "cat": "multi_agent",
        "org": "清华大学", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["双循环自主 Agent", "清华系出品", "规划+执行"],
        "github": "https://github.com/thu-coai/XAgent",
        "website": "",
        "stars": "数万",
        "desc": "清华系出品的双循环自主 Agent。",
    },
    {
        "name": "ChatDev", "file": "ChatDev", "cat": "multi_agent",
        "org": "OpenBMB", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["多智能体虚拟软件公司", "角色扮演", "瀑布流开发"],
        "github": "https://github.com/OpenBMB/ChatDev",
        "website": "",
        "stars": "数万",
        "desc": "多智能体虚拟软件公司框架。",
    },
    {
        "name": "Camel-AI", "file": "CamelAI", "cat": "multi_agent",
        "org": "CAMEL-AI", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["多智能体角色扮演通信", "社会仿真", "任务协作"],
        "github": "https://github.com/camel-ai/camel",
        "website": "https://camel-ai.org",
        "stars": "数万",
        "desc": "多智能体角色扮演通信框架。",
    },
    {
        "name": "Agno", "file": "Agno", "cat": "multi_agent",
        "org": "Agno (原 Phidata)", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["轻量级多模态 Agent", "快速构建", "工具集成"],
        "github": "https://github.com/agno-agi/agno",
        "website": "https://agno.com",
        "stars": "数万",
        "desc": "轻量级多模态 Agent 构建框架（原 Phidata）。",
    },
    {
        "name": "Letta", "file": "Letta", "cat": "multi_agent",
        "org": "Letta (原 MemGPT)", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["长期记忆", "状态化 Agent", "无限上下文"],
        "github": "https://github.com/letta-ai/letta",
        "website": "https://letta.com",
        "stars": "数万",
        "desc": "长期记忆与状态化 Agent 框架（原 MemGPT）。",
    },
    {
        "name": "Smolagents", "file": "Smolagents", "cat": "multi_agent",
        "org": "HuggingFace", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["极简代码驱动 Agent", "HuggingFace 官方", "工具调用"],
        "github": "https://github.com/huggingface/smolagents",
        "website": "",
        "stars": "~15k",
        "desc": "极简代码驱动 Agent，HuggingFace 官方出品。",
    },
    {
        "name": "Semantic Kernel", "file": "SemanticKernel", "cat": "multi_agent",
        "org": "Microsoft", "license": "MIT", "lang": "C# / Python / Java",
        "platforms": "Windows / macOS / Linux",
        "features": [".NET/Java/Python 三端一致", "企业级 Agent SDK", "Plugin 系统"],
        "github": "https://github.com/microsoft/semantic-kernel",
        "website": "https://learn.microsoft.com/semantic-kernel",
        "stars": "数万",
        "desc": ".NET/Java/Python 三端一致的企业级 Agent SDK。",
    },
    {
        "name": "Google ADK", "file": "GoogleADK", "cat": "multi_agent",
        "org": "Google", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["Agent 开发套件", "Gemini/Vertex 原生对接", "MCP 支持"],
        "github": "https://github.com/google/adk-python",
        "website": "",
        "stars": "增长中",
        "desc": "Google Agent 开发套件，原生对接 Gemini/Vertex。",
    },
    {
        "name": "OpenAI Agents SDK", "file": "OpenAIAgentsSDK", "cat": "multi_agent",
        "org": "OpenAI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["官方 Agent SDK", "Handoff", "Guardrails", "Tracing"],
        "github": "https://github.com/openai/openai-agents-python",
        "website": "https://openai.com",
        "stars": "~27k",
        "desc": "OpenAI 官方 Agent SDK：handoff、guardrails、tracing。",
    },
    {
        "name": "Pydantic AI", "file": "PydanticAI", "cat": "multi_agent",
        "org": "Pydantic", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["类型安全 Python Agent", "Pydantic 集成", "依赖注入", "结构化输出"],
        "github": "https://github.com/pydantic/pydantic-ai",
        "website": "",
        "stars": "数万",
        "desc": "类型安全的 Python Agent 框架。",
    },
    {
        "name": "DSPy", "file": "DSPy", "cat": "multi_agent",
        "org": "Stanford NLP", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["编程方式优化 Prompt", "自动调优", "模块化", "研究型框架"],
        "github": "https://github.com/stanfordnlp/dspy",
        "website": "https://dspy.ai",
        "stars": "数万",
        "desc": "斯坦福出品，用编程方式自动优化 Prompt 的研究型框架。",
    },
    {
        "name": "STORM", "file": "STORM", "cat": "multi_agent",
        "org": "Stanford", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["学术写作 Agent", "长文报告生成", "多智能体协作"],
        "github": "https://github.com/stanford-oval/storm",
        "website": "",
        "stars": "~28k",
        "desc": "斯坦福出品，学术写作/长文报告生成 Agent。",
    },
    {
        "name": "LaVague", "file": "LaVague", "cat": "multi_agent",
        "org": "LaVague", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["动作序列编排", "Web Agent", "浏览器自动化"],
        "github": "https://github.com/lavague-ai/LaVague",
        "website": "https://lavague.ai",
        "stars": "数万",
        "desc": "Web Agent 动作序列编排框架，支持浏览器自动化。",
    },

    # ════════════════════ MCP ════════════════════
    {
        "name": "MCP Gateway", "file": "MCPGateway", "cat": "mcp",
        "org": "Community", "license": "MIT", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["MCP 服务器网关", "工具聚合", "多服务器管理"],
        "github": "https://github.com/modelcontextprotocol/servers",
        "website": "https://modelcontextprotocol.io",
        "stars": "数万",
        "desc": "MCP 官方服务器网关，聚合和管理多个 MCP 服务器。",
    },
    {
        "name": "Composio", "file": "Composio", "cat": "mcp",
        "org": "Composio", "license": "开源", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["万能胶水工具", "MCP 集成", "200+ 应用对接", "认证管理"],
        "github": "https://github.com/composio/composio",
        "website": "https://composio.dev",
        "stars": "数万",
        "desc": "Agent 的万能胶水工具，200+ 应用集成，MCP 原生支持。",
    },
    {
        "name": "FastMCP", "file": "FastMCP", "cat": "mcp",
        "org": "Jlowin", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["MCP 开发框架", "快速构建 MCP Server", "装饰器 API"],
        "github": "https://github.com/jlowin/fastmcp",
        "website": "",
        "stars": "数万",
        "desc": "快速构建 MCP Server 的开发框架，装饰器 API 极简上手。",
    },
    {
        "name": "BrowserMCP", "file": "BrowserMCP", "cat": "mcp",
        "org": "Community", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["浏览器 MCP Server", "网页操作工具", "Playwright 集成"],
        "github": "https://github.com/anthropics/mcp-browser",
        "website": "",
        "stars": "数千",
        "desc": "浏览器操作的 MCP Server，让 Agent 通过 MCP 协议控制浏览器。",
    },
    {
        "name": "Playwright MCP", "file": "PlaywrightMCP", "cat": "mcp",
        "org": "Microsoft", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["Playwright MCP Server", "浏览器自动化", "截图/点击/输入"],
        "github": "https://github.com/microsoft/playwright-mcp",
        "website": "",
        "stars": "数千",
        "desc": "微软出品的 Playwright MCP Server，通过 MCP 协议提供浏览器自动化能力。",
    },

    # ════════════════════ RAG ════════════════════
    {
        "name": "LlamaIndex", "file": "LlamaIndex", "cat": "rag",
        "org": "LlamaIndex", "license": "MIT", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["RAG 生态龙头", "数据索引", "查询引擎", "Agent 集成"],
        "github": "https://github.com/run-llama/llama_index",
        "website": "https://llamaindex.ai",
        "stars": "数十万",
        "desc": "数据检索增强型 Agent 框架，RAG 生态龙头。",
    },
    {
        "name": "Haystack", "file": "Haystack", "cat": "rag",
        "org": "deepset", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["生产级 RAG", "Agent 编排", "Pipeline 架构", "组件化"],
        "github": "https://github.com/deepset-ai/haystack",
        "website": "https://haystack.deepset.ai",
        "stars": "数万",
        "desc": "生产级 RAG + Agent 编排框架。",
    },
    {
        "name": "RAGFlow", "file": "RAGFlow", "cat": "rag",
        "org": "InfiniFlow", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux / Docker",
        "features": ["深度融合 RAG+Agent", "深度文档解析", "知识图谱"],
        "github": "https://github.com/infiniflow/ragflow",
        "website": "",
        "stars": "数万",
        "desc": "深度融合 RAG + Agent 的检索增强引擎。",
    },
    {
        "name": "Dify", "file": "Dify", "cat": "rag",
        "org": "Dify.AI", "license": "开源", "lang": "Python / TypeScript",
        "platforms": "Docker / 云服务",
        "features": ["LLM 应用开发平台", "可视化编排", "Agent + RAG", "插件市场"],
        "github": "https://github.com/langgenius/dify",
        "website": "https://dify.ai",
        "stars": "数十万",
        "desc": "LLM 应用开发平台，可视化编排 Agent 与 RAG。",
    },
    {
        "name": "FastGPT", "file": "FastGPT", "cat": "rag",
        "org": "FastAI", "license": "开源", "lang": "TypeScript",
        "platforms": "Docker",
        "features": ["国产开源知识库", "Agent 搭建", "可视化编排"],
        "github": "https://github.com/labring/FastGPT",
        "website": "",
        "stars": "数万",
        "desc": "国产开源知识库 + Agent 搭建平台。",
    },
    {
        "name": "Flowise", "file": "Flowise", "cat": "rag",
        "org": "FlowiseAI", "license": "开源", "lang": "TypeScript",
        "platforms": "Docker / npm",
        "features": ["拖拽式工作流", "LLM/Agent 构建器", "无代码"],
        "github": "https://github.com/FlowiseAI/Flowise",
        "website": "https://flowiseai.com",
        "stars": "数万",
        "desc": "拖拽式 LLM/Agent 工作流构建器。",
    },
    {
        "name": "Langflow", "file": "Langflow", "cat": "rag",
        "org": "Langflow", "license": "开源", "lang": "Python",
        "platforms": "Docker / 云服务",
        "features": ["可视化 LangChain 编排", "拖拽式", "API 自动生成"],
        "github": "https://github.com/langflow-ai/langflow",
        "website": "https://langflow.org",
        "stars": "数万",
        "desc": "可视化 LangChain 工作流编排。",
    },
    {
        "name": "n8n", "file": "N8n", "cat": "rag",
        "org": "n8n", "license": "Fair-code (核心开源)", "lang": "TypeScript",
        "platforms": "Docker / npm",
        "features": ["通用工作流自动化", "AI Agent 节点", "400+ 集成", "自托管"],
        "github": "https://github.com/n8n-io/n8n",
        "website": "https://n8n.io",
        "stars": "数十万",
        "desc": "通用工作流自动化平台，AI Agent 节点日益完善。",
    },
    {
        "name": "Activepieces", "file": "Activepieces", "cat": "rag",
        "org": "Activepieces", "license": "MIT", "lang": "TypeScript",
        "platforms": "Docker",
        "features": ["开源自动化工作流", "MCP/Agent 集成", "无代码"],
        "github": "https://github.com/activepieces/activepieces",
        "website": "https://activepieces.com",
        "stars": "数万",
        "desc": "开源自动化工作流平台，MCP/Agent 集成。",
    },
    {
        "name": "CopilotKit", "file": "CopilotKit", "cat": "rag",
        "org": "CopilotKit", "license": "MIT", "lang": "TypeScript",
        "platforms": "Web",
        "features": ["嵌入式 AI Copilot", "React 集成", "CoAgent", "Agent 可视化"],
        "github": "https://github.com/CopilotKit/CopilotKit",
        "website": "https://copilotkit.ai",
        "stars": "数万",
        "desc": "将自定义 AI Copilot 嵌入 React 应用的开源框架。",
    },

    # ════════════════════ Memory ════════════════════
    {
        "name": "Mem0", "file": "Mem0", "cat": "memory",
        "org": "Mem0 Labs", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["Agent 长期记忆层", "跨会话持久化", "知识图谱", "自适应记忆"],
        "github": "https://github.com/mem0ai/mem0",
        "website": "https://mem0.ai",
        "stars": "数万",
        "desc": "面向 Agent 的长期记忆层。",
    },
    {
        "name": "OpenMemory", "file": "OpenMemory", "cat": "memory",
        "org": "Community", "license": "MIT", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["跨会话持久化上下文", "Claude Code/Codex/Gemini 兼容", "本地优先"],
        "github": "https://github.com/openmemory/openmemory",
        "website": "",
        "stars": "增长中",
        "desc": "跨会话持久化上下文，兼容 Claude Code/Codex/Gemini 等。",
    },
    {
        "name": "Graphiti", "file": "Graphiti", "cat": "memory",
        "org": "Zep AI", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["知识图谱记忆", "时序感知", "Neo4j 集成", "实时更新"],
        "github": "https://github.com/getzep/graphiti",
        "website": "",
        "stars": "数千",
        "desc": "基于知识图谱的 Agent 记忆系统，时序感知，Neo4j 驱动。",
    },
    {
        "name": "Supermemory", "file": "Supermemory", "cat": "memory",
        "org": "Supermemory", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["跨会话持久化", "Claude Code/Codex/Gemini 兼容", "语义搜索"],
        "github": "https://github.com/supermemoryai/supermemory",
        "website": "https://supermemory.ai",
        "stars": "增长中",
        "desc": "跨会话持久化上下文，兼容主流编码 Agent。",
    },

    # ════════════════════ Search ════════════════════
    {
        "name": "Firecrawl", "file": "Firecrawl", "cat": "search",
        "org": "Mendable AI", "license": "AGPL-3.0", "lang": "TypeScript",
        "platforms": "Docker / 云服务",
        "features": ["网页抓取转 Markdown", "结构化数据提取", "批量爬取", "JS 渲染"],
        "github": "https://github.com/mendableai/firecrawl",
        "website": "https://firecrawl.dev",
        "stars": "~130k",
        "desc": "网页抓取转 Markdown/结构化数据，Agent 的网络之眼。",
    },
    {
        "name": "Crawl4AI", "file": "Crawl4AI", "cat": "search",
        "org": "UncleCode", "license": "开源", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["面向 LLM 优化", "爬虫框架", "批量爬取", "Markdown 输出"],
        "github": "https://github.com/unclecode/crawl4ai",
        "website": "",
        "stars": "数万",
        "desc": "面向 LLM 优化的爬虫框架。",
    },
    {
        "name": "ScrapeGraph AI", "file": "ScrapeGraphAI", "cat": "search",
        "org": "ScrapeGraphAI", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["AI 驱动爬虫", "自然语言定义抓取", "多源支持"],
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai",
        "website": "",
        "stars": "数万",
        "desc": "AI 驱动的智能爬虫，用自然语言定义抓取任务。",
    },

    # ════════════════════ Voice Agent ════════════════════
    # (placeholder - no projects yet)

    # ════════════════════ Robotics ════════════════════
    # (placeholder - no projects yet)

    # ════════════════════ Benchmark ════════════════════
    # (placeholder - no projects yet)

    # ════════════════════ AI Chat Platforms ════════════════════
    {
        "name": "Open WebUI", "file": "OpenWebUI", "cat": "chat",
        "org": "Open WebUI", "license": "BSD-3", "lang": "Python / TypeScript",
        "platforms": "Docker / 本地",
        "features": ["自托管 ChatGPT 式界面", "Agent 支持", "工具调用", "多模型"],
        "github": "https://github.com/open-webui/open-webui",
        "website": "",
        "stars": "数万",
        "desc": "自托管的 ChatGPT 式 Web 界面，支持 Agent 与工具调用。",
    },
    {
        "name": "LobeChat", "file": "LobeChat", "cat": "chat",
        "org": "LobeHub", "license": "开源", "lang": "TypeScript",
        "platforms": "Web / Docker",
        "features": ["现代化 AI 聊天框架", "插件市场", "Agent 市场", "多模型"],
        "github": "https://github.com/lobehub/lobe-chat",
        "website": "https://lobehub.com",
        "stars": "数万",
        "desc": "现代化开源 AI 聊天框架，插件与 Agent 市场。",
    },
    {
        "name": "Cherry Studio", "file": "CherryStudio", "cat": "chat",
        "org": "Cherry Studio", "license": "开源", "lang": "TypeScript",
        "platforms": "macOS / Windows / Linux",
        "features": ["桌面端多模型 AI 助手", "多模型切换", "翻译助手"],
        "github": "https://github.com/CherryHQ/cherry-studio",
        "website": "",
        "stars": "数万",
        "desc": "桌面端多模型 AI 助手客户端。",
    },
    {
        "name": "AnythingLLM", "file": "AnythingLLM", "cat": "chat",
        "org": "Mintplex Labs", "license": "MIT", "lang": "JavaScript",
        "platforms": "Docker / 本地",
        "features": ["全栈私有化知识库", "Agent 应用", "多模型", "RAG"],
        "github": "https://github.com/Mintplex-Labs/anything-llm",
        "website": "https://anythingllm.com",
        "stars": "数万",
        "desc": "全栈私有化知识库 + Agent 应用。",
    },
    {
        "name": "LibreChat", "file": "LibreChat", "cat": "chat",
        "org": "LibreChat", "license": "MIT", "lang": "TypeScript",
        "platforms": "Docker",
        "features": ["多模型聚合", "ChatGPT 替代", "插件系统", "多用户"],
        "github": "https://github.com/danny-avila/LibreChat",
        "website": "",
        "stars": "数万",
        "desc": "多模型聚合的开源 ChatGPT 替代。",
    },
    {
        "name": "big-AGI", "file": "BigAGI", "cat": "chat",
        "org": "big-AGI", "license": "MIT", "lang": "TypeScript",
        "platforms": "Web / Docker",
        "features": ["功能丰富 AI 聊天", "Agent 客户端", "多模型", "语音"],
        "github": "https://github.com/enricoros/big-agi",
        "website": "",
        "stars": "数万",
        "desc": "功能丰富的开源 AI 聊天/Agent 客户端。",
    },
    {
        "name": "Jan", "file": "Jan", "cat": "chat",
        "org": "Jan", "license": "开源", "lang": "TypeScript",
        "platforms": "macOS / Windows / Linux",
        "features": ["完全离线优先", "ChatGPT 替代", "本地模型", "隐私优先"],
        "github": "https://github.com/janhq/jan",
        "website": "https://jan.ai",
        "stars": "数万",
        "desc": "完全离线优先的开源 ChatGPT 替代客户端。",
    },

    # ════════════════════ Local Inference ════════════════════
    {
        "name": "Ollama", "file": "Ollama", "cat": "local",
        "org": "Ollama", "license": "MIT", "lang": "Go",
        "platforms": "macOS / Windows / Linux",
        "features": ["一条命令本地运行 LLM", "模型库", "API 兼容", "Agent 本地化首选"],
        "github": "https://github.com/ollama/ollama",
        "website": "https://ollama.com",
        "stars": "~162k",
        "desc": "一条命令本地运行 LLM 的 CLI 工具，Agent 本地化首选。",
    },
    {
        "name": "llama.cpp", "file": "LlamaCpp", "cat": "local",
        "org": "Georgi Gerganov", "license": "MIT", "lang": "C/C++",
        "platforms": "Windows / macOS / Linux",
        "features": ["C/C++ 本地推理引擎", "生态基石", "GGUF 格式", "CPU/GPU"],
        "github": "https://github.com/ggerganov/llama.cpp",
        "website": "",
        "stars": "数十万",
        "desc": "C/C++ 实现的 LLM 本地推理引擎，生态基石。",
    },
    {
        "name": "vLLM", "file": "vLLM", "cat": "local",
        "org": "vLLM Team", "license": "Apache-2.0", "lang": "Python / C++",
        "platforms": "Linux",
        "features": ["高吞吐 LLM 推理", "PagedAttention", "连续批处理", "分布式推理"],
        "github": "https://github.com/vllm-project/vllm",
        "website": "https://vllm.ai",
        "stars": "数万",
        "desc": "高吞吐 LLM 推理引擎，PagedAttention 技术。",
    },
    {
        "name": "GPT4All", "file": "GPT4All", "cat": "local",
        "org": "Nomic AI", "license": "开源", "lang": "C++ / Python",
        "platforms": "macOS / Windows / Linux",
        "features": ["无需联网", "消费级硬件可跑", "本地聊天", "隐私优先"],
        "github": "https://github.com/nomic-ai/gpt4all",
        "website": "https://gpt4all.io",
        "stars": "数万",
        "desc": "无需联网、消费级硬件可跑的本地聊天应用。",
    },
    {
        "name": "LocalAI", "file": "LocalAI", "cat": "local",
        "org": "LocalAI", "license": "MIT", "lang": "Go",
        "platforms": "Docker / 本地",
        "features": ["OpenAI API 兼容", "本地推理服务器", "多模态", "CPU/GPU"],
        "github": "https://github.com/mudler/LocalAI",
        "website": "",
        "stars": "数万",
        "desc": "OpenAI API 兼容的本地推理服务器。",
    },
    {
        "name": "text-generation-webui", "file": "TextGenerationWebUI", "cat": "local",
        "org": "oobabooga", "license": "MIT", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["本地大模型 Web UI", "API 端点", "多模型加载", "角色扮演"],
        "github": "https://github.com/oobabooga/text-generation-webui",
        "website": "",
        "stars": "数万",
        "desc": "本地大模型的 Web UI 与 API。",
    },
    {
        "name": "koboldcpp", "file": "KoboldCpp", "cat": "local",
        "org": "KoboldAI", "license": "MIT", "lang": "C++",
        "platforms": "Windows / macOS / Linux",
        "features": ["面向创作/角色扮演", "本地推理后端", "GGUF 支持", "Web UI"],
        "github": "https://github.com/LostRuins/koboldcpp",
        "website": "",
        "stars": "数万",
        "desc": "面向创作/角色扮演的本地推理后端。",
    },

    # ════════════════════ AI IDE / Editor ════════════════════
    {
        "name": "VSCodium", "file": "VSCodium", "cat": "ide",
        "org": "VSCodium", "license": "MIT", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["去微软遥测", "VS Code 开源构建", "完全兼容"],
        "github": "https://github.com/VSCodium/vscodium",
        "website": "https://vscodium.com",
        "stars": "数万",
        "desc": "去微软遥测的 VS Code 开源构建版。",
    },
    {
        "name": "Void", "file": "Void", "cat": "ide",
        "org": "Void", "license": "开源", "lang": "TypeScript",
        "platforms": "VS Code Fork",
        "features": ["最接近 Cursor 的开源替代", "VS Code 分支", "AI Agent 模式"],
        "github": "https://github.com/voideditor/void",
        "website": "",
        "stars": "~28k (开发已暂停)",
        "desc": "最接近 Cursor 的开源 VS Code 分支（开发已暂停）。",
    },
    {
        "name": "Theia", "file": "Theia", "cat": "ide",
        "org": "Eclipse Foundation", "license": "EPL-2.0", "lang": "TypeScript",
        "platforms": "Windows / macOS / Linux / 浏览器",
        "features": ["云端/桌面双用", "开源 IDE 框架", "AI Agent 嵌入", "Eclipse 基金会"],
        "github": "https://github.com/eclipse-theia/theia",
        "website": "https://theia-ide.org",
        "stars": "数万",
        "desc": "云端/桌面双用的开源 IDE 框架，可深度嵌入 AI Agent。",
    },
    {
        "name": "Zed", "file": "Zed", "cat": "ide",
        "org": "Zed Industries", "license": "开源", "lang": "Rust",
        "platforms": "macOS / Linux",
        "features": ["Rust 高性能协作编辑", "AI Agent 模式", "实时协作"],
        "github": "https://github.com/zed-industries/zed",
        "website": "https://zed.dev",
        "stars": "数万",
        "desc": "Rust 编写的高性能协作编辑器，内置 AI Agent 模式。",
    },
    {
        "name": "Lapce", "file": "Lapce", "cat": "ide",
        "org": "Lapce", "license": "MIT", "lang": "Rust",
        "platforms": "Windows / macOS / Linux",
        "features": ["Rust 高性能编辑器", "插件化 AI 能力", "远程开发"],
        "github": "https://github.com/lapce/lapce",
        "website": "https://lapce.dev",
        "stars": "数万",
        "desc": "Rust 高性能编辑器，插件化 AI 能力。",
    },
    {
        "name": "JupyterLab", "file": "JupyterLab", "cat": "ide",
        "org": "Project Jupyter", "license": "BSD-3", "lang": "Python / TypeScript",
        "platforms": "Windows / macOS / Linux",
        "features": ["Notebook 生态", "AI Agent 集成", "代码执行", "可视化"],
        "github": "https://github.com/jupyterlab/jupyterlab",
        "website": "https://jupyter.org",
        "stars": "数万",
        "desc": "Notebook 生态中集成 AI Agent 与代码执行。",
    },
    {
        "name": "code-server", "file": "Codeserver", "cat": "ide",
        "org": "Coder", "license": "MIT", "lang": "TypeScript",
        "platforms": "浏览器 / Docker",
        "features": ["VS Code 跑在浏览器", "AI Agent 沙盒 IDE", "远程开发"],
        "github": "https://github.com/coder/code-server",
        "website": "https://coder.com",
        "stars": "数万",
        "desc": "让 VS Code 跑在浏览器里，常被用作 AI Agent 沙盒 IDE。",
    },

    # ════════════════════ Security & Sandbox ════════════════════
    {
        "name": "E2B", "file": "E2B", "cat": "security",
        "org": "E2B", "license": "开源", "lang": "TypeScript / Python",
        "platforms": "云服务",
        "features": ["AI Agent 安全沙盒", "云端代码执行", "Firecracker microVM", "快速启动"],
        "github": "https://github.com/e2b-dev/E2B",
        "website": "https://e2b.dev",
        "stars": "数万",
        "desc": "为 AI Agent 提供安全云端代码执行沙盒。",
    },
    {
        "name": "Daytona", "file": "Daytona", "cat": "security",
        "org": "Daytona", "license": "开源", "lang": "Go",
        "platforms": "Docker / 云服务",
        "features": ["开发环境管理", "Agent 执行沙盒", "一键环境创建"],
        "github": "https://github.com/daytonaio/daytona",
        "website": "https://daytona.io",
        "stars": "增长中",
        "desc": "开发环境 / Agent 执行沙盒基础设施。",
    },
    {
        "name": "Guardrails AI", "file": "Guardrails", "cat": "security",
        "org": "Guardrails AI", "license": "Apache-2.0", "lang": "Python",
        "platforms": "Windows / macOS / Linux",
        "features": ["AI 行为阻断器", "输出验证", "幻觉检测", "内容过滤"],
        "github": "https://github.com/guardrails-ai/guardrails",
        "website": "https://guardrailsai.com",
        "stars": "数万",
        "desc": "AI 行为阻断器，验证 LLM 输出，检测幻觉。",
    },
]


def gen_md(p):
    """Generate unified format MD content for a project."""
    features_md = "\n".join(f"  - {f}" for f in p["features"])
    website_line = f"- 官网：{p['website']}" if p["website"] else ""
    github_line = f"- GitHub：{p['github']}" if p["github"] else f"- GitHub：暂无"

    return f"""# {p['name']}

- 类型：{CATEGORIES[p['cat']][0]}
- 开发组织：{p['org']}
- 开源协议：{p['license']}
- 编程语言：{p['lang']}
- 支持平台：{p['platforms']}
- 功能：
{features_md}
{github_line}
{website_line}
- Stars：{p['stars']}

> {p['desc']}

---
← 返回 [README](README.md)
"""


def gen_readme(projects):
    """Generate the new README with category-based navigation."""
    # Group projects by category
    by_cat = {}
    for p in projects:
        by_cat.setdefault(p["cat"], []).append(p)

    lines = [
        "# 🌐 Open-source-agents",
        "",
        "> **全球 AI Agent 开源工具导航**",
        "> 涵盖 Computer Agent、Browser Agent、Coding Agent、Multi-Agent、MCP、RAG、Memory、Search 等 12+ 分类。",
        "",
        f"共收录 **{len(projects)}** 个开源项目。",
        "",
        "---",
        "",
        "## 📋 分类总览",
        "",
    ]

    # Category overview with counts
    cat_order = [
        "computer", "browser", "coding", "mobile", "multi_agent",
        "mcp", "rag", "memory", "search", "voice", "robotics",
        "benchmark", "chat", "local", "ide", "security"
    ]

    for cat_key in cat_order:
        cat_name, cat_desc = CATEGORIES[cat_key]
        projs = by_cat.get(cat_key, [])
        count = len(projs)
        if count == 0:
            lines.append(f"- {cat_name} — {cat_desc}（即将收录）")
        else:
            lines.append(f"- {cat_name} — {cat_desc}（{count} 个项目）")

    lines.extend(["", "---", ""])

    # Each category section
    for cat_key in cat_order:
        cat_name, cat_desc = CATEGORIES[cat_key]
        projs = by_cat.get(cat_key, [])
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append(f"> {cat_desc}")
        lines.append("")

        if not projs:
            lines.append("*即将收录，敬请期待...*")
            lines.append("")
            continue

        lines.append("| # | 项目 | 开发组织 | 语言 | Stars | 简介 | 链接 |")
        lines.append("|:-:|------|---------|:----:|------:|------|------|")

        for i, p in enumerate(projs, 1):
            github_link = f"[→ 详情]({p['file']}.md)" if p["github"] else "暂无"
            desc_short = p["desc"][:40] + "..." if len(p["desc"]) > 40 else p["desc"]
            lines.append(
                f"| {i} | **{p['name']}** | {p['org']} | {p['lang']} | {p['stars']} | {desc_short} | {github_link} |"
            )

        lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        "## 🤝 贡献",
        "",
        "欢迎提交 Issue 和 PR，一起完善这个 AI Agent 导航项目！",
        "",
        "## 📄 许可证",
        "",
        "MIT License",
        "",
        "---",
        "",
        "*最后更新: 2026-07-05*",
    ])

    return "\n".join(lines)


# ── Main execution ──
if __name__ == "__main__":
    # Generate all MD files
    count = 0
    for p in PROJECTS:
        content = gen_md(p)
        filepath = os.path.join(REPO, f"{p['file']}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

    # Generate README
    readme_content = gen_readme(PROJECTS)
    readme_path = os.path.join(REPO, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Print summary
    by_cat = {}
    for p in PROJECTS:
        by_cat.setdefault(p["cat"], []).append(p)

    print(f"✅ Generated {count} project MD files")
    print(f"✅ Generated README.md")
    print()
    print("Category breakdown:")
    cat_order = [
        "computer", "browser", "coding", "mobile", "multi_agent",
        "mcp", "rag", "memory", "search", "voice", "robotics",
        "benchmark", "chat", "local", "ide", "security"
    ]
    for cat_key in cat_order:
        cat_name, _ = CATEGORIES[cat_key]
        projs = by_cat.get(cat_key, [])
        print(f"  {cat_name}: {len(projs)}")
