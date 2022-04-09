import type { Item } from '$lib/apiTypes/items';

export async function get() {
    const res = await fetch('http://localhost:8000/item');
    const item: Item = await res.json();
    return {
        body: {
            item: item
        }
    };
}