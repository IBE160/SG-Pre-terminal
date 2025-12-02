import { render, fireEvent, screen } from '@testing-library/svelte';
import Register from './+page.svelte';
import { describe, it, expect } from 'vitest';

describe('Register Component', () => {
  it('renders the registration form', () => {
    render(Register);
    expect(screen.getByLabelText('Email')).toBeInTheDocument();
    expect(screen.getByLabelText('Password')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Register' })).toBeInTheDocument();
  });

  it('shows an error message for short passwords', async () => {
    render(Register);
    const passwordInput = screen.getByLabelText('Password');
    await fireEvent.input(passwordInput, { target: { value: 'short' } });
    
    const registerButton = screen.getByRole('button', { name: 'Register' });
    await fireEvent.click(registerButton);

    expect(await screen.findByText('Password must be at least 8 characters long.')).toBeInTheDocument();
  });
});
