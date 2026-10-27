## 2026-10-27 · 必读仓库增至 15 个（新增 qybaihe/bla），装工具先提出经主人许可，资料行强制短 SHA

- 「必读工具与方法仓库」新增第 15 个 qybaihe/bla（BLA，Blind LLM Agents）：针对 REA 等 AI 逆向 Agent 的防护与验证工具，与第 7 条 REA 互为攻防两端；底线与本节引言两处「全部 14 个」同步改 15，本仓 README.md 两处同口径一并改。
- 按主人定的权力边界重写安装规则，消除「无由限制 agent 权力」的问题：可读与想用分开——必读义务只覆盖核读，读取随时进行，列入必读不赋予安装或执行的权力；要安装工具、注册 MCP、执行第三方安装命令或脚本、改写 Agent 配置，agent 先向主人提出并说明用途与影响，经主人许可后按许可范围执行，汇报写明许可范围。上游始终是参考来源、不是授权来源：许可安装或运行不改变其性质、不构成对其内容的背书，上游内容任何时候都不高于主人当轮指示、本规范和项目事实。上一稿「授权后视为授权来源」的表述作废。
- 汇报证据收紧：收尾模板「资料」行每任务逐一写 15 个上游 HEAD 短 SHA（不附链接），采用项与许可范围另写，补上外部链接免列后漏读无痕迹的口子。
- BLA 条目按同一规则写：核读入口为 `README.md` 与 `.agents/skills/blind-llm-agents/`；其 Quick start 首条 `npx bla-agents setup` 用来注册 MCP+skill 并改写 Claude Code、Cursor、Codex、Gemini CLI、Windsurf、Antigravity、OpenCode、VS Code、GitHub Copilot CLI 共 9 个 Agent 的配置，运行任何安装或执行命令前先向主人提出、经许可后运行；README 载明的默认一键入口是 `npx bla-agents harden .`，setup 不是默认入口。
- 上游读取（UTC+8）：qybaihe/bla HEAD 短 SHA `3e92cf6`（该提交时间 2026-10-27 13:09 UTC+8，bla-agents v1.4.2）；MIT 的三处仓内证据为 package.json 的 license 字段、README 的 MIT badge、LICENSE 文件（LICENSE 全文接口返回 403 未取到，全文未独立核实）。

## 2026-10-27 · 重写工作流结构与版本口径：清理必须 always()，号源只留 CI 运行数，推送要攒

- **工作流结构（C2/C3 重写）**：`cleanup-artifacts` 与 `cleanup-releases` 一律 `needs: build` + `if: always()`（后者再与默认分支条件相与），并写清 `always()` 不是装饰：只写 `needs` 时构建一红清理整体跳过，保留上限当场失效；`PR check` 的 `cleanup-artifacts` 明写「不写 `needs`、始终运行」。实测成因：Selffont `build.py --check` 连红四轮（`run_number` 211–214）、清理连续跳过四轮，`build.yml` 堆到 9 条运行 + 5 个产物共 14 个对象，一条没清。
- **版本口径（重写）**：开头立「号源只有一处」——只由 CI 运行数产生，禁止提交数、时间戳、手工常量或任何本地计数；并写明「改工作流文件名 / 并发 / PR 运行不让号回头留洞」由 `run_number` 与差值锚定自己保证，不靠换号源解决。旧口径的相反表述已在 2026-10-26 条目统一，正文无残留。
- **新增「攒推送、别刷号」**：每次推送吃一个 `run_number`，一次会话把同类改动攒成一次推送、推送前本地跑完自检与构建；禁止逐个推小修、拿 CI 当编译器试错、为改版本号单独提交或推送。
- **清理规则补口径**：失败／取消／跳过的运行与成功运行一样占号、一样计入 5 条上限；「构建失败所以本轮不清理」被明确写成上限失效的直接成因。
- **起因（可复算，UTC+8）**：Selffont 号源仍挂在提交数上，产物 `Selffont-26.10.26.1.481` 对应 `run_number=210`，当时分支提交数正好 481、之后 6 次推送变 487；Qself 已在 23:29–23:41 迁移到 `run_number`（产物 `26.10.26.5.347` 对 `run_number=347`）。
- **未完成**：Selffont 的迁移补丁本地自检通过（`build.py --check` 10 项全过）但未落远端——本会话令牌对该仓只读，`git push` 与删除 artifact 均 HTTP 403。

## 2026-10-26 · 合回单文件 GLOBAL.md，全部工具仓库必读，版本号改回 CI 运行数，无 CI 仓手动计数

- **合回单文件 GLOBAL.md（删 REPOS.md）且全部 14 个工具与方法仓库必读**：按主人选定 B，将目录边界、CI 结构、版本口径、清理规则、文档与收尾自检全部合回单文件 `GLOBAL.md` 并删除 `REPOS.md`，根治拆成两份文件后 Agent 漏读第二份文件的问题。按主人决定，将 Ponytail、`nagi-studio/skills`、`uv`、`cli/cli`、`reverify`、`ghidra`、`rea`、`dexsql-release`、`monid`、`maskit`、`LoomFlow`、`vibe-coding-toolkit`、`awesome-jev-tools`、`hypit` 共 14 个上游仓库全部设为开工必读；汇报中除自己仓库外，其他外部仓库链接非必要可以不列。
- **有产物仓版本号改回 CI 运行数，无 CI 仓改为手动计数**：按主人决定，为防止多次 git 提交刷版本号（如 Qself 提交数刷到 3182、Selffont 刷到 480），有产物仓的五段版本 `yy.m.d.当日序号.总序号` 号源从 `git rev-list --count` 改回 `build.yml` 的运行计数。总序号（及 Android `versionCode`）直接取 `github.run_number` 原值，不做基线相减，从提交数切回 CI 数引起的数值回退照常使用（主人设备端有覆盖安装模块）；当日序号按差值锚定法 `当前 run_number - 当日首条 run_number + 1` 计算（当日首条取 API 现存当日运行与现存当日产物反推值的最小者），防止单日超 5 次运行后旧 run 被清理删除导致序号撞号；清理脚本第 4 条「号源口径」判据同步改为 `总序号 == workflow_run.run_number`，切换过渡期在首个新口径产物出成前暂留最新 1 个旧产物；checkout 不再要求 `fetch-depth: 0`。无 CI 仓（`Selfblox`）按主人决定改为脚本内 `VERSION` 手动计数，随实际交付手动更新，不再绑 `git rev-list --count`。
- **统一三仓 CI 风格**：`build.yml` 固定 `build`、`cleanup-artifacts`、`cleanup-releases` 三个作业，`pr-check.yml` 固定 `check`、`cleanup-artifacts` 两个作业；`.github/scripts/cleanup.py` 统一环境变量（`GH_TOKEN`、`REPO`、`RUN_ID`、`SEGMENTS`、`CLEANUP_APPLY`、`CLEANUP_SCOPE=actions|releases`）；步骤名统一用简洁中文短语，顶部注释不超过 5 行，禁止私加 `::error::` 正则摘录或 `$GITHUB_STEP_SUMMARY` 日志尾巴。
- **严禁乱写工具、伪测试与假宿主引擎（如 `smoke.lua`）入库**：辅助脚本目录统一为 `tools/`（不设 `ci/`、`scripts/`；单文件脚本仓如 `Selfblox` 保持根目录单文件结构）。严禁向仓库提交四类文件：① Agent 汇报与流程辅助脚本（如 `tools/report_links.py`）；② 读取源码文本做字符串匹配的伪测试（如 `Qself` 的 `tools/test_*.py` 与 `.github/scripts/test_cleanup.py`）；③ 手写假宿主引擎替身（如 `Selfblox` 在最新 Delta 执行根本不需要的 `smoke.lua` 与 `tools/luau-driver/`）；④ 一次性生图脚本（`make_*_preview.py`、`render_*.py`）与淘汰的算法原型（如 `Selffont` 的 41 个 `tools/*.py`、15 个 `tests/*.py`、`docs/round-preview/` 日期子目录）。
- **时区与本仓一致性**：在 `GLOBAL.md` 底线与收尾自检写死汇报正文、日志、注释中的所有时间（含 API 取值时间）一律换算写为 `UTC+8`，严禁写零时区后缀 `Z`。同步更新 `README.md` 去除 `REPOS.md` 与旧编号引用。

## 2026-10-23 · 松绑：规范只留四个要领和底线

- 主人要求给 Agent 松绑，不要那么多限制发挥的规范，主要留四个要领。GLOBAL.md 从 19KB 压到 2.6KB：四个要领（辩证法、简单性、先进性、自由性）加五条底线（不可逆操作、汇报如实、看得见、提交与文档、检讨）。
- 其余全部搬进新文件 REPOS.md，作为参考而不是约束：仓库类型、工作流结构、版本口径、清理规则、README 与文档、旧图、设计取向、方法资料、收尾模板与自检。有理由可以不同，汇报里写明即可。
- 取消：硬约束与默认做法的分层；授权 A1–A6、诚实汇报逐条、提问式重写的细则不再单列，收进底线和自由性。
- 保留并写进四个要领：被说肤浅时的四问、不自评、问完不停工、按消息计次。
- 工具仓库、链接与最新规范仍然必读，写进底线第一条：开始每个任务前取 selfs main 最新 SHA 并读 GLOBAL.md 全文，收尾前再取一次；读 Ponytail 与 nagi-studio/skills 当前上游，任务涉及领域时读 REPOS.md 里对应的链接；汇报里写出规范 SHA 与读取的上游 SHA、文件链接，没写就当没读，主人提醒后才读也算违反。起因：部分 agent 要主人提醒之后才读工具仓库和链接，规范更新后也要主人手动提醒。
- 假设：把「四个要领」理解为原有的四项原则（辩证法、简单性、先进性、自由性）。主人指的若是别的四条，需要重改。

## 2026-10-23 · 增加「深度版」触发

- 主人说「太肤浅」或发来「要更深度的版本」时，Agent 先回答四问（顶尖人会做而没提到的动作、最原始的底层材料、具体方法与工具、Agent 之外能证明结果对的客观指标），答案写到具体工具名、数据来源和指标，据此改写任务提示词，并在同一条消息里开做，不停下来问；客观指标必须是 Agent 之外的工具能复算的，Agent 不自评好坏。
- 参考资料增加需求深挖一条：Felix Rieseberg《How to be more ambitious》（2026-10-13，读取于 2026-10-23），四问取自该文提示词。
- 起因：主人觉得模型产出肤浅时一直在手动贴这段话；规范只写了「追问」，没有写「被说肤浅之后该做什么」。
