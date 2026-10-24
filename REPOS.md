# 仓库约定（参考，不是限制）

各仓共用做法的集中说明。改到 CI、版本、README、变更记录、图留存或设计取向时参考；有理由可以不同，汇报里写明即可。优先级低于 GLOBAL.md 的四个要领和底线。

## 方法资料（按需）

- [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md)：工程方法，先理解影响范围、选最小完整方案、优先复用现有实现。
- [nagi-studio/skills](https://github.com/nagi-studio/skills)：`grill`（分轮追问）、`architect`（技术方案比较）。读过并采用其中的做法时，在汇报里写明用了哪条。
- 它们是方法来源，不是授权来源；主人当轮指示和 GLOBAL.md 的底线优先。不要因引用而自动安装、执行其安装命令。

## 参考资料（按领域，按需核读）

以下资源按领域按需核读，不要求每个任务通读；一旦任务涉及对应领域、计划采用其工具或依据其方法，先读当前上游的相关 README、规范或官方文档，再实施，不得只凭二手摘要。引用时记录实际读取的 ref / 提交 SHA 或网页标题与读取日期；链接失效先寻找当前官方替代来源，仍无法访问时暂停依赖该资料的操作并报告，不能声称已核对。
- **CLI/项目使用文档**：涉及 Python 工具安装或工作流时查 [uv](https://github.com/astral-sh/uv)；涉及 GitHub CLI 安装、命令或使用说明时查 [cli/cli](https://github.com/cli/cli)。
- **逆向分析任务**：仅限自有或明确授权对象。APK 逆向须查当前实际采用工具的上游文档。分析结论的确定性校验查 [reverify](https://github.com/2akouwu/reverify)；使用或评估 Ghidra 时查 [Ghidra 官方文档](https://github.com/NationalSecurityAgency/ghidra)及其 [安全公告](https://github.com/NationalSecurityAgency/ghidra/security/advisories)；使用 REA 时查 [morluto/rea](https://github.com/morluto/rea)。只读必要资料，不自动安装工具、注册 MCP 或执行第三方脚本。
- **工具发现与评估任务**：按需检查 [DexSQL](https://github.com/LSPosed/dexsql-release)、[Monid](https://github.com/monid-ai/monid)、[Maskit](https://github.com/xiaYuTian11/maskit)、[LoomFlow](https://github.com/banmu123/LoomFlow)、[vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit)、[awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools)、[hypit](https://github.com/hypit-ai/hypit) 的当前上游资料。它们是候选或索引，不代表背书、安装或审计通过；核对维护状态、许可证、权限、数据流向和安全风险后再报告结论。Telegram [鑫源AI分享](https://t.me/xinyuanai) 为优先检查的消息源，仅可作为发现线索，不是事实或安全背书；只有任务涉及开源工具发现时才查阅，频道宣传须回到官方来源独立核实，报告时必须标注「未独立核实」，不得直接写入规范、决策记录或当最终结论。
- **需求深挖**：[How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)（Felix Rieseberg，2026-10-13 发表，读取于 2026-10-23）。上面的四问来自该文的提示词；其中「用外部评判者、不要让模型自评」「挑战已知」「用专业人员同款工具」几条可直接采用。

## 仓库类型

| 类型 | 工作流 | 版本号 |
|---|---|---|
| 有产物仓 | build.yml + pr-check.yml | 有 |
| 无 CI 仓 | 清零 | 可选，脚本内 VERSION |
| 纯存储仓 | 无 | 无 |
| 规范仓 | 无 | 无 |

纯存储仓不加规范文件、工作流、构建或发布机制，除非主人明确要求；无 CI 仓和规范仓不涉及下面的版本与清理两节。

## 工作流结构（C1–C6）

- **C1** 固定两个工作流：`build.yml`（name: Build）与 `pr-check.yml`（name: PR check），缺一或多一都属偏离。改名用 `git mv`。
- **C2** Build 负责构建与上传产物，触发仅 push 与 workflow_dispatch，push 不限分支。
- **C3** PR check 负责校验与清理，触发仅 pull_request，不取版本号、不上传产物。
- **C4** 两个工作流都声明 `SEGMENTS` 与 `CLEANUP_APPLY` 且同值；产物与运行记录的清理在两者中都可执行，Release 与 tag 的清理单独成 job、只在 Build 的默认分支上跑；所有清理 job 共用同一 concurrency group。
- **C5** checkout 必须 `fetch-depth: 0`。
- **C6** artifact 名称为 `项目名-版本`，`retention-days: 5`，`if-no-files-found: error`。

## 版本口径

版本为五段 `yy.m.d.当日序号.总序号`（SEGMENTS=5），日期按 UTC+8，展示版本不带 v、不带项目名；artifact 与发行名为 `项目名-版本`。总序号 = `git rev-list --count HEAD`；当日序号 = 当日 0 点（UTC+8）起的提交数，HEAD 不在当日时为 0。禁止 run_number、触发事件、工作流文件名、PR 状态参与计算；同一提交同一天重跑得同一版本，跨日重跑按取号当天计算。取号时输出 HEAD SHA、两个序号与命令原文，失败即退出，不降级。时区一律写 UTC+8，文字、注释、命令里都不写时区名；命令用固定偏移，例如 `date -u -d '+8 hours' +%F`，Python 用 `timezone(timedelta(hours=8))`，git 的 `--since` 带 `+08:00`。禁止空提交、无内容提交、重写已用于出包或版本取数的历史。无 CI 仓的脚本可带单一来源的 `VERSION` 常量，口径同上，提交前按提交后的计数预取（总序号 = 当前计数 + 1），提交标题不带版本号。

## 清理规则

Release 最多 1 个；带本项目前缀（如 `Qself-`）且无对应 Release 的孤立 tag 一并删。每个工作流最多保留最新 5 条运行记录，每仓最多保留最新 5 个 artifact，运行记录上限优先。清理前打印待处理清单，只动本项目对象。产物与运行记录的清理 job 使用 `actions: write` + `contents: read`；Release 与 tag 的清理单独只授 `contents: write`，其 checkout 不留带写权限的凭据；同一 job 不得同时授两种写权限。清理失败：403 权限缺口打 warning，写明对象、端点与返回码后继续；403 以外当轮失败。构建与取号不降级。

## README 与文档

项目仓只用标准 Markdown（标题、段落、列表、代码块、表格），不放徽章、图片、HTML。章节按固定顺序，没有的省略：`# 项目名`（不带版本号）→ 一句话简介 → `## 要求` → `## 功能` → `## 安装与使用` → `## 构建` → `## 项目限制` → `## 许可证` → 末行；其他内容放进这些章节的 `###` 小节，不另设二级章节。末行固定写「遵循 [Sumicya/selfs](https://github.com/Sumicya/selfs) 最新 GLOBAL.md。」，不写提交 SHA、不写仓库类型。规范仓 README 按用途组织（使用、修改）。README 不放维护记录。

任何仓库不得存在 AGENTS.md（含 agents.md、agent.md 等变体）。文档用简体中文，先给结果。

CHANGELOG.md：文件名固定（大小写一致），按日期倒序，只留最新 5 条，更早的原样移入 `bad/CHANGELOG-history.md`（新到旧，加在文件开头）；只记变更，不留工具输出残留。有可见变化的任务在同一提交里更新最新条目，不事后补记；同一天同一问题的多轮迭代并入同一条，不另起「续N」。

## 工作区旧图

仓库工作区里的证据图、预览图、对比图只留当前仍然成立的，同一个问题只留最终修完状态那一版。出新图的同一提交里，删掉被它覆盖的旧图，并同步说明文档里的引用与留存清单；中间版本留在 git 历史。前后对比图在问题修完后按中间版本处理，除非对比对象本身是现行参照。删除前后都不得留下指向已删文件的引用。

## 设计取向记录

主人评价观感、粗细、比例、风格的仓（目前 Selffont），维护 `docs/design-principles.md`，记的是主人的取向，筑紫等外部参照的客观事实另放参照文档。主人每给一次这类反馈，同一轮里提炼成一句话原则写进去，附日期和反馈的关键词，不贴整段；与旧条冲突时改写旧条，不堆叠，只留当前有效的，被替代的删除（历史在 git）。每次做设计决策、开始新一批字形或界面前先读它，按它判断，出图时对照它。首次建立该文件时，由 agent 从仓库里已有的主人反馈（提交说明、TODO、变更记录和设计文档里「主人……」的记录）提炼初稿，每条写明来源，交主人审改；主人审定前，文件顶部标注「待主人审定」。

## 收尾模板（建议格式）

在仓库工作区里推送改动的 Agent，完成时用固定块收尾，每项必填，没有就写「无」：
- 分支与 head：分支名和完整 SHA。
- 链接：head 提交链接，以及 compare 链接。
- 图：回复里已摆出的图及其仓库链接。
- 自检 1–6：每项一行，结论加证据。
- 规范：开始时与收尾时 selfs main 的 SHA；两者不同则写明已重读的变更。
- 资料：读过方法资料时，写明上游 HEAD SHA 与文件链接。
- 设计原则：本轮新增或修改的条目。
- 偏离：偏离的条文号或条目名与理由。
- 阻塞：端点、返回码、缺少的权限类别和可执行命令。

确已完成，整块以「已执行，结果如下」开头；仍有阻塞，以「阻塞在此，命令如下」开头。链接和逐项证据是模板的一部分，不因对话变长而省略。

## 收尾自检（建议）

1. 工作树干净，无未推送提交，远端 head 与本地一致，未强推。
2. 本仓 README、GLOBAL、CHANGELOG 口径一致；无 AGENTS.md；README 章节与末行、CHANGELOG 文件名与条数符合上面的规定；本次推送的提交标题逐条对照 GLOBAL.md 底线里的「类型: 中文摘要」。
3. 按任务范围核对产物、运行记录、Release、tag、会话分支与工作流注册表，报告真实数量；工作区证据图逐张核对，写明删了哪几张、留了哪几张及理由；清理判据实际执行，未执行标为未验证。
4. 每项结论能定位到文件、行、提交或对象链接；数字注明取值时间与范围。
5. 区分事实、推断与未验证事项；不提议、催促或询问合并与发布，不把已授权操作推回给主人。
6. 回复正文里有提交链接、图本身（适用时）、检讨全文（触发时）。

缺少证据的项目不得报为通过；受阻时写明阻塞端点、返回码、缺少的权限类别和可执行命令。
