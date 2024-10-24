const http=require('http')
const server=http.createServer((req,res)=>{

    res.setHeader('Content-Type','text/plain')
    res.writeHead(200)
    res.end('Hello')
})
server.listen(3000,()=>{console.log('Listeningo on 3000')})
const fs=require('fs')
function asyncfunc(callback){
    fs.readFile('input.txt','utf-8',callback)
}
const timespent=Date.now()
setTimeout(()=>{
    console.log(`${Date.now()-timespent}ms is spent`)
},100)
asyncfunc(()=>{
    console.log("first statement")
    setTimeout(()=>{
        console.log("second")
    },1000)
    console.log("third statement")
})