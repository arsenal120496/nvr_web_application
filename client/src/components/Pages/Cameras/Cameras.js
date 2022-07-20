import './cameras.css'
import React, { useState } from 'react'
import CameraAltIcon from '@material-ui/icons/CameraAlt';


export default function Cameras(props) {
    const [cameras, setCameras] = useState(false)

    function toggleCameras(){
        setCameras(prevCameras => !prevCameras)
    }

  return (
    <div>
		<ul className='sidebarList'>
			<li className='sidebarListItem active'>
				<CameraAltIcon className='sidebarIcon' onClick={toggleCameras}/>Cameras
				{props.request && <h3>{props.request}</h3>}
				{cameras && <p>{props.status}</p>}
				<hr/>
			</li>
        </ul>
    </div>
  )
}

