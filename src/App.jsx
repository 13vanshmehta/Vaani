import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Dashboard } from "./dashboards/dashboard";
import { Header } from "./components/header";
import { Home } from "./sections/home";
import { Signin } from "./registration/sign-in";
import { Signup } from "./registration/sign-up";
import { Footer } from "./components/footer";

// Default layout with header and footer
const DefaultLayout = ({ children }) => (
  <>
    <Header />
    {children}
    <Footer />
  </>
);

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Routes with header and footer */}
        <Route
          path="/"
          element={
            <DefaultLayout>
              <Home />
            </DefaultLayout>
          }
        />
        <Route
          path="/login"
          element={
            <DefaultLayout>
              <Signin />
            </DefaultLayout>
          }
        />
        <Route
          path="/signup"
          element={
            <DefaultLayout>
              <Signup />
            </DefaultLayout>
          }
        />
        
        {/* Dashboard route without header and footer */}
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;