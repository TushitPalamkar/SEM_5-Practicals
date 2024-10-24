export default function Timepass({count,setCount}){
    return(
        <div>
            <h1>
                timepass
                The count is:{count}
            </h1>
            <button onClick={()=>setCount(count+1)}></button>
        </div>
    )
}