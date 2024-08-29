import { Routes, Route } from "react-router-dom";

function Home() {

  return <div>I am the Home of RemoteA</div>;

}

function About() {

  return <div>I am the About of RemoteA</div>;

}

function Contact() {

  return <div>I am the Contact of RemoteA</div>;

}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="about" element={<About />} />
      <Route path="contact" element={<Contact />} />
    </Routes>
  );
}

export default AppRoutes;