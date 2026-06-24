# Stage 10.0 — Universal Context Schema (UCS)

## Vision

Graphify should define a universal format for AI understanding.

Any AI system should be able to:

* Receive context
* Understand context
* Continue work
* Transfer context

using a common schema.

---

# Universal Context Schema

```json
{
  "identity": {},
  "history": {},
  "decisions": {},
  "reconstruction": {},
  "continuation": {},
  "quality": {}
}
```

---

# 1. Identity Layer

Purpose:

Identify the project.

Example:

```json
{
  "project_name": "Graphify",
  "goal": "Git for AI Context",
  "current_stage": "stage-9.5-stable"
}
```

---

# 2. History Layer

Purpose:

Explain project evolution.

Example:

```json
{
  "context_commits": [],
  "timeline": []
}
```

---

# 3. Decision Layer

Purpose:

Preserve why decisions were made.

Example:

```json
{
  "decisions": []
}
```

---

# 4. Reconstruction Layer

Purpose:

Allow another AI to rebuild project understanding.

Example:

```json
{
  "session_reconstruction": {}
}
```

---

# 5. Continuation Layer

Purpose:

Tell another AI what to do next.

Example:

```json
{
  "current_state": "",
  "next_objective": "",
  "recommended_actions": []
}
```

---

# 6. Quality Layer

Purpose:

Measure transfer readiness.

Example:

```json
{
  "transfer_score": 100,
  "history_coverage": 100,
  "decision_coverage": 100,
  "continuation_coverage": 100
}
```

---

# Stage 10 Goal

Every Graphify engine should eventually export data using this schema.

The Universal Context Schema becomes the standard format for AI context transfer.
