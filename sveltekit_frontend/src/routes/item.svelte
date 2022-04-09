<script lang="ts">
	import type { Item } from '$lib/apiTypes/items';
	export let item: Item;
</script>

<main>
	<h3>Item</h3>
	{#each Object.entries(item) as [key, value]}
		<p>{key}: {value}</p>
	{/each}
</main>
