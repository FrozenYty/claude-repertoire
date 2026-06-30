# Mermaid Diagram Reference

Short reference for generating Mermaid diagrams. draw.io's Mermaid parser
covers 28 diagram types. Use Mermaid as the DEFAULT for most diagram types
(flowcharts, sequences, ER, Gantt, mindmaps, etc.) - it's simpler, more
reliable, and auto-laid-out.

## When to use Mermaid vs XML

| Diagram type | Use | Why |
|-------------|-----|-----|
| Flowchart / decision tree | **Mermaid** | Auto-layout, no coordinates |
| Sequence diagram | **Mermaid** | Built-in lifelines, activation |
| ER diagram | **Mermaid** | Cardinality syntax, clean |
| Gantt chart | **Mermaid** | Date-aware layout |
| Mindmap | **Mermaid** | Indentation = hierarchy |
| State machine | **Mermaid** | Compound states, junctions |
| Class diagram | **Mermaid** | Relations, visibility |
| Timeline | **Mermaid** | Simple section/event syntax |
| Pie / donut | **Mermaid** | One-liner |
| Git graph | **Mermaid** | Branch/merge visualization |
| Architecture (cloud) | **XML** | Needs cloud icons (AWS/Azure/GCP) |
| Network topology | **XML** | Needs network device icons |
| Swimlane (BPMN) | **XML** | Lane structure |
| Custom layout / exact positioning | **XML** | Full coordinate control |
| Venn / quadrant | **Mermaid** | `venn-beta`, `quadrantChart` |

## General Rules

- First non-comment line selects the type: `flowchart`, `sequenceDiagram`,
  `classDiagram`, `stateDiagram-v2`, `erDiagram`, `gantt`, `mindmap`,
  `timeline`, `pie`, `gitGraph`, `journey`, `quadrantChart`, `sankey-beta`,
  `xychart-beta`, `block-beta`, `c4Context`, `architecture-beta`,
  `radar-beta`, `venn-beta`, `treemap-beta`, `kanban`, `zenuml`
- One statement per line
- Quote labels with special characters using `"` not `'`
- HTML in labels: `<br>`, `<b>`, `<i>` are reliable
- Match the language of labels to the user's language

## Flowchart (most common)

```
flowchart TD
  A[Start] --> B{Decision?}
  B -->|Yes| C[Do thing]
  B -->|No| D[Skip]
  C --> E((End)); D --> E
```

- **Direction:** `TD`/`LR`/`BT`/`RL`
- **Node shapes:** `[rect]`, `(rounded)`, `{rhombus}`, `((circle))`, `[(cylinder)]`,
  `[[subroutine]]`, `[/parallelogram/]`
- **Edges:** `-->` arrow, `---` no arrow, `-.->` dotted, `==>` thick
- **Subgraphs:** `subgraph Name ... end`
- **Styling:** `style A fill:#dfd,stroke:#0a0` or `classDef happy fill:#dfd` + `A:::happy`

## Sequence Diagram

```
sequenceDiagram
  participant U as User
  participant S as Server
  U->>S: Request
  S-->>U: Response
  Note right of S: Logged
```

- **Arrows:** `->>` request, `-->>` response, `-x` error
- **Blocks:** `alt/else/end`, `opt/end`, `loop/end`, `par/and/end`

## ER Diagram

```
erDiagram
  CUSTOMER ||--o{ ORDER : places
  CUSTOMER {
    string name
    string email PK
  }
```

- **Cardinality:** `||` exactly-one, `|o` zero-or-one, `}o` zero-or-many, `}|` one-or-many

## State Diagram

```
stateDiagram-v2
  [*] --> Idle
  Idle --> Running : start
  state Running {
    [*] --> Working
    Working --> Waiting : block
  }
```

Always use `stateDiagram-v2`, not v1.

## Gantt Chart

```
gantt
  title Project timeline
  dateFormat YYYY-MM-DD
  section Phase 1
  Design : a1, 2025-01-01, 7d
  Build  : after a1, 14d
```

## Mindmap

```
mindmap
  root((Project))
    Frontend
      React
      CSS
    Backend
      Node ::icon(fa fa-server)
      DB
```

Indentation (2 spaces) defines hierarchy.

## Class Diagram

```
classDiagram
  class Animal {
    +String name
    +eat() void
  }
  Animal <|-- Dog : inherits
```

- **Relations:** `<|--` inherit, `*--` composition, `o--` aggregation, `-->` association, `..>` dependency
- **Visibility:** `+` public, `-` private, `#` protected

## Other Types (quick reference)

| Type | Keyword | Key syntax |
|------|---------|-----------|
| Pie | `pie` | `"Slice" : 60` |
| Timeline | `timeline` | `section Name` then `Year : Event` |
| Quadrant | `quadrantChart` | `x-axis Low --> High`, points `[0.3, 0.6]` |
| Git graph | `gitGraph` | `commit`, `branch name`, `merge name` |
| Sankey | `sankey-beta` | CSV: `source,target,value` |
| XY chart | `xychart-beta` | `bar [v1, v2]`, `line [v1, v2]` |
| C4 | `C4Context` | `Person(id, label)`, `System(id, label)` |
| Kanban | `kanban` | `todo[To Do]`, `task1[Label]@{ assigned: "A" }` |
| Radar | `radar-beta` | `axis a["A"]`, `curve c["C"]{80, 60}` |
| Venn | `venn-beta` | `set A ["A"]`, `union A,B` |

## When to Prefer XML

- Cloud architecture (AWS, Azure, GCP icons)
- Network topology (routers, switches, firewalls)
- Swimlane / BPMN with lane structure
- Diagrams needing exact multi-color control per element
- Mixed shape libraries in one diagram

Default to Mermaid for the standard types above; reach for XML only when
Mermaid's syntax clearly can't express what's needed.
