# Sumicya 规范

以**辩证法、简单性、先进性、自由性**指导项目工作。[GLOBAL.md](GLOBAL.md) 是对外规范总纲，[REPOS.md](REPOS.md) 是各仓共用的目录边界、CI 结构、版本口径与文档约定，以 selfs `main` 最新提交为准（引用附提交 SHA 与链接），[CHANGELOG.md](CHANGELOG.md) 按日期记录变更；默认分支落后于最新规范提交时当轮报事实。本仓文档不带版本号。

## 使用

开始每个工程任务先用 `git ls-remote https://github.com/Sumicya/selfs refs/heads/main` 取最新 SHA，读 [GLOBAL.md](GLOBAL.md) 与 [REPOS.md](REPOS.md) 全文、Ponytail 与 `nagi-studio/skills` 当前上游（记录上游 HEAD SHA）和项目 `README.md`，并按 [REPOS.md](REPOS.md)「参考资料」核读与任务领域相关的辅助仓库和网页，再核对相关实现。有实际冲突就提问，已明确要求直接执行；事实、推断和未验证事项分开说明。

```text
读 Sumicya/selfs main 最新提交 <sha> 的 GLOBAL.md 与 REPOS.md、Ponytail 当前 main 的 skills/ponytail/SKILL.md、nagi-studio/skills 当前 main 的 grill 与 architect（记录各上游 HEAD SHA）和当前项目 README.md；按 REPOS.md 读取与本轮任务相关的辅助仓库及网页；本轮任务：……
```

项目事实与必要限制写在项目 `README.md`，末行留规范指针；任何仓库不得存在 `AGENTS.md`。README 不复制全局规则，不写版本号或同步戳，不登记 Agent 汇报辅助脚本。发现本仓条目与规范冲突，当轮改本仓条目并报主人。无法读取远端时如实说明，不假称已读最新。

## 修改

修改规范时清除相反表述，更新变更记录，核对本仓 `README.md`、[GLOBAL.md](GLOBAL.md)、[REPOS.md](REPOS.md) 与相关文档一致性。本轮改动提交并推送到会话分支，收尾按 [REPOS.md](REPOS.md)「收尾自检」1–6 项全跑，缺一项按未完成处理。合并与发布只由主人主动发起，会话不提议、不催促、不询问。

历史记录不作为现行规则例外。本仓不维护各项目的实时状态表，也不设置规范检查 CI；核对由 agent 在会话中完成。

规范指针：[GLOBAL.md](GLOBAL.md) · [REPOS.md](REPOS.md)（以 selfs `main` 最新提交为准）
