import './App.css';
import {Routes,Route, Navigate} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.css';
import { useEffect, useState } from 'react';
import Main from './components/Main'
function App() {
  return (
    <div className="App">
      <Main/>
    </div>
  );
}

export default App;


