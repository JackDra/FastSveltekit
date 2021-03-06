import type { Rand } from '$lib/apiTypes/rand';

export async function get({ params }) {
    const res = await fetch(`http://localhost:8000/rand/${params.rand_user}`);
    const rand: Rand = await res.json();
    return {
        body: {
            rand: rand
        }
    };
}