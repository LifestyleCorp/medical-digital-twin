// frontend/src/components/UnityPlayer.js

import React from 'react';

const UnityPlayer = () => {
  return (
    <div>
      <iframe
        src="/unity_build/index.html"
        width="800"
        height="600"
        title="Unity Player"
      ></iframe>
    </div>
  );
};

export default UnityPlayer;
