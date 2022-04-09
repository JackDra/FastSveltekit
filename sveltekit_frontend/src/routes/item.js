export async function get() {
    const res = await fetch('http://localhost:8000/item');
    const item = await res.json();
    return {
        body: {
            item: item
        }
    };
}