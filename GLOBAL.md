# Sumicya 全项目规范（第0版 · 2026-10-13）

四要领：辩证法、简单性、先进性、自由性。只解决真实问题。

## 辩证法

从需求、事实和现有实现出发。发现矛盾就改，改完验证。事实、推断、未验证分开说。已明确的要求直接执行。允许质疑一切，但不拿讨论拖延已定工作。改错误所在，并清掉同一要求的冲突表述，不以追加代替清除。

## 简单性

最小正确实现：先不做、复用、标准库、平台原生。一份职责不重复。删除无实际作用的东西。CI 只服务构建与清理，不设规范检查等冗余流程。规范由 agent 在会话中核对。

文档简体中文。先给结果，必要时才补极少量依据。禁止解释性标题，禁止为已知事实单独设章。输入信息不等于输出信息。严禁「对……」「你说得对……」开头，禁止「不是……而是……」句式。所有文档保持简单。

## 先进性

用现行受支持的机制和工具链。CI 用具体镜像，不用 `ubuntu-latest`。不支持的环境明确失败。

## 自由性

既有结构和历史实现都可以改。规则只约束交付结果和必要边界。不能擅自扩大任务、发布、合并或删除远端对象。无权限就直接说阻塞。

## 文档参考

按需查阅，不自动安装。

- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- [newliver666/apk-reverse](https://github.com/newliver666/apk-reverse/tree/main/skills/apk-reverse)
- [2akouwu/reverify](https://github.com/2akouwu/reverify)
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)
- [morluto/rea](https://github.com/morluto/rea)

## 交付要求

### 版本

产物统一 `yy.m.d.当日序号.总序号`，日界 UTC+8。文件名：`<项目名>-<五段版本>`。取数锚定本次 run 的 `run_id`/`run_attempt`/`created_at`，禁止查最新 run。缺失即失败。

### 保留

- Release：1 个
- Artifact：5 个
- 运行记录：有产物仓 5 条；无产物/无 CI 仓（selfs、qqapk、Selfblox 等）清零，禁止新增工作流

清理默认启用。最小 `actions: write`（只删本项目 artifact 与 run），禁止同时给 `contents: write`。删除前打印清单。

### 构建与发版

有产物必须构建并 upload-artifact。CI 出包 ≠ 发版。Release 只能人工明确授权后创建。

## 工作

先读项目 AGENTS.md 和本规范。用户指示优先。默认分支 GLOBAL.md 是入口。AGENTS.md 只记事实、限制、指针和「上次同步 = 第 N 版」。只操作授权仓库。改规范时同步改 CHANGELOG 和版本戳。

Arena 会话出现辱骂或同等愤怒时，先写不少于 1000 汉字检讨（每满 100 字标注），再继续。非 Arena 不写。
