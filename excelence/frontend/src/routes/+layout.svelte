<script lang="ts">
	import "./layout.css";
	import favicon from "$lib/assets/favicon.svg";
	import { authStore } from "$lib/stores/auth";
	import { themeStore } from "$lib/stores/theme";
	import { animationTrigger } from "$lib/stores/partyMode";
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import { browser } from "$app/environment";
	import Sidebar from "$lib/components/layout/Sidebar.svelte";
	import MoneyRain from "$lib/components/animations/MoneyRain.svelte";
	import Confetti from "$lib/components/animations/Confetti.svelte";

	let { children } = $props();

	function logout() {
		authStore.logout();
		goto("/login");
	}

	$effect(() => {
		if (browser && !$authStore.isAuthenticated) {
			const publicRoutes = ["/login", "/register"];
			if (!publicRoutes.includes($page.url.pathname)) {
				goto("/login");
			}
		}
	});

	// Initialize theme on mount
	$effect(() => {
		if (browser) {
			themeStore.init();
		}
	});

	// Debug animation trigger
	$effect(() => {
		console.log('Animation trigger changed:', $animationTrigger);
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if $authStore.isAuthenticated}
	<Sidebar />
	<main
		class="min-h-screen bg-slate-50 p-4 transition-all duration-300 dark:bg-slate-900 md:ml-64"
	>
		<div class="mb-4 flex justify-end">
			<button
				onclick={logout}
				class="rounded-md bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-600"
			>
				Logout
			</button>
		</div>
		{@render children()}
	</main>
	
	<!-- Party Mode Animations -->
	{#if $animationTrigger === 'money'}
		<MoneyRain />
	{/if}
	{#if $animationTrigger === 'confetti'}
		<Confetti />
	{/if}
{:else}
	<main class="min-h-screen bg-slate-50 dark:bg-slate-900">
		{@render children()}
	</main>
{/if}
