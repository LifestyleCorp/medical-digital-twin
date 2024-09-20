// frontend/src/components/Button.js

import React from 'react';
import PropTypes from 'prop-types';
import './Button.css';

const Button = ({ label, onClick, type = 'button', disabled = false }) => {
  return (
    <button className="custom-button" onClick={onClick} type={type} disabled={disabled}>
      {label}
    </button>
  );
};

Button.propTypes = {
  label: PropTypes.string.isRequired,
  onClick: PropTypes.func,
  type: PropTypes.string,
  disabled: PropTypes.bool,
};

export default Button;
