import http from 'node:http';
import path from 'node:path';
import fs from 'node:fs';
const root=path.resolve(import.meta.dirname,'../dist');
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.woff2':'font/woff2','.ttf':'font/ttf','.jpg':'image/jpeg','.png':'image/png'};
http.createServer((req,res)=>{let name;try{name=decodeURIComponent(new URL(req.url,'http://localhost').pathname)}catch{res.writeHead(400).end();return}const file=path.resolve(root,'.'+(name==='/'?'/index.html':name));if(file!==root&&!file.startsWith(root+path.sep)){res.writeHead(403).end();return}fs.stat(file,(error,stat)=>{if(error||!stat.isFile()){res.writeHead(404).end('Not found');return}res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-cache'});fs.createReadStream(file).pipe(res)})}).listen(4318,'127.0.0.1',()=>console.log('Local: http://127.0.0.1:4318'));
