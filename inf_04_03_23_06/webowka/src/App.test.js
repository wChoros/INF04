import { render, screen } from '@testing-library/react';
import Form from './components/Form/Form';

test('renders learn react link', () => {
  render(<Form />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
