# [Bug] Saving tasks for one category deletes tasks from other categories

**Branch to evaluate on:** `issue-3-hard`

## Description
We store tasks for multiple categories (e.g. "work" and "personal") in the
same JSON file, keyed by category. Users are reporting that saving their
"personal" tasks makes their previously-saved "work" tasks disappear
entirely — like the file gets wiped instead of updated.

This is a data-loss bug and needs to be understood carefully — it's not
obviously a single wrong line, it's about *how* the save function reads
existing data before writing.

## Steps to reproduce
```python
save_tasks(path, work_mgr.tasks, category="work")
save_tasks(path, personal_mgr.tasks, category="personal")
print(load_category(path, category="work"))  # I expect the work tasks back
```

## Expected behavior
Saving one category's tasks must not affect any other category already
stored in the same file. All previously saved categories should still be
readable afterward.

## Actual behavior
Only the most recently saved category survives in the file — everything
else is gone.

## Acceptance criteria
All tests in `tests/test_storage.py` pass, especially
`test_save_does_not_clobber_other_categories`.
