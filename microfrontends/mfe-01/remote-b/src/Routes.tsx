import { Routes, Route } from "react-router-dom";

function Home() {

  return <div>I am the Home of RemoteB</div>;

}

function About() {

  return <div>I am the About of RemoteB</div>;

}

function Contact() {

  return <div>I am the Contact of RemoteB</div>;

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