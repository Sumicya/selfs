# Sumicya 规范

以**第一性原理、苏格拉底式提问、辩证法、简单性、先进性、自由性**指导项目工作。[GLOBAL.md](GLOBAL.md) 是唯一对外规范入口，以 selfs 最新提交为准（有 open 规范 PR 时为其 head，无则为 `main`；引用附提交 SHA 与链接），[CHANGELOG.md](CHANGELOG.md) 按日期记录变更；默认分支落后于最新规范提交时当轮报事实。本仓文档不带版本号。

## 使用

每个工程任务先取生效提交：跑 `gh api 'repos/Sumicya/selfs/pulls?state=open&per_page=10'` 查 open 规范 PR，有则取其 head SHA（多个取 `updated_at` 最近者），无则用 `git ls-remote https://github.com/Sumicya/selfs refs/heads/main` 取 `main` SHA；读该提交的 [GLOBAL.md](GLOBAL.md) 全文，按「4 上游」读完七份入口全文并给读证，再读项目 `README.md` 与核对相关实现。该问的六类见 [GLOBAL.md](GLOBAL.md)「8 什么时候开口」，已明确要求直接执行；事实标三类（观测／推断／未知）。

```text
读 Sumicya/selfs 生效提交（open 规范 PR head 或 main）<ref> <sha> 的 GLOBAL.md 全文，按「4 上游」读七份入口全文和当前项目 README.md；本轮任务：……
```

项目事实与必要限制写在项目 `README.md`，末行留规范指针；任何仓库禁留 `AGENTS.md`。README 不复制全局规则，不写版本号或同步戳，不登记会话脚本或假引擎替身（见「11 目录」）。发现本仓条目与规范冲突，当轮改本仓条目并报主人。无法读取远端时如实说明，不假称已读最新。

## 修改

修改规范时清除相反表述与死引用，更新变更记录，核对本仓 `README.md`、[GLOBAL.md](GLOBAL.md)、[CHANGELOG.md](CHANGELOG.md) 口径一致。本轮改动提交并推送到会话分支，收尾按 [GLOBAL.md](GLOBAL.md)「25 自检」五条全跑，缺一按未完成。合并与发布只由主人主动发起，会话不提议、不催促、不询问。

历史记录不作为现行规则例外。本仓不维护各项目的实时状态表，也不设规范检查 CI；核对由 agent 在会话中按一条命令完成。

## 许可证

本仓采用 GNU General Public License v3.0（GPL-3.0），全文见 [LICENSE](LICENSE)。引用、转载或改写本规范条文须遵守该许可；各项目仓库保留自己的 LICENSE。GPL-3.0 与 OFL-1.1 执行要求见 [GLOBAL.md](GLOBAL.md)「17 许可」。

规范指针：[GLOBAL.md](GLOBAL.md)（有 open 规范 PR 时为其 head，无则为 `main`）
