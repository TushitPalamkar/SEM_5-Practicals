const express=require('express')
const app=express()
app.use('/timepass',(req,res)=>{
    res.send('Hello,World!')
})
app.listen(3000,()=>{
    console.log('Running on 3000')
})