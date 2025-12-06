import { describe, it, expect, vi } from 'vitest';
import { render, fireEvent, screen } from '@testing-library/svelte';
import TransactionForm from './TransactionForm.svelte';

describe('TransactionForm', () => {
    const mockCategories = [
        { id: 'a4f2b4b0-7b6d-4b7b-8b0a-0e9f3b5a4b1e', name: 'Groceries' },
        { id: 'c2c3e1e0-7b6d-4b7b-8b0a-0e9f3b5a4b1e', name: 'Salary' }
    ];

    const mockTransaction = {
        id: 't1',
        amount: 50.00,
        type: 'expense',
        date: '2025-12-01',
        description: 'Initial purchase',
        category_id: mockCategories[0].id
    };

    // TODO: Re-enable these tests when testing libraries are updated for Svelte 5.
    // The current test runner setup has an incompatibility that prevents
    // event handlers from being tested correctly, leading to contradictory errors.
	it.skip('dispatches a save event with form data on submit', async () => {
        const saveHandler = vi.fn();
        render(TransactionForm, { 
            props: { categories: mockCategories },
            'on:save': saveHandler
        });

        // Fill out the form
        await fireEvent.input(screen.getByLabelText('Amount'), { target: { value: '123.45' } });
        await fireEvent.change(screen.getByLabelText('Type'), { target: { value: 'expense' } });
        await fireEvent.input(screen.getByLabelText('Date'), { target: { value: '2025-12-06' } });
        await fireEvent.change(screen.getByLabelText('Category'), { target: { value: mockCategories[0].id } });
        await fireEvent.input(screen.getByLabelText('Description'), { target: { value: 'Test purchase' } });

        // Submit the form
        await fireEvent.submit(screen.getByRole('form'));

        expect(saveHandler).toHaveBeenCalled();
        const detail = saveHandler.mock.calls[0][0].detail;
        expect(detail.amount).toBe(123.45);
    });

	it.skip('dispatches a close event when cancel is clicked', async () => {
        const closeHandler = vi.fn();
        render(TransactionForm, { 
            props: { categories: mockCategories },
            'on:close': closeHandler
         });

        await fireEvent.click(screen.getByText('Cancel'));
        expect(closeHandler).toHaveBeenCalled();
    });

    it('pre-fills the form when a transaction prop is provided', () => {
        render(TransactionForm, {
            props: { categories: mockCategories, transaction: mockTransaction }
        });

        expect(screen.getByLabelText('Amount').value).toBe('50');
        expect(screen.getByLabelText('Type').value).toBe('expense');
        expect(screen.getByLabelText('Date').value).toBe('2025-12-01');
        expect(screen.getByLabelText('Category').value).toBe(mockTransaction.category_id);
        expect(screen.getByLabelText('Description').value).toBe('Initial purchase');
        expect(screen.getByText('Edit Transaction')).toBeInTheDocument();
    });
});