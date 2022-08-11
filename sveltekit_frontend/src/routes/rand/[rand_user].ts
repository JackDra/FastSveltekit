import type { Rand } from '$lib/apiTypes/rand';

export async function get({ params }) {
    const res = await fetch(`http://fastapi-backend-service:8080/rand/${params.rand_user}`);
    const rand: Rand = await res.json();
    return {
        body: {
            rand: rand
        }
    };
}