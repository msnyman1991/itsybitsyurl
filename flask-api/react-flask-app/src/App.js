import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [placeholder, setPlaceholder] = useState('Hi');

  useEffect(() => {
    fetch('/short_url').then(res => res.json()).then(data => {
      setPlaceholder(data.result);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        <p>Short URL : {placeholder}</p>
      </header>
    </div>
  );
}

export default App;
