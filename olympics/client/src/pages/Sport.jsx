import {Button as ShadcnButton} from '../components/ui/button';
import { useState, useEffect, useContext, useRef } from 'react';
import { userContext } from '../context/userContext';

const Sport = () => {
  
  const { user, dispatchUser, sportBtn } = useContext(userContext);
  const cntRenders = useRef(0);
  cntRenders.current++;
  console.log(`Sport page render number ${cntRenders.current}`)
  
  return (
    <div className="container">
        <h1 className="text-indigo-600 font-light text-3xl">Sport</h1>
        <h2 className="text-indigo-600 font-light text-2xl">{user.name}, welcome!</h2>
        <h3>Which sport do you like most?</h3>

        <ShadcnButton variant={sportBtn}
               onClick={(e)=>{
                  console.log('Before showing the reducer')
                  dispatchUser({type: 'JUST_SHOW'})
                  console.log('After showing the reducer')
               }} >
          Show Reducer</ShadcnButton>

        <ul>
            <li>Judo</li>
            <li>Surfing</li>
        </ul>
    </div>
  )
}

export default Sport