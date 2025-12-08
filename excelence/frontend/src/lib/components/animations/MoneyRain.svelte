<script lang="ts">
	let { duration = 3000 } = $props(); // How long the animation lasts
	
	let moneyEmojis = $state([]);
	let isAnimating = $state(true);

	const moneySymbols = ['💸', '💵', '💴', '💶', '💷', '💰', '🤑'];

	function createMoneyEmoji(id: number) {
		return {
			id,
			emoji: moneySymbols[Math.floor(Math.random() * moneySymbols.length)],
			left: Math.random() * 100, // Random horizontal position
			delay: Math.random() * 500, // Stagger the start
			duration: 2000 + Math.random() * 1000, // Random fall duration
			rotation: Math.random() * 360 // Random rotation
		};
	}

	// Initialize money emojis on mount
	$effect(() => {
		// Create 30 money emojis
		moneyEmojis = Array.from({ length: 30 }, (_, i) => createMoneyEmoji(i));

		// Stop animation after duration
		const timeout = setTimeout(() => {
			isAnimating = false;
		}, duration);

		return () => clearTimeout(timeout);
	});
</script>

{#if isAnimating}
	<div class="fixed inset-0 pointer-events-none z-[9999] overflow-hidden">
		{#each moneyEmojis as money (money.id)}
			<div
				class="absolute text-4xl animate-fall"
				style="
					left: {money.left}%;
					animation-delay: {money.delay}ms;
					animation-duration: {money.duration}ms;
					transform: rotate({money.rotation}deg);
				"
			>
				{money.emoji}
			</div>
		{/each}
	</div>
{/if}

<style>
	@keyframes fall {
		0% {
			top: -10%;
			opacity: 1;
		}
		100% {
			top: 110%;
			opacity: 0.7;
		}
	}

	.animate-fall {
		animation: fall linear forwards;
	}
</style>
