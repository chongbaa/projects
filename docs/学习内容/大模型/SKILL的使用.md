根据OpenCode文档，skills应放在以下位置：
项目级（当前项目专用）：
- .opencode/skills/<name>/SKILL.md
- .claude/skills/<name>/SKILL.md
全局级（所有项目可用）：
- ~/.config/opencode/skills/<name>/SKILL.md
- ~/.claude/skills/<name>/SKILL.md
每个skill需要创建一个文件夹（名称即skill名称），里面放置SKILL.md文件，文件开头需包含YAML格式的frontmatter（name和description字段必需）。