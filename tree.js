function submitExpr() {
  const expr = document.getElementById("expr").value;

  fetch("/parse", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ expression: expr })
  })
  .then(res => res.json())
  .then(drawTree)
  .catch(err => alert("Invalid expression"));
}

function drawTree(data) {
  d3.select("svg").selectAll("*").remove(); // clear old tree

  const width = 800;
  const height = 600;
  const svg = d3.select("svg");

  const root = d3.hierarchy(data, d => {
    if (d.type === "number") return null;
    return [d.left, d.right];
  });

  const treeLayout = d3.tree().size([width - 100, height - 100]);
  treeLayout(root);

  svg.selectAll(".link")
    .data(root.links())
    .enter().append("line")
    .attr("class", "link")
    .attr("x1", d => d.source.x + 50)
    .attr("y1", d => d.source.y + 50)
    .attr("x2", d => d.target.x + 50)
    .attr("y2", d => d.target.y + 50);

  const node = svg.selectAll(".node")
    .data(root.descendants())
    .enter().append("g")
    .attr("class", "node")
    .attr("transform", d => `translate(${d.x + 50},${d.y + 50})`);

  node.append("circle").attr("r", 20);

  node.append("text")
    .attr("dy", 5)
    .attr("text-anchor", "middle")
    .text(d => d.data.type === "number" ? d.data.value : d.data.type);
}