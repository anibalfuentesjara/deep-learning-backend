import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import {navigation} from "./constants";
import Header from './containers/header';
import Home from './containers/home';
import Classification from './containers/classification';

function App() {
  return (
  	<Router>
  		<Header />
	    <Routes>
	      <Route exact path={navigation.HOME} element={<Home />} />
	      <Route exact path={navigation.CLASSIFICATION} element={<Classification />} />
	      <Route path="/" element={<Home />} />
	    </Routes>
    </Router>
  );
}

export default App;
