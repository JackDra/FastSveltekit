import type { Item } from '$lib/apiTypes/item';

export async function get({ params }) {
    const res = await fetch(`http://fastapi_backend:8000/item/${params.item_id}`);
    const item: Item = await res.json();
    return {
        body: {
            item: item
        }
    };
}