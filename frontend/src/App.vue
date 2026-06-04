<template>
  <div class="min-h-screen bg-ink-950 font-body">

    <!-- Background grid texture -->
    <div class="fixed inset-0 pointer-events-none"
         style="background-image: linear-gradient(rgba(200,245,59,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(200,245,59,0.03) 1px, transparent 1px);
                background-size: 48px 48px;" />

    <!-- Content -->
    <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-8 py-12">

      <!-- ── Header ─────────────────────────────────────── -->
      <header class="mb-10 animate-slide-up">
        <div class="flex items-start justify-between flex-wrap gap-4">
          <div>
            <p class="text-xs font-display uppercase tracking-[0.2em] text-acid mb-2">
              Player Stats Dashboard
            </p>
            <h1 class="text-4xl sm:text-5xl font-display font-extrabold text-white leading-none
                       tracking-tight">
              Bảng xếp hạng
              <br />
              <span class="text-acid">người chơi</span>
            </h1>
          </div>
          <!-- Live indicator -->
          <div class="flex items-center gap-2 mt-1">
            <span class="w-2 h-2 rounded-full bg-acid animate-pulse" />
            <span class="text-xs font-mono text-ink-600">LIVE API</span>
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
            class="px-4 py-2.5 rounded-xl text-sm font-display font-semibold
                   border border-ink-600 text-ink-500 hover:text-white hover:border-ink-500
                   transition-all duration-150"
          >
            Tất cả
          </button>
          <button
            @click="handleSearch(searchQuery)"
            class="px-4 py-2.5 rounded-xl text-sm font-display font-semibold
                   bg-acid text-ink-950 hover:bg-acid-dim active:scale-95
                   transition-all duration-150 shadow-[0_0_20px_rgba(200,245,59,0.25)]"
          >
            Tìm kiếm
          </button>
        </div>
      </div>

      <!-- ── Mode indicator ────────────────────────────── -->
      <div class="flex items-center gap-2 mb-4 animate-fade-in">
        <span
          v-if="isSearchMode"
          class="text-xs font-mono px-2.5 py-1 rounded-lg bg-ink-800
                 border border-ink-700 text-ink-500"
        >
          Kết quả cho
          <span class="text-acid">"{{ activeSearchTerm }}"</span>
        </span>
        <span v-else class="text-xs font-mono text-ink-600">
          Hiển thị tất cả
        </span>

        <!-- Error badge -->
        <span
          v-if="error"
          class="text-xs font-mono px-2.5 py-1 rounded-lg bg-ember/10
                 border border-ember/30 text-ember"
        >
          {{ error }}
        </span>
      </div>

      <!-- ── Table ─────────────────────────────────────── -->
      <div class="animate-slide-up-3">
        <PlayerTable :players="displayedPlayers" :loading="loading" />
      </div>

      <!-- ── Footer ────────────────────────────────────── -->
      <footer class="mt-10 pt-6 border-t border-ink-800 flex items-center
                     justify-between text-xs font-mono text-ink-600 animate-slide-up-4">
        <span>Player Stats API <span class="text-acid">v2.0</span></span>
        <a
          href="http://localhost:8000/docs"
          target="_blank"
          class="hover:text-acid transition-colors duration-150"
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
