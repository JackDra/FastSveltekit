<script lang="ts">
	import type { Item } from '$lib/apiTypes/item';
	export let item: Item;
</script>

<main>
	<h3>Item</h3>
	{#each Object.entries(item) as [key, value]}
		<p>{key}: {value}</p>
	{/each}
	<h1>I MADE A CHANGE TO THE APP</h1>
</main>
