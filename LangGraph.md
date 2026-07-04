# LangGraph

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

## 简介

[LangGraph](https://github.com/langchain-ai/langgraph) 是 LangChain 团队推出的 **Agent 编排框架**，用于构建有状态、多角色的 LLM 应用，支持复杂的 Agent 工作流和循环执行。

⭐ **36.5k Stars** | 🍴 **5.8k Forks**

## 核心特性

| 特性 | 说明 |
|------|------|
| 🔄 状态管理 | 内置状态机，支持复杂的执行流程 |
| 🎭 多角色协作 | 支持多个 Agent 协同工作 |
| 🔁 循环执行 | 支持 Agent 循环和条件分支 |
| 💾 持久化 | 支持检查点和状态恢复 |
| 🔍 可观测性 | 内置调试和追踪能力 |
| 🌐 流式输出 | 支持实时流式响应 |

## 使用场景

- **复杂 Agent**：构建需要多步骤推理的智能体
- **人机协作**：设计人类介入的审批流程
- **工作流编排**：自动化业务流程和任务链
- **多 Agent 系统**：多个 Agent 协作完成复杂任务
- **状态机应用**：需要状态管理和转换的应用

## 快速开始

```bash
# 安装
pip install langgraph

# 基本用法
from langgraph.graph import StateGraph, MessagesState
from langchain_openai import ChatOpenAI

# 定义 Agent 节点
def agent(state: MessagesState):
    model = ChatOpenAI(model="gpt-4")
    response = model.invoke(state["messages"])
    return {"messages": [response]}

# 构建图
graph = StateGraph(MessagesState)
graph.add_node("agent", agent)
graph.set_entry_point("agent")
graph.set_finish_point("agent")

# 编译并运行
app = graph.compile()
result = app.invoke({"messages": [("user", "你好")]})
```

## 项目导航

← 返回 [README](README.md)

---
