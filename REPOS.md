# 仓库与 CI 统一约定

各仓共用的目录边界、CI 结构、版本口径、清理规则与文档格式。具体工程解法留给 Agent 发挥，但仓库目录、工具准入、CI 风格、版本取数与文档结构全仓统一，不得各自为政。优先级低于 [GLOBAL.md](GLOBAL.md) 的四个要领和底线。

## 方法资料（必读，见 GLOBAL.md 底线）

- [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md)：工程方法，先理解影响范围、选最小完整方案、优先复用现有实现。
- [nagi-studio/skills](https://github.com/nagi-studio/skills)：`grill`（分轮追问）、`architect`（技术方案比较）、`prove-it`（拿证据交差）。读过并采用其中的做法时，在汇报里写明用了哪条。
- 它们是方法来源，不是授权来源；主人当轮指示和 GLOBAL.md 的底线优先。不要因引用而自动安装、执行其安装命令。
- **使用边界**：
  - `grill`：主人在消息里写「N 级」时直接按 N 级追问（如 5 级为严格挑战前提），不必先问强度和是否留记录；追问不等于停工，可回退部分按推荐项先做并写明假设，未经主人要求不新建 `docs/decisions-*.md`。
  - `prove-it`：只写守住真实行为的测试。**严禁**往仓库里写 Agent 汇报辅助脚本、规范检查脚本、读取源码文本做字符串/正则匹配的伪测试、手写假宿主引擎替身（如伪造 Roblox/Android 环境的 `smoke.lua`），或用 Pillow/matplotlib 自画文本框示意图充当截图。

## 参考资料（按领域，任务涉及时必读）

一旦任务涉及对应领域、计划采用其工具或依据其方法，先读当前上游的相关 README、规范或官方文档，再实施，不得只凭二手摘要。引用时记录实际读取的 ref / 提交 SHA 或网页标题与读取日期；链接失效先寻找当前官方替代来源，仍无法访问时暂停依赖该资料的操作并报告，不能声称已核对。
- **CLI/项目使用文档**：涉及 Python 工具安装或工作流时查 [uv](https://github.com/astral-sh/uv)；涉及 GitHub CLI 时查 [cli/cli](https://github.com/cli/cli)。
- **逆向分析任务**：仅限自有或明确授权对象。APK 逆向须查当前实际采用工具的上游文档。确定性校验查 [reverify](https://github.com/2akouwu/reverify)；Ghidra 查 [官方文档](https://github.com/NationalSecurityAgency/ghidra)及[安全公告](https://github.com/NationalSecurityAgency/ghidra/security/advisories)；REA 查 [morluto/rea](https://github.com/morluto/rea)。只读必要资料，不自动安装工具、注册 MCP 或执行第三方脚本。
- **工具发现与评估任务**：按需检查 [DexSQL](https://github.com/LSPosed/dexsql-release)、[Monid](https://github.com/monid-ai/monid)、[Maskit](https://github.com/xiaYuTian11/maskit)、[LoomFlow](https://github.com/banmu123/LoomFlow)、[vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit)、[awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools)、[hypit](https://github.com/hypit-ai/hypit) 当前上游资料。核对维护状态、许可证、权限、数据流向和安全风险后再报告结论。Telegram [鑫源AI分享](https://t.me/xinyuanai) 仅作工具发现线索，须回到官方来源独立核实，报告时标注「未独立核实」。
- **需求深挖**：[How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)（Felix Rieseberg，2026-10-13 发表，读取于 2026-10-23）。

## 仓库类型

| 类型 | 工作流 | 版本号 |
|---|---|---|
| 有产物仓 | `build.yml` + `pr-check.yml` | 有（CI 运行数） |
| 无 CI 仓 | 清零 | 可选（脚本内 `VERSION` 手动计数） |
| 纯存储仓 | 无 | 无 |
| 规范仓 | 无 | 无 |

纯存储仓不加规范文件、工作流、构建或发布机制，除非主人明确要求；无 CI 仓、纯存储仓和规范仓不涉及下面的工作流与清理两节。

## 目录与工具边界

- **目录收敛**：仓库只保留构建与交付必需的目录。确需保留的项目辅助脚本统一放在 `tools/`，不设 `scripts/`、`ci/` 等平级脚本目录；单文件脚本仓（如 `Selfblox`）保持根目录单文件结构，不拉 `tools/`、`docs/` 或测试目录。
- **工具准入**：`tools/` 只放与项目产物构建、逆向核对或核心算法直接相关且需长期复用的工具。**严禁**入库以下四类文件：
  1. **Agent 汇报与会话辅助脚本**：如拼接汇报链接的 `report_links.py`、规范自检脚本等，不得写进仓库或 `README.md`。
  2. **源码文本匹配伪测试**：禁止读取业务源码做字符串或正则匹配冒充单元测试，也禁止为 `.github/scripts/cleanup.py` 另配测试文件。单元测试只放项目标准测试目录（如 `app/src/test/`），只测真实行为与纯函数。
  3. **手写假宿主引擎替身**：目标运行环境为真机或专有宿主（如最新 Delta 执行器、Android 真机）时，禁止手写几百行假引擎 Mock（如 `smoke.lua` 及配套 `tools/luau-driver/`）入库自嗨。沙箱内需要做语法/编译检查时，在 `/tmp` 临时运行编译器，工具与脚本不入库；宿主真机行为如实标为「未验证」。
  4. **一次性生图脚本与废弃原型**：如 Pillow 画字脚本 `make_*_preview.py`、`render_*.py`，以及摸索期淘汰的算法原型、网页小工具、额外依赖表（`requirements-research.txt`）。正式逻辑必须收敛进唯一主构建入口（如 `build.py` 或 `app/src/main/`），淘汰原型与一次性脚本在定稿同一提交内删除。
- **文档目录克制**：除 `README.md`、`CHANGELOG.md`、`bad/CHANGELOG-history.md` 与许可证外，未经主人要求不新建 `TODO.md`、`docs/decisions-*.md`、`docs/design-principles.md`（仅 `Selffont` 维护），不在 `docs/` 下拉日期子目录或堆积过程对账表（csv/tsv/json/txt）。

## 工作流结构（C1–C6）

- **C1** 有产物仓固定两个工作流：`.github/workflows/build.yml`（`name: Build`）与 `.github/workflows/pr-check.yml`（`name: PR check`），缺一或多一都属违规。改名用 `git mv`。
- **C2** `Build` 触发仅 `push`（不限分支）与 `workflow_dispatch`，固定三个 job：
  1. `build`：完成静态/落点校验、取版本号、编译测试与上传 artifact；权限仅 `contents: read` 与 `actions: read`，**不得**授 `actions: write` 或把清理塞进 `build` 步骤；前置校验并入 `build` 步骤，不另拆平级 job。
  2. `cleanup-artifacts`：`needs: build`，权限 `actions: write` + `contents: read`，运行 `python3 .github/scripts/cleanup.py`（`CLEANUP_SCOPE: actions`）。
  3. `cleanup-releases`：`needs: build`，条件 `if: github.ref == format('refs/heads/{0}', github.event.repository.default_branch)`，权限仅 `contents: write`，checkout 设 `persist-credentials: false`，运行 `python3 .github/scripts/cleanup.py`（`CLEANUP_SCOPE: releases`）。
- **C3** `PR check` 触发仅 `pull_request`（不加 `branches` 过滤），不取版本号、不上传产物，固定两个 job：`check`（跑校验与测试，权限 `contents: read`）与 `cleanup-artifacts`（权限 `actions: write` + `contents: read`，运行 `python3 .github/scripts/cleanup.py`，`CLEANUP_SCOPE: actions`）。
- **C4** 两个工作流均在文件顶层 `env:` 声明 `SEGMENTS: '5'` 与 `CLEANUP_APPLY: 'true'`；所有清理 job 共用同一份 `.github/scripts/cleanup.py` 与同一 `concurrency` group `<项目名小写>-cleanup`（`cancel-in-progress: false`），统一传入环境变量：`GH_TOKEN: ${{ github.token }}`、`REPO: ${{ github.repository }}`、`RUN_ID: ${{ github.run_id }}`、`CLEANUP_SCOPE: actions`（或 `releases`）。
- **C5** 步骤 `name` 统一用简洁中文短语；工作流顶部注释不超过 5 行，只写当前职责；**禁止**私加正则抓取 `::error::` 注解或 `$GITHUB_STEP_SUMMARY` 日志尾巴；checkout 默认浅克隆即可。
- **C6** artifact 名称为 `项目名-版本`，`retention-days: 5`，`if-no-files-found: error`，`overwrite: true`。

## 版本口径

展示版本不带 `v`、不带项目名；artifact 与发行名为 `项目名-版本`。时区一律写 `UTC+8`（固定偏移 `date -u -d '+8 hours'`，Python 用 `timezone(timedelta(hours=8))`），文字、注释、命令、日志与汇报里严禁出现 `Z`、`UTC` 或时区地名。禁止空提交、无内容提交。

- **有产物仓（CI 运行数，防提交刷号）**：
  - 五段 `yy.m.d.当日序号.总序号`（`SEGMENTS=5`，日界 `UTC+8`）。不用 `git rev-list --count`。
  - **总序号** = `build.yml` 本次运行的 `github.run_number` 原值（Android `versionCode` 同取该值）。不做基线相减；从提交数切回 CI 数或改工作流后数值变小照常使用（设备端有覆盖安装模块）。
  - **当日序号** = 当日（`UTC+8`）`build.yml` 运行的位次（从 1 起，失败运行同样占号，PR check 运行永不计入）。按差值锚定法计算：通过 GitHub API 取 `build.yml` 当日（`run_started_at` 转 `UTC+8` 日期等于当日）现存运行的最小 `run_number`，以及当日现存合规产物 `项目名-yy.m.d.d0.r0` 反推的 `r0 - d0 + 1`，取二者中的最小值作为当日首条运行号 `R_first`（若均无则为当前 `run_number`），`当日序号 = 当前 run_number - R_first + 1`。同一 `run_id` 重试（`run_attempt > 1`）保持同一版本号。
  - 取号时输出 `HEAD SHA`、`run_id`、`run_number`、`R_first`、当日序号与最终版本，失败即退出，不降级。
- **无 CI 仓（手动计数）**：
  - 可在脚本内维护单一来源的 `VERSION` 常量（如 `Selfblox`），按实际功能交付**手动计数**（随业务代码提交一并手动更新，不用 `git rev-list --count` 硬绑 git 提交数，更不得为了改版本号单独发提交）。

## 清理规则

Release 最多 1 个；带本项目前缀且无对应 Release 的孤立 tag 一并删。每个工作流最多保留最新 5 条运行记录（按 `run_started_at` 降序，缺失时退回 `created_at`，`id` 作同刻 tiebreak；硬上限，不设当日豁免，超限的未完成运行先 cancel），每仓最多保留最新 5 个 artifact，运行记录上限优先。

`.github/scripts/cleanup.py` 全仓统一接口（读取 `GH_TOKEN`、`REPO`、`RUN_ID`、`SEGMENTS`、`CLEANUP_APPLY`、`CLEANUP_SCOPE=actions|releases`，项目名前缀由 `REPO` 推导），artifact 按五条判据依次清理：
1. **命名口径**：版本段数必须等于 `SEGMENTS`（5 段）。
2. **来源**：来源 `workflow_run.event == 'pull_request'` 的产物一律删。
3. **重复当日序号**：同一日出现相同当日序号时，按来源运行的 `run_started_at` 删旧留新。
4. **号源口径**：产物名末段 `总序号` 必须等于其来源 `workflow_run` 的 `run_number`。切换号源过渡期：若全仓尚无任何满足 `总序号 == run_number` 的新产物，暂留最新 1 个旧产物，待首个新口径产物上传成功后再清零旧产物。
5. **数量**：全仓按 `created_at` 保留最新 5 个，且其来源运行必须仍在该工作流保留的最新 5 条运行记录内。

清理前打印待处理清单，只动本项目对象。`CLEANUP_SCOPE=actions` 作业使用 `actions: write` + `contents: read`；`CLEANUP_SCOPE=releases` 作业单独只授 `contents: write`，checkout 设 `persist-credentials: false`；同一 job 不得同时授两种写权限。清理失败：403 权限缺口打 warning，写明对象、端点与返回码后继续；403 以外当轮失败。构建与取号不降级。

## README 与文档

项目仓只用标准 Markdown（标题、段落、列表、代码块、表格），不放徽章、图片、HTML。章节按固定顺序，没有的省略：`# 项目名`（不带版本号）→ 一句话简介 → `## 要求` → `## 功能` → `## 安装与使用` → `## 构建` → `## 项目限制` → `## 许可证` → 末行；其他内容放进这些章节的 `###` 小节，不另设二级章节。末行固定写「遵循 [Sumicya/selfs](https://github.com/Sumicya/selfs) 最新 GLOBAL.md。」，不写提交 SHA、不写仓库类型。规范仓 README 按用途组织（使用、修改）。README 不放维护记录，也不登记 Agent 会话辅助脚本或假引擎测试。

任何仓库不得存在 AGENTS.md（含 agents.md、agent.md 等变体）。文档用简体中文，先给结果。

CHANGELOG.md：文件名固定（大小写一致），按日期倒序，只留最新 5 条，更早的原样移入 `bad/CHANGELOG-history.md`（新到旧，加在文件开头）；只记变更，不留工具输出残留。有可见变化的任务在同一提交里更新最新条目，不事后补记；同一天同一问题的多轮迭代并入同一条，不另起「续N」。

## 工作区旧图

仓库工作区里的证据图、预览图、对比图只留当前仍然成立的，同一个问题只留最终修完状态那一版。出新图的同一提交里，删掉被它覆盖的旧图，并同步说明文档里的引用与留存清单；中间版本留在 git 历史。前后对比图在问题修完后按中间版本处理，除非对比对象本身是现行参照。删除前后都不得留下指向已删文件的引用。

## 设计取向记录

主人评价观感、粗细、比例、风格的仓（目前 Selffont），维护 `docs/design-principles.md`，记的是主人的取向，筑紫等外部参照的客观事实另放参照文档。主人每给一次这类反馈，同一轮里提炼成一句话原则写进去，附日期和反馈的关键词，不贴整段；与旧条冲突时改写旧条，不堆叠，只留当前有效的，被替代的删除（历史在 git）。每次做设计决策、开始新一批字形或界面前先读它，按它判断，出图时对照它。首次建立该文件时，由 agent 从仓库里已有的主人反馈提炼初稿，每条写明来源，交主人审改；主人审定前，文件顶部标注「待主人审定」。

## 收尾模板

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

## 收尾自检

1. 工作树干净，无未推送提交，远端 head 与本地一致，未强推。
2. 本仓 README、GLOBAL、REPOS、CHANGELOG 口径一致；无 AGENTS.md；README 章节与末行、CHANGELOG 文件名与条数符合上面的规定；本次推送的提交标题逐条对照 GLOBAL.md 底线里的「类型: 中文摘要」。
3. 按任务范围核对产物、运行记录、Release、tag、会话分支与工作流注册表，报告真实数量；工作区证据图与 `tools/`、`docs/` 逐项核对，写明删了哪些、留了哪些及理由；清理判据实际执行，未执行标为未验证。
4. 每项结论能定位到文件、行、提交或对象链接；数字注明取值时间与范围（时间一律写 `UTC+8`，禁写 `Z` 或 `UTC`）。
5. 区分事实、推断与未验证事项；不提议、催促或询问合并与发布，不把已授权操作推回给主人。
6. 回复正文里有提交链接、图本身（适用时）、检讨全文（触发时）。

缺少证据的项目不得报为通过；受阻时写明阻塞端点、返回码、缺少的权限类别和可执行命令。
