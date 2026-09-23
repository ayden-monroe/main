# Weekly File-Control Audit

Run every Friday. Output is a short list of named exceptions with owners and due dates,
not a clean bill of health.

| Audit item | Standard | Owner |
| --- | --- | --- |
| Drive root | No loose files | Stephen Riner |
| Inbox aging | No unowned item older than 7 days | Sherry White |
| Duplicate review | Possible duplicates reviewed and resolved | Sherry White |
| Project dashboards | Every active project's `00` dashboard current | Project owners |
| Gmail filing | Material attachments and threads filed to Drive | Project owners |
| Calendar filing | Meeting records and deadlines filed | Project owners |
| FINAL folders | Only authoritative documents present | Project owners |
| Closed work | Completed matters moved to `90` | Project owners |
| Permissions | Restricted folders actually restricted in Drive | Stephen Riner |
| Ownership | No active file or project without a named owner | Stephen Riner |

## How to run it

For each item: check the actual state, record the result, and where the standard is not
met, write an exception with a corrective action, a named owner, and a due date. Exceptions
roll into the Control Center and stay `OPEN` until closed.

Check permissions by reading the actual Drive sharing settings, not the folder name. This
is the item most likely to be silently wrong, because nothing about the Drive interface
reminds anyone that a folder called "RESTRICTED" is shared with the whole organization.

## Reporting

Report in this shape:

```
Friday audit — <date>
Exceptions opened: N    Exceptions closed: N    Still open from prior weeks: N

<item> — <what was found> — <corrective action> — <owner> — <due>
```

Lead with what is wrong. A report that opens with nine passes buries the one finding that
needed attention, and the person reading it on a Friday afternoon will stop at the third
line.

## Recurring exceptions

When the same exception opens three weeks running, the problem is the system, not the
person. Say so, and propose the structural fix — a missing subfolder, an unclear
boundary between two master folders, a workroom nobody owns, an intake path that bypasses
the queue. That proposal is worth more than the tenth reminder.
