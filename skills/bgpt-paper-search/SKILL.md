---
name: bgpt-paper-search
description: Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including methods, results, sample sizes, quality scores, and conclusions. Use for literature reviews, evidence synthesis, and finding experimental details not available in abstracts alone.
description_zh: 生醫論文搜尋：文獻發現輔助。
license: MIT
compatibility: Requires the BGPT MCP server configured in the agent host (npx mcp-remote or npx bgpt-mcp), internet access to bgpt.pro, and an optional BGPT API key for paid usage.
metadata:
  zh-tw-added: "2026-09-28"
  upstream: K-Dense-AI/scientific-agent-skills
  version: "1.1"
  skill-author: BGPT
  website: https://bgpt.pro/mcp
  github: https://github.com/connerlambden/bgpt-mcp
---
> 本 skill 衍生自上游 K-Dense Scientific Agent Skills（MIT 授權），英文原文完整保留在下方，繁中導讀僅為使用輔助。

## 繁中導讀 Zh-Hant Guide

### 何時使用

- 生醫論文搜尋：文獻發現輔助。
- 詳細參數、工作流程與範例請見下方英文原文。

---

# BGPT Paper Search

## Overview

BGPT is a remote MCP server that searches a curated database of scientific papers built from raw experimental data extracted from full-text studies. Unlike traditional literature databases that return titles and abstracts, BGPT returns structured data from the actual paper content — methods, quantitative results, sample sizes, quality assessments, and 25+ metadata fields per paper.

## When to Use This Skill

Use this skill when:
- Searching for scientific papers with specific experimental details
- Conducting systematic or scoping literature reviews
- Finding quantitative results, sample sizes, or effect sizes across studies
- Comparing methodologies used in different studies
- Looking for papers with quality scores or evidence grading
- Needing structured data from full-text papers (not just abstracts)
- Building evidence tables for meta-analyses or clinical guidelines

## Setup

BGPT is a remote MCP server — no local installation required. Configure it in your agent's MCP settings before use; this skill instructs the agent to call the `search_papers` MCP tool and does not enable MCP access by itself.

### Claude Desktop / Claude Code

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "bgpt": {
      "command": "npx",
      "args": ["mcp-remote", "https://bgpt.pro/mcp/sse"]
    }
  }
}
```

### npm (alternative)

```bash
npx bgpt-mcp
```

## Usage

Once the BGPT MCP server is configured, call its `search_papers` tool via the agent's MCP interface (not via Bash):

```
Search for papers about: "CRISPR gene editing efficiency in human cells"
```

The server returns structured results including:
- **Title, authors, journal, year, DOI**
- **Methods**: Experimental techniques, models, protocols
- **Results**: Key findings with quantitative data
- **Sample sizes**: Number of subjects/samples
- **Quality scores**: Study quality assessments
- **Conclusions**: Author conclusions and implications

## Pricing

- **Free tier**: 50 searches per network, no API key required
- **Paid**: $0.01 per result with an API key from [bgpt.pro/mcp](https://bgpt.pro/mcp)

