<template>
  <div class="w-full overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-sm">

    <!-- Table header -->
    <table class="w-full text-sm">
      <thead>
        <tr class="border-b border-slate-200 bg-slate-50/50">
          <th class="text-left px-5 py-4 font-mono font-semibold text-sm uppercase
                     tracking-widest text-slate-400 w-8">#</th>
          <th class="text-left px-5 py-4 font-mono font-semibold text-sm uppercase
                     tracking-widest text-slate-400">Player</th>
          <th class="text-left px-5 py-4 font-mono font-semibold text-sm uppercase
                     tracking-widest text-slate-400">Team</th>
          <th class="text-right px-5 py-4 font-mono font-semibold text-sm uppercase
                     tracking-widest text-slate-400">KDA</th>
        </tr>
      </thead>

      <tbody>
        <!-- Skeleton rows -->
        <template v-if="loading">
          <tr v-for="i in 6" :key="`sk-${i}`"
              class="border-b border-slate-100">
            <td class="px-5 py-4" colspan="4">
              <div class="h-5 rounded-md bg-gradient-to-r from-slate-100 via-slate-200/50 to-slate-100
                          bg-[length:200%_100%] animate-shimmer" />
            </td>
          </tr>
        </template>

        <!-- Empty state -->
        <tr v-else-if="players.length === 0">
          <td colspan="4" class="px-5 py-16 text-center">
            <p class="text-4xl mb-3">🔍</p>
            <p class="text-slate-400 font-body">Không tìm thấy người chơi nào.</p>
          </td>
        </tr>

        <!-- Data rows -->
        <template v-else>
          <tr
            v-for="(player, idx) in players"
            :key="player.name"
            class="border-b border-slate-100 hover:bg-slate-50/70 transition-colors duration-150
                   group cursor-default"
            :style="{ animationDelay: `${idx * 40}ms` }"
            :class="idx < 8 ? `animate-slide-up-${Math.min(idx + 1, 4)}` : 'animate-fade-in'"
          >
            <!-- Rank -->
            <td class="px-5 py-4 font-mono text-xs text-slate-400">
              {{ String(idx + 1).padStart(2, "0") }}
            </td>

            <!-- Name -->
            <td class="px-5 py-4">
              <div class="flex items-center gap-3">
                <!-- Avatar initials -->
                <div
                  class="w-8 h-8 rounded-lg flex items-center justify-center shrink-0
                         font-bold text-xs text-slate-800 select-none shadow-sm"
                  :style="{ background: avatarColor(player.name) }"
                >
                  {{ initials(player.name) }}
                </div>
                <span class="font-body font-medium text-slate-800">{{ player.name }}</span>
              </div>
            </td>

            <!-- Team -->
            <td class="px-5 py-4">
              <span class="font-body text-slate-500 text-xs bg-slate-100 px-2.5 py-1 rounded-lg
                           border border-slate-200">
                {{ player.team }}
              </span>
            </td>

            <!-- KDA -->
            <td class="px-5 py-4 text-right">
              <span
                class="font-mono font-semibold"
                :class="kdaColor(player.kda)"
              >
                {{ player.kda.toFixed(2) }}
              </span>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <!-- Footer count -->
    <div v-if="!loading && players.length > 0"
         class="px-5 py-3.5 border-t border-slate-200 flex justify-between items-center bg-slate-50/30">
      <span class="text-sm text-slate-400 font-body">
        {{ players.length }} player
      </span>
      <span class="text-xs text-slate-500 font-mono">
        Average Players KDA:
        <span class="font-semibold ml-1">{{ avgKda }}</span>
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  players: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
});

function initials(name) {
  return name.slice(0, 2).toUpperCase();
}

function avatarColor(name) {
  // A palette of lighter, softer pastel colors for light theme avatar backgrounds
  const colors = [
    "#dbeafe", "#fee2e2", "#fef3c7", "#d1fae5",
    "#f3e8ff", "#fae8ff", "#ffedd5",
  ];
  let h = 0;
  for (let i = 0; i < name.length; i++) h = (h * 31 + name.charCodeAt(i)) & 0xffffffff;
  return colors[Math.abs(h) % colors.length];
}

function kdaColor(kda) {
  if (kda >= 5) return "text-amber-600";
  if (kda >= 3) return "text-emerald-600";
  if (kda >= 2) return "text-slate-700";
  return "text-slate-400";
}

const avgKda = computed(() => {
  if (!props.players.length) return "0.00";
  const sum = props.players.reduce((a, p) => a + p.kda, 0);
  return (sum / props.players.length).toFixed(2);
});
</script>
