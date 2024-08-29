import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
        <h1>I am the HOST Home</h1>
        <ul>
            <li><Link to="/remotes/remoteA/">Remote A Home</Link></li>
            <li><Link to="/remotes/remoteA/about">Remote A About</Link></li>
            <li><Link to="/remotes/remoteB/">Remote B Home</Link></li>
            <li><Link to="/remotes/remoteB/about">Remote B About</Link></li>
        </ul>
    </div>
  )
}

export default Home