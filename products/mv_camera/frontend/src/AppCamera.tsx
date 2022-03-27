import React from 'react';
import Camera, {FACING_MODES} from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';

import {notify} from "./Notifications";

function AppCamera() {
  function handleTakePhoto(dataUri: string) {
    // more about data URI format: https://en.wikipedia.org/wiki/Data_URI_scheme
    console.log('takePhoto');
    fetch('/api/camera/photo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        dataUri: dataUri
      })
    }).then((r: Response) => {
      return r.json()
    }).then(d => {
      notify(d)
    })
  }

  return (
    <Camera
      idealFacingMode={FACING_MODES.ENVIRONMENT}
      onTakePhoto={(dataUri: string) => {
        handleTakePhoto(dataUri);
      }}
    />
  );
}

export default AppCamera;
