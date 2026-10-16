const katex = require('katex');
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data',chunk=>input+=chunk);
process.stdin.on('end',()=>{
 const equations=JSON.parse(input);
 const results=equations.map(({tex,display})=>{
  try{return {html:katex.renderToString(tex,{displayMode:display,throwOnError:true,trust:false,strict:'ignore',output:'htmlAndMathml',maxExpand:1000})};}
  catch(e){return {error:String(e.message),tex};}
 });
 process.stdout.write(JSON.stringify(results));
});
