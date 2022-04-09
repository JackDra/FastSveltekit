<script lang="ts">
	export let item;
</script>

<main>
	<h3>Item</h3>
	{#each Object.entries(item) as [key, value]}
		<p>{key}: {value}</p>
	{/each}
</main>
