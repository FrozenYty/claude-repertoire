# Drawsmith Quickstart

Read this FIRST for any draw.io diagram. Covers 80% of requests.

## IEEE Color Palette

| Color Key | Fill | Stroke | Use for |
|-----------|------|--------|---------|
| `attention` | `#E1D5E7` | `#9673A6` | MHA, proposed method |
| `convolution` | `#DAE8FC` | `#6C8EBF` | CNN, main processing |
| `pooling` | `#D5E8D4` | `#82B366` | Max/Avg pool |
| `norm` | `#F5F5F5` | `#999999` | LayerNorm, Add & Norm |
| `fc` | `#FFE6CC` | `#D79B00` | Linear, Dense, projection |
| `input` | `#F8CECC` | `#B85450` | Token embeddings, data sources |
| `output` | `#FFF2CC` | `#D6B656` | Softmax, final output |
| `operator` | `#FFFFFF` | `#666666` | Element-wise ops, concat |

## Grid Formula

```
x = col * 180 + 40   (col 0=40, 1=220, 2=400...)
y = row * 120 + 60   (row 0=60, 1=180, 2=300...)
Standard node: 140x60. Decision diamond: 140x80. Ellipse: 60x60.
```

## Non-Negotiable Rules

1. `verticalAlign=middle` on EVERY content node.
2. Coords MUST be multiples of 10.
3. Node gap >= 30px (shorter arrows are invisible).
4. `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;` base style.
5. `fontFamily=Times New Roman` everywhere.
6. Legend required when >2 colors used.

## Edge Routing

- Default: source/target + exitX/exitY ONLY. No waypoints.
- Self-loop: exit RIGHT (exitX=1), curve up and back (3 waypoints).
- Bidirectional: different exitY per direction (0.25/0.75 or 0.35/0.65).
- Cross-panel: 2 waypoints through mid-column corridor.
- Multi-connection: distribute exitY evenly (N=3: 0.2, 0.5, 0.8).

## Top 3 Golden XML Templates

For most requests, find and copy from:
- **Section 1**: Vertical stack - protocols, layers, pipelines
- **Section 2**: Horizontal pipeline - CI/CD, multi-stage
- **Section 6**: Flowchart - decisions, process flows

Read `references/drawio-layouts.md` for the full 21-template library.

## Common XML Pattern

```xml
<mxCell id="node" value="Label"
  style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;fontFamily=Times New Roman;fontSize=12;fontColor=#333333;align=center;verticalAlign=middle"
  vertex="1" parent="1">
  <mxGeometry x="40" y="60" width="140" height="60" as="geometry"/>
</mxCell>
<mxCell id="e1"
  style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#333333;strokeWidth=1.5"
  edge="1" parent="1" source="node" target="next">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

After generating, run: `python scripts/drawio-check.py <file.drawio>`
