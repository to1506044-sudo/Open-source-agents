# CrewAI

![CrewAI](https://img.shields.io/badge/CrewAI-FF6B35?style=for-the-badge&logo=crewai&logoColor=white)

## 简介

[CrewAI](https://github.com/crewAIInc/crewAI) 是一个 **多 Agent 协作框架**，通过角色扮演和自主协作，让多个 AI 智能体协同工作，共同完成复杂任务。

⭐ **54.9k Stars** | 🍴 **8.2k Forks**

## 核心特性

| 特性 | 说明 |
|------|------|
| 🎭 角色定义 | 为每个 Agent 定义专业角色和职责 |
| 🤝 协作机制 | Agent 之间自动协作和任务分配 |
| 🔄 任务流程 | 支持顺序和并行的任务执行 |
| 🧠 记忆系统 | 共享记忆和上下文管理 |
| 🔧 工具集成 | 丰富的工具和能力扩展 |
| 📊 可观测性 | 内置执行追踪和调试能力 |

## 使用场景

- **团队协作**：模拟团队协作，分工完成项目
- **内容创作**：多角色协作生成高质量内容
- **研究报告**：分工收集、分析、撰写研究报告
- **代码开发**：架构师、开发者、测试员协作开发
- **业务流程**：自动化复杂的业务工作流

## 快速开始

```bash
# 安装
pip install crewai

# 基本用法
from crewai import Agent, Task, Crew

# 定义 Agent
researcher = Agent(
    role="研究员",
    goal="收集和分析信息",
    backstory="你是一位经验丰富的研究员"
)

writer = Agent(
    role="作家",
    goal="撰写高质量文章",
    backstory="你是一位专业的技术作家"
)

# 定义任务
research_task = Task(
    description="研究 AI Agent 最新趋势",
    agent=researcher
)

write_task = Task(
    description="根据研究结果撰写报告",
    agent=writer
)

# 组建团队
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

# 执行
result = crew.kickoff()
```

## 项目导航

← 返回 [README](README.md)

---
