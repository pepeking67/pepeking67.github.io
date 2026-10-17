const katex = require('katex');
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data',chunk=>input+=chunk);
process.stdin.on('end',()=>{
 const equations=JSON.parse(input);
 const results=equations.map(({tex,display})=>{
  try{let html=katex.renderToString(tex,{displayMode:display,throwOnError:true,trust:false,strict:'ignore',output:'htmlAndMathml',maxExpand:1000});if(/^\\text\{/.test(tex))html=html.replace('class="katex"','class="katex text-math"');return {html};}
  catch(e){return {error:String(e.message),tex};}
 });
 process.stdout.write(JSON.stringify(results));
});
