# starops-event-lab

这是一个完全由合成代码、合成事件和 dummy secret 组成的事件驱动 DevOps 实验仓库。

## E1：GitHub 确定性事件链

本仓库用于验证：

- Pull Request 的 branch/path 过滤；
- 同一 PR 新提交对旧工作流的并发取消；
- `workflow_dispatch` 手工重放；
- GitHub Environment 审批门禁和 secret 延迟释放；
- Artifact Attestation 的生成与验证。

## 本地验证

```bash
python3 -m unittest discover -s tests
```

禁止在本仓库中提交公司代码、真实流水线日志、真实密钥或内部系统标识。
