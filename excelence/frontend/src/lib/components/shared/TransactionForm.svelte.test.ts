import { describe, it, expect, vi } from 'vitest';
import { render, fireEvent } from '@testing-library/svelte';
import TransactionForm from './TransactionForm.svelte';

const mockCategories = [
	{ id: 'a4f2b4b0-7b6d-4b7b-8b0a-0e9f3b5a4b1e', name: 'Groceries' },
	{ id: 'c2c3e1e0-7b6d-4b7b-8b0a-0e9f3b5a4b1e', name: 'Salary' }
];

describe('TransactionForm', () => {
	it('dispatches a save event with form data on submit', async () => {
		const { getByLabelText, getByText, component } = render(TransactionForm, {
			props: { categories: mockCategories }
		});

		const saveHandler = vi.fn();
		component.$on('save', saveHandler);

		const amountInput = getByLabelText('Amount');
		const typeSelect = getByLabelText('Type');
		const dateInput = getByLabelText('Date');
		const categorySelect = getByLabelText('Category');
		const descriptionInput = getByLabelText('Description');
		const saveButton = getByText('Save');

		// Fill out the form
		await fireEvent.input(amountInput, { target: { value: '123.45' } });
		await fireEvent.change(typeSelect, { target: { value: 'expense' } });
		await fireEvent.input(dateInput, { target: { value: '2025-12-06' } });
		await fireEvent.change(categorySelect, { target: { value: mockCategories[0].id } });
		await fireEvent.input(descriptionInput, { target: { value: 'Test purchase' } });

		// Submit the form
		await fireEvent.click(saveButton);

		expect(saveHandler).toHaveBeenCalled();
		expect(saveHandler.mock.calls[0][0].detail).toEqual({
			amount: 123.45,
			type: 'expense',
			date: '2025-12-06',
			description: 'Test purchase',
			category_id: mockCategories[0].id
		});
	});

	it('dispatches a close event when cancel is clicked', async () => {
		const { getByText, component } = render(TransactionForm, {
			props: { categories: mockCategories }
		});

		const closeHandler = vi.fn();
		component.$on('close', closeHandler);

		const cancelButton = getByText('Cancel');
		await fireEvent.click(cancelButton);

		expect(closeHandler).toHaveBeenCalled();
	});
});
