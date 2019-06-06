var data = {
    "name": "Horus Rising",
    "children": [
        {
            "name": "False Gods",
            "children": [
                {
                    "name": "Galaxy In Flames",
                    "children": [
                        {
                            "name": "Flight of the Eisenstein",
                            "children": [
                                {
                                    "name": "The Last Church",
                                    "value": 1
                                },
                                {
                                    "name": "Fulgrim",
                                    "value": 2
                                }
                            ]
                        },
                        {
                            "name": "After Desh'ea",
                            "value": 3
                        },
                        {
                            "name": "Mechanicum",
                            "value": 4
                        }
                    ]
                }
            ]
        }

    ]

}


var treeLayout = d3.tree()
  .size([400, 200])

var root = d3.hierarchy(data)

treeLayout(root)

// Nodes
var nodes = d3.select('svg g.nodes')
  .selectAll('.node')
  .data(root.descendants())
  .enter();

nodes.append('circle')
    .classed('node', true)
  .attr('cx', function(d) {return d.x;})
  .attr('cy', function(d) {return d.y;})
  .attr('r', 4);

// Text
nodes.append("text")
      .attr("dy", ".35em")
  .attr("x", function(d) { return d.x; })
  .attr("y", function(d) { return d.y; })
//      .attr("y", function(d) { return d.children ? -20 : 20; })
      .style("text-anchor", "middle")
      .text(function(d) { return d.data.name; });

//var text = d3.select('svg g.nodes')
//  .selectAll('text.node')
//  .data(root.descendants())
//  .enter()
//  .append('text');
//
//var textAttrs = text.attr("dy", ".35em")
//  .attr("text-anchor", "middle")
//  .attr("x", function(d) { return d.x; })
//  .attr("y", function(d) { return d.y; })
////  .attr("y", function(d) {
////          return d.data.children || d.data._children ? -18 : 18; })
//  .text(function(d) { return d.data.name; });

// Links
d3.select('svg g.links')
  .selectAll('line.link')
  .data(root.links())
  .enter()
  .append('line')
  .classed('link', true)
  .attr('x1', function(d) {return d.source.x;})
  .attr('y1', function(d) {return d.source.y;})
  .attr('x2', function(d) {return d.target.x;})
  .attr('y2', function(d) {return d.target.y;});

//
//var margin = {top: 40, right: 120, bottom: 20, left: 120},
//    width = 960 - margin.right - margin.left,
//    height = 500 - margin.top - margin.bottom;
//
//var i = 0;
//
//var tree = d3.layout.tree()
//    .size([height, width]);
//
//var diagonal = d3.svg.diagonal()
//    .projection(function(d) { return [d.x, d.y]; });
//
//var svg = d3.select("body").append("svg")
//    .attr("width", width + margin.right + margin.left)
//    .attr("height", height + margin.top + margin.bottom)
//  .append("g")
//    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
//
//root = treeData[0];
//
//update(root);
//
//function update(source) {
//
//  // Compute the new tree layout.
//  var nodes = tree.nodes(root).reverse(),
//      links = tree.links(nodes);
//
//  // Normalize for fixed-depth.
//  nodes.forEach(function(d) { d.y = d.depth * 100; });
//
//  // Declare the nodes…
//  var node = svg.selectAll("g.node")
//      .data(nodes, function(d) { return d.id || (d.id = ++i); });
//
//  // Enter the nodes.
//  var nodeEnter = node.enter().append("g")
//      .attr("class", "node")
//      .attr("transform", function(d) {
//          return "translate(" + d.x + "," + d.y + ")"; });
//
//  nodeEnter.append("circle")
//      .attr("r", 10)
//      .style("fill", "#fff");
//
//  nodeEnter.append("text")
//      .attr("y", function(d) {
//          return d.children || d._children ? -18 : 18; })
//      .attr("dy", ".35em")
//      .attr("text-anchor", "middle")
//      .text(function(d) { return d.name; })
//      .style("fill-opacity", 1);
//
//  // Declare the links…
//  var link = svg.selectAll("path.link")
//      .data(links, function(d) { return d.target.id; });
//
//  // Enter the links.
//  link.enter().insert("path", "g")
//      .attr("class", "link")
//      .attr("d", diagonal);
//
//}
