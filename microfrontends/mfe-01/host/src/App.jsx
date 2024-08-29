import './App.css';
import { Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import About from './pages/About';
import Home from './pages/Home';
import RemoteRoutes from './routes/RemoteRoutes';

function App() {
  

  return (
    <>
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>

        <Route path="/" >

          <Route index element={ <Home /> } />
          <Route path="about" element={ <About /> } />

        </Route>

        <Route path="/remotes/*" element={<RemoteRoutes />} />
        

      </Routes>
    </Suspense>
    </>
  )
}

export default App