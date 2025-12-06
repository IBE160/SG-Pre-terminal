<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let categories: { id: number; name: string }[] = [];

	let amount: number | null = null;
	let type: 'income' | 'expense' = 'expense';
	let date = new Date().toISOString().split('T')[0];
	let description = '';
	let category_id: number | null = null;

	const dispatch = createEventDispatcher();

	function closeModal() {
		dispatch('close');
	}

	function handleSave() {
		if (!amount || !category_id) {
			// Basic validation
			alert('Amount and category are required.');
			return;
		}
		dispatch('save', {
			amount,
			type,
			date,
			description,
			category_id
		});
	}
</script>

<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
	<div class="bg-white p-6 rounded-lg shadow-xl w-full max-w-md">
		<h2 class="text-xl font-bold mb-4">Add Transaction</h2>
		<form on:submit|preventDefault={handleSave}>
			<div class="mb-4">
				<label for="amount" class="block text-sm font-medium text-gray-700">Amount</label>
				<input
					type="number"
					id="amount"
					bind:value={amount}
					class="mt-1 block w-full p-2 border rounded"
					required
				/>
			</div>
			<div class="mb-4">
				<label for="type" class="block text-sm font-medium text-gray-700">Type</label>
				<select id="type" bind:value={type} class="mt-1 block w-full p-2 border rounded">
					<option value="expense">Expense</option>
					<option value="income">Income</option>
				</select>
			</div>
			<div class="mb-4">
				<label for="date" class="block text-sm font-medium text-gray-700">Date</label>
				<input
					type="date"
					id="date"
					bind:value={date}
					class="mt-1 block w-full p-2 border rounded"
					required
				/>
			</div>
			<div class="mb-4">
				<label for="category" class="block text-sm font-medium text-gray-700">Category</label>
				<select id="category" bind:value={category_id} class="mt-1 block w-full p-2 border rounded" required>
					<option value={null} disabled>Select a category</option>
					{#each categories as category}
						<option value={category.id}>{category.name}</option>
					{/each}
				</select>
			</div>
			<div class="mb-4">
				<label for="description" class="block text-sm font-medium text-gray-700">Description</label>
				<input
					type="text"
					id="description"
					bind:value={description}
					class="mt-1 block w-full p-2 border rounded"
				/>
			</div>
			<div class="flex justify-end gap-4">
				<button type="button" on:click={closeModal} class="text-gray-600">Cancel</button>
				<button
					type="submit"
					class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
				>
					Save
				</button>
			</div>
		</form>
	</div>
</div>
