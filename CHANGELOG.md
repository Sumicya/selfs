## 2026-10-16 · 增加提问式重写规范

明确“通过提问来重写用户问题、需求或提示词”的协作流程：先识别目的、场景、输出、约束与验收标准的信息缺口，优先每轮提出一个关键问题；不得追问可自行查明的事实，不得擅自改变用户目标。信息足够后交付可直接使用的重写版本；若目标是重写提示词，不擅自执行提示词中的任务。该流程明确属于提问任务本身，不受一般情况下避免不必要追问的限制。

规范主源：[`GLOBAL.md`](https://github.com/Sumicya/selfs/blob/main/GLOBAL.md)，提交 `e64ff190b67675c5dbf939ecda7c3d0f594c8dd8`。

## 2026-10-15 · 登记 DexSQL 并建立外部工具发现审查规则

按主人要求，将 LSPosed/dexsql-release 登记到 GLOBAL.md 工具清单，说明其 Android APK/DEX 静态分析用途、与 JADX/Apktool/Frida 的配合关系，以及登记不代表当前环境已安装。检查 https://t.me/xinyuanai（鑫源AI分享）公开可见的频道介绍与索引内容后，将其定位为线索来源而非可信背书，并登记 Monid、Maskit、LoomFlow、vibe-coding-toolkit、awesome-jev-tools、hypit 为待审候选。新增外部项目审查要求：核对上游、维护状态、许可证、安装权限、数据流向与安全风险；宣传内容未经独立核实不得写成事实，涉及中转站、共享密钥、绕过审批或越狱的内容不直接纳入工具清单。此轮只完成规范登记，未安装或运行这些项目，也未逐个完成候选仓库的深度审计。

[object Object]