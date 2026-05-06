# Pipeline state

This file is the source of truth for resumable progress across sessions. Each
iteration reads `state.json`, does the next batch, updates state, commits,
pushes. Future sessions can pick up from where the last left off.

## State machine

```
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
extract → curate → split → traces → struct → index → eval → judge → analyze
   ✓        →       →      3/30      3/30     0/30    0    0
```

Read `state.json` to see exact progress. Each problem ID flows through stages:

```
candidate → curated (judgeable=true) → assigned (split=trace|eval)
  → traced (trace.md exists)
  → structed (struct.md exists)        # for trace problems only
  → indexed (in retrieval index)
  → answered_no_rag, answered_rag      # for eval problems only
  → judged (score recorded)
```

## Conventions

- Each fresh batch of work writes a separate set of files, never edits-in-place.
- Every iteration ends with: `git add -A && git commit && git push`.
- `state.json` schema is versioned (`schema_version`); incompatible changes
  bump the version and migrate.
- Subagent invocations log to `logs/<iteration>/<batch>.log` (prompt + agent
  result summary only — never full transcripts, to avoid context bleed).
