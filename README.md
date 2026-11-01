# Sumicya 规范

以**辩证法、简单性、先进性、自由性**指导项目工作。[GLOBAL.md](GLOBAL.md) 是唯一对外规范入口，[CHANGELOG.md](CHANGELOG.md) 记条款沿革。本仓文档不带版本号。

## 使用

**生效点是本仓全仓最新提交**：跨分支按 `commit.committer.date` 取最晚者，不看有没有 open PR，不以 `main` 兜底。

```text
gh api "repos/Sumicya/selfs/branches?per_page=100" --jq '.[].name'
gh api repos/Sumicya/selfs/commits/<sha> --jq .commit.committer.date
gh api repos/Sumicya/selfs/contents/GLOBAL.md?ref=<sha> --jq .sha
```

取到最新那个提交后，读该提交下的 [GLOBAL.md](GLOBAL.md) 全文，再取「五、上游必读」17 个仓库的当前 HEAD、核读其入口文件，然后读目标项目的 `README.md` 与相关实现。有实际冲突就提问（该问的四类见 [GLOBAL.md](GLOBAL.md)「零、开动：五问与提问裁决」）；已明确要求直接执行。事实、推断、未验证分开写。

给 agent 的一句话：

```text
读 Sumicya/selfs 全仓最新提交 <sha> 的 GLOBAL.md 全文，取「五、上游必读」17 个上游仓库当前 HEAD 并核读入口文件，再读当前项目 README.md 与相关实现；本轮任务：……
```

项目事实与限制写在项目自己的 `README.md`，末行留规范指针；任何仓库不得存在 `AGENTS.md`。README 不复制全局规则，不写「当前最新」这类会腐化的数字，不登记 Agent 汇报辅助脚本或假引擎测试。发现本仓条目与规范冲突，当轮改条目并报主人。读不到远端就如实说明，不假称已读最新。

## 修改

改规范时清掉相反表述，同步 `CHANGELOG.md`，并核对本仓 `README.md` 与 [GLOBAL.md](GLOBAL.md) 口径一致。改动提交并推送到会话分支，收尾按 [GLOBAL.md](GLOBAL.md)「收尾自检」1–6 项全跑，缺一项按未完成处理。合并与发布只由主人主动发起，会话不提议、不催促、不询问。

历史条目不是现行规则的例外；本仓不维护项目状态表，也不设规范检查 CI，核对由 agent 在会话中完成。

## 许可证

本仓采用 GNU General Public License v3.0（GPL-3.0），全文见 [LICENSE](LICENSE)，与 Qself 同源。引用、转载或改写条文须遵守该许可；各项目仓库保留自己的 `LICENSE`，不因引用本规范而改变。逐条执行义务见 [GLOBAL.md](GLOBAL.md)「八、许可证执行（GPL-3）」。

规范指针：[GLOBAL.md](GLOBAL.md)（以 selfs 全仓最新提交为准）
