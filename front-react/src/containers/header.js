import React from 'react';
import ReactDOM from 'react-dom';
import {
  Link
} from "react-router-dom";
import {navigation} from "../constants";

const Header = () => {
  return (
  <header>
    <ul>
      <Link to={navigation.HOME}> Home </Link>
      <Link to={navigation.CLASSIFICATION}> Classification </Link>
    </ul>
  </header>
  );
}

export default Header;