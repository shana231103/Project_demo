/**
 * API Service - tầng abstraction cho HTTP calls
 * Tương đương "infrastructure" bên frontend
 */

const BASE_URL = import.meta.env.VITE_API_URL ?? "";

export async function fetchAllPlayers() {
  const res = await fetch(`${BASE_URL}/players`);
  if (!res.ok) throw new Error(`Lỗi ${res.status}: Không thể tải danh sách.`);
  return res.json();
}

export async function searchPlayers(name) {
  const params = new URLSearchParams({ name });
  const res = await fetch(`${BASE_URL}/search?${params}`);
  if (!res.ok) throw new Error(`Lỗi ${res.status}: Tìm kiếm thất bại.`);
  return res.json();
}
