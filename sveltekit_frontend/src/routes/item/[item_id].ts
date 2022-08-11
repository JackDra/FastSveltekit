import type { Item } from '$lib/apiTypes/item';

export async function get({ params }) {
    const res = await fetch(`http://fastapi-backend-service:8080/item/${params.item_id}`);
    const item: Item = await res.json();
    return {
        body: {
            item: item
        }
    };
}