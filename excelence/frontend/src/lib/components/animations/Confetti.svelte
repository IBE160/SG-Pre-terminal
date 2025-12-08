<script lang="ts">
	let { duration = 3000 } = $props(); // How long the animation lasts
	
	let confettiPieces = $state([]);
	let isAnimating = $state(true);

	const colors = [
		'#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
		'#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B739', '#52B788'
	];

	function createConfettiPiece(id: number) {
		return {
			id,
			color: colors[Math.floor(Math.random() * colors.length)],
			left: Math.random() * 100,
			delay: Math.random() * 300,
			duration: 1500 + Math.random() * 1000,
			rotation: Math.random() * 360,
			size: 8 + Math.random() * 8 // 8-16px
		};
	}

	// Initialize confetti on mount
	$effect(() => {
		// Create 50 confetti pieces
		confettiPieces = Array.from({ length: 50 }, (_, i) => createConfettiPiece(i));

		// Stop animation after duration
		const timeout = setTimeout(() => {
			isAnimating = false;
		}, duration);

		return () => clearTimeout(timeout);
	});
</script>

{#if isAnimating}
	<div class="fixed inset-0 pointer-events-none z-[9999] overflow-hidden">
		{#each confettiPieces as piece (piece.id)}
			<div
				class="absolute animate-confetti"
				style="
					left: {piece.left}%;
					background-color: {piece.color};
					width: {piece.size}px;
					height: {piece.size}px;
					animation-delay: {piece.delay}ms;
					animation-duration: {piece.duration}ms;
					transform: rotate({piece.rotation}deg);
				"
			></div>
		{/each}
	</div>
{/if}

<style>
	@keyframes confetti {
		0% {
			top: -10%;
			opacity: 1;
			transform: translateY(0) rotateZ(0deg);
		}
		100% {
			top: 110%;
			opacity: 0;
			transform: translateY(1000px) rotateZ(720deg);
		}
	}

	.animate-confetti {
		animation: confetti ease-in forwards;
		border-radius: 2px;
	}
</style>
