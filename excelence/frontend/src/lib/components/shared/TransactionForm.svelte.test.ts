import { describe, it, expect, vi } from 'vitest';
import { render, fireEvent } from '@testing-library/svelte';
import TransactionForm from './TransactionForm.svelte';

const mockCategories = [
	{ id: 1, name: 'Groceries' },
	{ id: 2, name: 'Salary' }
];

describe('TransactionForm', () => {
	// TODO: Improve these tests to properly check for event dispatching in Svelte 5
	it('renders without errors', () => {
		const { container } = render(TransactionForm, {
			props: { categories: mockCategories }
		});
		expect(container).toBeInTheDocument();
	});
});
