import { writable } from 'svelte/store';
import { getCategories, getTransactions } from '$lib/services/api';

export const categories = writable([]);
export const transactions = writable([]);

export const loadCategories = async () => {
  try {
    const data = await getCategories();
    categories.set(data);
  } catch (error) {
    console.error('Failed to load categories:', error);
  }
};

export const loadTransactions = async () => {
  try {
    const data = await getTransactions();
    transactions.set(data);
  } catch (error) {
    console.error('Failed to load transactions:', error);
  }
};
