# Sumicya 规范与集合

Sumicya 全项目的全局规则放在这里：`GLOBAL.md` 是**唯一权威**，`CHANGELOG.md` 记每一版改了什么。各项目仓库的 `AGENTS.md` 只写该项目的条目，再加一行指向本仓库的指针和「上次同步 = 第 N 版」的版本戳。

## 怎么用

- 开新会话 / 换窗口 / 换项目时，贴给会话的只要一行：

  `读 Sumicya/selfs 的 GLOBAL.md（最新版）和本仓库 AGENTS.md，按规范干活；本轮任务：……`

- 会话每轮开头会回一行「已读 AGENTS.md（项目规则）+ 规范第 N 版；本轮项目核对清单是……」——没看到这行就是它没读。

- 会话自己核对版本落后没落后：

  `gh api repos/Sumicya/selfs/contents/GLOBAL.md --jq .sha`（记下 sha），`gh api repos/Sumicya/selfs/contents/GLOBAL.md --jq .content | base64 -d | head -1`（看标题里的第几版）。

- 查某个仓库的 `AGENTS.md` 和默认分支：

  `gh api repos/Sumicya/<仓库>/contents/AGENTS.md --jq .size`、`gh api repos/Sumicya/<仓库> --jq .default_branch`

## 怎么改

- 改规则：改 `GLOBAL.md`，在 `CHANGELOG.md` 顶部加一条（版本、日期、改了什么），标题里的版本号一起 +1。
- 改完让下一个会话在项目 `AGENTS.md` 里把版本戳更新掉；版本戳落后会让会话按旧规则干活，这是要防的事。
- 不在这里放会腐烂的东西：不列「各仓库现状表」，不复制各项目的核对清单（那些在各仓库自己的 `AGENTS.md` 里），不写死 run 号、最大值这类现值，只写查法。
