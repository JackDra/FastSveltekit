<script>
	import { onMount } from 'svelte';
	import * as d3 from 'd3';

	let Plotly;
	let x_data = [];
	let y_data = [];
	let z_data = [];
	let plotAwait;

	async function gen3DScatter() {
		Plotly = (await import('plotly.js-dist')).default;
		await d3.csv(
			'https://raw.githubusercontent.com/plotly/datasets/master/alpha_shape.csv',
			function (rows) {
				x_data.push(rows['x']);
				y_data.push(rows['y']);
				z_data.push(rows['z']);
			}
		);

		let data = [
			{
				x: x_data,
				y: y_data,
				z: z_data,
				mode: 'markers',
				type: 'scatter3d',
				marker: {
					color: 'rgb(23, 190, 207)',
					size: 2
				}
			},
			{
				alphahull: 7,
				opacity: 0.1,
				type: 'mesh3d',
				x: x_data,
				y: y_data,
				z: z_data
			}
		];
		let layout = {
			autosize: true,
			height: 480,
			scene: {
				aspectratio: {
					x: 1,
					y: 1,
					z: 1
				},
				camera: {
					center: {
						x: 0,
						y: 0,
						z: 0
					},
					eye: {
						x: 1.25,
						y: 1.25,
						z: 1.25
					},
					up: {
						x: 0,
						y: 0,
						z: 1
					}
				},
				xaxis: {
					type: 'linear',
					zeroline: false
				},
				yaxis: {
					type: 'linear',
					zeroline: false
				},
				zaxis: {
					type: 'linear',
					zeroline: false
				}
			},
			title: '3d point clustering',
			width: 477
		};
		await Plotly.newPlot('plotDiv', data, layout);
	}

	onMount(async () => {
		plotAwait = gen3DScatter();
		await plotAwait;
	});

	function clickGraph() {}
</script>

{#await plotAwait}
	<h1>Loading...</h1>
{/await}
<div id="plotly">
	<div
		on:click={() => {
			clickGraph();
		}}
		id="plotDiv"
	>
		<!-- Plotly chart will be drawn inside this DIV -->
	</div>
</div>
