import { getSportsmen } from '../services/getData';
import { useState, useEffect, useContext, useRef } from 'react';
import { userContext } from '../context/userContext';

const Sportsmen = () => {
  const [list,setList] = useState({});
  const { user, dispatchUser } = useContext(userContext);
  const cntRenders = useRef(0);
  cntRenders.current++;
  console.log(`Sportsmen page render number ${cntRenders.current}`)
  
  useEffect(() => {

    (async function fillSportsmanList() {

        const data = await getSportsmen(dispatchUser);
        
        setList(data);

    })()

  },[])

  return (
    <div className="container">
        <h1 className="text-indigo-600 font-light text-3xl">Our Olympic Sportsmen</h1>
        <h2 className="text-indigo-600 font-light text-2xl">{user.name}, you're one of them, right?</h2>
        <h3>They're just great people, but some of them also got Olympic medals ...</h3>

        <ul>
            {
                list.length > 0 ? list.map((sportsman,i) => <li key={i}>{sportsman.name}</li>)
                                : <p className="text-indigo-600 font-light text-2xl">Loading ...</p>
            }
        </ul>
    </div>
  )
}

export default Sportsmen