import React from 'react';
import AppCamera from "./AppCamera";
import {Notifications} from "./Notifications";

function App() {
  return (
    <React.Fragment>
      <Notifications />
      <AppCamera />
    </React.Fragment>
  );
}

export default App;
