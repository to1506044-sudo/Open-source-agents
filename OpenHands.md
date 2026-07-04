# OpenHands

![OpenHands](https://img.shields.io/badge/OpenHands-FF6B35?style=for-the-badge&logo=github&logoColor=white)

## 简介

[OpenHands](https://github.com/OpenHands/OpenHands) 是一个 **AI 驱动的软件开发平台**，让 AI 智能体能够像人类开发者一样编写代码、修改文件、执行命令，完成端到端的软件开发任务。

⭐ **79.4k Stars** | 🍴 **8.5k Forks**

## 核心特性

| 特性 | 说明 |
|------|------|
| 🤖 AI 开发者 | 像人类一样编写和修改代码 |
| 💻 终端操作 | 执行 shell 命令和脚本 |
| 📁 文件管理 | 创建、读取、修改文件 |
| 🌐 浏览器控制 | 自动化网页操作和测试 |
| 🔧 工具集成 | 丰富的开发工具链支持 |
| 📊 可视化界面 | 提供直观的 Web UI 监控 |

## 使用场景

- **全栈开发**：从零开始构建完整应用
- **Bug 修复**：自动定位并修复代码问题
- **功能迭代**：根据需求自动添加新功能
- **代码重构**：大规模代码优化和结构调整
- **自动化测试**：生成和执行测试用例

## 快速开始

```bash
# Docker 方式（推荐）
docker pull docker.all-hands.dev/all-hands-ai/openhands:0.9

# 运行
docker run -it --pull always \
  -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.9-nikolaik \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -p 3000:3000 \
  docker.all-hands.dev/all-hands-ai/openhands:0.9
```

## 项目导航

← 返回 [README](README.md)

---
