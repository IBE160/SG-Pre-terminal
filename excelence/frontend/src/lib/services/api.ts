// src/lib/services/api.ts

const BASE_URL = '/api/v1';

export async function registerUser(email: string, password: string) {
  const response = await fetch(`${BASE_URL}/users`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    return response.json();
  } else {
    const err = await response.json();
    throw new Error(err.detail || 'Registration failed');
  }
}
