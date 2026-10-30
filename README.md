# Sumicya 规范

以**辩证法、简单性、先进性、自由性**指导项目工作。[GLOBAL.md](GLOBAL.md) 是唯一对外规范入口，以 selfs 最新提交为准（有 open 规范 PR 时为其 head 提交，无则为 `main`；引用附提交 SHA 与链接），[CHANGELOG.md](CHANGELOG.md) 按日期记录变更；默认分支落后于最新规范提交时当轮报事实。本仓文档不带版本号。

## 使用

开始每个工程任务先取生效提交：跑 `gh api 'repos/Sumicya/selfs/pulls?state=open&per_page=10'` 查 open 规范 PR，有则取其 head SHA（多个取 `updated_at` 最近者），无则用 `git ls-remote https://github.com/Sumicya/selfs refs/heads/main` 取 `main` SHA；读该提交的 [GLOBAL.md](GLOBAL.md) 全文、取 [GLOBAL.md](GLOBAL.md)「必读工具与方法仓库」全部 17 个上游仓库的当前 HEAD SHA 并核读其核心文档，再读项目 `README.md` 与核对相关实现。有实际冲突就提问，已明确要求直接执行；事实、推断和未验证事项分开说明。

```text
读 Sumicya/selfs 生效提交（open 规范 PR head 或 main）<ref> <sha> 的 GLOBAL.md 全文，读取 GLOBAL.md「必读工具与方法仓库」全部 17 个上游仓库当前 HEAD 和当前项目 README.md；本轮任务：……
```

项目事实与必要限制写在项目 `README.md`，末行留规范指针；任何仓库不得存在 `AGENTS.md`。README 不复制全局规则，不写版本号或同步戳，不登记 Agent 汇报辅助脚本或假引擎测试。发现本仓条目与规范冲突，当轮改本仓条目并报主人。无法读取远端时如实说明，不假称已读最新。

## 修改

修改规范时清除相反表述，更新变更记录，核对本仓 `README.md`、[GLOBAL.md](GLOBAL.md) 与相关文档一致性。本轮改动提交并推送到会话分支，收尾按 [GLOBAL.md](GLOBAL.md)「收尾自检」1–6 项全跑，缺一项按未完成处理。合并与发布只由主人主动发起，会话不提议、不催促、不询问。

历史记录不作为现行规则例外。本仓不维护各项目的实时状态表，也不设置规范检查 CI；核对由 agent 在会话中完成。

规范指针：[GLOBAL.md](GLOBAL.md)（以 selfs `main` 最新提交为准）
