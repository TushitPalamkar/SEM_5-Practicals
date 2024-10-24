import { useState, useRef, useEffect } from 'react';
import './App.css';
import Timepass from './timepass';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<AboutUs />} />
      </Routes>
    </Router>
  );
}

function Home() {
  const [count, setCount] = useState(0);
 
  const inputRef = useRef(null);

  const list = [
    {
      id: 1,
      title: 'abcd'
    },
    {
      id: 2,
      title: 'efgh'
    }
  ];

function accessref(){
  if(inputRef.current){
    inputRef.current.focus()
  }
}

  return (
    <>
      <div>
        Homepage
        <Timepass count={count} setCount={setCount} />
        <h3>The list is</h3>
        {list.map((item, index) => (
          <li key={item.id}>
            {item.title} with the key {item.id} and index: {index}
          </li>
        ))}
        {/* <input ref={inputRef} value={inputRef.current} /> Attach ref here */}
      <input ref={inputRef} placeholder='Focus here' />
      <button onClick={accessref}></button>
      </div>
    </>
  );
}

function AboutUs() {
  return (
    <>
      <div>
        About Us
      </div>
    </>
  );
}

export default App;
