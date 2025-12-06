<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';

	let { children } = $props();

	function logout() {
		authStore.logout();
		goto('/login');
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if $authStore.isAuthenticated}
	<div class="absolute top-4 right-4">
		<button
			onclick={logout}
			class="px-4 py-2 font-bold text-white bg-blue-500 rounded-md hover:bg-blue-600"
		>
			Logout
		</button>
	</div>
{/if}

{@render children()}
