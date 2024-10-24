const fs=require('fs')
// const filedata=fs.readFileSync('input.txt','utf-8')
// console.log(filedata)

fs.readFile('input.txt',(err,data)=>{
    if(err){
        console.log(err)
    }
   
    console.log('This is from async file:'+data.toString())
})
console.log('hello')
const readstream=fs.createReadStream('input.txt','utf-8')
readstream.on('data',(data)=>{
    console.log(data)
    console.log('end of file')
})