import { render, screen, waitFor } from '@testing-library/svelte';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import TransactionList from './TransactionList.svelte';

// Mock the API service
vi.mock('$lib/services/api', () => ({
  getTransactions: vi.fn(),
  getCategories: vi.fn(() => Promise.resolve({ data: [] })),
}));

import { getTransactions } from '$lib/services/api';

const mockTransactions = [
  {
    id: '1',
    date: '2025-12-05',
    description: 'Coffee',
    amount: 5.00,
    type: 'expense',
    category_id: 'cat1',
  },
  {
    id: '2',
    date: '2025-12-04',
    description: 'Salary',
    amount: 2000.00,
    type: 'income',
    category_id: 'cat2',
  },
];


describe('TransactionList Component', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders a list of transactions on successful fetch', async () => {
    getTransactions.mockResolvedValue({ data: mockTransactions });
    render(TransactionList);

    await waitFor(() => {
      expect(screen.getByText('Coffee')).toBeInTheDocument();
      expect(screen.getByText('Salary')).toBeInTheDocument();
      expect(screen.getByText('-$5.00')).toBeInTheDocument();
      expect(screen.getByText('+$2000.00')).toBeInTheDocument();
    });
  });

  it('renders the empty state message when no transactions are returned', async () => {
    getTransactions.mockResolvedValue({ data: [] });
    render(TransactionList);

    await waitFor(() => {
      expect(screen.getByText('No transactions found. Add one to get started!')).toBeInTheDocument();
    });
  });

  it('renders an error message when the fetch fails', async () => {
    getTransactions.mockRejectedValue(new Error('Failed to fetch'));
    render(TransactionList);

    await waitFor(() => {
      expect(screen.getByText('Error: Failed to fetch')).toBeInTheDocument();
    });
  });

});
