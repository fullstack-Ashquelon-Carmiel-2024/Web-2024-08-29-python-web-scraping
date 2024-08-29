import React from 'react';
import { Routes, Route } from "react-router-dom";
const RemoteA = React.lazy(() => import("remoteA/App"));
const RemoteB = React.lazy(() => import("remoteB/App"));

function RemoteRoutes() {
  return (
    <Routes>
      <Route path="remoteA/*" element={<RemoteA />} />
      <Route path="remoteB/*" element={<RemoteB />} />
    </Routes>
  );
}

export default RemoteRoutes;