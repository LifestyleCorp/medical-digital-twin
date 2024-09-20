import React from 'react';
import { render, screen } from '@testing-library/react';
import Header from '../Header';

test('renders header title', () => {
  render(<Header />);
  const titleElement = screen.getByText(/Human Digital Twin/i);
  expect(titleElement).toBeInTheDocument();
});
