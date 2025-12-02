// src/lib/stores/auth.ts
import { writable } from 'svelte/store';
import { browser } from '$app/environment';

export const jwt_token = writable(browser && localStorage.getItem('jwt_token'));
export const isAuthenticated = writable(browser && !!localStorage.getItem('jwt_token'));

jwt_token.subscribe((token) => {
  if (browser) {
    if (token) {
      localStorage.setItem('jwt_token', token);
      isAuthenticated.set(true);
    } else {
      localStorage.removeItem('jwt_token');
      isAuthenticated.set(false);
    }
  }
});
