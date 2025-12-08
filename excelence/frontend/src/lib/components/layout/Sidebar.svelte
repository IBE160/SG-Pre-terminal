<script lang="ts">
	import { page } from "$app/stores";
	import { partyModeStore } from "$lib/stores/partyMode";

	// Derived state for the current path
	let currentPath = $derived($page.url.pathname);

	// Sidebar visibility state (mobile)
	let isOpen = $state(false);

	const links = [
		{ href: "/dashboard", label: "Dashboard" },
		{ href: "/spreadsheet", label: "Spreadsheet" },
		{ href: "/settings", label: "Settings" },
	];

	function toggle() {
		isOpen = !isOpen;
	}

	function togglePartyMode() {
		console.log("Toggling party mode, current state:", $partyModeStore);
		partyModeStore.toggle();
		console.log("Party mode after toggle:", $partyModeStore);
	}

	// Close sidebar when navigating
	$effect(() => {
		// dependency on currentPath triggers this
		if (currentPath) {
			isOpen = false;
		}
	});
</script>

<!-- Hamburger Button (Mobile Only) -->
<button
	class="fixed top-2 left-2 z-50 rounded-lg bg-white p-2 text-slate-600 focus:ring-2 focus:ring-slate-200 focus:outline-none dark:bg-slate-800 dark:text-slate-400 dark:focus:ring-slate-700 md:hidden"
	onclick={toggle}
	aria-controls="sidebar"
	aria-expanded={isOpen}
>
	<span class="sr-only">Open sidebar</span>
	<svg
		class="h-6 w-6"
		fill="currentColor"
		viewBox="0 0 20 20"
		xmlns="http://www.w3.org/2000/svg"
	>
		<path
			clip-rule="evenodd"
			fill-rule="evenodd"
			d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 5A.75.75 0 012.75 9h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 9.75zm0 5A.75.75 0 012.75 14h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 14.75z"
		></path>
	</svg>
</button>

<aside
	id="sidebar"
	class="fixed top-0 left-0 z-40 h-screen w-64 border-r border-slate-200 bg-white transition-transform duration-300 md:translate-x-0 dark:border-slate-700 dark:bg-slate-800"
	class:translate-x-0={isOpen}
	class:-translate-x-full={!isOpen}
	aria-label="Sidebar"
>
	<div class="h-full overflow-y-auto px-3 py-4">
		<div class="mb-6 px-4">
			<span
				class="self-center text-xl font-black whitespace-nowrap text-slate-800 dark:text-white"
			>
				Excelence
			</span>
		</div>
		<ul class="space-y-2 font-medium">
			{#each links as link}
				{@const isActive =
					currentPath === link.href ||
					(link.href !== "/" && currentPath.startsWith(link.href))}
				<li>
					<a
						href={link.href}
						class="group flex items-center rounded-lg p-2 transition-colors duration-200"
						class:bg-blue-50={isActive}
						class:text-blue-600={isActive}
						class:text-slate-600={!isActive}
						class:hover:bg-blue-50={!isActive}
						class:hover:text-blue-600={!isActive}
						class:dark:text-slate-200={!isActive}
						class:dark:hover:bg-slate-700={!isActive}
					>
						<span class="ms-3">{link.label}</span>
					</a>
				</li>
			{/each}
		</ul>

		<!-- Party Mode Toggle -->
		<div class="mt-6 pt-6 border-t border-slate-200 dark:border-slate-700">
			<button
				onclick={togglePartyMode}
				class="w-full flex items-center justify-between rounded-lg p-3 transition-colors duration-200"
				class:bg-gradient-to-r={$partyModeStore}
				class:from-purple-500={$partyModeStore}
				class:to-pink-500={$partyModeStore}
				class:text-white={$partyModeStore}
				class:bg-slate-100={!$partyModeStore}
				class:text-slate-600={!$partyModeStore}
				class:hover:bg-slate-200={!$partyModeStore}
				class:dark:bg-slate-700={!$partyModeStore}
				class:dark:text-slate-200={!$partyModeStore}
				class:dark:hover:bg-slate-600={!$partyModeStore}
			>
				<span class="font-medium">🎉 Party Mode</span>
				<span class="text-sm">
					{$partyModeStore ? "ON" : "OFF"}
				</span>
			</button>
		</div>
	</div>
</aside>

<!-- Overlay for mobile -->
{#if isOpen}
	<div
		class="fixed inset-0 z-30 bg-slate-900/50 md:hidden"
		onclick={toggle}
		role="presentation"
	></div>
{/if}
