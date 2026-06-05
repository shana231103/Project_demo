<template>
  <div class="min-h-screen bg-slate-300 font-body text-slate-600">

    <!-- Background grid texture -->
    <div class="fixed inset-0 pointer-events-none"
         style="background-image: linear-gradient(rgba(15, 23, 42, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
                background-size: 48px 48px;" />

    <!-- Content -->
    <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-8 py-12">

      <!-- ── Header ─────────────────────────────────────── -->
      <header class="mb-10 animate-slide-up">
        <div class="flex items-start justify-between flex-wrap gap-4">
          <div>
            <p class="text-sm uppercase tracking-[0.2em] text-slate-500 mb-2">
              Tournament Tracking Website
            </p>
            <h1 class="text-4xl sm:text-5xl font-bold text-blue-600 leading-none tracking-tight">
              PLAYER STATS DASHBOARD
            </h1>
          </div>
          <!-- Live indicator -->
          <div class="flex items-center gap-2 mt-1">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span class="text-sm font-semibold text-slate-400 text-black">LIVE API</span>
          </div>
        </div>
      </header>

      <!-- ── Stats Cards ────────────────────────────────── -->
      <div class="mb-8">
        <StatsCards :players="displayedPlayers" />
      </div>

      <!-- ── Search + Toolbar ──────────────────────────── -->
      <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center
                  justify-between mb-6 animate-slide-up-2">
        <SearchBar
          v-model="searchQuery"
          @search="handleSearch"
          @clear="handleClear"
        />

        <div class="flex gap-2 shrink-0">
          <button
            @click="handleClear"
            class="px-4 py-2.5 rounded-xl text-sm font-semibold
                   border border-slate-300 bg-white text-slate-600 hover:text-slate-800 hover:border-slate-400
                   transition-all duration-150"
          >
            Tất cả
          </button>
          <button
            @click="handleSearch(searchQuery)"
            class="px-4 py-2.5 rounded-xl text-sm font-semibold
                   bg-blue-600 text-white hover:bg-blue-700 active:scale-95
                   transition-all duration-150 shadow-[0_4px_12px_rgba(37,99,235,0.2)]"
          >
            Tìm kiếm
          </button>
        </div>
      </div>

      <!-- ── Mode indicator ────────────────────────────── -->
      <div class="flex items-center gap-2 mb-4 animate-fade-in">
        <span
          v-if="isSearchMode"
          class="text-xs font-mono px-2.5 py-1 rounded-lg bg-slate-200/50
                 border border-slate-200 text-slate-600"
        >
          Kết quả cho
          <span class="text-blue-500 font-semibold">"{{ activeSearchTerm }}"</span>
        </span>
        <span v-else class="text-base text-black font-bold">
          Hiển thị tất cả
        </span>

        <!-- Error badge -->
        <span
          v-if="error"
          class="text-xs font-mono px-2.5 py-1 rounded-lg bg-red-50
                 border border-red-200 text-red-600"
        >
          {{ error }}
        </span>
      </div>

      <!-- ── Table ─────────────────────────────────────── -->
      <div class="animate-slide-up-3">
        <PlayerTable :players="displayedPlayers" :loading="loading" />
      </div>

      <!-- ── Footer ────────────────────────────────────── -->
      <footer class="mt-10 pt-6 border-t border-slate-200 flex items-center
                     justify-between text-xs font-mono text-slate-400 animate-slide-up-4">
        <span>Player Stats API <span class="text-blue-600 font-semibold">v2.0</span></span>
        <a
          href="http://localhost:8000/docs"
          target="_blank"
          class="hover:text-blue-600 transition-colors duration-150"
        >
          Xem /docs →
        </a>
      </footer>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import SearchBar from "./components/SearchBar.vue";
import PlayerTable from "./components/PlayerTable.vue";
import StatsCards from "./components/StatsCards.vue";
import { fetchAllPlayers, searchPlayers } from "./service/playerApi.js";

const allPlayers = ref([]);
const displayedPlayers = ref([]);
const loading = ref(false);
const error = ref("");
const searchQuery = ref("");
const activeSearchTerm = ref("");
const isSearchMode = ref(false);

// ── Load all players on mount ──────────────────────────────────
onMounted(async () => {
  loading.value = true;
  error.value = "";
  try {
    allPlayers.value = await fetchAllPlayers();
    displayedPlayers.value = allPlayers.value;
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
});

// ── Search handler ─────────────────────────────────────────────
async function handleSearch(name) {
  const trimmed = (name ?? searchQuery.value).trim();
  if (!trimmed) {
    handleClear();
    return;
  }
  loading.value = true;
  error.value = "";
  isSearchMode.value = true;
  activeSearchTerm.value = trimmed;
  try {
    displayedPlayers.value = await searchPlayers(trimmed);
  } catch (e) {
    error.value = e.message;
    displayedPlayers.value = [];
  } finally {
    loading.value = false;
  }
}

// ── Clear / reset ──────────────────────────────────────────────
function handleClear() {
  searchQuery.value = "";
  activeSearchTerm.value = "";
  isSearchMode.value = false;
  error.value = "";
  displayedPlayers.value = allPlayers.value;
}
</script>
