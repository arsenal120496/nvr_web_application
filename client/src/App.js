import React from 'react'
import { useState } from 'react'
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Cameras from './components/Pages/Cameras/Cameras';
import Debug from './components/Pages/Debug/Debug';
import Home from './components/Pages/Home/Home';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import logo from './logo.svg';
import { Link } from 'react-router-dom';
import { Topbar } from './components/Topbar/Topbar';
import CamerasData from './components/SidebarData/CamerasData';
import DebugData from './components/SidebarData/DebugData';
import LoginForm from './components/Pages/Login/LoginForm';

function App() {
  const adminUser = {
    email: "admin@gmail.com",
    passworld: "admin123"
  };

  const [user, setUser] = useState({name:"", email:""});
  const [error, setError] = useState("");

  const Login = details => {
    console.log(details);

    if (details.email == adminUser.email && details.passworld == adminUser.passworld) {
      console.log("Logged in");
      setUser({
        name: details.name,
        email: details.passworld
      })
    } else{
      console.log("Details do not match!")
      setError("Details do not match!")
    }
  };

  const Logout = () => {
    setUser({name:"", email:""});
  };




  const cameraElements = CamerasData.map(data1 =>{
    return(
      <Cameras
        id={data1.id}
        request={data1.request}
        status={data1.status}
      />
    )
  });

  const debugElements = DebugData.map(data2 =>{
    return(
      <Debug
        id={data2.id}
        request={data2.request}
        status={data2.status}
      />
    )
  });

  

  

  return (
    <div className="App">
      {(user.email != "") ? (<div className='welcome'>
        <h2>Welcome, <span>{user.name}</span></h2>
        <button onClick={Logout}>Logout</button>
      </div>): (
        <LoginForm Login={Login} error={error}/>
      )}

      <div className='sidebarWrapper'>
          <div className='sidebarMenu'>
            <div className='topbar'>
              <div className='topbarWrapper'>
                <div className='topLeft'>
                    <img src={logo} height={50} alt='logo' />
                </div>

                <div className='topRight'>
                  <div className='topbarIconContainer'>
                    <MoreVertIcon />
                </div>
                
                </div>
            </div>
        </div>
                
                <ul className='sidebarList'>
                    <li className='sidebarListItem active'>
                        <nav className='sidebarIcon'/><Cameras />
                    </li>

                    <li className='sidebarListItem'>
                        <nav className='sidebarIcon'/><Debug />
                    </li>
                </ul>
                
          </div>
        </div>

        

    </div>
  );
}

export default App;
