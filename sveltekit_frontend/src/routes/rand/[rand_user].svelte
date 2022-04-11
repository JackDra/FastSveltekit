<script lang="ts">
	import type { Rand } from '$lib/apiTypes/rand';
	export let rand: Rand;
</script>

<main>
	<h3>Rand</h3>
	{#each Object.entries(rand) as [key, value]}
		<p>{key}: {value}</p>
	{/each}
</main>
