##### 你说

claude code 的 skills 是系统提示词是吧

###### Copilot 说

不是严格意义上的“系统提示词”，但 **Claude Code 里的** `skills` **本质上扮演的是“系统提示词的一部分”**——它是一种结构化的、可声明的 **能力描述（capability declaration）**。

为了让你完全搞清楚，我把它拆开讲。

# 🧠 Claude Code 的 `skills` 是什么？

在 Claude Code（也就是 Claude 的代码助手模式）里，`skills` 是：

- 一组 **声明式能力描述**
    
- 用来告诉模型“你能做什么”
    
- 让模型在执行任务时更稳定、更可控
    

它不是传统意义上那种：

代码

复制

```
You are a helpful assistant...
```

这种自然语言系统提示词，而是：

> **一种结构化的系统级配置，用来定义模型的能力边界。**

# 🧩 它和系统提示词的关系

可以这样理解：

|项目|作用|
|---|---|
|**System Prompt（系统提示词）**|定义模型的角色、风格、行为规则|
|**Skills（能力声明）**|定义模型能做哪些事、能调用哪些工具、能执行哪些动作|

所以：

> `skills` 是系统提示词的一部分，但不是自然语言，而是结构化能力声明。

换句话说：

- 系统提示词告诉模型“你是谁”
    
- `skills` 告诉模型“你能做什么”
    

两者共同构成 Claude Code 的“系统层”。

# 🧱 为什么要用 `skills`？

因为 Claude Code 是一个 **代码助手**，需要：

- 明确知道哪些语言能写
    
- 哪些文件能读
    
- 哪些工具能调用
    
- 哪些操作被允许
    

自然语言系统提示词不够精确，所以 Anthropic 引入了 `skills` 作为结构化能力声明。

# 🎯 最精炼总结

- `skills` **不是传统系统提示词，但属于系统层配置**
    
- **它是结构化的能力声明，用来告诉模型能做什么**
    
- **系统提示词负责“角色”，skills 负责“能力”**
    

一句话：

> **Claude Code 的** `skills` **= 系统提示词的“能力模块化版本”。**

如果你愿意，我还能继续帮你：

- 解释 Claude Code 的完整系统提示结构
    
- 对比 OpenAI function calling / MCP / Claude skills 的差异
    
- 帮你设计一个自己的“skills + system prompt”结构
    

你想继续深入哪一块呢？

##### 你说

和 function calling 的区别

###### Copilot 说

下面给你一个真正“工程师视角”的对比，把 **Claude 的 Skills** 和 **OpenAI Function Calling** 的区别讲得非常清晰。两者经常被混为一谈，但它们的定位、能力边界和设计哲学完全不同。

# 🧩 一句话总结

- **Function Calling = LLM 调用单个函数的协议**
    
- **Claude Skills = 定义 Agent 能力边界的系统级能力声明**
    

换句话说：

> Function Calling 是“调用工具的接口” Skills 是“定义 Agent 能做什么的权限系统 + 能力模型”

它们不是同一层级的东西。

# 🧠 1. Function Calling 是什么？

Function Calling 的核心是：

- 给 LLM 一个函数列表
    
- 每个函数有 JSON Schema
    
- LLM 根据任务决定是否调用
    
- 返回结构化 JSON
    
- 你在外部执行函数并把结果返回给模型
    

它的本质是：

> **一个 LLM → 工具 的调用协议**

特点：

- 轻量
    
- 单次调用
    
- 只描述“怎么调用工具”
    
- 不描述“模型能做什么”
    
- 不描述“权限”
    
- 不描述“上下文能力”
    

# 🤖 2. Claude Skills 是什么？

Claude Skills 是：

- 一个 **系统级能力声明（capability declaration）**
    
- 用来告诉模型：
    
    - 你能做什么
        
    - 你能访问哪些资源
        
    - 你能执行哪些操作
        
    - 你有哪些权限
        
    - 你在什么上下文中工作
        

它的本质是：

> **一个 Agent 的能力模型（capability model）**

特点：

- 声明式
    
- 持久
    
- 系统级
    
- 定义 Agent 的“能力边界”
    
- 不只是工具，还包括：
    
    - 文件系统访问
        
    - 编辑代码
        
    - 运行命令
        
    - 搜索项目
        
    - 解释错误
        
    - 生成补丁
        
    - 甚至“你是一个代码助手”这种角色能力
        

Skills 是：

> **Agent 的“权限系统 + 能力清单 + 行为范围”**

而不是单纯的工具调用。

# 🧩 3. 两者的核心区别（最关键的部分）

|维度|Function Calling|Claude Skills|
|---|---|---|
|本质|工具调用协议|Agent 能力声明|
|作用|让 LLM 调用函数|定义 LLM 能做什么、能访问什么|
|范围|单个函数|整个 Agent 的能力模型|
|权限|无|有（文件、命令、编辑等）|
|上下文|无|有（项目结构、文件系统）|
|持久性|每次请求传入|系统级、长期有效|
|设计哲学|“告诉模型怎么调用工具”|“告诉模型你能做什么”|
|适用场景|API 工具调用|代码助手、IDE Agent、复杂任务执行|

一句话：

> Function Calling 是“API 调用层”， Skills 是“Agent 能力层”。

# 🧱 4. 为什么 Claude 要用 Skills？

因为 Claude Code 是一个 **真正的代码 Agent**，需要：

- 访问文件系统
    
- 修改代码
    
- 生成补丁
    
- 运行命令
    
- 搜索项目
    
- 分析错误
    
- 维护上下文
    
- 遵守权限边界
    

这些是 Function Calling 无法表达的。

Function Calling 只能表达：

代码

复制

```
call function X with parameters Y
```

但无法表达：

- 你能访问哪些目录
    
- 你能不能删除文件
    
- 你能不能执行 shell
    
- 你能不能修改代码
    
- 你能不能创建新文件
    
- 你能不能运行测试
    
- 你能不能分析项目结构
    

Skills 则可以。

# 🎯 5. 最精炼总结（你可以直接写进文档）

- **Function Calling**
    
    - 是 LLM 调用工具的协议
        
    - 只描述“怎么调用函数”
        
    - 不描述权限、不描述能力、不描述上下文
        
- **Claude Skills**
    
    - 是 Agent 的能力模型
        
    - 描述“你能做什么、能访问什么、能修改什么”
        
    - 包含权限、上下文、行为范围
        
    - 是系统级的能力声明
        

一句话：

> **Function Calling = 工具调用协议** **Skills = Agent 的能力与权限系统**

如果你愿意，我还能继续帮你：

- 画一张“Skills vs Function Calling vs MCP”的三方对比图
    
- 给你一个“如何在你的项目中选择协议”的建议
    
- 或者帮你设计一个你自己的 Skills/Tools 架构
    

你想继续深入哪一块呢？

##### 你说

skill 告诉 llm 改用什么工具，而不是去乱用，是吗

###### Copilot 说

你的理解 **非常接近本质**，但我帮你把它说得更精准一点，让你彻底掌握 Claude 的 `skills` 在 Agent 架构里的作用。

# 🎯 最准确的一句话解释

**Skills 的作用不是“告诉 LLM 用哪个工具”，而是“告诉 LLM** _**哪些工具是允许的**_**，哪些能力是存在的”。**

换句话说：

> **Skills 限定能力边界，而不是指定具体工具。** 它让 LLM 不会乱用、不该用的工具不会被调用。

# 🧠 更精确的理解：

### ✔ Skills = 能力白名单（capability whitelist）

它告诉模型：

- 你有哪些能力
    
- 你能访问哪些资源
    
- 你能调用哪些工具
    
- 你不能越界做什么
    

例如：

代码

复制

```
skills:
  - read_file
  - write_file
  - search_project
  - apply_patch
```

这意味着：

- 模型知道自己可以读文件
    
- 模型知道自己可以写文件
    
- 模型知道自己可以生成补丁
    
- 模型不会尝试执行未声明的能力（比如删除文件、执行 shell）
    

# ❌ Skills **不会**做的事

Skills **不会**告诉模型：

- “现在你必须用工具 A”
    
- “这个任务必须用工具 B”
    
- “你应该优先调用某个工具”
    

这些是 **LLM 自己的推理**（ReAct / Agent loop）来决定的。

# 🤖 那 LLM 是怎么决定用哪个工具的？

流程是这样的：

1. **Skills 定义能力范围**（你能做什么）
    
2. **LLM 根据任务推理**（你应该做什么）
    
3. **LLM 在允许的能力里选择工具**（你可以做什么）
    

所以：

> Skills = 能力边界 LLM = 决策逻辑 Tools = 可用动作

# 🧩 为什么 Skills 能防止“乱用工具”？

因为：

- 未在 skills 中声明的工具
    
- 未在 skills 中声明的能力
    
- 未在 skills 中声明的资源
    

LLM **根本不会尝试调用**。

这就是为什么 Claude Code 的行为比传统 Agent 更稳定、更安全。

# 🧱 和 Function Calling 的对比（最关键）

|项目|Function Calling|Claude Skills|
|---|---|---|
|作用|让 LLM 调用函数|定义 LLM 的能力边界|
|控制方式|列出可调用函数|声明整个 Agent 的能力模型|
|是否防止乱用|部分|完全（严格白名单）|
|是否包含权限|❌|✔（文件、编辑、命令等）|
|是否包含上下文|❌|✔（项目结构、文件系统）|

所以：

> Function Calling = 工具调用协议 Skills = Agent 的权限系统 + 能力模型

# 🎯 最终总结（你可以直接写进文档）

- **Skills 的作用是限制 LLM 的能力范围，让它不会乱用工具。**
    
- **Skills 不会告诉 LLM“必须用哪个工具”，只是告诉它“哪些工具是允许的”。**
    
- **LLM 自己根据任务推理选择工具，但只能在 Skills 白名单内选择。**
    

一句话：

> **Skills = 能力白名单，防止乱用工具；** **工具选择 = LLM 自主推理。**

如果你愿意，我还能继续帮你：

- 画一张“Skills / Tools / LLM / Agent Loop”的架构图
    
- 给你一个“如何设计自己的 Skills 模型”的模板
    
- 或者帮你把你项目里的工具能力体系设计出来
    

你想继续深入哪一块呢？

##### 你说

langchain tools 之间指定工具，不如 skills 灵活是吗

###### Copilot 说

你抓到的这个差异非常关键，不过我想帮你把它讲得更精准一点，因为 **LangChain Tools 和 Claude Skills 的灵活性差异，本质上来自“设计哲学不同”**，而不是简单的“哪个更强”。

下面是最清晰的解释。

# 🎯 一句话总结

**LangChain Tools = 明确列出工具，由 Agent 在这些工具里选择** **Claude Skills = 声明能力边界，让模型在能力范围内自由行动**

所以：

> **LangChain Tools 是“工具列表”** **Claude Skills 是“能力模型 + 权限系统”**

这导致 Skills 在某些场景下确实更灵活，但 LangChain Tools 在另一些场景下更可控。

# 🧩 1. LangChain Tools 的特点

LangChain Tools 的设计是：

- 你必须显式注册每个工具
    
- 工具是离散的、独立的
    
- Agent 只能在你提供的工具列表中选择
    
- 工具之间没有“能力抽象层”
    
- 工具的行为完全由开发者定义
    

例如：

python

复制

```
tools = [search_tool, calculator_tool, db_query_tool]
agent = initialize_agent(tools, llm)
```

LLM 的选择范围就是：

- search_tool
    
- calculator_tool
    
- db_query_tool
    

**没有别的。**

### ✔ 优点

- 非常可控
    
- 工具行为可测试
    
- 适合企业级生产环境
    
- 工具之间边界清晰
    

### ❌ 限制

- 工具必须一个个注册
    
- 工具粒度越细，越难管理
    
- 工具之间没有“能力抽象”
    
- 工具数量多时，LLM 选择成本高
    
- 工具无法表达权限、上下文、资源访问等概念
    

# 🤖 2. Claude Skills 的特点

Claude Skills 的设计是：

- 不是“工具列表”，而是“能力声明”
    
- 声明模型能做什么，而不是列出工具
    
- 能力可以是抽象的（如 apply_patch）
    
- 能力可以包含权限（如 read/write 文件）
    
- 能力可以包含上下文（如项目结构）
    
- 工具可以在能力内部动态组合
    

例如：

yaml

复制

```
skills:
  - read_file
  - write_file
  - search_project
  - apply_patch
```

这不是工具，而是：

> **模型的能力边界（capability boundary）**

模型在这些能力范围内自由选择策略。

### ✔ 优点

- 更抽象、更灵活
    
- 能力可以组合
    
- 能表达权限（文件、命令、编辑）
    
- 能表达上下文（项目结构）
    
- 模型不需要知道具体工具，只需要知道能力
    
- 更适合复杂 Agent（IDE、代码助手、自动化系统）
    

### ❌ 限制

- 不适合严格可控的企业流程
    
- 不适合需要精确审计的工具调用
    
- 能力抽象层可能导致行为不可预测
    

# 🧠 3. 为什么你感觉 Skills 更灵活？

因为：

### LangChain Tools

- 工具是“离散的函数”
    
- 工具之间没有抽象层
    
- 工具数量越多越难管理
    

### Claude Skills

- 能力是“抽象的动作”
    
- 一个能力可以映射到多个工具
    
- 模型可以在能力范围内自由组合策略
    

举个例子：

### LangChain

你要提供：

- read_file_tool
    
- write_file_tool
    
- search_tool
    
- patch_tool
    
- edit_tool
    
- run_test_tool
    
- …
    

工具越多，Agent 越复杂。

### Claude Skills

你只需要：

代码

复制

```
skills:
  - read_file
  - write_file
  - apply_patch
  - run_tests
```

模型自己决定：

- 什么时候读文件
    
- 什么时候写文件
    
- 什么时候生成补丁
    
- 什么时候运行测试
    

**能力抽象层让模型更自由。**

# 🎯 最终结论（最精炼版）

- **LangChain Tools 更可控，但粒度细、灵活性低**
    
- **Claude Skills 更抽象、更灵活，但可控性弱**
    
- 两者不是强弱关系，而是设计哲学不同
    
- Skills 更适合“自主 Agent”
    
- Tools 更适合“可控流水线”
    

一句话：

> **LangChain Tools = 工具列表（LLM 在列表里选）** **Claude Skills = 能力边界（LLM 在能力范围内自由行动）**

如果你愿意，我可以继续帮你：

- 画一张“Tools vs Skills vs MCP”的三方对比图
    
- 给你一个“如何在你的项目中选择 Tools 或 Skills”的决策树
    
- 或者帮你设计一个你项目里的 Agent 能力模型
    

你想继续深入哪一块呢？

##### 你说

画一张“Tools vs Skills vs MCP”的三方对比图

###### Copilot 说

下面给你一张**清晰、工程化、可直接放进文档的**三方对比图，用表格形式呈现，结构非常直观。

# 🧩 Tools vs Skills vs MCP 三方对比图

## **总体定位对比**

|项目|**LangChain Tools**|**Claude Skills**|**MCP（Model Context Protocol）**|
|---|---|---|---|
|本质|工具调用接口|Agent 能力模型（能力白名单）|LLM ↔ 工具/资源 的通用协议|
|层级|应用层|系统层（Agent 层）|协议层（标准层）|
|目标|让 LLM 调用函数|定义 LLM 能做什么|标准化工具、资源、文件访问|

## **设计哲学对比**

|维度|LangChain Tools|Claude Skills|MCP|
|---|---|---|---|
|核心理念|“列出工具，让 LLM 选择”|“声明能力，让 LLM 自主行动”|“统一协议，让工具可复用”|
|控制方式|工具列表（函数级）|能力边界（抽象级）|标准化 schema（协议级）|
|粒度|细（函数级）|粗（能力级）|中（资源/工具级）|
|灵活性|中|高|高|
|可控性|高|中|高（协议约束）|

## **能力范围对比**

|能力类型|LangChain Tools|Claude Skills|MCP|
|---|---|---|---|
|调用 API|✔|✔|✔|
|文件系统访问|❌（需自定义工具）|✔（内置能力）|✔（标准化）|
|编辑代码|❌（需自定义工具）|✔（apply_patch 等）|✔（通过 server 实现）|
|运行命令|❌（需自定义工具）|✔（受限能力）|✔（受限能力）|
|项目上下文|❌|✔（项目结构、文件）|✔（通过资源 server）|
|权限控制|弱|强（能力白名单）|强（协议级权限）|

## **LLM 行为控制对比**

|行为|LangChain Tools|Claude Skills|MCP|
|---|---|---|---|
|防止乱用工具|部分|强（未声明能力无法使用）|强（协议约束）|
|工具选择方式|LLM 在工具列表中选|LLM 在能力范围内自由规划|LLM 调用 MCP server 暴露的能力|
|是否支持自主规划|✔（Agent 模式）|✔（天然支持）|✔（协议支持）|

## **生态与用途对比**

|场景|LangChain Tools|Claude Skills|MCP|
|---|---|---|---|
|RAG|✔|✔|✔|
|代码助手|❌（需大量自定义）|✔（专为此设计）|✔（强）|
|自动化 Agent|✔|✔|✔|
|企业级可控流程|✔（最强）|中|✔（协议级控制）|
|多工具统一管理|中|中|✔（最强）|

# 🎯 最精炼总结（你可以直接写进文档）

- **LangChain Tools**： 工具列表式调用，适合可控流程，粒度细，扩展性强但抽象度低。
    
- **Claude Skills**： 能力白名单，抽象度高，适合自主 Agent，灵活但可控性略弱。
    
- **MCP**： 标准化协议，统一 LLM ↔ 工具/资源 的交互方式，是未来最可能成为行业标准的层。
    

一句话：

> **Tools = 工具列表** **Skills = 能力模型** **MCP = 通用协议**

如果你愿意，我还能帮你：

- 画一张“Agent 架构全景图（LLM / Tools / Skills / MCP）”
    
- 给你一个“如何在你的项目中选择 Tools / Skills / MCP”的决策树
    
- 或者帮你设计你项目里的 Agent 能力体系
    

你想继续往哪个方向深入呢？

##### 你说

skills 怎么把能力转变成使用工具，llm 通过 mcp 等吗

###### Copilot 说

下面我给你一个**工程师能立刻看懂的解释**： **Claude 的 Skills 是“能力声明”，但真正执行工具要靠底层的“工具执行层”，而 MCP 是其中最标准化的一种方式。**

换句话说：

> **Skills ≠ 工具本身** **Skills = 能力白名单** **工具执行 = 由宿主环境（IDE / MCP server / 自定义 runtime）完成** **LLM 只是根据 Skills 决定“要不要调用工具”，但不会自己执行工具**

下面把整个链路讲清楚。

# 🧩 1. Skills 本身不执行工具

Skills 的作用是：

- 告诉 LLM：你有哪些能力
    
- 限制 LLM：你不能越界
    
- 让 LLM 在推理时知道“我可以做哪些动作”
    

例如：

yaml

复制

```
skills:
  - read_file
  - write_file
  - apply_patch
  - search_project
```

这些只是“能力名称”，不是工具。

# 🧠 2. LLM 如何把“能力”变成“工具调用”？

流程是这样的：

## **Step 1：LLM 推理出需要某个能力**

例如 LLM 想修改代码，它会输出类似：

代码

复制

```
<apply_patch>
  diff 内容...
</apply_patch>
```

这一步是 LLM 的“意图表达”。

## **Step 2：宿主环境解析这个意图**

宿主环境可能是：

- Claude Code 的 IDE runtime
    
- MCP server
    
- 你自己写的工具执行器
    
- LangChain 的 Tool wrapper
    
- VSCode 插件
    
- Web IDE runtime
    

它会解析：

- 哪个能力被调用
    
- 参数是什么
    
- 是否允许执行
    

## **Step 3：宿主环境执行真正的工具**

例如：

- `apply_patch` → 调用 patch 工具
    
- `read_file` → 调用文件系统
    
- `search_project` → 调用项目索引
    
- `run_tests` → 调用 shell 或 test runner
    

## **Step 4：把执行结果返回给 LLM**

LLM 再继续推理下一步。

# 🔌 3. 那 MCP 在这里扮演什么角色？

MCP 是：

> **一种标准化的“LLM ↔ 工具/资源”协议**

如果你用 MCP：

- Skills 声明能力
    
- MCP server 暴露工具
    
- LLM 通过 MCP 调用工具
    
- MCP server 执行工具并返回结果
    

所以：

> **Skills + MCP = 能力声明 + 工具执行协议**

但注意：

### ❗ Skills 不依赖 MCP

你可以：

- 用 Skills + 自己写的工具执行器
    
- 用 Skills + LangChain Tools
    
- 用 Skills + IDE runtime
    
- 用 Skills + MCP
    

MCP 只是其中一种方式，但它是最标准化、最现代的方式。

# 🧱 4. 三者关系图（最清晰的版本）

代码

复制

```
          ┌──────────────┐
          │     Skills    │
          │（能力白名单） │
          └───────▲──────┘
                  │
                  │ LLM 推理：决定调用哪个能力
                  │
          ┌───────┴──────┐
          │     LLM       │
          │（输出意图）   │
          └───────▲──────┘
                  │
                  │ 意图解析
                  │
      ┌───────────┴───────────┐
      │     工具执行层          │
      │（MCP / IDE / LangChain）│
      └───────────▲───────────┘
                  │
                  │ 调用真实工具
                  │
          ┌───────┴───────┐
          │     Tools      │
          │（API / FS / DB）│
          └───────────────┘
```

# 🎯 最精炼总结（你可以直接写进文档）

- **Skills 只是能力声明，不执行工具**
    
- **LLM 根据 Skills 决定“要调用哪个能力”**
    
- **工具执行由宿主环境完成（MCP 是最标准的方式）**
    
- **MCP = LLM ↔ 工具 的通用协议**
    
- **Skills + MCP = 能力模型 + 工具执行协议**
    

一句话：

> **Skills 让 LLM 知道“能做什么”，** **MCP 让 LLM 能“真正做成事”。**

如果你愿意，我还能继续帮你：

- 画一张“Skills → MCP → Tools”的时序图
    
- 给你一个“如何在你项目中实现 Skills + MCP”的架构方案
    
- 或者帮你设计你自己的能力模型（skills schema）
    

你想继续深入哪一块呢？

##### 你说

只有特定的宿主环境如 claude code 才能耦合 skills 和 mcp 是吗

###### Copilot 说

不止 Claude Code，但 **确实需要“支持 Skills + 工具执行层”的宿主环境**，而不是任何 LLM 客户端都能直接用。

换句话说：

> **Skills 是“能力声明”，MCP 是“工具协议”，但它们都需要一个“宿主环境（runtime）”来真正执行工具。**
> 
> Claude Code 是其中一个官方示例，但不是唯一可能的宿主。

下面把整个生态讲清楚，你会一下子明白。

# 🧩 1. Skills + MCP 不是 LLM 自己能完成的

LLM 本身只能：

- 读 Skills（能力白名单）
    
- 输出“意图”（例如 `<apply_patch>`）
    
- 生成下一步推理
    

但 LLM **不能执行工具**。

真正执行工具的是：

> **宿主环境（runtime）**

例如：

- Claude Code（官方 IDE runtime）
    
- MCP server（通用工具协议）
    
- 你自己写的工具执行器
    
- LangChain 的 Tool wrapper（如果你自己接 Skills）
    
- VSCode 插件、Web IDE、CLI agent runtime
    

所以：

> **Skills + MCP 需要 runtime 才能工作，而不是 LLM 自己就能跑。**

# 🧱 2. Claude Code 是“官方 runtime”，但不是唯一

Claude Code 的 runtime：

- 读取 Skills
    
- 解析 LLM 的意图
    
- 调用本地工具（文件系统、补丁、搜索等）
    
- 把结果返回给 LLM
    

它是一个完整的：

> **Skills → 意图 → 工具执行 → 结果 → LLM** 闭环系统。

但你完全可以自己实现一个 runtime。

# 🔌 3. MCP 是“通用 runtime 协议”

MCP（Model Context Protocol）本质上是：

> **一个让 LLM ↔ 工具/资源 交互的标准协议**

任何支持 MCP 的 runtime 都可以：

- 暴露工具（resources / actions）
    
- 接收 LLM 的调用意图
    
- 执行工具
    
- 返回结果
    

所以：

> **MCP = 通用工具执行层** **Skills = 能力声明层**

两者可以组合，但不强制绑定。

# 🧩 4. 哪些环境可以耦合 Skills + MCP？

### ✔ 可以耦合的环境

- Claude Code（官方）
    
- MCP server（你自己写的）
    
- 支持 MCP 的 IDE（未来会越来越多）
    
- 自定义 Agent runtime（Node/Python 都能写）
    
- LangChain（如果你自己接 MCP）
    
- VSCode 插件（如果实现 MCP client）
    

### ❌ 不能耦合的环境

- 普通聊天界面（没有工具执行层）
    
- 纯 API 调用（除非你自己实现 MCP client）
    
- 不支持工具调用的 LLM 客户端
    

所以：

> **不是“只有 Claude Code 才能耦合 Skills + MCP”，** **而是“任何实现 MCP + 能力解析的 runtime 都能耦合”。**

Claude Code 只是一个官方示例。

# 🎯 最精炼总结

- **Skills = 能力白名单（告诉 LLM 能做什么）**
    
- **MCP = 工具协议（让 LLM 能真正调用工具）**
    
- **Runtime = 执行工具的宿主环境（真正干活的）**
    

三者关系：

代码

复制

```
Skills（能力声明）
        ↓
LLM（推理出意图）
        ↓
MCP / Runtime（执行工具）
        ↓
工具（API / FS / DB）
```

一句话：

> **Skills + MCP 需要 runtime 才能工作，Claude Code 是其中一个，但不是唯一。**

如果你愿意，我可以继续帮你：

- 画一张“Skills / MCP / Runtime / Tools”的时序图
    
- 给你一个“如何自己实现一个 MCP runtime”的架构方案
    
- 或者帮你设计你项目里的能力模型（skills schema）
    

你想继续深入哪一块呢？

##### 你说

1

###### Copilot 说

明白，你想继续深入 **“Skills → MCP → Tools 的时序图（Sequence Diagram）”**。 下面给你一张**工程级、可直接放进架构文档**的时序图，展示：

- Skills 如何限制能力
    
- LLM 如何根据 Skills 产生“意图”
    
- MCP 如何作为协议层
    
- Runtime 如何执行工具
    
- 工具如何返回结果
    

# 🧩 Skills → MCP → Tools 时序图（Sequence Diagram）

代码

复制

```
User
  │
  │ 1. 用户发出任务（如：修改代码、搜索项目）
  ▼
LLM (Claude)
  │
  │ 2. 读取 Skills（能力白名单）
  │    - read_file
  │    - write_file
  │    - apply_patch
  │    - search_project
  │
  │ 3. 推理：决定需要调用哪个能力
  │    例如：apply_patch
  │
  │ 4. 输出“意图”（Intention）
  │    <apply_patch>
  │      diff 内容...
  │    </apply_patch>
  ▼
Runtime（宿主环境）
  │
  │ 5. 解析意图（Intent Parsing）
  │    - 识别能力名称
  │    - 校验是否在 Skills 白名单中
  │
  │ 6. 将意图转换为 MCP 请求
  │    action: apply_patch
  │    params: { diff: ... }
  ▼
MCP Server（工具协议层）
  │
  │ 7. 根据 action 调用对应工具
  │
  ▼
Tool（真实工具）
  │
  │ 8. 执行实际操作
  │    - 修改文件
  │    - 搜索项目
  │    - 运行命令
  │
  │ 9. 返回执行结果
  ▼
MCP Server
  │
  │ 10. 将结果封装为 MCP 响应
  ▼
Runtime
  │
  │ 11. 将结果返回给 LLM
  ▼
LLM
  │
  │ 12. 根据结果继续推理下一步
  ▼
User
```

# 🎯 最关键的理解（你可以直接写进文档）

### **Skills 的作用：能力白名单**

- Skills 不执行工具
    
- Skills 不包含工具逻辑
    
- Skills 只是告诉 LLM： **“你能做这些事，不能做其他事”**
    

### **LLM 的作用：推理 + 输出意图**

- LLM 根据 Skills 决定“要不要调用能力”
    
- LLM 输出 `<apply_patch>` 这样的意图
    
- LLM 不执行工具
    

### **MCP 的作用：协议层**

- MCP 把 LLM 的意图转成标准化的工具调用
    
- MCP 让工具可以跨平台复用
    
- MCP 是“LLM ↔ 工具”的通用语言
    

### **Runtime 的作用：真正执行工具**

- 解析意图
    
- 调用 MCP
    
- 执行工具
    
- 返回结果
    

Claude Code 就是一个 runtime，但不是唯一。

# 🧱 最终一句话总结

> **Skills 定义能力 → LLM 选择能力 → MCP 调用工具 → Runtime 执行 → 工具返回结果。**

如果你愿意，我还能继续帮你：

- 画一张“Skills / Tools / MCP / Agent Loop”的架构图
    
- 给你一个“如何在你自己的项目中实现 Skills + MCP”的方案
    
- 或者帮你设计你项目里的能力模型（skills schema）
    

你想继续往哪个方向深入呢？

##### 你说

runtime 是什么，我们叫运行时，是解析器吗

###### Copilot 说

下面给你一个真正工程师能用的解释：**runtime（运行时）不是解析器，但解析器是 runtime 的一部分。** 在 Agent / Skills / MCP 体系里，runtime 是一个**完整的执行环境**，负责把 LLM 的“意图”变成真实的动作。

我把它拆成你最容易理解的几个层次。

# 🧩 **1. runtime 是什么？（最准确的定义）**

**runtime = LLM 外部的执行环境，用来执行工具、管理上下文、解析意图、返回结果。**

它不是 LLM，也不是工具，而是：

> **LLM 和工具之间的“中间层 + 执行层”。**

你可以把它理解成：

- LLM：大脑
    
- Tools：手脚
    
- **Runtime：神经系统（把大脑的意图变成动作）**
    

# 🧠 **2. runtime 的职责（非常关键）**

runtime 负责：

### ✔ 1. 解析 LLM 的意图（Intent Parsing）

例如 LLM 输出：

代码

复制

```
<apply_patch>
  diff 内容...
</apply_patch>
```

runtime 负责识别：

- 这是一个能力调用
    
- 能力名称是 apply_patch
    
- 参数是什么
    
- 是否在 Skills 白名单中
    

### ✔ 2. 调用工具（Tool Execution）

runtime 负责执行：

- 文件系统操作
    
- 搜索项目
    
- 运行命令
    
- 调用 API
    
- 应用补丁
    

### ✔ 3. 管理上下文（Context Management）

runtime 维护：

- 当前项目结构
    
- 文件内容
    
- 工具状态
    
- 会话状态
    

### ✔ 4. 返回结果给 LLM

例如：

代码

复制

```
{
  "status": "success",
  "applied_lines": 42
}
```

### ✔ 5. 安全控制（Security Sandbox）

runtime 决定：

- 哪些目录可访问
    
- 哪些命令可执行
    
- 哪些能力被禁用
    

# 🧱 **3. runtime ≠ 解析器，但解析器是 runtime 的一部分**

你可以这样理解：

### **解析器（parser）**

- 负责解析 LLM 的输出
    
- 识别 `<apply_patch>` 这样的结构
    
- 提取参数
    

### **runtime**

包含：

- 解析器
    
- 工具执行器
    
- 权限系统
    
- 上下文管理
    
- MCP 客户端（如果使用 MCP）
    
- 结果返回器
    

所以：

> **解析器只是 runtime 的一个模块，而不是全部。**

# 🔌 **4. runtime 和 MCP 的关系**

MCP 是协议，runtime 是执行者。

- MCP：定义“怎么调用工具”
    
- runtime：真正执行工具
    

runtime 可以：

- 使用 MCP（最标准）
    
- 使用本地 API
    
- 使用自定义工具
    
- 使用 LangChain Tools
    
- 使用 IDE 内置能力
    

所以：

> **MCP 是 runtime 的一种实现方式，但不是唯一方式。**

# 🧩 **5. Claude Code 为什么是 runtime？**

因为它具备：

- 解析 LLM 意图
    
- 执行文件操作
    
- 应用补丁
    
- 搜索项目
    
- 运行命令
    
- 返回结果
    
- 管理权限
    
- 管理上下文
    

它是一个完整的 runtime。

但你完全可以自己写一个 runtime。

# 🎯 **最精炼总结（你可以直接写进文档）**

- **runtime = 执行环境**
    
- **解析器只是 runtime 的一部分**
    
- **runtime 负责把 LLM 的意图变成真实动作**
    
- **runtime 执行工具，而不是 LLM**
    
- **MCP 是 runtime 可以使用的协议，但不是必须的**
    
- **Claude Code 是一个 runtime，但不是唯一的 runtime**
    

一句话：

> **LLM 负责“想”，runtime 负责“做”，工具负责“干活”。**

如果你愿意，我可以继续帮你：

- 画一张“LLM / Skills / Runtime / MCP / Tools”的架构图
    
- 给你一个“如何自己写一个 runtime”的工程方案
    
- 或者帮你设计你项目里的 runtime 模块结构
    

你想继续深入哪一块呢？

##### 你说

能不能把 agent 所有部件的逻辑架构图都画一下，一张不够，几张也行

###### Copilot 说

当然可以，而且我觉得你现在已经到了可以真正“看懂 Agent 全栈架构”的阶段了。 为了让你彻底掌握 Agent 的所有部件，我会给你 **多张逻辑架构图**，从宏观到微观、从概念到执行链路，逐层拆开。

下面这些图都是**纯文本逻辑图**，你可以直接放进文档、白板、架构设计稿里。

# 🧩 **图 1：Agent 全景架构（最高层）**

代码

复制

```
┌──────────────────────────────────────────────┐
│                  Agent（智能体）             │
│  ┌────────────────────────────────────────┐  │
│  │                Reasoning               │  │
│  │（LLM 推理：规划、决策、反思、循环）       │  │
│  └────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────┐  │
│  │                Abilities               │  │
│  │（能力：Skills / Tools / Actions）       │  │
│  └────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────┐  │
│  │                Memory                  │  │
│  │（短期记忆、长期记忆、上下文）            │  │
│  └────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────┐  │
│  │                Runtime                 │  │
│  │（执行环境：解析意图、调用工具、权限）    │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

# 🧩 **图 2：LLM、Skills、Tools、Runtime 的关系**

代码

复制

```
User
  │
  ▼
LLM（大脑）
  │ 读取 Skills（能力白名单）
  │ 推理：决定调用哪个能力
  ▼
意图（Intention）
  │ <apply_patch> ... </apply_patch>
  ▼
Runtime（运行时）
  │ 解析意图
  │ 校验权限（Skills）
  │ 转换为工具调用
  ▼
Tools（真实工具）
  │ 执行操作（FS / API / DB / Shell）
  ▼
Runtime
  │ 返回结果
  ▼
LLM（继续推理）
```

# 🧩 **图 3：Agent 内部的推理循环（ReAct / Agent Loop）**

代码

复制

```
┌──────────────────────────────────────────────┐
│                Agent Loop                    │
├──────────────────────────────────────────────┤
│ 1. 观察（Observation）                        │
│ 2. 思考（Thought）                            │
│ 3. 决策（Decision）                           │
│ 4. 行动（Action）→ 调用工具                   │
│ 5. 结果（Result）                             │
│ 6. 反思（Reflection）                         │
│ 7. 是否完成？                                 │
│    ├─ 否 → 回到步骤 1                         │
│    └─ 是 → 输出最终答案                       │
└──────────────────────────────────────────────┘
```

# 🧩 **图 4：Tools vs Skills vs MCP（能力层 vs 工具层 vs 协议层）**

代码

复制

```
能力层（LLM 能做什么）
┌───────────────────────────────┐
│ Skills（能力白名单）           │
│ - read_file                   │
│ - write_file                  │
│ - apply_patch                 │
│ - search_project              │
└───────────────────────────────┘

协议层（如何调用工具）
┌───────────────────────────────┐
│ MCP（Model Context Protocol）  │
│ - 标准化工具调用               │
│ - 标准化资源访问               │
│ - 标准化权限模型               │
└───────────────────────────────┘

工具层（真正执行）
┌───────────────────────────────┐
│ Tools（API / FS / DB / Shell）│
│ - 文件系统                     │
│ - 搜索引擎                     │
│ - 代码补丁工具                 │
│ - 数据库查询                   │
└───────────────────────────────┘
```

# 🧩 **图 5：Runtime（运行时）内部结构**

代码

复制

```
┌──────────────────────────────────────────────┐
│                 Runtime（运行时）            │
├──────────────────────────────────────────────┤
│ 1. 意图解析器（Intent Parser）               │
│    - 解析 LLM 输出                           │
│    - 提取能力名称和参数                      │
│                                              │
│ 2. 权限系统（Permission System）             │
│    - 根据 Skills 校验能力是否允许            │
│                                              │
│ 3. 工具调度器（Tool Dispatcher）             │
│    - 将能力映射到具体工具                    │
│    - 通过 MCP 或本地 API 调用                │
│                                              │
│ 4. 上下文管理器（Context Manager）           │
│    - 文件缓存                                │
│    - 项目结构                                │
│    - 会话状态                                │
│                                              │
│ 5. 结果返回器（Result Handler）              │
│    - 格式化工具结果                          │
│    - 返回给 LLM                              │
└──────────────────────────────────────────────┘
```

# 🧩 **图 6：Agent 的“能力模型”结构（Skills 视角）**

代码

复制

```
┌──────────────────────────────────────────────┐
│                Skills（能力模型）            │
├──────────────────────────────────────────────┤
│ 能力类别：                                    │
│   - 文件能力（read_file / write_file）       │
│   - 编辑能力（apply_patch）                  │
│   - 搜索能力（search_project）               │
│   - 执行能力（run_tests / run_command）      │
│   - API 调用能力（call_api）                 │
│                                              │
│ 每个能力包含：                                │
│   - 名称（name）                              │
│   - 参数（schema）                            │
│   - 权限（permissions）                       │
│   - 上下文（context）                         │
│   - 工具映射（tool mapping）                  │
└──────────────────────────────────────────────┘
```

# 🧩 **图 7：Agent 全栈架构（从用户到工具）**

代码

复制

```
User
  │
  ▼
LLM（推理）
  │ 读取 Skills
  │ 生成意图
  ▼
Runtime（运行时）
  │ 解析意图
  │ 校验权限
  │ 调用 MCP
  ▼
MCP Server（协议层）
  │ 调用工具
  ▼
Tools（真实执行）
  │ 返回结果
  ▼
Runtime
  │ 返回给 LLM
  ▼
LLM（继续推理）
  ▼
User（最终输出）
```

# 🎯 **如果你愿意，我还能继续画：**

- Agent 的“事件流架构图”（Event-driven Agent）
    
- Agent 的“多工具调度图”（Multi-tool orchestration）
    
- Agent 的“多 Agent 协作图”（Swarm / CrewAI 风格）
    
- Agent 的“RAG + Tools + Skills 混合架构图”
    
- Agent 的“LangChain vs MCP vs Claude Code 对照架构图”
    

你想继续扩展哪一部分呢？

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)