## 2026-10-27 · 清理作业构建失败也要跑，号源只留 CI 运行数并要求攒推送

- **清理作业加 `if: always()`（C2/C3）**：`cleanup-artifacts` / `cleanup-releases` 只写 `needs: build` 时，构建一红就整体跳过清理，失败运行只吃号不清理，运行记录会堆到上限之上。实测 Selffont：`build.yml` 现存 9 条运行（上限 5）+ 5 个 artifact，共 14 个对象挂在 Actions 页一次没被清，原因就是 211–214 四次构建全红、清理作业连续四轮跳过。改为 `needs: build` + `if: always()`（`cleanup-releases` 为 `if: always() && 默认分支`）。
- **号源唯一**：版本口径里写明有产物仓号源只有 CI 运行数一处，禁止改用提交数、时间戳或手工常量。
- **新增「攒推送、别刷号」**：每次推送都吃一个 `run_number`，一次会话把同类改动攒成一次推送，推送前先在本地跑完自检与构建；禁止把小修逐个推送、拿 CI 当编译器反复试错，也禁止为改版本号单独提交或推送。
- **起因（事实，可复算）**：Selffont 的 `build.py` 仍按 2026-10-14 的旧口径 `git rev-list --count` 取号，某会话 2026-10-26 23:39–23:48（UTC+8）连推 6 次、产出 4 次失败运行（`run_number` 211–214，全红在 `build.py --check` 的 `supplemental_font_reference`），最新产物仍叫 `Selffont-26.10.26.1.481`，而它对应的 `run_number` 只有 `210`——号源没迁移 + 推送没攒，两个口子一起把版本号刷到 481（提交数），CI 数停在 210。Qself 已在 2026-10-26 23:29–23:38（UTC+8）迁移到 `run_number`（`build.yml` 里现取 `gh api` 算 `R_first`）。
- **未完成**：Selffont 的迁移补丁已写好并本地自检通过（`build.py --check` 10 项全过），但本会话的 GitHub 令牌对 `Sumicya/Selffont` 只读，`git push` 与删除 artifact 均返回 HTTP 403（`Resource not accessible by integration`），补丁未落到远端；产物与运行记录的清理同样未执行。

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

## 2026-10-23 · 计次按消息，设计取向初稿由 agent 提炼，不静默替换指定输入

- 主人确认 Arena 按消息计次、不按 token 计：规范里的表述由「按次计」改为「按消息计次」，并要求每条消息尽量做完能做的全部工作，不为提问、补链接、补图多耗一条消息，非必要不问。补发链接、再问一轮、再要一张图都会多耗一条消息，所以汇报一次做完整比事后补更省。
- 新增诚实汇报第 8 条：不静默替换主人指定的输入，找不到或不可用时汇报写明「指定的是 X，实际用了 Y，原因」，并同步改仓库文档里的引用。起因：主人指定首要视觉参照是筑紫 B，找不到可用的字体包后改用了筑紫 A；规范原先没有要求这种替换必须在汇报里明确写出。Selffont 的 `docs/decisions-笔画简化.md` 事后已加了「后因候选不合格而撤回」的说明，这条规则要求的是当次汇报就写明，而不是事后补。
- 主人选定设计取向的建立方式：首次建立 `docs/design-principles.md` 由 agent 从仓库里已有的主人反馈提炼初稿，每条写明来源，交主人审改，审定前标注「待主人审定」。
