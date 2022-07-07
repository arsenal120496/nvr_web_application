import './debug.css'
import React, { useState } from 'react'
import BugReportIcon from '@material-ui/icons/BugReport';

export default function Debug(props) {
    const [debug, setDebug] = useState(false)

    function toggleDebug(){
        setDebug(prevDebug => !prevDebug)
    }

  return (
    <div>
		<ul className='sidebarList'>
			<li className='sidebarListItem active'>
				<BugReportIcon className='sidebarIcon' onClick={toggleDebug}/>Debug
				{props.request && <h3>{props.request}</h3>}
				{debug && <p>{props.status}</p>}
				<hr/>
			</li>
    </ul>
    </div>
  )
}

